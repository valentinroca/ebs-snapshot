#!/usr/bin/env python
#
# ebs-snapshot.py version 1.0
#

from datetime import datetime
import boto.ec2
from config import config

region = config['region']
aws_access_key_id = config['aws_access_key_id']
aws_secret_access_key = config['aws_secret_access_key']

print "Connecting to AWS.."
conn = boto.ec2.connect_to_region(region_name=region, aws_access_key_id=aws_access_key_id, aws_secret_access_key=aws_secret_access_key)
print "done\n"

print "Finding volumes to backup.."
volumes_to_backup = conn.get_all_volumes(filters={'tag:' + config['tag_key']: config['tag_value']})
print "done\n"

for volume in volumes_to_backup:
    print "Creating new snapshot for %s" % (volume.id)
    desc = "%s snapshot created at %s using ebs-snapshot" % (volume.id, datetime.today().strftime('%d-%m-%Y %H:%M:%S'))
    volume.create_snapshot(description=desc)
    print "done\n"
    snapshots = sorted(volume.snapshots(), key=lambda x: x.start_time)
    while len(snapshots) > config['snapshots_to_keep']:
        print "Removing old snapshot for %s" % (volume.id)
        snapshots[0].delete()
        snapshots.pop(0)
        print "done\n"
