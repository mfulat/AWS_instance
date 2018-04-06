#!/Library/Frameworks/Python.framework/Versions/3.6/bin/python3
# descript key pairs and describe instances
import boto3

ec2 = boto3.client('ec2')
response = ec2.describe_key_pairs()
print(response)

ec2 = boto3.client('ec2')
response = ec2.describe_instances()
print(response)
