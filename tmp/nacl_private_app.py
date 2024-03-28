import pulumi_aws as aws
from pulumi import ResourceOptions
from pulumi_aws.config import region

from config import (
    project_name,
    environment,
    owner,
    vpc_cidr, 
)

from resources.vpc.vpc_4azs import (
    vpc, 
    private_app_subnet_az1, 
    private_app_subnet_az2, 
    private_app_subnet_az3, 
    private_app_subnet_az4,
)

## 01. Private App Network ACL
## 02. 


############## Private App Network ACL ##############
# StackName-environmentName-aws:region-private-app-nacl
# ej. project-dev-us-east-1-private-app-nacl
private_app_network_acl = aws.ec2.NetworkAcl(
    resource_name = f'{project_name}-{environment}-{region}-private-app-nacl',
    opts = ResourceOptions(depends_on = [ vpc ]),
    vpc_id = vpc.id,
    tags = {
        'Name': f'{project_name}-{environment}-{region}-private-app-nacl',
        'Network': 'private',
        'Owner': owner,
        'Project': project_name,
        'Environment': environment,
    },
)

inbound_app_nacl_rule_allow_http = aws.ec2.NetworkAclRule(
    resource_name = 'inbound_app_nacl_rule_allow_http',
    opts = ResourceOptions(depends_on = [ private_app_network_acl ]),
    network_acl_id = private_app_network_acl.id,
    rule_number = 100,
    egress = False,
    protocol = 'tcp',
    rule_action = 'allow',
    cidr_block = vpc_cidr,
    from_port = 80,
    to_port = 80,
)

inbound_app_nacl_rule_allow_https = aws.ec2.NetworkAclRule(
    resource_name = 'inbound_app_nacl_rule_allow_https',
    opts = ResourceOptions(depends_on = [ private_app_network_acl ]),
    network_acl_id = private_app_network_acl.id,
    rule_number = 150,
    egress = False,
    protocol = 'tcp',
    rule_action = 'allow',
    cidr_block = vpc_cidr,
    from_port = 443,
    to_port = 443,
)

inbound_ephemeral_app_nacl_rule_allow_all = aws.ec2.NetworkAclRule(
    resource_name = 'inbound_ephemeral_app_nacl_rule_allow_all',
    opts = ResourceOptions(depends_on = [ private_app_network_acl ]),
    network_acl_id = private_app_network_acl.id,
    rule_number = 200,
    egress = False,
    protocol = 'tcp',
    rule_action = 'allow',
    cidr_block = '0.0.0.0/0',
    from_port = 1024,
    to_port = 65535,
)

outbound_app_nacl_rule_allow_http = aws.ec2.NetworkAclRule(
    resource_name = 'outbound_app_nacl_rule_allow_http',
    opts = ResourceOptions(depends_on = [ private_app_network_acl ]),
    network_acl_id = private_app_network_acl.id,
    rule_number = 100,
    egress = True,
    protocol = 'tcp',
    rule_action = 'allow',
    cidr_block = '0.0.0.0/0',
    from_port = 80,
    to_port = 80,
)

outbound_app_nacl_rule_allow_https = aws.ec2.NetworkAclRule(
    resource_name = 'outbound_app_nacl_rule_allow_https',
    opts = ResourceOptions(depends_on = [ private_app_network_acl ]),
    network_acl_id = private_app_network_acl.id,
    rule_number = 150,
    egress = True,
    protocol = 'tcp',
    rule_action = 'allow',
    cidr_block = '0.0.0.0/0',
    from_port = 443,
    to_port = 443,
)

outbound_app_vpc_nacl_rule_allow_all = aws.ec2.NetworkAclRule(
    resource_name = 'outbound_app_vpc_nacl_rule_allow_all',
    opts = ResourceOptions(depends_on = [ private_app_network_acl ]),
    network_acl_id = private_app_network_acl.id,
    rule_number = 200,
    egress = True,
    protocol = 'all',
    rule_action = 'allow',
    cidr_block = vpc_cidr,
    from_port = 1,
    to_port = 65535,
)

# Private App Subnet Association
private_app_subnet_nacl_association1 = aws.ec2.NetworkAclAssociation(
    resource_name = 'private_app_subnet_nacl_association1',
    opts = ResourceOptions(depends_on = [ private_app_network_acl, private_app_subnet_az1 ]),
    network_acl_id = private_app_network_acl.id,
    subnet_id = private_app_subnet_az1.id,
)

private_app_subnet_nacl_association2 = aws.ec2.NetworkAclAssociation(
    resource_name = 'private_app_subnet_nacl_association2',
    opts = ResourceOptions(depends_on = [ private_app_network_acl, private_app_subnet_az2 ]),
    network_acl_id = private_app_network_acl.id,
    subnet_id = private_app_subnet_az2.id,
)

private_app_subnet_nacl_association3 = aws.ec2.NetworkAclAssociation(
    resource_name = 'private_app_subnet_nacl_association3',
    opts = ResourceOptions(depends_on = [ private_app_network_acl, private_app_subnet_az3 ]),
    network_acl_id = private_app_network_acl.id,
    subnet_id = private_app_subnet_az3.id,
)

private_app_subnet_nacl_association4 = aws.ec2.NetworkAclAssociation(
    resource_name = 'private_app_subnet_nacl_association4',
    opts = ResourceOptions(depends_on = [ private_app_network_acl, private_app_subnet_az4 ]),
    network_acl_id = private_app_network_acl.id,
    subnet_id = private_app_subnet_az4.id,
)