import boto3

print("List all the AWS EC2 instances this account has:")
ec2 = boto3.resource('ec2')
for instance in ec2.instances.all():
     print(instance.id, instance.state)
