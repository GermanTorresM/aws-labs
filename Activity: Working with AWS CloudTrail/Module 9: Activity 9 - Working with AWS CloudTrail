# Module 9: Activity 9 - Working with AWS CloudTrail

## Activity overview

In this activity, you will create an AWS CloudTrail trail that audits actions taken in your account. You will then conduct an investigation to determine who modified the Mom & Pop Café website.

The activity starts with an Amazon Elastic Compute Cloud (Amazon EC2) instance named Cafe Web Server, which runs a web application that hosts the Mom & Pop Café website.

* In __Task 1__, you observe that the website looks normal.

* In __Task 2__, soon after you create a trail with AWS CloudTrail, you notice that the website has been hacked, and that part of the hack involved an action where someone modified the security group settings.

* In __Task 3__, you use a variety of methods to analyze the CloudTrail logs, including the Linux grep utility and the AWS CLI.

* In __Task 4__, you use Amazon Athena to search the CloudTrail logs.

* In the Challenge section that concludes Task 4, you work to identify the hacker.

* In __Task 5__, now that you have discovered the culprit, you remove that user's access. You also take steps to reduce the chances that the AWS account and the Mom & Pop Café website will be hacked again.
  The architectural diagram here illustrates the setup that is used in this activity.

![alt text](img/architectural-diagram.png)


## Duration

This lab will require approximately __75 minutes__ to complete.
 

## Activity objectives

After completing this lab, you should be able to do the following:

* __Configure__ an AWS CloudTrail trail.

* __Analyze__ CloudTrail logs by using various methods to discover relevant information.

* __Import__ AWS CloudTrail log data into Amazon Athena.

* __Run__ queries in Amazon Athena to filter AWS CloudTrail log entries.

* __Resolve__ security concerns within the AWS account and on an EC2 Linux instance.
 
 
## Business case relevance

__A new request from the Mom & Pop Café leadership team__

![alt text](img/cafe-scene.png)

Mom and Pop are concerned because the website was hacked. They are relying on you to discover who did it and to make sure it does not happen again.

Natalia, Pop, Emma, and others make frequent changes to the website, and sometimes those changes cause issues. Also, this morning, it looks like the website was hacked. Mom and Pop are asking Sophie if there is a way to track what was changed and who made the changes.

Play the role of Sophie, become a detective, and discover the culprit.
 

## Launching the activity environment

1. At the top of these instructions, choose Start Lab to launch your lab.

   A Start Lab panel opens displaying the lab status.

2. Wait until you see the message "__Lab status: ready__", then choose the __X__ to close the Start Lab panel.

3. At the top of these instructions, choose AWS

   This will open the AWS Management Console in a new browser tab. The system will automatically log you in.

   __Tip__: If a new browser tab does not open, there will typically be a banner or icon at the top of your browser indicating that your browser is preventing the site from opening pop-up windows. Choose the banner or icon and choose "Allow pop ups."

4. Arrange the AWS Management Console tab so that it displays along side these instructions. Ideally, you will be able to see both browser tabs at the same time, to make it easier to follow the lab steps.

 
## Task 1: Modify a security group and observe the website

5. From the __Services__ menu, choose the __EC2__ service.

6. Choose __Instances__, then locate and select the __Cafe Web Server__ instance.

7. Choose the __Security__ tab below and then choose __WebSecurityGroup__.

8. In the __Inbound rules__ tab, notice that only one inbound rule has been defined, which is for HTTP access over TCP port 80.

9. Choose __Edit inbound rules__, then choose __Add Rule__ and configure the rule as follows:

   * __Port Range__: 22
   * __Source__: My IP

   __Important__: Confirm that the TCP port 22 access will only be open to your IP address. The entry should show a Classless Inter-Domain Routing (CIDR) block that has a particular IP address followed by /32, not to all IP addresses (which would be shown by 0.0.0.0/0).

10. Choose __Save rules__ at the bottom of the page.

11. Observe the Café website:

    * Choose __Instances__, select the __Cafe Web Server__ instance, and copy the __Public IPv4 address__ value.

    * Open a new browser tab and navigate to http://<WebServerIP>/mompopcafe/ (substitute the actual <WebServerIP> value).

    * Notice that the website looks normal. For example, the photos are all appropriate for a bakery café.


