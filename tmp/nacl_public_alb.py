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
    public_alb_subnet_az1, 
    public_alb_subnet_az2, 
    public_alb_subnet_az3, 
    public_alb_subnet_az4,
    private_app_subnet_az1,
    private_app_subnet_az2,
    private_app_subnet_az3,
    private_app_subnet_az4,
)

## 01. Public ALB Network ACL
## 02. Public ALB Network ACL Allow HTTP
## 03. Public ALB Network ACL Allow HTTPS
## 04. Public ALB Network ACL Deny MSSQL
## 05. Public ALB Network ACL Deny Oracke
## 06. Public ALB Network ACL Deny MySql
## 07. Public ALB Network ACL Deny NFS
## 08. Public ALB Network ACL Deny RDP
## 09. Public ALB Network ACL Deny Postgres
## 10. Public ALB Network ACL Deny LDAP
## 11. Public ALB Network ACL Deny SSH



############## Public ALB Network ACL ##############
# StackName-environmentName-aws:region-public-alb-nacl
# ej. project-dev-us-east-1-public-alb-nacl
public_alb_network_acl = aws.ec2.NetworkAcl(
    resource_name = f'{project_name}-{environment}-{region}-public-alb-nacl',
    opts = ResourceOptions(depends_on = [ vpc ]),
    vpc_id = vpc.id,
    tags = {
        'Name': f'{project_name}-{environment}-{region}-public-alb-nacl',
        'Network': 'public',
        'Owner': owner,
        'Project': project_name,
        'Environment': environment,
    },
)

# Create inbound rule allowing traffic to port 80
inbound_public_alb_nacl_rule_allow_http = aws.ec2.NetworkAclRule(
    resource_name = 'inbound_public_alb_nacl_rule_allow_http',
    opts = ResourceOptions(depends_on = [ public_alb_network_acl ]),
    network_acl_id = public_alb_network_acl.id,
    rule_number = 200,
    egress = False,
    protocol = 'tcp',
    rule_action = 'allow',
    cidr_block = '0.0.0.0/0',
    from_port = 80,
    to_port = 80,
)

# Create inbound rule allowing traffic to port 443
inbound_public_alb_nacl_rule_allow_https = aws.ec2.NetworkAclRule(
    resource_name = 'inbound_public_alb_nacl_rule_allow_https',
    opts = ResourceOptions(depends_on = [ public_alb_network_acl ]),
    network_acl_id = public_alb_network_acl.id,
    rule_number = 300,
    egress = False,
    protocol = 'tcp',
    rule_action = 'allow',
    cidr_block = '0.0.0.0/0',
    from_port = 443,
    to_port = 443,
)

inbound_public_alb_nacl_rule_deny_mssql = aws.ec2.NetworkAclRule(
    resource_name = 'inbound_public_alb_nacl_rule_deny_mssql',
    opts = ResourceOptions(depends_on = [ public_alb_network_acl ]),
    network_acl_id = public_alb_network_acl.id,
    rule_number = 800,
    egress = False,
    protocol = 'tcp',
    rule_action = 'deny',
    cidr_block = '0.0.0.0/0',
    from_port = 1433,
    to_port = 1433,
)

inbound_public_alb_nacl_rule_deny_oracle = aws.ec2.NetworkAclRule(
    resource_name = 'inbound_public_alb_nacl_rule_deny_oracle',
    opts = ResourceOptions(depends_on = [ public_alb_network_acl ]),
    network_acl_id = public_alb_network_acl.id,
    rule_number = 810,
    egress = False,
    protocol = 'tcp',
    rule_action = 'deny',
    cidr_block = '0.0.0.0/0',
    from_port = 1521,
    to_port = 1521,
)

inbound_public_alb_nacl_rule_deny_mysql = aws.ec2.NetworkAclRule(
    resource_name = 'inbound_public_alb_nacl_rule_deny_mysql',
    opts = ResourceOptions(depends_on = [ public_alb_network_acl ]),
    network_acl_id = public_alb_network_acl.id,
    rule_number = 820,
    egress = False,
    protocol = 'tcp',
    rule_action = 'deny',
    cidr_block = '0.0.0.0/0',
    from_port = 3306,
    to_port = 3306,
)

