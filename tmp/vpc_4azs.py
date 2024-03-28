import pulumi_aws as aws
from pulumi import ResourceOptions
from pulumi_aws.config import region

from config import (
    project_name,
    environment,
    owner,
    vpc_cidr,
    availability_zone_az1,
    availability_zone_az2,
    availability_zone_az3,
    availability_zone_az4,
    public_alb_subnet_cidr_az1,
    public_alb_subnet_cidr_az2,
    public_alb_subnet_cidr_az3,
    public_alb_subnet_cidr_az4,
    public_shared_subnet_cidr_az1,
    public_shared_subnet_cidr_az2,
    public_shared_subnet_cidr_az3,
    public_shared_subnet_cidr_az4,
    private_app_subnet_cidr_az1,
    private_app_subnet_cidr_az2,
    private_app_subnet_cidr_az3,
    private_app_subnet_cidr_az4,
    private_db_subnet_cidr_az1,
    private_db_subnet_cidr_az2,
    private_db_subnet_cidr_az3,
    private_db_subnet_cidr_az4,
    private_keycloak_subnet_cidr_az1,
    private_keycloak_subnet_cidr_az2,
    private_keycloak_subnet_cidr_az3,
    private_keycloak_subnet_cidr_az4,
    private_kafka_subnet_cidr_az1,
    private_kafka_subnet_cidr_az2,
    private_kafka_subnet_cidr_az3,
    private_kafka_subnet_cidr_az4,
    private_cache_subnet_cidr_az1,
    private_cache_subnet_cidr_az2,
    private_cache_subnet_cidr_az3,
    private_cache_subnet_cidr_az4,
    private_spare_subnet_cidr_az1,
    private_spare_subnet_cidr_az2,
    private_spare_subnet_cidr_az3,
    private_spare_subnet_cidr_az4,
)

## 01. VPC
## 02. Four Availability Zones
## 03. Subnet for Application Load Balancer.
## 04. Subnet for Shared Services.
## 05. Subnet for Application.
## 06. Subnet for Database.
## 07. Subnet for Keycloak.
## 08. Subnet for Kafka.
## 09. Subnet for Cache.
## 10. Subnet for Spare.
## 11. Internet Gateway, with a default route on the public subnets.
## 12. NAT Gateways in Subnet Shared (one in each AZ).


############## Create VPC ##############
# projectName-environmentName-aws:region-vpc
# ej. project-dev-us-east-1-vpc
vpc = aws.ec2.Vpc(
    resource_name = f'{project_name}-{environment}-{region}-vpc',
    cidr_block = vpc_cidr,    
    enable_dns_hostnames = True,
    enable_dns_support = True,
    instance_tenancy = 'default',
    tags={
        'Name': f'{project_name}-{environment}-{region}-vpc',
        'Owner': owner,
        'Project': project_name,
        'Environment': environment,        
    },
)

############## Create Subnet ##############
# projectName-environmentName-aws-availabilityZone1-public-subnet
# ej. project-dev-us-east-1a-public-subnet-alb
public_alb_subnet_az1 = aws.ec2.Subnet(
    resource_name = f'{project_name}-{environment}-{availability_zone_az1}-public-subnet-alb',
    opts = ResourceOptions(depends_on = [ vpc ]),
    cidr_block = public_alb_subnet_cidr_az1,
    vpc_id = vpc.id,
    map_public_ip_on_launch = False,
    availability_zone = availability_zone_az1,    
    tags={
        'Name': f'{project_name}-{environment}-{availability_zone_az1}-public-subnet-alb',
        'Network': 'public',
        'Owner': owner,
        'Project': project_name,
        'Environment': environment,
        f'kubernetes.io/cluster/{project_name}-{environment}-{region}-eks-cluster': 'shared',
        'kubernetes.io/role/elb': '1',
    }
)

# projectName-environmentName-aws-availabilityZone2-public-subnet
# ej. project-dev-us-east-1b-public-subnet-alb
public_alb_subnet_az2 = aws.ec2.Subnet(
    resource_name = f'{project_name}-{environment}-{availability_zone_az2}-public-subnet-alb',
    opts = ResourceOptions(depends_on = [ vpc ]),
    cidr_block = public_alb_subnet_cidr_az2,
    vpc_id = vpc.id,
    map_public_ip_on_launch = False,
    availability_zone = availability_zone_az2,    
    tags={
        'Name': f'{project_name}-{environment}-{availability_zone_az2}-public-subnet-alb',
        'Network': 'public',
        'Owner': owner,
        'Project': project_name,
        'Environment': environment,
        f'kubernetes.io/cluster/{project_name}-{environment}-{region}-eks-cluster': 'shared',
        'kubernetes.io/role/elb': '1',
    }
)

# projectName-environmentName-aws-availabilityZone3-public-subnet
# ej. project-dev-us-east-1c-public-subnet-alb
public_alb_subnet_az3 = aws.ec2.Subnet(
    resource_name = f'{project_name}-{environment}-{availability_zone_az3}-public-subnet-alb',
    opts = ResourceOptions(depends_on = [ vpc ]),
    cidr_block = public_alb_subnet_cidr_az3,
    vpc_id = vpc.id,
    map_public_ip_on_launch = False,
    availability_zone = availability_zone_az3,    
    tags={
        'Name': f'{project_name}-{environment}-{availability_zone_az3}-public-subnet-alb',
        'Network': 'public',
        'Owner': owner,
        'Project': project_name,
        'Environment': environment,
        f'kubernetes.io/cluster/{project_name}-{environment}-{region}-eks-cluster': 'shared',
        'kubernetes.io/role/elb': '1',
    }
)