## Task 2: Create an AWS CloudTrail log and observe the hacked website

In this task, you will create an AWS CloudTrail trail in your AWS account. You will also notice that soon after creating the trail, the Mom & Pop Café website is hacked.

#### Task 2.1: Create an AWS CloudTrail log

12. In the AWS Management Console, in the search box next to __ Services__ search for and select the __CloudTrail__ service to open the CloudTrail console.

13. In the  menu on the left, choose __Trails__ and then choose __Create trail__.

14. Configure the trail as follows described below.

    * In the __Choose trail attributes__ screen:

      * __Trail name__: Monitor

        __Important__: Verify that you set the __Trail name__ as Monitor, or this activity will not work as intended.

      * __Storage location__: Create a new S3 bucket

      * __Trail log bucket and folder__: monitoring#### (where #### are four random digits)

      * __Log file SSE-KMS encryption__: Uncheck (to disable)

      * Keep the other default trail attributes and choose Next.

    * In the __Choose log events__ screen:

      * __Event type__: Keep __Management events__ checked. 

      * __API activity__: Keep __Read__ and __Write__ selected.

      * Choose __Next__.

15. Scroll down and choose __Create trail__.


## Task 2.2: Observe the hacked website

16. Return to the browser tab where you have the Café website open, and refresh the page.

    __Important__: You might need to wait a full minute before the hack will occur. Also, your browser may be caching the images on this website, press and hold SHIFT while you also choose the browser refresh button in order to see the latest changes to the website.

    Notice that the website has been hacked. Who put that image there? The image certainly does not look correct.

    It is up to you to figure out who hacked the website.

    It is good that you enabled CloudTrail before this happened. CloudTrail can give you valuable information about what users have been doing in your account.

17. Back in the AWS Management Console, browse to the __EC2__ service and observe the __Cafe Web Server__ instance details.

    Does anything look suspicious?

18. In the __Security__ tab, choose __WebSecurityGroup__ again and then choose the __Inbound rules__ tab.

    Where did that extra entry come from?

    You still see the entry you created earlier: the rule that opens port 22 to only your IP address.

    However, you also now see that someone else created an additional inbound rule that allows Secure Shell (SSH) access from anywhere (0.0.0.0/0). 

    Who added this security hole? You can search the CloudTrail logs to find out.

 
## Task 3: Analyze the CloudTrail Logs by using grep

In this task, you will analyze the CloudTrail logs by using the grep Linux utility to see if you can figure out who hacked the website.


### Task 3.1: Connect to the Cafe Web Server host EC2 instance by using SSH

In this task, you will connect to the Cafe Web Server EC2 instance. You will use SSH to connect to the instance.

Windows users should follow Task 3.2 for Windows. Both macOS and Linux users should follow Task 3.2 for macOS/Linux.

__macOS /Linux users__ —scroll down for the SSH instructions.

 
### Task 3.2 for Windows: SSH

These instructions are for Windows users only.

If you are using macOS or Linux, skip to the next section.

19. Read through the three bullet points in this step before you start to complete the actions, because you will not be able see these instructions when the Details panel is open.

    * Choose the Details drop down menu above these instructions you are currently reading, and then choose Show. A Credentials window will open.

    * Choose the __Download PPK__ button and save the __labsuser.ppk__ file. Typically your browser will save it to the Downloads directory.

    * Then exit the Details panel by choosing the __X__.

20. Download needed software.

    * You will use __PuTTY__ to SSH to Amazon EC2 instances. If you do not have PuTTY installed on your computer, download it here.

21. Open __putty.exe__

22. Configure PuTTY to not timeout:

    * Choose __Connection__

    * Set __Seconds between keepalives__ to 30

    This allows you to keep the PuTTY session open for a longer period of time.

23. Configure your PuTTY session:

    * Choose __Session__
    
    * __Host Name (or IP address)__: Paste the Public DNS or IPv4 address of the Bastion Host instance that you noted earlier. 

    * Back in PuTTY, in the Connection list, expand  __SSH__

    * Choose Auth and expand  __Credentials__
    
    * Under __Private key file for authentication__: Choose __Browse__

    * Browse to the labsuser.ppk file that you downloaded, select it, and choose __Open__

    * Choose __Open__ again

24. To trust and connect to the host, choose __Accept__.