inbound_public_alb_nacl_rule_deny_nfs = aws.ec2.NetworkAclRule(
    resource_name = 'inbound_public_alb_nacl_rule_deny_nfs',
    opts = ResourceOptions(depends_on = [ public_alb_network_acl ]),
    network_acl_id = public_alb_network_acl.id,
    rule_number = 830,
    egress = False,
    protocol = 'tcp',
    rule_action = 'deny',
    cidr_block = '0.0.0.0/0',
    from_port = 2049,
    to_port = 2049,
)
    
inbound_public_alb_nacl_rule_deny_rdp = aws.ec2.NetworkAclRule(
    resource_name = 'inbound_public_alb_nacl_rule_deny_rdp',
    opts = ResourceOptions(depends_on = [ public_alb_network_acl ]),
    network_acl_id = public_alb_network_acl.id,
    rule_number = 840,
    egress = False,
    protocol = 'tcp',
    rule_action = 'deny',
    cidr_block = '0.0.0.0/0',
    from_port = 3389,
    to_port = 3389,
)
  
inbound_public_alb_nacl_rule_deny_postgre = aws.ec2.NetworkAclRule(
    resource_name = 'inbound_public_alb_nacl_rule_deny_postgre',
    opts = ResourceOptions(depends_on = [ public_alb_network_acl ]),
    network_acl_id = public_alb_network_acl.id,
    rule_number = 850,
    egress = False,
    protocol = 'tcp',
    rule_action = 'deny',
    cidr_block = '0.0.0.0/0',
    from_port = 5432,
    to_port = 5432,
)

inbound_public_alb_nacl_rule_deny_ldap = aws.ec2.NetworkAclRule(
    resource_name = 'inbound_public_alb_nacl_rule_deny_ldap',
    opts = ResourceOptions(depends_on = [ public_alb_network_acl ]),
    network_acl_id = public_alb_network_acl.id,
    rule_number = 860,
    egress = False,
    protocol = 'tcp',
    rule_action = 'deny',
    cidr_block = '0.0.0.0/0',
    from_port = 631,
    to_port = 631,
)
       
inbound_public_alb_nacl_rule_deny_8080 = aws.ec2.NetworkAclRule(
    resource_name = 'inbound_public_alb_nacl_rule_deny_8080',
    opts = ResourceOptions(depends_on = [ public_alb_network_acl ]),
    network_acl_id = public_alb_network_acl.id,
    rule_number = 870,
    egress = False,
    protocol = 'tcp',
    rule_action = 'deny',
    cidr_block = '0.0.0.0/0',
    from_port = 8080,
    to_port = 8080,
)

inbound_public_alb_nacl_rule_deny_8443 = aws.ec2.NetworkAclRule(
    resource_name = 'inbound_public_alb_nacl_rule_deny_8443',
    opts = ResourceOptions(depends_on = [ public_alb_network_acl ]),
    network_acl_id = public_alb_network_acl.id,
    rule_number = 880,
    egress = False,
    protocol = 'tcp',
    rule_action = 'deny',
    cidr_block = '0.0.0.0/0',
    from_port = 8443,
    to_port = 8443,
)

inbound_ephemeral_vpc_alb_nacl_rule_allow_all1 = aws.ec2.NetworkAclRule(
    resource_name = 'inbound_ephemeral_vpc_alb_nacl_rule_allow_all1',
    opts = ResourceOptions(depends_on = [ public_alb_network_acl, private_app_subnet_az1 ]),
    network_acl_id = public_alb_network_acl.id,
    rule_number = 1100,
    egress = False,
    protocol = 'tcp',
    rule_action = 'allow',
    cidr_block = private_app_subnet_cidr_az1,
    from_port = 1024,
    to_port = 65535,
)

