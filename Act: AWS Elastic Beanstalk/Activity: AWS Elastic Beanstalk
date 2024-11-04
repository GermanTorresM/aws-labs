# Activity: AWS Elastic Beanstalk

## Lab overview

This activity provides you with an Amazon Web Services (AWS) account where an AWS Elastic Beanstalk environment has been pre-created for you. You will deploy code to it and observe the AWS resources that make up the Elastic Beanstalk environment.

## Duration

This activity takes approximately 30 minutes to complete.

## AWS service restrictions

In this lab environment, access to AWS services and service actions might be restricted to the ones that are needed to complete the lab instructions. You might encounter errors if you attempt to access other services or perform actions beyond the ones that are described in this lab.

## Accessing the AWS Management Console

1. At the top of these instructions, choose __Start Lab__.

   * The lab session starts.

   * A timer displays at the top of the page and shows the time remaining in the session.

     __Tip:__ To refresh the session length at any time, choose  Start Lab again before the timer reaches 0:00.

   * Before you continue, wait until the circle icon to the right of the AWS  link in the upper-left corner turns green. 

2. To connect to the AWS Management Console, choose the AWS link in the upper-left corner.

   * A new browser tab opens and connects you to the console.

     __Tip:__ If a new browser tab does not open, a banner or icon is usually at the top of your browser with the message that your browser is preventing the site from opening pop-up windows. Choose the banner or icon, and then choose __Allow pop-ups__.

3. Arrange the AWS Management Console tab so that it displays along side these instructions. Ideally, you will be able to see both browser tabs at the same time, to make it easier to follow the lab steps.


## Getting Credit for your work

At the end of this lab you will be instructed to submit the lab to receive a score based on your progress.

__Tip:__ The script that checks you works may only award points if you name resources and set configurations as specified. In particular, values in these instructions that appear in This Format should be entered exactly as documented (case-sensitive).

 
## Task 1: Access the Elastic Beanstalk environment

4. In the console, in the search box to the right of to  __*Services*__, search for and choose __*Elastic Beanstalk*__. 

   A page titled __Environments__ should open, and it should show a table that lists the details for an existing Elastic Beanstalk application.  

   __Note:__ If the status in the __Health__ column is not Ok, it has not finished starting yet. Wait a few moments, and it should change to Ok.

   ![alt text](img/elastic-beanstalk-app.png)

5. Under the __Environment name__ column, choose the name of the environment.

   The __Dashboard__ page for your Elastic Beanstalk environment opens.

6. Notice that the page shows that the health of your application is Ok.

   The Elastic Beanstalk environment is ready to host an application. However, it does not yet have running code.

7. Test access to the environment.

   * Near the top of the page, choose the Domain link (the URL ends in elasticbeanstalk.com).

   * When you choose the URL, a new browser tab opens. However, you should see that it displays an __HTTP Status 404 - Not Found__ message. 

     This behavior is expected because this application server doesn't have an application running on it yet. 

   * Return to the Elastic Beanstalk console.

     In the next step, you will deploy code in your Elastic Beanstalk environment.

 
## Task 2: Deploy a sample application to Elastic Beanstalk

8. To download a sample application, choose this link:
https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/samples/tomcat.zip

9. Back in the Elastic Beanstalk Dashboard, choose __Upload and Deploy__.

10. Choose __Choose File__, then navigate to and open the __tomcat.zip__ file that you just downloaded.

11. Choose __Deploy__.

    It will take a minute or two for Elastic Beanstalk to update your environment and deploy the application.

12. After the deployment is complete, choose the Domain URL link (or, if you still have the browser tab that displayed the 404 status, refresh that page).

    The web application that you deployed displays.

    ![alt text](img/web-app.png)

    Congratulations, you have successfully deployed an application on Elastic Beanstalk!

13. Back in the Elastic Beanstalk console, choose __Configuration__ in the left pane.

    Notice the details here.

    For example, in the __Instance traffic and scaling__ panel, it indicates the EC2 Security groups, minimum and maximum instances, and instance type details of the Amazon Elastic Compute Cloud (Amazon EC2) instances that are hosting your web application.

14. In the __Networking, database, and tags__ panel, no configuration details display, because the environment does not include a database.

15. In the __Networking, database, and tags__ row, choose __Edit__.

    Note that you could easily enable a database to this environment if you wanted to: you only need to set a few basic configurations and choose __Apply__. (However, for the purposes of this activity, you do not need to add a database.)

    * Choose __Cancel__ at the bottom of the screen.

16. In the left panel under Environment, choose __Monitoring__.

    Browse through the charts to see the kinds of information that are available to you.


## Task 3: Explore the AWS resources that support your application

17. In the console, in the search box to the right of to  __*Services*__, search for and choose __EC2__

18. Choose __Instances__.

    Note that two instances that support your web application are running (they both contain samp in their names). 

19. If you want to continue exploring the Amazon EC2 service resources that were created by Elastic Beanstalk, feel free to explore them. You will find:

    * A security group with port 80 open

    * A load balancer that both instances belong to

    * An Auto Scaling group that runs from two to six instances, depending on the network load

    Though Elastic Beanstalk created these resources for you, you still have access to them.


## Submitting your work

20. To record your progress, choose __Submit__ at the top of these instructions.

21. When prompted, choose __Yes__.

    After a couple of minutes, the grades panel appears and shows you how many points you earned for each task. If the results don't display after a couple of minutes, choose __Grades__ at the top of these instructions.

    __Important__:  Some of the checks made by the submission process in this lab will only give you credit if it has been at least 5 minutes since you completed the action. If you do not receive credit the first time you submit, you may need to wait a couple minutes and the submit again to receive credit for these items. 

    __Tip__: You can submit your work multiple times. After you change your work, choose __Submit__ again. Your last submission is recorded for this lab.

22. To find detailed feedback about your work, choose __Submission Report__.

    __Tip__: For any checks where you did not receive full points, there are sometimes helpful details provided in the submission report.


## Activity complete

Congratulations! You have completed the activity.

23. At the top of this page, choose End Lab and then to confirm that you want to end the activity, choose Yes.  

    A panel appears, with a message that indicates: DELETE has been initiated... You may close this message box now.

24. To close the panel, go to the top-right corner and choose the __X__.

 

© 2023, Amazon Web Services, Inc. and its affiliates. All rights reserved. This work may not be reproduced or redistributed, in whole or in part, without prior written permission from Amazon Web Services, Inc. Commercial copying, lending, or selling is prohibited.