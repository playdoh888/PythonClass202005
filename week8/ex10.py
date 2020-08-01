from boto3 import client

BUCKET_NAME = 'messages-periship'  # replace with your bucket name

conn = client('s3')  # again assumes boto.cfg setup, assume AWS S3
for key in conn.list_objects(Bucket=BUCKET_NAME)['Contents']:
    print(key['Key'])
