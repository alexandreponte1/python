from google.cloud import secretmanager

PROJECT_ID = "PROJECT_ID"

def create_secret(secret_id):
    # Create the Secret Manager client.
    client = secretmanager.SecretManagerServiceClient()

    # Build the resource name of the parent project.
    parent = f"projects/{PROJECT_ID}"

    # Build a dict of settings for the secret
    secret = {'replication': {'automatic': {}}}

    # Create the secret
    response = client.create_secret(secret_id=secret_id, parent=parent, secret=secret)

    # Print the new secret name.
    print(f'Created secret: {response.name}')   


create_secret("my_secret_value")
