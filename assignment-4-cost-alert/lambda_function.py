import boto3
from datetime import date, timedelta

THRESHOLD_USD = 0.01   # TEMPORARY low value to force-test the alert path
SNS_TOPIC_ARN = "arn:aws:sns:us-east-1:153659547591:aws-cost-alerts"

ce = boto3.client("ce")
sns = boto3.client("sns")

def lambda_handler(event, context):
    today = date.today()
    start_of_month = today.replace(day=1).isoformat()
    tomorrow = (today + timedelta(days=1)).isoformat()

    response = ce.get_cost_and_usage(
        TimePeriod={"Start": start_of_month, "End": tomorrow},
        Granularity="MONTHLY",
        Metrics=["UnblendedCost"],
    )
    amount = float(response["ResultsByTime"][0]["Total"]["UnblendedCost"]["Amount"])
    print(f"Month-to-date spend: ${amount:.2f}")

    if amount > THRESHOLD_USD:
        sns.publish(
            TopicArn=SNS_TOPIC_ARN,
            Subject="AWS Cost Alert",
            Message=f"Month-to-date spend is ${amount:.2f}, exceeding the ${THRESHOLD_USD} threshold."
        )
        print("Alert published.")

    return {"month_to_date_spend": amount}