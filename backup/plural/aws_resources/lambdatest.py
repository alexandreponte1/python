import boto3

def lambda_handler(event, context):
    # Define a região alvo
    region = 'us-east-1'
    
    # Cria um recurso EC2 na região especificada
    ec2 = boto3.resource('ec2', region_name=region)

    print(f"Region: {region}")

    # Filtra apenas as instâncias que estão rodando
    instances = ec2.instances.filter(
        Filters=[{'Name': 'instance-state-name', 'Values': ['running']}]
    )

    # Desliga as instâncias
    stopped_instances = []
    for instance in instances:
        instance.stop()
        stopped_instances.append(instance.id)
        print(f'Stopped instance: {instance.id}')
    
    return {
        'statusCode': 200,
        'body': f'Stopped instances: {stopped_instances}'
    }