# projectName-environmentName-aws-availabilityZone4-public-subnet
# ej. project-dev-us-east-1d-public-subnet-alb
public_alb_subnet_az4 = aws.ec2.Subnet(
    resource_name = f'{project_name}-{environment}-{availability_zone_az4}-public-subnet-alb',
    opts = ResourceOptions(depends_on = [ vpc ]),
    cidr_block = public_alb_subnet_cidr_az4,
    vpc_id = vpc.id,
    map_public_ip_on_launch = False,
    availability_zone = availability_zone_az4,    
    tags={
        'Name': f'{project_name}-{environment}-{availability_zone_az4}-public-subnet-alb',
        'Network': 'public',
        'Owner': owner,
        'Project': project_name,
        'Environment': environment,
        f'kubernetes.io/cluster/{project_name}-{environment}-{region}-eks-cluster': 'shared',
        'kubernetes.io/role/elb': '1',
    }
)

# projectName-environmentName-aws-availabilityZone1-public-subnet
# ej. project-dev-us-east-1a-public-subnet-shared
public_shared_subnet_az1 = aws.ec2.Subnet(
    resource_name = f'{project_name}-{environment}-{availability_zone_az1}-public-subnet-shared',
    opts = ResourceOptions(depends_on = [ vpc ]),
    cidr_block = public_shared_subnet_cidr_az1,
    vpc_id = vpc.id,
    map_public_ip_on_launch = False,
    availability_zone = availability_zone_az1,    
    tags={
        'Name': f'{project_name}-{environment}-{availability_zone_az1}-public-subnet-shared',
        'Network': 'public',
        'Owner': owner,
        'Project': project_name,
        'Environment': environment,
    }
)

# projectName-environmentName-aws-availabilityZone2-public-subnet
# ej. project-dev-us-east-1b-public-subnet-shared
public_shared_subnet_az2 = aws.ec2.Subnet(
    resource_name = f'{project_name}-{environment}-{availability_zone_az2}-public-subnet-shared',
    opts = ResourceOptions(depends_on = [ vpc ]),
    cidr_block = public_shared_subnet_cidr_az2,
    vpc_id = vpc.id,
    map_public_ip_on_launch = False,
    availability_zone = availability_zone_az2,    
    tags={
        'Name': f'{project_name}-{environment}-{availability_zone_az2}-public-subnet-shared',
        'Network': 'public',
        'Owner': owner,
        'Project': project_name,
        'Environment': environment,
    }
)

# projectName-environmentName-aws-availabilityZone3-public-subnet
# ej. project-dev-us-east-1c-public-subnet-shared
public_shared_subnet_az3 = aws.ec2.Subnet(
    resource_name = f'{project_name}-{environment}-{availability_zone_az3}-public-subnet-shared',
    opts = ResourceOptions(depends_on = [ vpc ]),
    cidr_block = public_shared_subnet_cidr_az3,
    vpc_id = vpc.id,
    map_public_ip_on_launch = False,
    availability_zone = availability_zone_az3,    
    tags={
        'Name': f'{project_name}-{environment}-{availability_zone_az3}-public-subnet-shared',
        'Network': 'public',
        'Owner': owner,
        'Project': project_name,
        'Environment': environment,
    }
)

# projectName-environmentName-aws-availabilityZone4-public-subnet
# ej. project-dev-us-east-1d-public-subnet-shared
public_shared_subnet_az4 = aws.ec2.Subnet(
    resource_name = f'{project_name}-{environment}-{availability_zone_az4}-public-subnet-shared',
    opts = ResourceOptions(depends_on = [ vpc ]),
    cidr_block = public_shared_subnet_cidr_az4,
    vpc_id = vpc.id,
    map_public_ip_on_launch = False,
    availability_zone = availability_zone_az4,    
    tags={
        'Name': f'{project_name}-{environment}-{availability_zone_az4}-public-subnet-shared',
        'Network': 'public',
        'Owner': owner,
        'Project': project_name,
        'Environment': environment,
    }
)

# projectName-environmentName-aws-availabilityZone1-private-subnet-app
# ej. project-dev-us-east-1a-private-subnet-app
private_app_subnet_az1 = aws.ec2.Subnet(
    resource_name = f'{project_name}-{environment}-{availability_zone_az1}-private-subnet-app',
    opts = ResourceOptions(depends_on = [ vpc ]),
    cidr_block = private_app_subnet_cidr_az1,
    vpc_id = vpc.id,
    map_public_ip_on_launch = False,
    availability_zone = availability_zone_az1,    
    tags={
        'Name': f'{project_name}-{environment}-{availability_zone_az1}-private-subnet-app',
        'Network': 'private',
        'Owner': owner,
        'Project': project_name,
        'Environment': environment,
        f'kubernetes.io/cluster/{project_name}-{environment}-{region}-eks-cluster': 'shared',
        'kubernetes.io/role/internal-elb': 1,
    }
)

# projectName-environmentName-aws-availabilityZone2-private-subnet-app
# ej. project-dev-us-east-1b-private-subnet-app
private_app_subnet_az2 = aws.ec2.Subnet(
    resource_name = f'{project_name}-{environment}-{availability_zone_az2}-private-subnet-app',
    opts = ResourceOptions(depends_on = [ vpc ]),
    cidr_block = private_app_subnet_cidr_az2,
    vpc_id = vpc.id,
    map_public_ip_on_launch = False,
    availability_zone = availability_zone_az2,
    tags={
        'Name': f'{project_name}-{environment}-{availability_zone_az2}-private-subnet-app',
        'Network': 'private',
        'Owner': owner,
        'Project': project_name,
        'Environment': environment,
        f'kubernetes.io/cluster/{project_name}-{environment}-{region}-eks-cluster': 'shared',
        'kubernetes.io/role/internal-elb': 1,
    }
)

# projectName-environmentName-aws-availabilityZone3-private-subnet-app
# ej. project-dev-us-east-1c-private-subnet-app
private_app_subnet_az3 = aws.ec2.Subnet(
    resource_name = f'{project_name}-{environment}-{availability_zone_az3}-private-subnet-app',
    opts = ResourceOptions(depends_on = [ vpc ]),
    cidr_block = private_app_subnet_cidr_az3,
    vpc_id = vpc.id,
    map_public_ip_on_launch = False,
    availability_zone = availability_zone_az3,    
    tags={
        'Name': f'{project_name}-{environment}-{availability_zone_az3}-private-subnet-app',
        'Network': 'private',
        'Owner': owner,
        'Project': project_name,
        'Environment': environment,
        f'kubernetes.io/cluster/{project_name}-{environment}-{region}-eks-cluster': 'shared',
        'kubernetes.io/role/internal-elb': 1,
    }
)

