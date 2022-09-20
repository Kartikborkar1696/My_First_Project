import boto3
client = boto3.client('s3')

response = client.delete_object(
    Bucket='newprojectboto3',
    Key='data.json'
)