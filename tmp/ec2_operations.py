# Import all the modules and Libraries
import boto3

# Open Management Console
aws_management_console = boto3.session.Session(profile_name="terraform-user")

# Open EC2 Console
ec2_console = aws_management_console.client(service_name="ec2")

# Use Boto3 Documentation to get more information (https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#client)
response = ec2_console.stop_instances(
    InstanceIds=['i-035b322341f9301a3']
)

response = ec2_console.start_instances(
    InstanceIds=['i-035b322341f9301a3']
)