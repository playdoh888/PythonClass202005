import boto3
import botocore
from botocore.exceptions import ClientError


BUCKET_NAME = 'messages-periship' # replace with your bucket name
KEY = 'CurrentTempsAnimation/animation.gif' # replace with your object key

s3 = boto3.resource('s3')

try:
    s3.Bucket(BUCKET_NAME).download_file(KEY, 'my_local_image.jpg')
except ClientError as e:
    if e.response['Error']['Code'] == "404":
        print("The object does not exist.")
    else:
        raise