# projectName-environmentName-aws-availabilityZone4-private-subnet-app
# ej. project-dev-us-east-1d-private-subnet-app
private_app_subnet_az4 = aws.ec2.Subnet(
    resource_name = f'{project_name}-{environment}-{availability_zone_az4}-private-subnet-app',
    opts = ResourceOptions(depends_on = [ vpc ]),
    cidr_block = private_app_subnet_cidr_az4,
    vpc_id = vpc.id,
    map_public_ip_on_launch = False,
    availability_zone = availability_zone_az4,
    tags={
        'Name': f'{project_name}-{environment}-{availability_zone_az4}-private-subnet-app',
        'Network': 'private',
        'Owner': owner,
        'Project': project_name,
        'Environment': environment,
        f'kubernetes.io/cluster/{project_name}-{environment}-{region}-eks-cluster': 'shared',
        'kubernetes.io/role/internal-elb': 1,
    }
)

# projectName-environmentName-aws-availabilityZone1-private-subnet-db
# ej. project-dev-us-east-1a-private-subnet-db
private_db_subnet_az1 = aws.ec2.Subnet(
    resource_name = f'{project_name}-{environment}-{availability_zone_az1}-private-subnet-db',
    opts = ResourceOptions(depends_on = [ vpc ]),
    cidr_block = private_db_subnet_cidr_az1,
    vpc_id = vpc.id,
    map_public_ip_on_launch = False,
    availability_zone = availability_zone_az1,    
    tags={
        'Name': f'{project_name}-{environment}-{availability_zone_az1}-private-subnet-db',
        'Network': 'private',
        'Owner': owner,
        'Project': project_name,
        'Environment': environment,
    }
)

# projectName-environmentName-aws-availabilityZone2-private-subnet-db
# ej. project-dev-us-east-1b-private-subnet-db
private_db_subnet_az2 = aws.ec2.Subnet(
    resource_name = f'{project_name}-{environment}-{availability_zone_az2}-private-subnet-db',
    opts = ResourceOptions(depends_on = [ vpc ]),
    cidr_block = private_db_subnet_cidr_az2,
    vpc_id = vpc.id,
    map_public_ip_on_launch = False,
    availability_zone = availability_zone_az2,    
    tags={
        'Name': f'{project_name}-{environment}-{availability_zone_az2}-private-subnet-db',
        'Network': 'private',
        'Owner': owner,
        'Project': project_name,
        'Environment': environment,
    }
)

# projectName-environmentName-aws-availabilityZone3-private-subnet-db
# ej. project-dev-us-east-1c-private-subnet-db
private_db_subnet_az3 = aws.ec2.Subnet(
    resource_name = f'{project_name}-{environment}-{availability_zone_az3}-private-subnet-db',
    opts = ResourceOptions(depends_on = [ vpc ]),
    cidr_block = private_db_subnet_cidr_az3,
    vpc_id = vpc.id,
    map_public_ip_on_launch = False,
    availability_zone = availability_zone_az3,    
    tags={
        'Name': f'{project_name}-{environment}-{availability_zone_az3}-private-subnet-db',
        'Network': 'private',
        'Owner': owner,
        'Project': project_name,
        'Environment': environment,
    }
)

# projectName-environmentName-aws-availabilityZone4-private-subnet-db
# ej. project-dev-us-east-1d-private-subnet-db
private_db_subnet_az4 = aws.ec2.Subnet(
    resource_name = f'{project_name}-{environment}-{availability_zone_az4}-private-subnet-db',
    opts = ResourceOptions(depends_on = [ vpc ]),
    cidr_block = private_db_subnet_cidr_az4,
    vpc_id = vpc.id,
    map_public_ip_on_launch = False,
    availability_zone = availability_zone_az4,
    tags={
        'Name': f'{project_name}-{environment}-{availability_zone_az4}-private-subnet-db',
        'Network': 'private',
        'Owner': owner,
        'Project': project_name,
        'Environment': environment,
    }
)

# projectName-environmentName-aws-availabilityZone1-private-subnet-kc
# ej. project-dev-us-east-1a-private-subnet-kc
private_keycloak_subnet_az1 = aws.ec2.Subnet(
    resource_name = f'{project_name}-{environment}-{availability_zone_az1}-private-subnet-kc',
    opts = ResourceOptions(depends_on = [ vpc ]),
    cidr_block = private_keycloak_subnet_cidr_az1,
    vpc_id = vpc.id,
    map_public_ip_on_launch = False,
    availability_zone = availability_zone_az1,
    tags={
        'Name': f'{project_name}-{environment}-{availability_zone_az1}-private-subnet-kc',
        'Network': 'private',
        'Owner': owner,
        'Project': project_name,
        'Environment': environment,
    }
)

# projectName-environmentName-aws-availabilityZone2-private-subnet-kc
# ej. project-dev-us-east-1b-private-subnet-kc
private_keycloak_subnet_az2 = aws.ec2.Subnet(
    resource_name = f'{project_name}-{environment}-{availability_zone_az2}-private-subnet-kc',
    opts = ResourceOptions(depends_on = [ vpc ]),
    cidr_block = private_keycloak_subnet_cidr_az2,
    vpc_id = vpc.id,
    map_public_ip_on_launch = False,
    availability_zone = availability_zone_az2,
    tags={
        'Name': f'{project_name}-{environment}-{availability_zone_az2}-private-subnet-kc',
        'Network': 'private',
        'Owner': owner,
        'Project': project_name,
        'Environment': environment,
    }
)

