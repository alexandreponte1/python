import boto3

aws_access_key = ""
aws_secret_key = ""
aws_region = "us-east-1"

bucket_name = "ps-course-test-bucket-goku123"

s3_client = boto3.client(
    "s3",
    aws_access_key_id=aws_access_key,
    aws_secret_access_key=aws_secret_key,
    region_name=aws_region
)

def get_location_constraint(region_name):
    if region_name == "us-east-1":
        return ""
    else:
        return region_name

def create_s3_bucket(bucket_name):
    response = s3_client.create_bucket(Bucket=bucket_name)
    print(f"S3 Bucket '{bucket_name}' created successfully")
    print(response)

def delete_s3_bucket(bucket_name):
    response = s3_client.delete_bucket(Bucket=bucket_name)
    print(f"S3 Bucket '{bucket_name}' deleted successfully")

if __name__ == "__main__":
    create_s3_bucket(bucket_name)