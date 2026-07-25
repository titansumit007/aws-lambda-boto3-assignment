import boto3
from datetime import datetime, timezone, timedelta

VOLUME_ID = "vol-0a5f8145eca191784"   # <-- paste your real volume ID here
RETENTION = timedelta(days=30)
TAG_KEY, TAG_VALUE = "CreatedBy", "Lambda-Backup"

ec2 = boto3.client("ec2")

def lambda_handler(event, context):
    snap = ec2.create_snapshot(
        VolumeId=VOLUME_ID,
        Description="Automated backup via Lambda",
        TagSpecifications=[{
            "ResourceType": "snapshot",
            "Tags": [{"Key": TAG_KEY, "Value": TAG_VALUE}]
        }]
    )
    new_snap_id = snap["SnapshotId"]
    print(f"Created snapshot: {new_snap_id}")

    now = datetime.now(timezone.utc)
    deleted = []
    paginator = ec2.get_paginator("describe_snapshots")
    for page in paginator.paginate(
        OwnerIds=["self"],
        Filters=[{"Name": f"tag:{TAG_KEY}", "Values": [TAG_VALUE]}]
    ):
        for s in page["Snapshots"]:
            age = now - s["StartTime"]
            if age > RETENTION and s["SnapshotId"] != new_snap_id:
                ec2.delete_snapshot(SnapshotId=s["SnapshotId"])
                deleted.append(s["SnapshotId"])
                print(f"Deleted snapshot: {s['SnapshotId']} (age: {age})")

    print(f"Created: {new_snap_id}, Deleted: {deleted}")
    return {"created": new_snap_id, "deleted": deleted}