# projectName-environmentName-aws-availabilityZone3-private-subnet-kc
# ej. project-dev-us-east-1c-private-subnet-kc
private_keycloak_subnet_az3 = aws.ec2.Subnet(
    resource_name = f'{project_name}-{environment}-{availability_zone_az3}-private-subnet-kc',
    opts = ResourceOptions(depends_on = [ vpc ]),
    cidr_block = private_keycloak_subnet_cidr_az3,
    vpc_id = vpc.id,
    map_public_ip_on_launch = False,
    availability_zone = availability_zone_az3,
    tags={
        'Name': f'{project_name}-{environment}-{availability_zone_az3}-private-subnet-kc',
        'Network': 'private',
        'Owner': owner,
        'Project': project_name,
        'Environment': environment,
    }
)

# projectName-environmentName-aws-availabilityZone4-private-subnet-kc
# ej. project-dev-us-east-1d-private-subnet-kc
private_keycloak_subnet_az4 = aws.ec2.Subnet(
    resource_name = f'{project_name}-{environment}-{availability_zone_az4}-private-subnet-kc',
    opts = ResourceOptions(depends_on = [ vpc ]),
    cidr_block = private_keycloak_subnet_cidr_az4,
    vpc_id = vpc.id,
    map_public_ip_on_launch = False,
    availability_zone = availability_zone_az4,
    tags={
        'Name': f'{project_name}-{environment}-{availability_zone_az4}-private-subnet-kc',
        'Network': 'private',
        'Owner': owner,
        'Project': project_name,
        'Environment': environment,
    }
)

# projectName-environmentName-aws-availabilityZone1-private-subnet-kafka
# ej. project-dev-us-east-1a-private-subnet-kafka
private_kafka_subnet_az1 = aws.ec2.Subnet(
    resource_name = f'{project_name}-{environment}-{availability_zone_az1}-private-subnet-kafka',
    opts = ResourceOptions(depends_on = [ vpc ]),
    cidr_block = private_kafka_subnet_cidr_az1,
    vpc_id = vpc.id,
    map_public_ip_on_launch = False,
    availability_zone = availability_zone_az1,    
    tags={
        'Name': f'{project_name}-{environment}-{availability_zone_az1}-private-subnet-kafka',
        'Network': 'private',
        'Owner': owner,
        'Project': project_name,
        'Environment': environment,
    }
)

# projectName-environmentName-aws-availabilityZone2-private-subnet-kafka
# ej. project-dev-us-east-1b-private-subnet-kafka
private_kafka_subnet_az2 = aws.ec2.Subnet(
    resource_name = f'{project_name}-{environment}-{availability_zone_az2}-private-subnet-kafka',
    opts = ResourceOptions(depends_on = [ vpc ]),
    cidr_block = private_kafka_subnet_cidr_az2,
    vpc_id = vpc.id,
    map_public_ip_on_launch = False,
    availability_zone = availability_zone_az2,
    tags={
        'Name': f'{project_name}-{environment}-{availability_zone_az2}-private-subnet-kafka',
        'Network': 'private',
        'Owner': owner,
        'Project': project_name,
        'Environment': environment,
    }
)

# projectName-environmentName-aws-availabilityZone3-private-subnet-kafka
# ej. project-dev-us-east-1c-private-subnet-kafka
private_kafka_subnet_az3 = aws.ec2.Subnet(
    resource_name = f'{project_name}-{environment}-{availability_zone_az3}-private-subnet-kafka',
    opts = ResourceOptions(depends_on = [ vpc ]),
    cidr_block = private_kafka_subnet_cidr_az3,
    vpc_id = vpc.id,
    map_public_ip_on_launch = False,
    availability_zone = availability_zone_az3,
    tags={
        'Name': f'{project_name}-{environment}-{availability_zone_az3}-private-subnet-kafka',
        'Network': 'private',
        'Owner': owner,
        'Project': project_name,
        'Environment': environment,
    }
)

# projectName-environmentName-aws-availabilityZone4-private-subnet-kafka
# ej. project-dev-us-east-1d-private-subnet-kafka
private_kafka_subnet_az4 = aws.ec2.Subnet(
    resource_name = f'{project_name}-{environment}-{availability_zone_az4}-private-subnet-kafka',
    opts = ResourceOptions(depends_on = [ vpc ]),
    cidr_block = private_kafka_subnet_cidr_az4,
    vpc_id = vpc.id,
    map_public_ip_on_launch = False,
    availability_zone = availability_zone_az4,
    tags={
        'Name': f'{project_name}-{environment}-{availability_zone_az4}-private-subnet-kafka',
        'Network': 'private',
        'Owner': owner,
        'Project': project_name,
        'Environment': environment,
    }
)

# projectName-environmentName-aws-availabilityZone1-private-subnet-cache
# ej. project-dev-us-east-1a-private-subnet-cache
private_cache_subnet_az1 = aws.ec2.Subnet(
    resource_name = f'{project_name}-{environment}-{availability_zone_az1}-private-subnet-cache',
    opts = ResourceOptions(depends_on = [ vpc ]),
    cidr_block = private_cache_subnet_cidr_az1,
    vpc_id = vpc.id,
    map_public_ip_on_launch = False,
    availability_zone = availability_zone_az1,
    tags={
        'Name': f'{project_name}-{environment}-{availability_zone_az1}-private-subnet-cache',
        'Network': 'private',
        'Owner': owner,
        'Project': project_name,
        'Environment': environment,
    }
)

# projectName-environmentName-aws-availabilityZone2-private-subnet-cache
# ej. project-dev-us-east-1b-private-subnet-cache
private_cache_subnet_az2 = aws.ec2.Subnet(
    resource_name = f'{project_name}-{environment}-{availability_zone_az2}-private-subnet-cache',
    opts = ResourceOptions(depends_on = [ vpc ]),
    cidr_block = private_cache_subnet_cidr_az2,
    vpc_id = vpc.id,
    map_public_ip_on_launch = False,
    availability_zone = availability_zone_az2,
    tags={
        'Name': f'{project_name}-{environment}-{availability_zone_az2}-private-subnet-cache',
        'Network': 'private',
        'Owner': owner,
        'Project': project_name,
        'Environment': environment,
    }
)

