import boto3
from datetime import datetime, timezone, timedelta

BUCKET_NAME = "herovirs3asign1"
AGE_THRESHOLD = timedelta(days=30)   # switch to timedelta(minutes=1) only while testing

s3 = boto3.client("s3")

def lambda_handler(event, context):
    now = datetime.now(timezone.utc)
    deleted = []

    paginator = s3.get_paginator("list_objects_v2")
    for page in paginator.paginate(Bucket=BUCKET_NAME):
        for obj in page.get("Contents", []):
            age = now - obj["LastModified"]
            if age > AGE_THRESHOLD:
                s3.delete_object(Bucket=BUCKET_NAME, Key=obj["Key"])
                deleted.append(obj["Key"])
                print(f"Deleted: {obj['Key']} (age: {age})")

    print(f"Total deleted: {len(deleted)} -> {deleted}")
    return {"deleted_objects": deleted, "count": len(deleted)}