# Lab 5: Build Your DB Server and Interact With Your DB Using an App

## Lab Overview and objectives

This lab is designed to reinforce the concept of leveraging an AWS-managed database instance for solving relational database needs.

__Amazon Relational Database Service__ (Amazon RDS) makes it easy to set up, operate, and scale a relational database in the cloud. It provides cost-efficient and resizable capacity while managing time-consuming database administration tasks, which allows you to focus on your applications and business. Amazon RDS provides you with six familiar database engines to choose from: Amazon Aurora, Oracle, Microsoft SQL Server, PostgreSQL, MySQL and MariaDB.

By the end of this lab, you will be able to:

* Launch an Amazon RDS DB instance with high availability.

* Configure the DB instance to permit connections from your web server.

* Open a web application and interact with your database.

 
## Duration

This lab takes approximately __30 minutes__.

 
## AWS service restrictions

In this lab environment, access to AWS services and service actions might be restricted to the ones that are needed to complete the lab instructions. You might encounter errors if you attempt to access other services or perform actions beyond the ones that are described in this lab.

 
## Scenario

When you start the lab, the following infrastructure is provided:

![alt text](img/image-18.png)

By the end of the lab, you will have this infrastructure:

![alt text](img/image-19.png)

 
## Accessing the AWS Management Console

1. At the top of these instructions, choose __Start Lab__.

   * The lab session starts.

   * A timer displays at the top of the page and shows the time remaining in the session.

     __Tip__: To refresh the session length at any time, choose  __Start Lab__ again before the timer reaches 0:00.

   * Before you continue, wait until the circle icon to the right of the AWS  link in the upper-left corner turns green. 

2. To connect to the AWS Management Console, choose the __AWS__ link in the upper-left corner.

   * A new browser tab opens and connects you to the console.

     __Tip__: If a new browser tab does not open, a banner or icon is usually at the top of your browser with the message that your browser is preventing the site from opening pop-up windows. Choose the banner or icon, and then choose __Allow pop-ups__.

3. Arrange the AWS Management Console tab so that it displays along side these instructions. Ideally, you will be able to see both browser tabs at the same time, to make it easier to follow the lab steps.

 

## Getting Credit for your work

At the end of this lab you will be instructed to submit the lab to receive a score based on your progress.

 __Tip__: The script that checks you works may only award points if you name resources and set configurations as specified. In particular, values in these instructions that appear in This Format should be entered exactly as documented (case-sensitive).

 

## Task 1: Create a Security Group for the RDS DB Instance

In this task, you will create a security group to allow your web server to access your RDS DB instance. The security group will be used when you launch the database instance.

4. In the AWS Management Console, in the search box next to  __Services__ , search for and select __VPC__.

5. In the left navigation pane, choose __Security groups__.

6. Choose <span style="color:orange">Create security group</span> and then configure:

   * __Security group name__: DB Security Group

   * __Description__: Permit access from Web Security Group

   * __VPC__: Lab VPC

     __Tip__: Choose the X next to VPC that is already selected, then choose __Lab VPC__ from the menu.

7. In the __Inbound rules__ pane, choose __Add rule__

   The security group currently has no rules. You will add a rule to permit access from the Web Security Group.

8. Configure the following settings:

   * __Type__: MySQL/Aurora (3306)

   * __Source__: Place you cursor in the field to the right of Custom, type sg, and then select Web Security Group.

   This configures the Database security group to permit inbound traffic on port 3306 from any EC2 instance that is associated with the Web Security Group.

9. Choose <span style="color:orange">Create security group</span>

You will use this security group when launching an Amazon RDS database in this lab.

 
## Task 2: Create a DB Subnet Group

In this task, you will create a DB subnet group that is used to tell RDS which subnets can be used for the database. Each DB subnet group requires subnets in at least two Availability Zones.

10. In the AWS Management Console, in the search box next to __Services__, search for and select __RDS__.

11. In the left navigation pane, choose __Subnet groups__.

    If the navigation pane is not visible, choose the  menu icon in the top-left corner.

12. Choose <span style="color:orange">Create DB Subnet Group</span> then configure:

    * __Name__: DB-Subnet-Group

    * __Description__: DB Subnet Group

    * __VPC__: Lab VPC

13. Scroll down to the Add subnets section.

14. Expand the list of values under Availability Zones and  select the first two zones: us-east-1a and us-east-1b.

15. Expand the list of values under Subnets and select the subnets associated with the CIDR ranges 10.0.1.0/24 and 10.0.3.0/24.

    These subnets should now be shown in the Subnets selected table.

16. Choose <span style="color:orange">Create</span>

    You will use this DB subnet group when creating the database in the next task.

 
## Task 3: Create an Amazon RDS DB Instance

In this task, you will configure and launch a Multi-AZ Amazon RDS deployment of a MySQL database instance.