# projectName-environmentName-aws-availabilityZone3-private-subnet-cache
# ej. project-dev-us-east-1c-private-subnet-cache
private_cache_subnet_az3 = aws.ec2.Subnet(
    resource_name = f'{project_name}-{environment}-{availability_zone_az3}-private-subnet-cache',
    opts = ResourceOptions(depends_on = [ vpc ]),
    cidr_block = private_cache_subnet_cidr_az3,
    vpc_id = vpc.id,
    map_public_ip_on_launch = False,
    availability_zone = availability_zone_az3,
    tags={
        'Name': f'{project_name}-{environment}-{availability_zone_az3}-private-subnet-cache',
        'Network': 'private',
        'Owner': owner,
        'Project': project_name,
        'Environment': environment,
    }
)

# projectName-environmentName-aws-availabilityZone4-private-subnet-cache
# ej. project-dev-us-east-1d-private-subnet-cache
private_cache_subnet_az4 = aws.ec2.Subnet(
    resource_name = f'{project_name}-{environment}-{availability_zone_az4}-private-subnet-cache',
    opts = ResourceOptions(depends_on = [ vpc ]),
    cidr_block=private_cache_subnet_cidr_az4,
    vpc_id = vpc.id,
    map_public_ip_on_launch = False,
    availability_zone = availability_zone_az4,
    tags={
        'Name': f'{project_name}-{environment}-{availability_zone_az4}-private-subnet-cache',
        'Network': 'private',
        'Owner': owner,
        'Project': project_name,
        'Environment': environment,
    }
)

# projectName-environmentName-aws-availabilityZone1-private-subnet-spare
# ej. project-dev-us-east-1a-private-subnet-spare
private_spare_subnet_az1 = aws.ec2.Subnet(
    resource_name = f'{project_name}-{environment}-{availability_zone_az1}-private-subnet-spare',
    opts = ResourceOptions(depends_on = [ vpc ]),
    cidr_block = private_spare_subnet_cidr_az1,
    vpc_id = vpc.id,
    map_public_ip_on_launch = False,
    availability_zone = availability_zone_az1,
    tags={
        'Name': f'{project_name}-{environment}-{availability_zone_az1}-private-subnet-spare',
        'Network': 'private',
        'Owner': owner,
        'Project': project_name,
        'Environment': environment,
    }
)

# projectName-environmentName-aws-availabilityZone2-private-subnet-spare
# ej. project-dev-us-east-1b-private-subnet-spare
private_spare_subnet_az2 = aws.ec2.Subnet(
    resource_name = f'{project_name}-{environment}-{availability_zone_az2}-private-subnet-spare',
    opts = ResourceOptions(depends_on = [ vpc ]),
    cidr_block = private_spare_subnet_cidr_az2,
    vpc_id = vpc.id,
    map_public_ip_on_launch = False,
    availability_zone = availability_zone_az2,
    tags={
        'Name': f'{project_name}-{environment}-{availability_zone_az2}-private-subnet-spare',
        'Network': 'private',
        'Owner': owner,
        'Project': project_name,
        'Environment': environment,
    }
)

# projectName-environmentName-aws-availabilityZone3-private-subnet-spare
# ej. project-dev-us-east-1c-private-subnet-spare
private_spare_subnet_az3 = aws.ec2.Subnet(
    resource_name = f'{project_name}-{environment}-{availability_zone_az3}-private-subnet-spare',
    opts = ResourceOptions(depends_on = [ vpc ]),
    cidr_block = private_spare_subnet_cidr_az3,
    vpc_id = vpc.id,
    map_public_ip_on_launch = False,
    availability_zone = availability_zone_az3,
    tags={
        'Name': f'{project_name}-{environment}-{availability_zone_az3}-private-subnet-spare',
        'Network': 'private',
        'Owner': owner,
        'Project': project_name,
        'Environment': environment,
    }
)

# projectName-environmentName-aws-availabilityZone4-private-subnet-spare
# ej. project-dev-us-east-1d-private-subnet-spare
private_spare_subnet_az4 = aws.ec2.Subnet(
    resource_name = f'{project_name}-{environment}-{availability_zone_az4}-private-subnet-spare',
    opts = ResourceOptions(depends_on = [ vpc ]),
    cidr_block = private_spare_subnet_cidr_az4,
    vpc_id = vpc.id,
    map_public_ip_on_launch = False,
    availability_zone = availability_zone_az4,
    tags={
        'Name': f'{project_name}-{environment}-{availability_zone_az4}-private-subnet-spare',
        'Network': 'private',
        'Owner': owner,
        'Project': project_name,
        'Environment': environment,
    }
)

############## Create Internet Gateway ##############
# projectName-environmentName-aws:region-igw
# ej. project-dev-us-east-1-igw
internet_gateway = aws.ec2.InternetGateway(
    resource_name = f'{project_name}-{environment}-{region}-igw',
    opts = ResourceOptions(depends_on = [ vpc ]),
    vpc_id = vpc.id,
    tags={
        'Name': f'{project_name}-{environment}-{region}-igw',
        'Owner': owner,
        'Project': project_name,
        'Environment': environment,
    }
)

############## Create Route Table Public ##############
# StackName-environmentName-public-rtb
# ej. project-dev-public-rtb
route_table_public = aws.ec2.RouteTable(
    resource_name = f'{project_name}-{environment}-{region}-public-rtb',
    opts = ResourceOptions(depends_on = [ vpc ]),
    vpc_id = vpc.id,
    tags = {
        'Name': f'{project_name}-{environment}-{region}-public-rtb',
        'Network': 'public',
        'Owner': owner,
        'Project': project_name,
        'Environment': environment,
    },
)

route_table_public_internet_route = aws.ec2.Route(
    resource_name = f'{project_name}-{environment}-{region}-route',
    opts = ResourceOptions(depends_on = [ internet_gateway, route_table_public ]),
    destination_cidr_block = '0.0.0.0/0',
    gateway_id = internet_gateway.id,
    route_table_id = route_table_public.id,
)

