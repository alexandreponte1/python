import boto3

aws_access_key = ""
aws_secret_key = ""
aws_region = "us-east-1"


ec2_re = boto3.resource(
    "ec2",
    aws_access_key_id=aws_access_key,
    aws_secret_access_key=aws_secret_key,
    region_name=aws_region
)

ec2_client = boto3.client(
    "ec2",
    aws_access_key_id=aws_access_key,
    aws_secret_access_key=aws_secret_key,
    region_name=aws_region
)



response = ec2_client.run_instances(
    ImageId ="ami-0ebfd941bbafe70c6",
    InstanceType="t2.micro",
    KeyName="goku123",
    MinCount=1,
    MaxCount=1
)

print(response)