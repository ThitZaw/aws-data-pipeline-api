import pandas as pd
import boto3
import io

s3 = boto3.client("s3")

def transform_csv_to_parquet(bucket_name, input_key, output_key):
    # 1. Read CSV from S3
    obj = s3.get_object(Bucket=bucket_name, Key=input_key)
    df = pd.read_csv(io.BytesIO(obj["Body"].read()))

    print("Original Data:")
    print(df.head())

    # 2. Basic cleaning (KEEP SIMPLE for now)
    df = df.dropna()  # remove nulls

    # Optional: standardize column names
    df.columns = [col.lower().replace(" ", "_") for col in df.columns]

    # 3. Convert to Parquet (in memory)
    out_buffer = io.BytesIO()
    df.to_parquet(out_buffer, index=False, engine="pyarrow")

    # 4. Upload to S3 (processed)
    s3.put_object(
        Bucket=bucket_name,
        Key=output_key,
        Body=out_buffer.getvalue()
    )

    print(f"Uploaded parquet to {output_key}")