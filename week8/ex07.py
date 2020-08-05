import boto3

print("List all the AWS S3 buckets this account has:")
s3 = boto3.resource('s3')
targeted_bucket = None
# for bucket in s3.buckets.all():
#     if bucket.name.find("the4thpythonbucket") != -1:
#         targeted_bucket = bucket
#
# for obj in targeted_bucket.objects.filter(Prefix='the4thpythonbucket'):
#     s3.Object(bucket.name, obj.key).delete()

for bucket in s3.buckets.all():
    print(bucket.name)

