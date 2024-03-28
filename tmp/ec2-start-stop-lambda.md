# Create Policy


# Create Role


# Create Lambda
## ec2-start-mvi-edge-transmission-line
```
import boto3
region = 'us-east-1'
instances = ['']
ec2 = boto3.client('ec2', region_name=region)

def lambda_handler(event, context):
    print('Starting instances')
    ec2.start_instances(InstanceIds=instances)
```

## ec2-stop-mvi-edge-transmission-line
```
import boto3
region = 'us-east-1'
instances = ['i-0fdf129634745c845']
ec2 = boto3.client('ec2', region_name=region)

def lambda_handler(event, context):
    print('Stopping instances')
    ec2.stop_instances(InstanceIds=instances)
```