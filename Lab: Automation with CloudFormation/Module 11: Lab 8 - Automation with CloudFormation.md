# Module 11: Lab 8 - Automation with CloudFormation

Deploying infrastructure in a consistent, reliable manner is difficult — it requires people to follow documented procedures without taking any undocumented shortcuts. Plus, it can be difficult to deploy infrastructure out-of-hours when less staff are available. AWS CloudFormation changes this by defining infrastructure in a template that can be automatically deployed — even on an automated schedule.

This lab provides experience in deploying and editing CloudFormation stacks. It is an interactive experience, requiring you to consult documentation to discover how to define resources within a CloudFormation template.

The lab will demonstrate how to:

* __Deploy__ an AWS CloudFormation stack with a defined Virtual Private Cloud (VPC), and Security Group.
* __Configure__ an AWS CloudFormation stack with resources, such as an Amazon Simple Storage Solution (S3) bucket and Amazon Elastic Compute Cloud (EC2).
* __Terminate__ an AWS CloudFormation and its respective resources.


## Duration

This lab will require approximately 45 minutes to complete.

 
## Accessing the AWS Management Console

1. At the top of these instructions, choose Start Lab to launch your lab.

   A Start Lab panel opens displaying the lab status.

2. Wait until you see the message "__Lab status: ready__", then choose the __X__ to close the Start Lab panel.

3. At the top of these instructions, choose AWS

   This will open the AWS Management Console in a new browser tab. The system will automatically log you in.

   [!TIP]
   __Tip__: If a new browser tab does not open, there will typically be a banner or icon at the top of your browser indicating that your browser is preventing the site from opening pop-up windows. Choose the banner or icon and choose "Allow pop ups."

4. Arrange the AWS Management Console tab so that it displays along side these instructions. Ideally, you will be able to see both browser tabs at the same time, to make it easier to follow the lab steps.

   Please do not change the Region during this lab.

 
## Task 1: Deploy a CloudFormation Stack

You will begin by deploying a CloudFormation stack that creates a VPC as shown in this diagram:

![alt text](img/Task-1-deployment.png)

5. Right-click this link and download the CloudFormation template: task1.yaml

6. Open this file in a Text Editor (not a Word Processor).

   Look through the file. You will notice several sections:

   * The Parameters section is used to prompt for inputs that can be used elsewhere in the template. The template is asking for two IP address (CIDR) ranges for defining the VPC.

   * The Resources section is used to define the infrastructure to be deployed. The template is defining the VPC, and a Security Group.

   * The Outputs section is used to provide  selective information about resources in the stack. The template is providing the Default Security Group for the VPC that is created.

   The template is written in a format called YAML, which is commonly used for configuration files. The format of the file is important, including the indents and hyphens. CloudFormation templates can also be written in JSON.

   You will now use this __template__ to launch a __CloudFormation stack__.

7. In the __AWS Management Console__, on the <span style="color:gray">Services</span>  menu, choose __CloudFormation__.

8. Choose <span style="color:orange">Create stack</span> then:

   * Choose  __Upload a template file__

   * Select __Choose file__ and upload the template file you downloaded earlier

   * Choose <span style="color:orange">Next</span>

9. On the __Specify stack details__ page, configure:

   * __Stack name__: <span style="color:red">Lab</span>

     In the __Parameters__ section, you will see that CloudFormation is prompting for the IP address ('CIDR') range for the VPC and Subnet. A default value has been specified by the template, so there is no need to modify these values.

10. Choose <span style="color:orange">Next</span>

    The __Configure stack options__ page can be used to specify additional parameters. You can browse the page, but leave settings at their default values.

11. Choose <span style="color:orange">Next</span>

    The __Review Lab__ page displays a summary of all settings.

12. Choose <span style="color:orange">Create stack</span>

    The stack will now enter the <span style="color:blue">CREATE_IN_PROGRESS</span> status.

