import boto3

# Define a região alvo
aws_access_key = ""
aws_secret_key = ""
aws_region = "us-east-1"

# Cria um recurso EC2 na região especificada
ec2 = boto3.resource('ec2', 
    aws_access_key_id=aws_access_key,
    aws_secret_access_key=aws_secret_key,
    region_name=aws_region
)

print(f"Region: {aws_region}")

# Filtra apenas as instâncias que estão rodando
instances = ec2.instances.filter(
    Filters=[{'Name': 'instance-state-name', 'Values': ['running']}]
)

# Desliga as instâncias
for instance in instances:
    instance.stop()
    print('Stopped instance: ', instance.id)