# Route Table Subnet Associations
route_table_association_public_alb_az1 = aws.ec2.RouteTableAssociation(
    resource_name = f'{project_name}-{environment}-{availability_zone_az1}-route-table-association-alb',
    subnet_id = public_alb_subnet_az1.id,
    route_table_id = route_table_public.id,
)

route_table_association_public_alb_az2 = aws.ec2.RouteTableAssociation(
    resource_name = f'{project_name}-{environment}-{availability_zone_az2}-route-table-association-alb',
    subnet_id = public_alb_subnet_az2.id,
    route_table_id = route_table_public.id,
)

route_table_association_public_alb_az3 = aws.ec2.RouteTableAssociation(
    resource_name = f'{project_name}-{environment}-{availability_zone_az3}-route-table-association-alb',
    subnet_id = public_alb_subnet_az3.id,
    route_table_id = route_table_public.id,
)

route_table_association_public_alb_az4 = aws.ec2.RouteTableAssociation(
    resource_name = f'{project_name}-{environment}-{availability_zone_az4}-route-table-association-alb',
    subnet_id = public_alb_subnet_az4.id,
    route_table_id = route_table_public.id,
)

# StackName-environmentName-availabilityZone1-public-rtb
# ej. project-dev-us-east-1a-public-shared-rtb
route_table_public_shared_az1 = aws.ec2.RouteTable(
    resource_name = f'{project_name}-{environment}-{availability_zone_az1}-public-shared-rtb',
    opts = ResourceOptions(depends_on = [ vpc ]),
    vpc_id = vpc.id,    
    tags = {
        'Name': f'{project_name}-{environment}-{availability_zone_az1}-public-shared-rtb',
        'Network': 'public',
        'Owner': owner,
        'Project': project_name,
        'Environment': environment,
    },
)

route_table_public_shared_internet_route_az1 = aws.ec2.Route(
    resource_name = f'{project_name}-{environment}-{availability_zone_az1}-shared-route',
    destination_cidr_block = '0.0.0.0/0',
    gateway_id = internet_gateway.id,
    route_table_id = route_table_public_shared_az1.id,
)

route_table_association_public_shared_az1 = aws.ec2.RouteTableAssociation(
    resource_name = f'{project_name}-{environment}-{availability_zone_az1}-route-table-association-shared',
    subnet_id = public_shared_subnet_az1.id,
    route_table_id = route_table_public_shared_az1.id,
)

# StackName-environmentName-availabilityZone2-public-rtb
# ej. project-dev-us-east-1b-public-shared-rtb
route_table_public_shared_az2 = aws.ec2.RouteTable(
    resource_name = f'{project_name}-{environment}-{availability_zone_az2}-public-shared-rtb',
    opts = ResourceOptions(depends_on = [ vpc ]),
    vpc_id = vpc.id,    
    tags = {
        'Name': f'{project_name}-{environment}-{availability_zone_az2}-public-shared-rtb',
        'Network': 'public',
        'Owner': owner,
        'Project': project_name,
        'Environment': environment,
    },
)

route_table_public_shared_internet_route_az2 = aws.ec2.Route(
    resource_name = f'{project_name}-{environment}-{availability_zone_az2}-shared-route',
    destination_cidr_block = '0.0.0.0/0',
    gateway_id = internet_gateway.id,
    route_table_id = route_table_public_shared_az2.id,
)

route_table_association_public_shared_az2 = aws.ec2.RouteTableAssociation(
    resource_name = f'{project_name}-{environment}-{availability_zone_az2}-route-table-association-shared',
    subnet_id = public_shared_subnet_az2.id,
    route_table_id = route_table_public_shared_az2.id,
)

# StackName-environmentName-availabilityZone3-public-rtb
# ej. project-dev-us-east-1c-public-shared-rtb
route_table_public_shared_az3 = aws.ec2.RouteTable(
    resource_name = f'{project_name}-{environment}-{availability_zone_az3}-public-shared-rtb',
    opts = ResourceOptions(depends_on = [ vpc ]),
    vpc_id = vpc.id,    
    tags = {
        'Name': f'{project_name}-{environment}-{availability_zone_az3}-public-shared-rtb',
        'Network': 'public',
        'Owner': owner,
        'Project': project_name,
        'Environment': environment,
    },
)

route_table_public_shared_internet_route_az3 = aws.ec2.Route(
    resource_name = f'{project_name}-{environment}-{availability_zone_az3}-shared-route',
    destination_cidr_block = '0.0.0.0/0',
    gateway_id = internet_gateway.id,
    route_table_id = route_table_public_shared_az3.id,
)

route_table_association_public_shared_az3 = aws.ec2.RouteTableAssociation(
    resource_name = f'{project_name}-{environment}-{availability_zone_az3}-route-table-association-shared',
    subnet_id = public_shared_subnet_az3.id,
    route_table_id = route_table_public_shared_az3.id,
)

# StackName-environmentName-availabilityZone4-public-rtb
# ej. project-dev-us-east-1d-public-shared-rtb
route_table_public_shared_az4 = aws.ec2.RouteTable(
    resource_name = f'{project_name}-{environment}-{availability_zone_az4}-public-shared-rtb',
    opts = ResourceOptions(depends_on = [ vpc ]),
    vpc_id = vpc.id,    
    tags = {
        'Name': f'{project_name}-{environment}-{availability_zone_az4}-public-shared-rtb',
        'Network': 'public',
        'Owner': owner,
        'Project': project_name,
        'Environment': environment,
    },
)

route_table_public_shared_internet_route_az4 = aws.ec2.Route(
    resource_name = f'{project_name}-{environment}-{availability_zone_az4}-shared-route',
    destination_cidr_block = '0.0.0.0/0',
    gateway_id = internet_gateway.id,
    route_table_id = route_table_public_shared_az4.id,
)

route_table_association_public_shared_az4 = aws.ec2.RouteTableAssociation(
    resource_name = f'{project_name}-{environment}-{availability_zone_az4}-route-table-association-shared',
    subnet_id = public_shared_subnet_az4.id,
    route_table_id = route_table_public_shared_az4.id,
)