13. Choose the Events tab and scroll through the events. Choose the refresh icon to make the latest events display more quickly.

    The events show (in reverse order) the activities performed by AWS CloudFormation, such as starting to create a resource and then completing the resource creation. Any errors encountered during the creation of the stack will be listed in this tab.

14. Choose the __Resources__ tab.

    The listing shows the resources that are being created or have been created. By default, AWS CloudFormation determines the optimal order for resources to be created, such as creating the VPC before the subnet.

15. Wait until the status of the stack changes to <span style="color:green">CREATE_COMPLETE</span>. You can choose  __Refresh__ occasionally to update the display.

    __Optional__: Go to the VPC console to see the Lab VPC that was created. Then, return to the CloudFormation console.

 
## Task 2: Add an Amazon S3 Bucket to the Stack

In this task, you will gain experience in editing a CloudFormation template.

Your objective is:

* Add an Amazon S3 bucket to the template

* Then __update the stack__ with the revised template

This will result in a new bucket being deployed.

Rather than following pre-defined steps, you will need to discover how to __update the template yourself!__

Here are some tips:

* You should edit the __task1.yaml__ file you downloaded earlier to include an Amazon S3 bucket

* Use this documentation page for assistance: [Amazon S3 Template Snippets](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/quickref-s3.html)

* Look at the __YAML example__

* Your code should go under the __Resources:__ header in the template file

* __You do not require any Properties for this bucket resource__

* Indents are important in YAML — use two spaces for each indent

* The correct solution is actually __only needs two lines__ — one for the identifier and one for the Type

Once you have edited the template, continue with the following steps to update the stack.

16. In the CloudFormation console, select  __Lab__.

17. Choose __Update__.

18. Choose __Replace current template__, then choose __Upload a template file__. Choose __Choose file__, then browse to and select the task1.yaml file that you modified.

19. Choose <span style="color:orange">Next</span>

    If you receive an error message, ask your instructor for assistance in debugging the problem.

20. On the __Specify stack details__ page, choose <span style="color:orange">Next</span>

21. On the __Configure stack options__ page, choose <span style="color:orange">Next</span>

    Wait for CloudFormation to calculate the changes. Towards the bottom of the page, you should see something similar to this:

    ![alt text](img/Preview-Changes-1.png)

    This indicates that CloudFormation will Add an Amazon S3 bucket. All other resources defined in the template will be unchanged. This demonstrates that it is fast and easy to add additional resources to an existing stack, since those resources do not need to be redeployed.

22. Choose <span style="color:orange">Update stack</span>

    After a minute, the stack status will change from <span style="color:blue">UPDATE_IN_PROGRESS</span> to <span style="color:green">UPDATE_COMPLETE</span>.

