import boto3

aws_access_key = ""
aws_secret_key = ""
aws_region = "us-east-1"


s3_re = boto3.resource(
    "s3",
    aws_access_key_id=aws_access_key,
    aws_secret_access_key=aws_secret_key,
    region_name=aws_region
)


s3_client = boto3.client(
    "s3",
    aws_access_key_id=aws_access_key,
    aws_secret_access_key=aws_secret_key,
    region_name=aws_region
)

for bucket in s3_re.buckets.all():
    print(bucket.name)

def delete_s3_bucket(bucket_name):
    response = s3_client.delete_bucket(Bucket=bucket_name)
    print(f"S3 Bucket '{bucket_name}' deleted successfully")


for bucket in s3_re.buckets.all():
    delete_s3_bucket(bucket.name)