25. When prompted __login as__, enter: ec2-user

    This will connect you to the EC2 instance.

26. Windows Users: Scroll past the macOS/Linux Task 3.2 instructions below and continue with Task 3.3.


### Task 3.2 for macOS/Linux: SSH

These instructions are for Mac/Linux users only. If you are a Windows user, skip ahead to the next task.

27. Read through the three bullet points in this step before you start to complete the actions, because you will not be able see these instructions when the Details panel is open.

    * Choose the Details drop down menu above these instructions you are currently reading, and then choose Show. A Credentials window will open.

    * Choose the __Download PEM__ button and save the __labsuser.pem__ file.

    * Then exit the Details panel by choosing the __X__.

28. Open a terminal window, and change directory cd to the directory where the labsuser.pem file was downloaded.

    For example, run this command, if it was saved to your Downloads directory:

    ```bash
    cd ~/Downloads
    ```

29. Change the permissions on the key to be read only, by running this command:

    ```bash
    chmod 400 labsuser.pem
    ```

30. Return to the AWS Management Console, and in the EC2 service, choose __Instances__. Check the box next to the Cafe Web Server instance and choose the __Details__ tab.

31. Copy the __Public IPv4 address__ value.

32. Return to the terminal window and run this command (replace <__public-ip__> with the actual public IP address you copied):

    ```bash
    ssh -i labsuser.pem ec2-user@<public-ip>
    ```

33. Type yes when prompted to allow a first connection to this remote SSH server.

    Because you are using a key pair for authentication, you will not be prompted for a password.



### Task 3.3: Download and extract the CloudTrail logs

34. Verify that your terminal is connected via SSH to the Cafe Web Server EC2 instance.

35. Create a local directory on the web server to download the CloudTrail Log files to:

    ```bash
    mkdir ctraillogs
    ```

36. Change the directory to the new directory:

    ```bash
    cd ctraillogs
    ```

37. List the buckets to recall the bucket name:

    ```
    aws s3 ls
    ```

38. Download the CloudTrail logs by running the following command. Replace <monitoring####> with the actual bucket name that starts with monitoring (the bucket name is part of the output from the ls command that you ran).

    ```bash
    aws s3 cp s3://<monitoring####>/ . --recursive
    ```

    If the command is successful, you should see that a few log files are downloaded.

    Important: If there was no output in the command line when you ran the last command, it likely means that not enough time has passed since you created the CloudWatch trail. CloudWatch posts logs to Amazon Simple Storage Service (Amazon S3) every 5 minutes. You might need to wait and try running the command again. Do not proceed to the next step until you have downloaded at least one log file.

39. Use the cd command and ls commands repeatedly (or enter cd followed by pressing TAB multiple times) as necessary to change the directory to the subdirectory where the logs were downloaded. When you run ls, all of the downloaded log files should display. They will be located in an AWSLogs/<account-num>/CloudTrail/<Region>/<yyyy>/<mm>/<dd> subdirectory.

    Notice that the log files end in json.gz, which indicates that they are compressed as GNU zip files.

40. Run this command to extract the logs:

    ```bash
    gunzip *.gz
    ```
41. Run ls again. Notice that all files are now extracted.

 
### Task 3.4: Analyze the logs by using grep

In this section of the activity, you will analyze the CloudTrail Logs by using the Linux grep utility.

42. Analyze the structure of the logs. To do this:

    * Copy one of the file names returned by the ls command that you ran.

    * Enter cat in the terminal window, followed by a space, and then paste the copied file name. Run the command.

    * Note that the files are in JavaScript Object Notation (JSON) format. However, it is difficult to read them in this output format.

    * Run the cat command again, but this time format the output (replace <filename.json> with the actual file name):

    ```bash
    cat <filename.json> | python -m json.tool
    ```
    
    This format is more readable. You can now also see the structure of the log entries. Notice that each entry contains the same standard fields, including awsRegion, eventName, eventSource, eventTime, requestParameters, sourceIPAddress, userIdentity, and more.

    An example log entry is shown in the graphic below.

    ![alt text](img/example-log-entry.png)

    You can now read the log entries. However, the number of entries—even in just this one log file—can be large. You might have downloaded more than just one log because new log files are created over time. You will need to find a way to search log entries across multiple files and also filter the results.

