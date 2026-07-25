import boto3
from datetime import date

ec2 = boto3.client("ec2")

def lambda_handler(event, context):
    instance_id = event["detail"]["instance-id"]

    ec2.create_tags(
        Resources=[instance_id],
        Tags=[
            {"Key": "LaunchDate", "Value": str(date.today())},
            {"Key": "Owner", "Value": "auto-tag-lambda"},
        ]
    )
    print(f"Tagged instance {instance_id} with LaunchDate and Owner")
    return {"tagged_instance": instance_id}