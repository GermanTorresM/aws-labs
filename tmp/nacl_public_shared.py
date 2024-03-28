import pulumi_aws as aws
from pulumi import ResourceOptions
from pulumi_aws.config import region

from config import (
    project_name,
    environment,
    owner,
    private_app_subnet_cidr_az1,
    private_app_subnet_cidr_az2,
    private_app_subnet_cidr_az3,
    private_app_subnet_cidr_az4,   
)

from resources.vpc.vpc_4azs import (
    vpc, 
    private_app_subnet_az1, 
    private_app_subnet_az2, 
    private_app_subnet_az3, 
    private_app_subnet_az4,
    public_shared_subnet_az1,
    public_shared_subnet_az2,
    public_shared_subnet_az3,
    public_shared_subnet_az4,
)

## 01. Public Shared Network ACL
## 02. 


############## Public Shared Network ACL ##############
# StackName-environmentName-aws:region-public-shared-nacl
# ej. project-dev-us-east-1-public-shared-nacl
public_shared_network_acl = aws.ec2.NetworkAcl(
    resource_name = f'{project_name}-{environment}-{region}-public-shared-nacl',
    opts = ResourceOptions(depends_on = [ vpc ]),
    vpc_id = vpc.id,
    tags = {
        'Name': f'{project_name}-{environment}-{region}-public-shared-nacl',
        'Network': 'public',
        'Owner': owner,
        'Project': project_name,
        'Environment': environment,
    },
)

inbound_ephemeral_shared_nacl_rule_allow = aws.ec2.NetworkAclRule(
    resource_name = 'inbound_ephemeral_shared_nacl_rule_allow',
    opts = ResourceOptions(depends_on = [ public_shared_network_acl ]),
    network_acl_id = public_shared_network_acl.id,
    rule_number = 100,
    egress = False,
    protocol = 'tcp',
    rule_action = 'allow',
    cidr_block = '0.0.0.0/0',
    from_port = 1024,
    to_port = 65535,
)

inbound_shared_app_nacl_rule_allow1 = aws.ec2.NetworkAclRule(
    resource_name = 'inbound_shared_app_nacl_rule_allow1',
    opts = ResourceOptions(depends_on = [ public_shared_network_acl, private_app_subnet_az1 ]),
    network_acl_id = public_shared_network_acl.id,
    rule_number = 200,
    egress = False,
    protocol = 'tcp',
    rule_action = 'allow',
    cidr_block = private_app_subnet_cidr_az1,
    from_port = 0,
    to_port = 65535,
)

inbound_shared_app_nacl_rule_allow2 = aws.ec2.NetworkAclRule(
    resource_name = 'inbound_shared_app_nacl_rule_allow2',
    opts = ResourceOptions(depends_on = [ public_shared_network_acl, private_app_subnet_az2 ]),
    network_acl_id = public_shared_network_acl.id,
    rule_number = 250,
    egress = False,
    protocol = 'tcp',
    rule_action = 'allow',
    cidr_block = private_app_subnet_cidr_az2,
    from_port = 0,
    to_port = 65535,
)

inbound_shared_app_nacl_rule_allow3 = aws.ec2.NetworkAclRule(
    resource_name = 'inbound_shared_app_nacl_rule_allow3',
    opts = ResourceOptions(depends_on = [ public_shared_network_acl, private_app_subnet_az3 ]),
    network_acl_id = public_shared_network_acl.id,
    rule_number = 300,
    egress = False,
    protocol = 'tcp',
    rule_action = 'allow',
    cidr_block = private_app_subnet_cidr_az3,
    from_port = 0,
    to_port = 65535,
)

inbound_shared_app_nacl_rule_allow4 = aws.ec2.NetworkAclRule(
    resource_name = 'inbound_shared_app_nacl_rule_allow4',
    opts = ResourceOptions(depends_on = [ public_shared_network_acl, private_app_subnet_az4 ]),
    network_acl_id = public_shared_network_acl.id,
    rule_number = 350,
    egress = False,
    protocol = 'tcp',
    rule_action = 'allow',
    cidr_block = private_app_subnet_cidr_az4,
    from_port = 0,
    to_port = 65535,
)

outbound_ephemeral_shared_nacl_rule_allow_all = aws.ec2.NetworkAclRule(
    resource_name = 'outbound_ephemeral_shared_nacl_rule_allow_all',
    opts = ResourceOptions(depends_on = [ public_shared_network_acl ]),
    network_acl_id = public_shared_network_acl.id,
    rule_number = 100,
    egress = True,
    protocol = 'tcp',
    rule_action = 'allow',
    cidr_block = '0.0.0.0/0',
    from_port = 1024,
    to_port = 65535,
)

outbound_shared_nacl_rule_allow_http = aws.ec2.NetworkAclRule(
    resource_name = 'outbound_shared_nacl_rule_allow_http',
    opts = ResourceOptions(depends_on = [ public_shared_network_acl ]),
    network_acl_id = public_shared_network_acl.id,
    rule_number = 200,
    egress = True,
    protocol = 'tcp',
    rule_action = 'allow',
    cidr_block = '0.0.0.0/0',
    from_port = 80,
    to_port = 80,
)

outbound_shared_nacl_rule_allow_https = aws.ec2.NetworkAclRule(
    resource_name = 'outbound_shared_nacl_rule_allow_https',
    opts = ResourceOptions(depends_on = [ public_shared_network_acl ]),
    network_acl_id = public_shared_network_acl.id,
    rule_number = 300,
    egress = True,
    protocol = 'tcp',
    rule_action = 'allow',
    cidr_block = '0.0.0.0/0',
    from_port = 443,
    to_port = 443,
)

# Public Alb Subnet Association
public_shared_subnet_nacl_association1 = aws.ec2.NetworkAclAssociation(
    resource_name = 'public_shared_subnet_nacl_association1',
    opts = ResourceOptions(depends_on = [ public_shared_network_acl, public_shared_subnet_az1 ]),
    network_acl_id = public_shared_network_acl.id,
    subnet_id = public_shared_subnet_az1.id,
)

public_shared_subnet_nacl_association2 = aws.ec2.NetworkAclAssociation(
    resource_name = 'public_shared_subnet_nacl_association2',
    opts = ResourceOptions(depends_on = [ public_shared_network_acl, public_shared_subnet_az2 ]),
    network_acl_id = public_shared_network_acl.id,
    subnet_id = public_shared_subnet_az2.id,
)

public_shared_subnet_nacl_association3 = aws.ec2.NetworkAclAssociation(
    resource_name = 'public_shared_subnet_nacl_association3',
    opts = ResourceOptions(depends_on = [ public_shared_network_acl, public_shared_subnet_az3 ]),
    network_acl_id = public_shared_network_acl.id,
    subnet_id = public_shared_subnet_az3.id,
)

public_shared_subnet_nacl_association4 = aws.ec2.NetworkAclAssociation(
    resource_name = 'public_shared_subnet_nacl_association4',
    opts = ResourceOptions(depends_on = [ public_shared_network_acl, public_shared_subnet_az4 ]),
    network_acl_id = public_shared_network_acl.id,
    subnet_id = public_shared_subnet_az4.id,
)