23. Choose the __Resources__ tab.

    The bucket will now be displayed in the list of resources. CloudFormation will have assigned it a random name so that it does not conflict with any existing buckets.

    If the bucket was not correctly created, please ask your instructor for assistance.

    To download a sample solution, right-click and download this link: [task2.yaml](https://aws-tc-largeobjects.s3-us-west-2.amazonaws.com/CUR-TF-200-RESOPS/lab8vocareum/task2.yaml)

    __Optional__: Go to the S3 console to see the bucket that was created. Then, return to the CloudFormation console.

 
## Task 3: Add an Amazon EC2 Instance to the Stack

In this task, your objective is to __add an Amazon EC2 instance to the template__, then update the stack with the revised template.

Whereas the bucket definition was rather simple (just two lines), defining an Amazon EC2 instance is more complex because it needs to use associated resources, such as an AMI, security group and subnet.

First, however, you will add a special parameter that is used to provide a value for the Amazon Machine Image (AMI).

24. Update the template by adding these lines in the __Parameters__ section:

    ```yaml
    AmazonLinuxAMIID:
    Type: AWS::SSM::Parameter::Value<AWS::EC2::Image::Id>
    Default: /aws/service/ami-amazon-linux-latest/amzn2-ami-hvm-x86_64-gp2
    ```

    This parameter uses the __AWS Systems Manager Parameter Store__ to retrieve the latest AMI (specified in the Default parameter, which in this case is Amazon Linux 2) for the stack's region. This makes it easy to deploy stacks in different regions without having to manually specify an AMI ID for every region.

    For more details of this method, see: [AWS Compute Blog: Query for the latest Amazon Linux AMI IDs using AWS Systems Manager Parameter Store](http://aws.amazon.com/blogs/compute/query-for-the-latest-amazon-linux-ami-ids-using-aws-systems-manager-parameter-store/).

    When writing CloudFormation templates, you can refer to other resources in the template by using the !Ref keyword. For example, here is a portion of the task1.yaml template that defines a VPC, then references the VPC within the Route Table definition:

    ```yaml
    VPC:
      Type: AWS::EC2::VPC
      Properties:
        CidrBlock: 10.0.0.0/16

    PublicRouteTable:
      Type: AWS::EC2::RouteTable
      Properties:
        VpcId: !Ref VPC
    ```

    Note that it uses <span style="color:red">!Ref VPC</span> to refer to the VPC resource. You will use this technique when defining the EC2 instance.

25. Use the tips below to update the template to __add an Amazon EC2 instance__ with the following __Properties__:

    * __ImageId:__ Refer to <span style="color:red">AmazonLinuxAMIID</span>, which is the parameter added in the previous step

    * __InstanceType:__ <span style="color:red">t2.micro</span>

    * __SecurityGroupIds:__ Refer to <span style="color:red">AppSecurityGroup</span>, which is defined elsewhere in the template

    * __SubnetId:__ Refer to <span style="color:red">PublicSubnet</span>, which is defined elsewhere in the template

    * __Tags:__ Use this YAML block:

    ```yaml
      Tags:
        - Key: Name
          Value: App Server
    ```

Here are some tips:

* Use this documentation page for assistance: [AWS::EC2::Instance](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-instance.html)

* Use the __YAML version__

* Your code should go under the __Resources:__ header in the template file

* __Only add the five Properties listed above__, there is no need to include any other properties

* When referring to other resources in the same template, use <span style="color:red">!Ref</span> — see the example at the beginning of this task

* When referring to __SecurityGroupIds__, the template is actually expecting a list of security groups. You therefore need to list the security group like this:

```yaml
      SecurityGroupIds:
        - !Ref AppSecurityGroup
```

26. Once you have edited the template, update the stack with your revised template file.

    You should see this before deploying the update:

    ![alt text](img/Preview-Changes-2.png)

    If you are experiencing difficulties in editing the template, please ask your instructor for assistance.

    To download a sample solution, right-click and download this link: [task3.yaml](https://aws-tc-largeobjects.s3-us-west-2.amazonaws.com/CUR-TF-200-RESOPS/lab8vocareum/task3.yaml)

    The instance will now be displayed in the Resources tab.

    Optional: Go to the EC2 console to see the App Server that was created. Then, return to the CloudFormation console.

 
## Task 4: Delete the Stack

When a CloudFormation stack is deleted, CloudFormation will automatically delete the resources that it created.

You will now delete the stack.

27. In the CloudFormation console, select  __Lab__.

28. Choose __Delete__, then at the prompt, choose <span style="color:orange">Delete stack</span>.

    The stack will show <span style="color:blue">DELETE_IN_PROGRESS</span>. After a few minutes, the stack will disappear.

    __Optional__: Verify that the Amazon S3 bucket, Amazon EC2 instance and the VPC have been deleted.

 
## Lab Complete

Congratulations! You have completed the lab.

29. Choose End Lab at the top of this page and then choose <span style="color:blue">Yes</span> to confirm that you want to end the lab.  

    A panel will appear, indicating that "DELETE has been initiated... You may close this message box now."

30. Choose the __X__ in the top right corner to close the panel.