43. Consider how you want to target the search. You are not interested in everything that is happening in this account. Instead, your interest is in an action that was taken on a particular EC2 instance (that is, the web server that was hacked).

    Start by filtering the log results where the sourceIpAddress matches the IP address of the Cafe Web Server instance.

    Run the following command to set the WebServerIP address as a variable that you can use in future commands (replace <WebServerIP> with the actual Public IPv4 address of the Cafe Web Server instance):

    ```bash
    ip=<WebServerIP>
    ```

44. Run the following command:

    ```bash
    for i in $(ls); do echo $i && cat $i | python -m json.tool | grep sourceIPAddress ; done
    ```

    The command you ran does the following:

    * It creates a for loop that includes the names of the files in the current directory.

    * During each iteration of the for loop, it echoes the file name and then prints the contents of the file in JSON format.

    * However, only the lines of JSON that contain the sourceIPAddress tag are printed.

    Note that there are several log entries in the trail where the __sourceIPAddress__ was the Cafe Web Server instance.

45. Now run a similarly structured command, but where the command returns the __eventName__ of every captured event:

    ```bash
    for i in $(ls); do echo $i && cat $i | python -m json.tool | grep eventName ; done
    ```
    
    The command you ran follows the same logic as the command you ran before, but this time, it filters log entries for the __eventName__.

    The results of the previous command are more interesting. Many describe and list actions were recorded, and they look relatively harmless. However, if you scroll through the list, you can notice that occasional update actions were also recorded. You could use a text editor like vi to open a log that contains a recorded event that you want to know more about. You can then search for that eventName and look at the details.

    However, you might benefit from using a different tool other than grep to locate the interesting log entries more easily.


### Task 3.5: Analyze the logs by using AWS CLI cloudtrail commands

Another approach you can use to analyze CloudTrail logs is to use AWS CLI cloudtrail commands.

46. Open the AWS CLI Reference page for CloudTrail.

47. Choose the __lookup-events__ command to see details about the command.

    * Notice that you can look up events based on one of eight different attributes, including AWS access key, event name, user name, and others.

    * In the AWS CLI Command Reference page, scroll to the Examples, which shows how to filter the trail for console logins. Run that command in your terminal window:

    ```bash
    aws cloudtrail lookup-events --lookup-attributes AttributeKey=EventName,AttributeValue=ConsoleLogin
    ```

    The results of the command are interesting. It is good to know that the only user who has logged into the console is the same user that you are logged into the console as.

    However, there are other ways to modify resources on AWS instead of using the console.  The hacker might have used a different approach.

48. Run this command to find any actions that were taken on security groups in the AWS account:

    ```bash
    aws cloudtrail lookup-events --lookup-attributes AttributeKey=ResourceType,AttributeValue=AWS::EC2::SecurityGroup --output text
    ```

    Something in this result set might contain some information that would help you discover what happened, but there might be too many results for you to easily identify the issue.

    Perhaps you can narrow the search results further, so that you only get the results related to the security group that is used by the web server instance.

49. Run the following commands to find the security group ID that is used by the Cafe Web Server instance, and then echo the result to the terminal:

    ```bash
    region=$(curl http://169.254.169.254/latest/dynamic/instance-identity/document|grep region | cut -d '"' -f4)
    sgId=$(aws ec2 describe-instances --filters "Name=tag:Name,Values='Cafe Web Server'" --query 'Reservations[*].Instances[*].SecurityGroups[*].[GroupId]' --region $region --output text)
    echo $sgId
    ```
    
    Notice that a single security group ID was found.

50. Now use the security group ID that was returned by the previous command to further filter your AWS CLI cloudtrail command results:

    ```bash
    aws cloudtrail lookup-events --lookup-attributes AttributeKey=ResourceType,AttributeValue=AWS::EC2::SecurityGroup --region $region --output text | grep $sgId
    ```

    You could keep experimenting with different commands to filter the log results. However, you might wonder whether there is a better tool or solution for reading these logs. AWS has the AWS Partner Network (APN), where companies specialize in helping AWS customers with this challenge. See https://aws.amazon.com/cloudtrail/partners/ for a listing of APN Partner solutions.

    The APN Partner solutions suit the needs of many AWS customers. However, for the purposes of this activity, there is one additional approach to examining AWS CloudTrail log files that you might use, and it uses another AWS service. In the next task, you will explore AWS CloudTrail logs by using Amazon Athena.

 
