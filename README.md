## ebs-snapshot
Simple python script to create EBS snapshots.

### Requirements
Python, Boto SDK and proper IAM permissions

### Usage
1. Update config.py with AWS credentials (optional: region, tag and snapshots_to_keep)
2. Tag each volume you want a snapshot of

    ```
    "Key": "Backup"
    "Value": "True"
    ```

3. Manually run `ebs-snapshot.py` or install as a cron job

### Note
By default, `ebs-snapshot` keeps 3 snapshots of the same volume. If more snapshots exist, the oldest ones will be removed first.