Amazon RDS __Multi-AZ__ deployments provide enhanced availability and durability for Database (DB) instances, making them a natural fit for production database workloads. When you provision a Multi-AZ DB instance, Amazon RDS automatically creates a primary DB instance and synchronously replicates the data to a standby instance in a different Availability Zone (AZ).

17. In the left navigation pane, choose __Databases__.

18. Choose <span style="color:orange">Create database</span>

 If you see __Switch to the new database creation flow__ at the top of the screen, please choose it.

19. Select  __MySQL__ under __Engine Options__.

20. Under __Templates__ choose __Dev/Test__.

21. Under __Availability and durability__ choose __Multi-AZ DB instance__.

22. Under __Settings__, configure:

    * __DB instance identifier__: lab-db

    * __Master username__: main

    * __Master password__: lab-password

    * __Confirm password__: lab-password

23. Under __DB instance class__, configure:

    * Select  __Burstable classes (includes t classes)__.

    * Select _db.t3.micro_

24. Under __Storage__, configure:

    * __Storage type__: General Purpose (SSD)

    * __Allocated storage__: 20

25. Under __Connectivity__, configure:

    * __Virtual Private Cloud (VPC)__: _Lab VPC_

26. Under __Existing VPC security groups__, from the dropdown list:

    * Choose _DB Security Group_.

    * Deselect _default_.

27. Under __Monitoring__ expand __Additional configuration__.

    * Uncheck __Enable Enhanced monitoring__.

28. Under __Additional configuration__, configure:

    * __Initial database name__: lab

    * Uncheck __Enable automatic backups__.

    * Uncheck __Enable encryption__

    This will turn off backups, which is not normally recommended, but will make the database deploy faster for this lab.

29. Choose <span style="color:orange">Create database</span>

    Your database will now be launched.

    If you receive an error that mentions "not authorized to perform: iam:CreateRole", make sure you unchecked Enable Enhanced monitoring in the previous step.

30. Choose __lab-db__ (choose the link itself).

    You will now need to wait __approximately 4 minutes__ for the database to be available. The deployment process is deploying a database in two different Availability zones.

    While you are waiting, you might want to review the Amazon RDS FAQs or grab a cup of coffee.

31. Wait until __Info__ changes to __Modifying__ or __Available__.

32. Scroll down to the __Connectivity & security__ section and copy the __Endpoint__ field.

    It will look similar to: _lab-db.xxxx.us-east-1.rds.amazonaws.com_.

33. Paste the Endpoint value into a text editor. You will use it later in the lab.

 
## Task 4: Interact with Your Database

In this task, you will open a web application running on a web server that has been created for you. You will configure it to use the database that you just created.

34. To discover the __WebServer__ IP address, choose on the  AWS Details drop down menu above these instructions. Copy the IP address value.

35. Open a new web browser tab, paste the WebServer IP address and press Enter.

    The web application will be displayed, showing information about the EC2 instance.

36. Choose the __RDS__ link at the top of the page.

    You will now configure the application to connect to your database.

37. Configure the following settings:

    * __Endpoint__: Paste the Endpoint you copied to a text editor earlier

    * __Database__: lab

    * __Username__: main

    * __Password__: lab-password

    * Choose __Submit__

    A message will appear explaining that the application is running a command to copy information to the database. After a few seconds the application will display an __Address Book__.

    The Address Book application is using the RDS database to store information.

38. Test the web application by adding, editing and removing contacts.

    The data is being persisted to the database and is automatically replicating to the second Availability Zone.

 
## Submitting your work

39. To record your progress, choose __Submit__ at the top of these instructions.

40. When prompted, choose __Yes__.

    After a couple of minutes, the grades panel appears and shows you how many points you earned for each task. If the results don't display after a couple of minutes, choose __Grades__ at the top of these instructions.

    __Tip__: You can submit your work multiple times. After you change your work, choose __Submit__ again. Your last submission is recorded for this lab.

41. To find detailed feedback about your work, choose __Submission Report__.

    __Tip__: For any checks where you did not receive full points, there are sometimes helpful details provided in the submission report.

 
## Lab Complete

Congratulations! You have completed the lab.

42. Choose End Lab at the top of this page and then choose <span style="color:blue">Yes</span> to confirm that you want to end the lab.  

    A panel will appear, indicating that "DELETE has been initiated... You may close this message box now."

43. Choose the X in the top right corner to close the panel.

 

©2023 Amazon Web Services, Inc. and its affiliates. All rights reserved. This work may not be reproduced or redistributed, in whole or in part, without prior written permission from Amazon Web Services, Inc. Commercial copying, lending, or selling is prohibited.


### Attributions

Bootstrap v3.3.5 - http://getbootstrap.com/

The MIT License (MIT)

Copyright (c) 2011-2016 Twitter, Inc.

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.