## Task 4: Analyze the CloudTrail logs by using Amazon Athena

As you experienced in the previous task, it can be difficult to find specific information within a very large dataset. CloudTrail logs are verbose for a reason—you might want to know every relevant detail about a particular action that was taken in your AWS account. However, using command line tools to filter the logs can be tedious.

It would be convenient if all the log data was in a database and you could use structured query language (SQL) queries to search for the log entries that you are most interested in. Amazon Athena provides such a solution. Athena is an interactive query service that makes it easy to analyze data in Amazon Simple Storage Service (Amazon S3) by using standard SQL.

In this task, you will use Amazon Athena to analyze your CloudTrail logs.

 
### Task 4.1: Create the Amazon Athena table

51. In the AWS Management Console, in the search box next to  __Services__ search for and select the __CloudTrail__ service to open the CloudTrail console.

52. In the navigation pane, choose __Event history__.

    Notice that CloudTrail provides this event history interface where you can apply filters and conduct a basic search based on parameters, such as __Event name__ or __Resource type__. The __Event history__ page can be a useful tool, and you are free to explore it. However, in this activity, you will use Amazon Athena.

53. From the __Event history__ page, choose __Create Athena table__.

    * __Storage location__: Choose the __monitoring####__ Amazon S3 bucket where you configured CloudTrail to store log files.

54. Take a moment to analyze how the Amazon Athena CREATE TABLE statement is formed.

It will create a database column for each of the standard name-value pairs in each JSON-formatted CloudTrail log entry. Refer back to the image of the JSON format of a typical log entry in Task 3.4 to confirm this.

At the bottom of the CREATE TABLE SQL statement, notice the LOCATION statement. This indicates the Amazon S3 location where the table data will be stored. In this case, the data is already there. You are defining the table schema that will be used to parse existing JSON-structured data.

For details on AWS CloudTrail record structure, see https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-event-reference.html.

For details on how this Amazon Athena table was created, see the CREATE EXTERNAL TABLE document at https://docs.aws.amazon.com/athena/latest/ug/cloudtrail-logs.html.

 

55. After you are done analyzing the CREATE TABLE details, choose Create table.

    The table is created with a default name that includes the name of the Amazon S3 bucket.

56. In the search box next to  __Services__ search for and select the __Athena__ service to open the Athena console.

 
### Task 4.2: Analyze logs using Athena

The advantage of using Athena is that you can now run SQL queries over your log data.

57. If you do not already see the __Athena Query Editor__, choose __Explore the query editor__ and it should then display.

58. In the left panel of the  __Athena Query Editor__, you should see the __cloudtrail_logs_monitoring####__ table.

    Choose the plus icon next to table name to reveal the column names.

    __Analysis__: Notice how each standard child element that exists in a CloudTrail log record in JSON format has a corresponding column name in this database. The useridentity database column is a struct, because it contains more than a single name-value pair. Similarly, the resources database column is an array.

59. Start by setting up a query results location and then running a simple query to get an idea of the data that is available in the logs.

    * Choose the __View settings__ button that appears above the query panel, then choose __Manage__.

    * Choose __Browse S3__, select your monitoring#### bucket, and select __Choose__.

    * In the Location of query result box, add /results/ to the value, so that it now reads s3://monitoring####/results/where monitoring#### is the name of the bucket you created earlier.

    * Choose __Save__.

    * Return to the __Editor__ tab. 

    * Paste the following SQL query into the __New query 1__ panel. Replace #### with the numbers in your actual table, and choose __Run__.

    ```sql
    SELECT *
    FROM cloudtrail_logs_monitoring####
    LIMIT 5
    ```

    This query returns 5 rows of data. Look at the result set (scroll to the right in the __Results__ panel to see additional column data).

    The useridentity, eventtime, eventsource, eventname, requestparameters columns look like they contain interesting data.

    That useridentity column has lots of detail that make it more difficult to read though. You will now return only the user name for that column.

60. Run a new query that selects only those columns that were previously mentioned. This time, limit the results to 30 rows:

    ```sql
    SELECT useridentity.userName, eventtime, eventsource, eventname, requestparameters
    FROM cloudtrail_logs_monitoring####
    LIMIT 30
    ```

    This information is interesting, but recall what you are looking for.

    Specifically, someone modified the security group that is associated with the Cafe Web Server instance, and you want to know who it was.

