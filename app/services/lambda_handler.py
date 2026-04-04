import json
from app.services.transform import transform_csv_to_parquet

def lambda_handler(event, context):
    # Get S3 info from event
    record = event["Records"][0]
    
    bucket = record["s3"]["bucket"]["name"]
    input_key = record["s3"]["object"]["key"]

    # Only process CSV in raw/
    if not input_key.startswith("raw/") or not input_key.endswith(".csv"):
        print("Skipping file:", input_key)
        return

    # Generate output path
    output_key = input_key.replace("raw/", "processed/").replace(".csv", ".parquet")

    # Run transformation
    transform_csv_to_parquet(bucket, input_key, output_key)

    return {
        "statusCode": 200,
        "body": json.dumps("Transformation complete")
    }