############## Create Route Table Private ##############
# StackName-environmentName-aws:availabilityZone1-private1-rtb
# ej. project-dev-us-east-1a-private-app-rtb
route_table_private_app_az1 = aws.ec2.RouteTable(
    resource_name = f'{project_name}-{environment}-{availability_zone_az1}-private-app-rtb',
    opts = ResourceOptions(depends_on = [ vpc ]),
    vpc_id = vpc.id,    
    tags = {
        'Name': f'{project_name}-{environment}-{availability_zone_az1}-private-app-rtb',
        'Network': 'private',
        'Owner': owner,
        'Project': project_name,
        'Environment': environment,
    },
)

route_table_association_private_app_az1 = aws.ec2.RouteTableAssociation(
    resource_name = f'{project_name}-{environment}-{availability_zone_az1}-route-table-association-app',
    opts = ResourceOptions(depends_on = [ private_app_subnet_az1, route_table_private_app_az1 ]),
    subnet_id = private_app_subnet_az1.id,
    route_table_id = route_table_private_app_az1.id,
)

# ej. project-dev-us-east-1b-private-app-rtb
route_table_private_app_az2 = aws.ec2.RouteTable(
    resource_name = f'{project_name}-{environment}-{availability_zone_az2}-private-app-rtb',
    opts = ResourceOptions(depends_on = [ vpc ]),
    vpc_id = vpc.id,    
    tags = {
        'Name': f'{project_name}-{environment}-{availability_zone_az2}-private-app-rtb',
        'Network': 'private',
        'Owner': owner,
        'Project': project_name,
        'Environment': environment,
    },
)

route_table_association_private_app_az2 = aws.ec2.RouteTableAssociation(
    resource_name = f'{project_name}-{environment}-{availability_zone_az2}-route-table-association-app',
    opts = ResourceOptions(depends_on = [ private_app_subnet_az2, route_table_private_app_az2 ]),
    subnet_id = private_app_subnet_az2.id,
    route_table_id = route_table_private_app_az2.id,    
)

# ej. project-dev-us-east-1c-private-app-rtb
route_table_private_app_az3 = aws.ec2.RouteTable(
    resource_name = f'{project_name}-{environment}-{availability_zone_az3}-private-app-rtb',
    opts = ResourceOptions(depends_on = [ vpc ]),
    vpc_id = vpc.id,    
    tags = {
        'Name': f'{project_name}-{environment}-{availability_zone_az3}-private-app-rtb',
        'Network': 'private',
        'Owner': owner,
        'Project': project_name,
        'Environment': environment,
    },
)

route_table_association_private_app_az3 = aws.ec2.RouteTableAssociation(
    resource_name = f'{project_name}-{environment}-{availability_zone_az3}-route-table-association-app',
    opts = ResourceOptions(depends_on = [ private_app_subnet_az3, route_table_private_app_az3 ]),
    subnet_id = private_app_subnet_az3.id,
    route_table_id = route_table_private_app_az3.id,
)

# ej. project-dev-us-east-1d-private-app-rtb
route_table_private_app_az4 = aws.ec2.RouteTable(
    resource_name = f'{project_name}-{environment}-{availability_zone_az4}-private-app-rtb',
    opts = ResourceOptions(depends_on = [ vpc ]),
    vpc_id = vpc.id,    
    tags = {
        'Name': f'{project_name}-{environment}-{availability_zone_az4}-private-app-rtb',
        'Network': 'private',
        'Owner': owner,
        'Project': project_name,
        'Environment': environment,
    },
)

route_table_association_private_app_az4 = aws.ec2.RouteTableAssociation(
    resource_name = f'{project_name}-{environment}-{availability_zone_az4}-route-table-association-app',
    opts = ResourceOptions(depends_on = [ private_app_subnet_az4, route_table_private_app_az4 ]),
    subnet_id = private_app_subnet_az4.id,
    route_table_id = route_table_private_app_az4.id,
)

# StackName-environmentName-aws:availabilityZone1-private-db-rtb
# ej. project-dev-us-east-1a-private-db-rtb
route_table_private_db_az1 = aws.ec2.RouteTable(
    resource_name = f'{project_name}-{environment}-{availability_zone_az1}-private-db-rtb',
    opts = ResourceOptions(depends_on = [ vpc ]),
    vpc_id = vpc.id,    
    tags = {
        'Name': f'{project_name}-{environment}-{availability_zone_az1}-private-db-rtb',
        'Network': 'private',
        'Owner': owner,
        'Project': project_name,
        'Environment': environment,
    },
)

route_table_association_private_db_az1 = aws.ec2.RouteTableAssociation(
    resource_name = f'{project_name}-{environment}-{availability_zone_az1}-route-table-association-db',
    opts = ResourceOptions(depends_on = [ private_db_subnet_az1, route_table_private_db_az1 ]),
    subnet_id = private_db_subnet_az1.id,
    route_table_id = route_table_private_db_az1.id,
)

# StackName-environmentName-aws:availabilityZone2-private-db-rtb
# ej. project-dev-us-east-1b-private-db-rtb
route_table_private_db_az2 = aws.ec2.RouteTable(
    resource_name = f'{project_name}-{environment}-{availability_zone_az2}-private-db-rtb',
    opts = ResourceOptions(depends_on = [ vpc ]),
    vpc_id = vpc.id,    
    tags = {
        'Name': f'{project_name}-{environment}-{availability_zone_az2}-private-db-rtb',
        'Network': 'private',
        'Owner': owner,
        'Project': project_name,
        'Environment': environment,
    },
)

route_table_association_private_db_az2 = aws.ec2.RouteTableAssociation(
    resource_name = f'{project_name}-{environment}-{availability_zone_az2}-route-table-association-db',
    opts = ResourceOptions(depends_on = [ private_db_subnet_az2, route_table_private_db_az2 ]),
    subnet_id = private_db_subnet_az2.id,
    route_table_id = route_table_private_db_az2.id,
)