### Challenge: Identify the hacker
In this section of the activity, you are challenged to discover the log entry that includes the essential information about who hacked the website. Specific steps are not provided. Instead, you must experiment with running different queries until you find the information that you are looking for.

TIPS:

* __TIP #1__: Look at the data that was returned by the last command that you ran. Even if none of the log entry details that display are the log entry you are looking for, they still give you an indication of what kinds of data the different columns contain. Don't be afraid to experiment with running modified SQL queries. Choose the + icon next to __New query 1__ to create a second query tab. This way, you can preserve older queries without deleting them.

* __TIP #2__: Try filtering by events that are related to the EC2 service. Remember that you can add WHERE clauses, such as WHERE eventsource = 'ec2.amazonaws.com'

* __TIP #3__: To ensure you are querying the entire log set, remove the LIMIT clause from your query.

* __TIP #4__: Take a look at the kind of data that is captured in the eventname column. Can you further refine your SQL query so that it looks for only events that contain the word Security? Remember that SQL allows you to use compound WHERE clauses that look for pattern matches. For example: WHERE columnName = 'some value' AND otherColumnName LIKE '%part of some value%'

* __TIP #5__: After you have successfully filtered all security-related actions in the log, analyze the eventnames further. Do any of them look suspicious? Can you adjust the WHERE clause to search for a particular eventname?

* __TIP #6__: If you are still looking for the entry that shows who opened port 22 to the world, here is a general query that is often useful to run. This query might help identify the action:

  ```sql
  SELECT DISTINCT useridentity.userName, eventName, eventSource FROM cloudtrail_logs_monitoring#### WHERE from_iso8601_timestamp(eventtime) > date_add('day', -1, now()) ORDER BY eventSource;
  ```

  It returns a list of all users who were active in the account in the past day, and the distinct actions they have taken.

  You have successfully completed the challenge if you can identify the following information:

  * The name of the AWS user who created the security hole in the Cafe Web Server security group

  * The exact time that they hacked the security group

  * The IP address from which they hacked it (copy this value to a text file for later reference)

  * The method they used to perform the hack (console or programmatic access)

Congratulations—you have successfully uncovered the identity of the hacker!


## Task 5: Further Analysis of the Hack and Improving Security

In this last task, you will work to secure both your AWS account, and the web server instance.


### Task 5.1: Check the OS users

61. In the terminal where you have an active SSH session to the web server instance, run the following command to find out who has recently logged into this OS:

    ```bash
    sudo aureport --auth
    ```
    
    That is interesting! There is evidence that a user other than ec2-user has logged in. Who is that chaos-user?

62. Run the who command to figure out who is currently logged in:

    ```bash
    who
    ```

    Whoa! The user is still logged in! Let's get them off this instance right away.

63. Try removing the chaos-user OS user:

    ```bash
    sudo userdel -r chaos-user
    ```

    That didn't work, because they are still logged in. However, it did return the process number they are connected as.

64. Stop the process that has the active chaos-user login session (replace __ProcNum__ with the process number returned by the last command):

    ```bash
    sudo kill -9 ProcNum
    ```

65. Run the who command again to verify they are no longer connected:

    ```bash
    who
    ```

    Now you (the ec2-user) should be the only user connected.

66. Try again to delete the chaos-user OS user:

    ```bash
    sudo userdel -r chaos-user
    ```

    It should succeed this time.

67. Verify no other suspicious OS users who can login:

    ```bash
    sudo cat /etc/passwd | grep -v nologin
    ```

    Note that the grep part of the command you just ran filtered out the OS users who do not have a login.

    The root, sync, shutdown, and halt users are all standard OS users in Amazon Linux, so there are no other concerning user logins on this instance.

 
### Task 5.2: Update SSH security
 
68. Analyze SSH settings on the instance.

    You have removed the OS user who hacked in, but how did they manage to SSH into this instance in the first place?

    You have been careful about who has access to the key pair file. However, maybe you should check the SSH settings on this instance.

    ```bash
    sudo ls -l /etc/ssh/sshd_config
    ```

    Notice the last modified timestamp for the file. This file was modified today! That is concerning.

