import pulumi_aws as aws
from pulumi import ResourceOptions
from pulumi_aws.config import region

from config import (
    project_name,
    environment,
    owner,
    availability_zone_az1,
    availability_zone_az2,
    availability_zone_az3,
    availability_zone_az4, 
)

from resources.vpc.vpc_4azs import (
    internet_gateway,
    public_shared_subnet_az1,
    public_shared_subnet_az2,
    public_shared_subnet_az3,
    public_shared_subnet_az4,
    route_table_private_app_az1,
    route_table_private_app_az2,
    route_table_private_app_az3,
    route_table_private_app_az4,
)


# The NAT IP for the public shared subnet, as seen from within the public one
# ej. project-dev-us-east-1a-public-shared-ip
shared_nat_eip_az1 = aws.ec2.Eip(
    resource_name = f'{project_name}-{environment}-{availability_zone_az1}-public-shared-ip',
    opts = ResourceOptions(depends_on = [ internet_gateway ]),
    vpc = True,    
    tags = {
        'Name': f'{project_name}-{environment}-{availability_zone_az1}-public-shared-ip',
        'Network': 'public',
        'Owner': owner,
        'Project': project_name,
        'Environment': environment,
    },
)

# ej. project-dev-us-east-1b-public-shared-ip
shared_nat_eip_az2 = aws.ec2.Eip(
    resource_name = f'{project_name}-{environment}-{availability_zone_az2}-public-shared-ip',
    opts = ResourceOptions(depends_on = [ internet_gateway ]),
    vpc = True,    
    tags = {
        'Name': f'{project_name}-{environment}-{availability_zone_az2}-public-shared-ip',
        'Network': 'public',
        'Owner': owner,
        'Project': project_name,
        'Environment': environment,
    },
)

# ej. project-dev-us-east-1c-public-shared-ip
shared_nat_eip_az3 = aws.ec2.Eip(
    resource_name = f'{project_name}-{environment}-{availability_zone_az3}-public-shared-ip',
    opts = ResourceOptions(depends_on = [ internet_gateway ]),
    vpc = True,
    tags = {
        'Name': f'{project_name}-{environment}-{availability_zone_az3}-public-shared-ip',
        'Network': 'public',
        'Owner': owner,
        'Project': project_name,
        'Environment': environment,
    },
)

# ej. project-dev-us-east-1d-public-shared-ip
shared_nat_eip_az4 = aws.ec2.Eip(
    resource_name = f'{project_name}-{environment}-{availability_zone_az4}-public-shared-ip',
    opts = ResourceOptions(depends_on = [ internet_gateway ]),
    vpc = True,
    tags = {
        'Name': f'{project_name}-{environment}-{availability_zone_az4}-public-shared-ip',
        'Network': 'public',
        'Owner': owner,
        'Project': project_name,
        'Environment': environment,
    },
)

############## Create NAT Gateway ##############
# The NAT gateway for the private shared  subnet
# ej. project-dev-us-east-1a-nat-gw
nat_gateway_az1 = aws.ec2.NatGateway(
    resource_name = f'{project_name}-{environment}-{availability_zone_az1}-nat-gw',
    opts = ResourceOptions(depends_on = [ public_shared_subnet_az1 ]),
    allocation_id = shared_nat_eip_az1.id,
    subnet_id = public_shared_subnet_az1.id,
    tags={
        'Name': f'{project_name}-{environment}-{availability_zone_az1}-nat-gw',
        'Network': 'public',
        'Owner': owner,
        'Project': project_name,
        'Environment': environment,
    },
)

# ej. project-dev-us-east-1b-nat-gw
nat_gateway_az2 = aws.ec2.NatGateway(
    resource_name = f'{project_name}-{environment}-{availability_zone_az2}-nat-gw',
    opts = ResourceOptions(depends_on = [ public_shared_subnet_az2 ]),
    allocation_id = shared_nat_eip_az2.id,
    subnet_id = public_shared_subnet_az2.id,    
    tags={
        'Name': f'{project_name}-{environment}-{availability_zone_az2}-nat-gw',
        'Network': 'public',
        'Owner': owner,
        'Project': project_name,
        'Environment': environment,
    },
)

# ej. project-dev-us-east-1c-nat-gw
nat_gateway_az3 = aws.ec2.NatGateway(
    resource_name = f'{project_name}-{environment}-{availability_zone_az3}-nat-gw',
    opts = ResourceOptions(depends_on = [ public_shared_subnet_az3 ]),
    allocation_id = shared_nat_eip_az3.id,
    subnet_id = public_shared_subnet_az3.id,
    tags={
        'Name': f'{project_name}-{environment}-{availability_zone_az3}-nat-gw',
        'Network': 'public',
        'Owner': owner,
        'Project': project_name,
        'Environment': environment,
    },
)

# ej. project-dev-us-east-1d-nat-gw
nat_gateway_az4 = aws.ec2.NatGateway(
    resource_name = f'{project_name}-{environment}-{availability_zone_az4}-nat-gw',
    opts = ResourceOptions(depends_on = [ public_shared_subnet_az4 ]),
    allocation_id = shared_nat_eip_az4.id,
    subnet_id = public_shared_subnet_az4.id,    
    tags={
        'Name': f'{project_name}-{environment}-{availability_zone_az4}-nat-gw',
        'Network': 'public',
        'Owner': owner,
        'Project': project_name,
        'Environment': environment,
    },
)

route_table_private_app_internet_route_az1 = aws.ec2.Route(
    resource_name = f'{project_name}-{environment}-{availability_zone_az1}-app-route',
    opts = ResourceOptions(depends_on = [ nat_gateway_az1 ]),
    destination_cidr_block = '0.0.0.0/0',
    gateway_id = nat_gateway_az1.id,
    route_table_id = route_table_private_app_az1.id,
)

route_table_private_app_internet_route_az2 = aws.ec2.Route(
    resource_name = f'{project_name}-{environment}-{availability_zone_az2}-app-route',
    opts = ResourceOptions(depends_on = [ nat_gateway_az2 ]),
    destination_cidr_block = '0.0.0.0/0',
    gateway_id = nat_gateway_az2.id,
    route_table_id = route_table_private_app_az2.id,    
)

route_table_private_app_internet_route_az3 = aws.ec2.Route(
    resource_name = f'{project_name}-{environment}-{availability_zone_az3}-app-route',
    opts = ResourceOptions(depends_on = [ nat_gateway_az3 ]),
    destination_cidr_block = '0.0.0.0/0',
    gateway_id = nat_gateway_az3.id,
    route_table_id = route_table_private_app_az3.id,
)

route_table_private_app_internet_route_az4 = aws.ec2.Route(
    resource_name = f'{project_name}-{environment}-{availability_zone_az4}-app-route',
    opts = ResourceOptions(depends_on = [ nat_gateway_az4 ]),
    destination_cidr_block = '0.0.0.0/0',
    gateway_id = nat_gateway_az4.id,
    route_table_id = route_table_private_app_az4.id,
)