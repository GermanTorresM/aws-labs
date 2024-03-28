import pulumi_aws as aws
from pulumi import ResourceOptions
from pulumi_aws.config import region

from config import (
    project_name,
    environment,
    owner,
    db_tcp_port_number,
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
    private_db_subnet_az1,
    private_db_subnet_az2,
    private_db_subnet_az3,
    private_db_subnet_az4,
)

## 01. Private DB Network ACL
## 02. 


############## Private DB Network ACL ##############
# StackName-environmentName-aws:region-private-db-nacl
# ej. project-dev-us-east-1-private-db-nacl
private_db_network_acl = aws.ec2.NetworkAcl(
    resource_name = f'{project_name}-{environment}-{region}-private-db-nacl',
    opts = ResourceOptions(depends_on = [ vpc ]),
    vpc_id = vpc.id,
    tags = {
        'Name': f'{project_name}-{environment}-{region}-private-db-nacl',
        'Network': 'private',
        'Owner': owner,
        'Project': project_name,
        'Environment': environment,
    },
)

inbound_db_nacl_rule_allow1 = aws.ec2.NetworkAclRule(
    resource_name = 'inbound_db_nacl_rule_allow1',
    opts = ResourceOptions(depends_on = [ private_db_network_acl, private_app_subnet_az1 ]),
    network_acl_id = private_db_network_acl.id,
    rule_number = 100,
    egress = False,
    protocol = 'tcp',
    rule_action = 'allow',
    cidr_block = private_app_subnet_cidr_az1,
    from_port = db_tcp_port_number,
    to_port = db_tcp_port_number,
)

inbound_db_nacl_rule_allow2 = aws.ec2.NetworkAclRule(
    resource_name = 'inbound_db_nacl_rule_allow2',
    opts = ResourceOptions(depends_on = [ private_db_network_acl, private_app_subnet_az2 ]),
    network_acl_id = private_db_network_acl.id,
    rule_number = 150,
    egress = False,
    protocol = 'tcp',
    rule_action = 'allow',
    cidr_block = private_app_subnet_cidr_az2,
    from_port = db_tcp_port_number,
    to_port = db_tcp_port_number,
)

inbound_db_nacl_rule_allow3 = aws.ec2.NetworkAclRule(
    resource_name = 'inbound_db_nacl_rule_allow3',
    opts = ResourceOptions(depends_on = [ private_db_network_acl, private_app_subnet_az3 ]),
    network_acl_id = private_db_network_acl.id,
    rule_number = 200,
    egress = False,
    protocol = 'tcp',
    rule_action = 'allow',
    cidr_block = private_app_subnet_cidr_az3,
    from_port = db_tcp_port_number,
    to_port = db_tcp_port_number,
)

inbound_db_nacl_rule_allow4 = aws.ec2.NetworkAclRule(
    resource_name = 'inbound_db_nacl_rule_allow4',
    opts = ResourceOptions(depends_on = [ private_db_network_acl, private_app_subnet_az4 ]),
    network_acl_id = private_db_network_acl.id,
    rule_number = 250,
    egress = False,
    protocol = 'tcp',
    rule_action = 'allow',
    cidr_block = private_app_subnet_cidr_az4,
    from_port = db_tcp_port_number,
    to_port = db_tcp_port_number,
)

outbound_db_nacl_rule_allow1 = aws.ec2.NetworkAclRule(
    resource_name = 'outbound_db_nacl_rule_allow1',
    opts = ResourceOptions(depends_on = [ private_db_network_acl, private_app_subnet_az1 ]),
    network_acl_id = private_db_network_acl.id,
    rule_number = 100,
    egress = True,
    protocol = 'tcp',
    rule_action = 'allow',
    cidr_block = private_app_subnet_cidr_az1,
    from_port = 1024,
    to_port = 65535,
)

outbound_db_nacl_rule_allow2 = aws.ec2.NetworkAclRule(
    resource_name = 'outbound_db_nacl_rule_allow2',
    opts = ResourceOptions(depends_on = [ private_db_network_acl, private_app_subnet_az2 ]),
    network_acl_id = private_db_network_acl.id,
    rule_number = 150,
    egress = True,
    protocol = 'tcp',
    rule_action = 'allow',
    cidr_block = private_app_subnet_cidr_az2,
    from_port = 1024,
    to_port = 65535,
)

outbound_db_nacl_rule_allow3 = aws.ec2.NetworkAclRule(
    resource_name = 'outbound_db_nacl_rule_allow3',
    opts = ResourceOptions(depends_on = [ private_db_network_acl, private_app_subnet_az3 ]),
    network_acl_id = private_db_network_acl.id,
    rule_number = 200,
    egress = True,
    protocol = 'tcp',
    rule_action = 'allow',
    cidr_block = private_app_subnet_cidr_az3,
    from_port = 1024,
    to_port = 65535,
)

outbound_db_nacl_rule_allow4 = aws.ec2.NetworkAclRule(
    resource_name = 'outbound_db_nacl_rule_allow4',
    opts = ResourceOptions(depends_on = [ private_db_network_acl, private_app_subnet_az4 ]),
    network_acl_id = private_db_network_acl.id,
    rule_number = 250,
    egress = True,
    protocol = 'tcp',
    rule_action = 'allow',
    cidr_block = private_app_subnet_cidr_az4,
    from_port = 1024,
    to_port = 65535,
)

# Private DB Subnet Association
private_db_subnet_nacl_association1 = aws.ec2.NetworkAclAssociation(
    resource_name = 'private_db_subnet_nacl_association1',
    opts = ResourceOptions(depends_on = [ private_db_network_acl, private_db_subnet_az1 ]),
    network_acl_id = private_db_network_acl.id,
    subnet_id = private_db_subnet_az1.id,
)

private_db_subnet_nacl_association2 = aws.ec2.NetworkAclAssociation(
    resource_name = 'private_db_subnet_nacl_association2',
    opts = ResourceOptions(depends_on = [ private_db_network_acl, private_db_subnet_az2 ]),
    network_acl_id = private_db_network_acl.id,
    subnet_id = private_db_subnet_az2.id,
)

private_db_subnet_nacl_association3 = aws.ec2.NetworkAclAssociation(
    resource_name = 'private_db_subnet_nacl_association3',
    opts = ResourceOptions(depends_on = [ private_db_network_acl, private_db_subnet_az3 ]),
    network_acl_id = private_db_network_acl.id,
    subnet_id = private_db_subnet_az3.id,
)

private_db_subnet_nacl_association4 = aws.ec2.NetworkAclAssociation(
    resource_name = 'private_db_subnet_nacl_association4',
    opts = ResourceOptions(depends_on = [ private_db_network_acl, private_db_subnet_az4 ]),
    network_acl_id = private_db_network_acl.id,
    subnet_id = private_db_subnet_az4.id,
)