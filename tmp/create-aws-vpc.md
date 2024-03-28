# Create AWS VPC

## Step 1: Create VPC
1. Before creating VPC make sure that you have selected the correct region.

2. Enter VPC Name and CIDR block (130.33.0.0/16)

## Step 2: Create Subnet
Subnet is the logical partition of your VPC Network. IP addresses with common prefixes are in the same subnet. E.g 172.81.x.x are used in the same subnet. This is done because the maintenance of a smaller network is easier and it also provides security to the network from other networks.

1. Select new VPC

2. Enter Subnet Name

3. Select availability Zone and CIDR block for Subnet. In our example we are creating subnet using CIDR block 130.33.16.0/20

## Step 3: Create Route Tables
Route table contains a set of rules called routes which determine where traffic has to be directed. We can configure multiple route tables in a given VPC. When VPC is created it also create Route table automatically.

1. Enter Name and Select VPC

## Step 4: Create Internet Gateway (IGW)
Internet Gateway is a combination of hardware and software that provides your private network with a route to the world outside. An IGW is horizontally scaled, and it is a highly available VPC component that allows communication between instance and the internet. Only one IGW can be attached to a VPC at a time.

1. Create new Internet Gateway and attach with VPC

## Step 5: Attach Internet Gateways to RouteTable
We will attach IGW to route-table so that traffic from and to the Internet can be redirected via RouteTables. Follow mentioned steps to attach IGW to route table.

1. Select Route table and click on Edit routes

2. Add 0.0.0.0/0 (Open to all) and select Internet gateway as Target and save record.

## Step 6: Create New Subnet
1. Select new VPC

2. Enter Subnet Name

3. Select availability Zone and CIDR block for Subnet. In our example we are creating subnet using CIDR block 130.33.0.0/20

Note: Do not attach Internet Gateway to this Private subnet.

## Step 7: Create new Route table for Private Subnet
1. Enter Route table name

2. Select VPC

3. Edit Subnet associations and select Private Subnet which is created in Step 6

## Step 8: Create NAT Gateway
1. Enter name of NAT gateway

2. Select Public Subnet which is created in step 2

3. Allocate Elastic IP to NAT gateway

## Step 9: Update Private Route table
1. Edit Routes of private Route table which is created in step 7

2. Add 0.0.0.0/0 (Open to all) and select NAT gateway as Target and save record.

Now we are ready to use new VPC, test your VPC setup by creating EC2 instance.

## Step 10: Launch EC2 Instance
1. Select AMI

2. Select new VPC

3. Select Public Subnet which is created in step 2

4. Launch EC2 instance

If you want to attach new AWS VPC to lambda function follow below mentioned steps

1. While creating Lambda function select new VPC

2. Select Private Subnet created in step 6

Now Lambda function will have internet access using NAT Gateway

Note: In lambda do not attach subnet which has internet gateway attached in its associated route table.