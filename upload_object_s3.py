import boto3
client = boto3.client('s3')

file_reader = open('data.json').read()
response = client.put_object(
    ACL='private',
    Body=file_reader,
    Bucket='newprojectboto3',
    Key='data.json'
)