inbound_ephemeral_vpc_alb_nacl_rule_allow_all2 = aws.ec2.NetworkAclRule(
    resource_name = 'inbound_ephemeral_vpc_alb_nacl_rule_allow_all2',
    opts = ResourceOptions(depends_on = [ public_alb_network_acl, private_app_subnet_az2 ]),
    network_acl_id = public_alb_network_acl.id,
    rule_number = 1200,
    egress = False,
    protocol = 'tcp',
    rule_action = 'allow',
    cidr_block = private_app_subnet_cidr_az2,
    from_port = 1024,
    to_port = 65535,
)

inbound_ephemeral_vpc_alb_nacl_rule_allow_all3 = aws.ec2.NetworkAclRule(
    resource_name = 'inbound_ephemeral_vpc_alb_nacl_rule_allow_all3',
    opts = ResourceOptions(depends_on = [ public_alb_network_acl, private_app_subnet_az3 ]),
    network_acl_id = public_alb_network_acl.id,
    rule_number = 1300,
    egress = False,
    protocol = 'tcp',
    rule_action = 'allow',
    cidr_block = private_app_subnet_cidr_az3,
    from_port = 1024,
    to_port = 65535,
)

inbound_ephemeral_vpc_alb_nacl_rule_allow_all4 = aws.ec2.NetworkAclRule(
    resource_name = 'inbound_ephemeral_vpc_alb_nacl_rule_allow_all4',
    opts = ResourceOptions(depends_on = [ public_alb_network_acl, private_app_subnet_az4 ]),
    network_acl_id = public_alb_network_acl.id,
    rule_number = 1400,
    egress = False,
    protocol = 'tcp',
    rule_action = 'allow',
    cidr_block = private_app_subnet_cidr_az4,
    from_port = 1024,
    to_port = 65535,
)

# Create outbound rule allowing traffic from port 1024 to port 65535
outbound_ephemeral_alb_nacl_rule_allow_all = aws.ec2.NetworkAclRule(
    resource_name = 'outbound_ephemeral_alb_nacl_rule_allow_all',
    opts = ResourceOptions(depends_on = [ public_alb_network_acl ]),
    network_acl_id = public_alb_network_acl.id,
    rule_number = 1000,
    egress = True,
    protocol = 'tcp',
    rule_action = 'allow',
    cidr_block = '0.0.0.0/0',
    from_port = 1024,
    to_port = 65535,
)

outbound_vpc_alb_nacl_rule_allow_http1 = aws.ec2.NetworkAclRule(
    resource_name = 'outbound_vpc_alb_nacl_rule_allow_http1',
    opts = ResourceOptions(depends_on = [ public_alb_network_acl, private_app_subnet_az1 ]),
    network_acl_id = public_alb_network_acl.id,
    rule_number = 1100,
    egress = True,
    protocol = 'tcp',
    rule_action = 'allow',
    cidr_block = private_app_subnet_cidr_az1,
    from_port = 80,
    to_port = 80,
)

outbound_vpc_alb_nacl_rule_allow_http2 = aws.ec2.NetworkAclRule(
    resource_name = 'outbound_vpc_alb_nacl_rule_allow_http2',
    opts = ResourceOptions(depends_on = [ public_alb_network_acl, private_app_subnet_az2 ]),
    network_acl_id = public_alb_network_acl.id,
    rule_number = 1200,
    egress = True,
    protocol = 'tcp',
    rule_action = 'allow',
    cidr_block = private_app_subnet_cidr_az2,
    from_port = 80,
    to_port = 80,
)

outbound_vpc_alb_nacl_rule_allow_http3 = aws.ec2.NetworkAclRule(
    resource_name = 'outbound_vpc_alb_nacl_rule_allow_http3',
    opts = ResourceOptions(depends_on = [ public_alb_network_acl, private_app_subnet_az3 ]),
    network_acl_id = public_alb_network_acl.id,
    rule_number = 1300,
    egress = True,
    protocol = 'tcp',
    rule_action = 'allow',
    cidr_block = private_app_subnet_cidr_az3,
    from_port = 80,
    to_port = 80,
)

