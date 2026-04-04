from app.services.transform import transform_csv_to_parquet

bucket = "aws-data-pipeline-thit"

transform_csv_to_parquet(
    bucket_name=bucket,
    input_key="raw/tea_vs_coffee_global_final.csv"
)