69. Edit the SSH configuration file in the VI editor:

    ```bash
    sudo vi /etc/ssh/sshd_config
    ```

    * Analyze the details of this file. Type :set number to see the line numbers in this file.

    * Notice on line 61 that password authentication is enabled. That is definitely not a security best practice!

    * That means that anyone who knows (or can correctly guess) the username and password combination of an OS user can remotely access this instance, without using an SSH key pair. This setting needs to be corrected.

    * Move your cursor (using the arrow up or down keys) to the "PasswordAuthentication yes" line and comment it out.

    __Tip__: Type a on your keyboard to enter edit mode in VI, add a # character at the start of the line.

    * Next, move your cursor to "#PasswordAuthentication no" line (line 63) by using the arrow keys and uncomment this line (remove the # character).

    * Choose the __Esc key__ on your keyboard to exit edit mode.

    * __Save__ the changes and exit the VI editor using this command: :wq

70. Restart the SSH service so that the changes go into effect:

    ```bash
    sudo service sshd restart
    ```

    Note: If running the command above interrupts your SSH connection, reestablish the SSH connection before continuing on to the next step.

71. Finally, in the EC2 console, return to the Web Server Security Group settings.

    With the WebSecurityGroup selected, go to the __Inbound rules__ tab choose __Edit inbound rules__.

    Delete the inbound rule that allows port 22 access from 0.0.0.0/0 (the one the hacker created)

72. Choose __Save rules__ to save the change.

Nice work! You have kicked the hacker out of this instance and remove the login account that they used. You also updated the SSH settings so that only users who have the correct key pair and the same source IP address as you can connect to it.

 
### Task 5.3: Fix the website
Now that the hacker no longer has access to this instance, you can fix the issue with the website.

73. Back in the terminal window where you are connect to the Cafe Web Server instance, navigate to the directory where the website image files are held and review the contents:

    ```bash
    cd /var/www/html/mompopcafe/images/
    ls -l
    ```

    It looks like the hacker created a backup of the original file.

74. Restore the original graphic on the website.

    ```bash
    sudo mv Coffee-and-Pastries.backup Coffee-and-Pastries.png
    ``` 

75. Test the fix, by reloading the http://<WebServerIP>/mompopcafe website in the browser.

    Tip: You may need to hold the Shift key down and choose the browser refresh button to see the change.

    That looks better!

 
## Task 5.4: Delete the AWS hacker user

Recall that the hacker not only accessed the EC2 instance hosting the website, but they also managed to run an AWS CLI command that opened port 22 in the security group to the entire internet. In this step you will remove the chaos IAM user from the account.

76. In the AWS Management Console, in the search box next to  __Services__ search for and select the __IAM__service to open the IAM console.

77. Choose the __Users__ link and check the box next to the chaos user.

78. Delete the chaos user.

    * Choose __Delete__, type in the user name chaos  and choose __Delete__.

      An error appears indicating that you must first delete the user's login profile.

    * Return to the terminal window and run the command below to delete the login profile.

      ```bash
      aws iam delete-login-profile --user-name=chaos
      ```

    * Return to the IAM console and try deleting the user again. This time the action should succeed.

      Nice work! That chaos user shouldn't be causing any trouble in the AWS account anymore.

__Update from Mom & Pop Café__

![alt text](img/cafe-scene.png)

Everyone at Mom & Pop Café is relieved that Sophie was able to uncover the identity of the person who committed the hack and remove their access to the web server and to the AWS account.

In the end, they were lucky that it looks like the hacker was just trying to have fun. However, they all know that the hacker could have caused serious damage. Everyone on the team at the cafe who participates in updating and maintaining the website now knows how important it is to keep the site secure. They are also definitely going to continue to use CloudTrail as a key tool for auditing activity on their AWS account.

 
## Activity complete

Congratulations! You have completed the lab.

79. Choose __End Lab__ at the top of this page and then choose __Yes__ to confirm that you want to end the lab.  

    A panel will appear, indicating that "DELETE has been initiated... You may close this message box now."

80. Choose the __X__ in the top right corner to close the panel.

 

© 2022, Amazon Web Services, Inc. and its affiliates. All rights reserved. This work may not be reproduced or redistributed, in whole or in part, without prior written permission from Amazon Web Services, Inc. Commercial copying, lending, or selling is prohibited.