outbound_vpc_alb_nacl_rule_allow_http4 = aws.ec2.NetworkAclRule(
    resource_name = 'outbound_vpc_alb_nacl_rule_allow_http4',
    opts = ResourceOptions(depends_on = [ public_alb_network_acl, private_app_subnet_az4 ]),
    network_acl_id = public_alb_network_acl.id,
    rule_number = 1400,
    egress = True,
    protocol = 'tcp',
    rule_action = 'allow',
    cidr_block = private_app_subnet_cidr_az4,
    from_port = 80,
    to_port = 80,
)
  
outbound_vpc_alb_nacl_rule_allow_https1 = aws.ec2.NetworkAclRule(
    resource_name = 'outbound_vpc_alb_nacl_rule_allow_https1',
    opts = ResourceOptions(depends_on = [ public_alb_network_acl, private_app_subnet_az1 ]),
    network_acl_id = public_alb_network_acl.id,
    rule_number = 2100,
    egress = True,
    protocol = 'tcp',
    rule_action = 'allow',
    cidr_block = private_app_subnet_cidr_az1,
    from_port = 443,
    to_port = 443,
)

outbound_vpc_alb_nacl_rule_allow_https2 = aws.ec2.NetworkAclRule(
    resource_name = 'outbound_vpc_alb_nacl_rule_allow_https2',
    opts = ResourceOptions(depends_on = [ public_alb_network_acl, private_app_subnet_az2 ]),
    network_acl_id = public_alb_network_acl.id,
    rule_number = 2200,
    egress = True,
    protocol = 'tcp',
    rule_action = 'allow',
    cidr_block = private_app_subnet_cidr_az2,
    from_port = 443,
    to_port = 443,
)

outbound_vpc_alb_nacl_rule_allow_https3 = aws.ec2.NetworkAclRule(
    resource_name = 'outbound_vpc_alb_nacl_rule_allow_https3',
    opts = ResourceOptions(depends_on = [ public_alb_network_acl, private_app_subnet_az3 ]),
    network_acl_id = public_alb_network_acl.id,
    rule_number = 2300,
    egress = True,
    protocol = 'tcp',
    rule_action = 'allow',
    cidr_block = private_app_subnet_cidr_az3,
    from_port = 443,
    to_port = 443,
)

outbound_vpc_alb_nacl_rule_allow_https4 = aws.ec2.NetworkAclRule(
    resource_name = 'outbound_vpc_alb_nacl_rule_allow_https4',
    opts = ResourceOptions(depends_on = [ public_alb_network_acl, private_app_subnet_az4 ]),
    network_acl_id = public_alb_network_acl.id,
    rule_number = 2400,
    egress = True,
    protocol = 'tcp',
    rule_action = 'allow',
    cidr_block = private_app_subnet_cidr_az4,
    from_port = 443,
    to_port = 443,
)

# Public Alb Subnet Association
public_alb_subnet_nacl_association1 = aws.ec2.NetworkAclAssociation(
    resource_name = 'public_alb_subnet_nacl_association1',
    opts = ResourceOptions(depends_on = [ public_alb_network_acl, public_alb_subnet_az1]),
    network_acl_id = public_alb_network_acl.id,
    subnet_id = public_alb_subnet_az1.id,
)

public_alb_subnet_nacl_association2 = aws.ec2.NetworkAclAssociation(
    resource_name = 'public_alb_subnet_nacl_association2',
    opts = ResourceOptions(depends_on = [ public_alb_network_acl, public_alb_subnet_az2 ]),
    network_acl_id = public_alb_network_acl.id,
    subnet_id = public_alb_subnet_az2.id,
)

public_alb_subnet_nacl_association3 = aws.ec2.NetworkAclAssociation(
    resource_name = 'public_alb_subnet_nacl_association3',
    opts = ResourceOptions(depends_on = [ public_alb_network_acl, public_alb_subnet_az3 ]),
    network_acl_id = public_alb_network_acl.id,
    subnet_id = public_alb_subnet_az3.id,
)

public_alb_subnet_nacl_association4 = aws.ec2.NetworkAclAssociation(
    resource_name = 'public_alb_subnet_nacl_association4',
    opts = ResourceOptions(depends_on = [ public_alb_network_acl, public_alb_subnet_az4 ]),
    network_acl_id = public_alb_network_acl.id,
    subnet_id = public_alb_subnet_az4.id,
)