# StackName-environmentName-aws:availabilityZone3-private-db-rtb
# ej. project-dev-us-east-1c-private-db-rtb
route_table_private_db_az3 = aws.ec2.RouteTable(
    resource_name = f'{project_name}-{environment}-{availability_zone_az3}-private-db-rtb',
    opts = ResourceOptions(depends_on = [ vpc ]),
    vpc_id = vpc.id,    
    tags = {
        'Name': f'{project_name}-{environment}-{availability_zone_az3}-private-db-rtb',
        'Network': 'private',
        'Owner': owner,
        'Project': project_name,
        'Environment': environment,
    },
)

route_table_association_private_db_az3 = aws.ec2.RouteTableAssociation(
    resource_name = f'{project_name}-{environment}-{availability_zone_az3}-route-table-association-db',
    opts = ResourceOptions(depends_on = [ private_db_subnet_az3, route_table_private_db_az3 ]),
    subnet_id = private_db_subnet_az3.id,
    route_table_id = route_table_private_db_az3.id,
)

# StackName-environmentName-aws:availabilityZone4-private-db-rtb
# ej. project-dev-us-east-1d-private-db-rtb
route_table_private_db_az4 = aws.ec2.RouteTable(
    resource_name = f'{project_name}-{environment}-{availability_zone_az4}-private-db-rtb',
    opts = ResourceOptions(depends_on = [ vpc ]),
    vpc_id = vpc.id,    
    tags = {
        'Name': f'{project_name}-{environment}-{availability_zone_az4}-private-db-rtb',
        'Network': 'private',
        'Owner': owner,
        'Project': project_name,
        'Environment': environment,
    },
)

route_table_association_private_db_az4 = aws.ec2.RouteTableAssociation(
    resource_name = f'{project_name}-{environment}-{availability_zone_az4}-route-table-association-db',
    opts = ResourceOptions(depends_on = [ private_db_subnet_az4, route_table_private_db_az4 ]),
    subnet_id = private_db_subnet_az4.id,
    route_table_id = route_table_private_db_az4.id,
)

# StackName-environmentName-aws:availabilityZone1-private-spare-rtb
# ej. project-dev-us-east-1a-private-spare-rtb
route_table_private_spare_az1 = aws.ec2.RouteTable(
    resource_name = f'{project_name}-{environment}-{availability_zone_az1}-private-spare-rtb',
    opts = ResourceOptions(depends_on = [ vpc ]),
    vpc_id = vpc.id,
    tags = {
        'Name': f'{project_name}-{environment}-{availability_zone_az1}-private-spare-rtb',
        'Network': 'private',
        'Owner': owner,
        'Project': project_name,
        'Environment': environment,
    },
)

route_table_association_private_spare_az1 = aws.ec2.RouteTableAssociation(
    resource_name = f'{project_name}-{environment}-{availability_zone_az1}-route-table-association-spare',
    opts = ResourceOptions(depends_on = [ private_spare_subnet_az1, route_table_private_spare_az1 ]),
    subnet_id = private_spare_subnet_az1.id,
    route_table_id = route_table_private_spare_az1.id,
)

# StackName-environmentName-aws:availabilityZone2-private-spare-rtb
# ej. project-dev-us-east-1b-private-spare-rtb
route_table_private_spare_az2 = aws.ec2.RouteTable(
    resource_name = f'{project_name}-{environment}-{availability_zone_az2}-private-spare-rtb',
    opts = ResourceOptions(depends_on = [ vpc ]),
    vpc_id = vpc.id,
    tags = {
        'Name': f'{project_name}-{environment}-{availability_zone_az2}-private-spare-rtb',
        'Network': 'private',
        'Owner': owner,
        'Project': project_name,
        'Environment': environment,
    },
)

route_table_association_private_spare_az2 = aws.ec2.RouteTableAssociation(
    resource_name = f'{project_name}-{environment}-{availability_zone_az2}-route-table-association-spare',
    opts = ResourceOptions(depends_on = [ private_spare_subnet_az2, route_table_private_spare_az2 ]),
    subnet_id = private_spare_subnet_az2.id,
    route_table_id = route_table_private_spare_az2.id,
)

# StackName-environmentName-aws:availabilityZone3-private-spare-rtb
# ej. project-dev-us-east-1c-private-spare-rtb
route_table_private_spare_az3 = aws.ec2.RouteTable(
    resource_name = f'{project_name}-{environment}-{availability_zone_az3}-private-spare-rtb',
    opts = ResourceOptions(depends_on = [ vpc ]),
    vpc_id = vpc.id,
    tags = {
        'Name': f'{project_name}-{environment}-{availability_zone_az3}-private-spare-rtb',
        'Network': 'private',
        'Owner': owner,
        'Project': project_name,
        'Environment': environment,
    },
)

route_table_association_private_spare_az3 = aws.ec2.RouteTableAssociation(
    resource_name = f'{project_name}-{environment}-{availability_zone_az3}-route-table-association-spare',
    opts = ResourceOptions(depends_on = [ private_spare_subnet_az3, route_table_private_spare_az3 ]),
    subnet_id = private_spare_subnet_az3.id,
    route_table_id = route_table_private_spare_az3.id,
)

# StackName-environmentName-aws:availabilityZone4-private-spare-rtb
# ej. project-dev-us-east-1d-private-spare-rtb
route_table_private_spare_az4 = aws.ec2.RouteTable(
    resource_name = f'{project_name}-{environment}-{availability_zone_az4}-private-spare-rtb',
    opts = ResourceOptions(depends_on = [ vpc ]),
    vpc_id = vpc.id,
    tags = {
        'Name': f'{project_name}-{environment}-{availability_zone_az4}-private-spare-rtb',
        'Network': 'private',
        'Owner': owner,
        'Project': project_name,
        'Environment': environment,
    },
)

route_table_association_private_spare_az4 = aws.ec2.RouteTableAssociation(
    resource_name = f'{project_name}-{environment}-{availability_zone_az4}-route-table-association-spare',
    opts = ResourceOptions(depends_on = [ private_spare_subnet_az4, route_table_private_spare_az4 ]),
    subnet_id = private_spare_subnet_az4.id,
    route_table_id = route_table_private_spare_az4.id,
)