# Lab 4: Working with EBS

## Lab Overview

![alt text](img/architectural-diagram.png)

This lab focuses on Amazon Elastic Block Store (Amazon EBS), a key underlying storage mechanism for Amazon EC2 instances. In this lab, you will learn how to create an Amazon EBS volume, attach it to an instance, apply a file system to the volume, and then take a snapshot backup.

 
## Topics covered

By the end of this lab, you will be able to:

* Create an Amazon EBS volume

* Attach and mount your volume to an EC2 instance

* Create a snapshot of your volume

* Create a new volume from your snapshot

* Attach and mount the new volume to your EC2 instance

 
## Duration
This lab will require approximately __30 minutes__ to complete.

 
## AWS service restrictions
In this lab environment, access to AWS services and service actions might be restricted to the ones that are needed to complete the lab instructions. You might encounter errors if you attempt to access other services or perform actions beyond the ones that are described in this lab.

 
### What is Amazon Elastic Block Store?

__Amazon Elastic Block Store (Amazon EBS)__ offers persistent storage for Amazon EC2 instances. Amazon EBS volumes are network-attached and persist independently from the life of an instance. Amazon EBS volumes are highly available, highly reliable volumes that can be leveraged as an Amazon EC2 instances boot partition or attached to a running Amazon EC2 instance as a standard block device.

When used as a boot partition, Amazon EC2 instances can be stopped and subsequently restarted, enabling you to pay only for the storage resources used while maintaining your instance's state. Amazon EBS volumes offer greatly improved durability over local Amazon EC2 instance stores because Amazon EBS volumes are automatically replicated on the backend (in a single Availability Zone).

For those wanting even more durability, Amazon EBS provides the ability to create point-in-time consistent snapshots of your volumes that are then stored in Amazon Simple Storage Service (Amazon S3) and automatically replicated across multiple Availability Zones. These snapshots can be used as the starting point for new Amazon EBS volumes and can protect your data for long-term durability. You can also easily share these snapshots with co-workers and other AWS developers.

This lab guide explains basic concepts of Amazon EBS in a step-by-step fashion. However, it can only give a brief overview of Amazon EBS concepts. For further information, see the Amazon EBS documentation.

 
### Amazon EBS Volume Features

Amazon EBS volumes deliver the following features:

* __Persistent storage:__ Volume lifetime is independent of any particular Amazon EC2 instance.

* __General purpose:__ Amazon EBS volumes are raw, unformatted block devices that can be used from any operating system.

* __High performance:__ Amazon EBS volumes are equal to or better than local Amazon EC2 drives.

* __High reliability:__ Amazon EBS volumes have built-in redundancy within an Availability Zone.

* __Designed for resiliency:__ The AFR (Annual Failure Rate) of Amazon EBS is between 0.1% and 1%.

* __Variable size:__ Volume sizes range from 1 GB to 16 TB.

* __Easy to use:__ Amazon EBS volumes can be easily created, attached, backed up, restored, and deleted.

 
## Accessing the AWS Management Console

1. At the top of these instructions, choose  __Start Lab__.

   * The lab session starts.

   * A timer displays at the top of the page and shows the time remaining in the session.

     __Tip:__ To refresh the session length at any time, choose  __Start Lab__ again before the timer reaches 0:00.

   * Before you continue, wait until the circle icon to the right of the AWS  link in the upper-left corner turns green. 

2. To connect to the AWS Management Console, choose the __AWS__ link in the upper-left corner.

   * A new browser tab opens and connects you to the console.

     __Tip:__ If a new browser tab does not open, a banner or icon is usually at the top of your browser with the message that your browser is preventing the site from opening pop-up windows. Choose the banner or icon, and then choose __Allow pop-ups__.

3. Arrange the AWS Management Console tab so that it displays along side these instructions. Ideally, you will be able to see both browser tabs at the same time, to make it easier to follow the lab steps.

 
## Getting Credit for your work
At the end of this lab you will be instructed to submit the lab to receive a score based on your progress.

__Tip:__ The script that checks you works may only award points if you name resources and set configurations as specified. In particular, values in these instructions that appear in This Format should be entered exactly as documented (case-sensitive).

 
## Task 1: Create a New EBS Volume

In this task, you will create and attach an Amazon EBS volume to a new Amazon EC2 instance.

4. In the AWS Management Console, in the search box next to  __Services__, search for and select __EC2__.

5. In the left navigation pane, choose __Instances__.

   An Amazon EC2 instance named __Lab__ has already been launched for your lab.

6. Note the __Availability Zone__ of the instance. It will look similar to us-east-1a.

7. In the left navigation pane, choose __Volumes__.

   You will see an existing volume that is being used by the Amazon EC2 instance. This volume has a size of 8 GiB, which makes it easy to distinguish from the volume you will create next, which will be 1 GiB in size.

8. Choose <span style="color:orange">Create volume</span> then configure:

   * __Volume Type__: General Purpose SSD (gp2)

   * __Size (GiB)__: 1. __NOTE__: You may be restricted from creating large volumes.

   * __Availability Zone__: Select the same availability zone as your EC2 instance.

   * Choose __Add tag__

   * In the Tag Editor, enter:

     * __Key__: Name

     * __Value__: My Volume

9. Choose <span style="color:orange">Create Volume</span>

   Your new volume will appear in the list, and will move from the Creating state to the Available state. You may need to choose __refresh__  to see your new volume.

 
## Task 2: Attach the Volume to an Instance

In this task you will attach the new EBS volume to the Amazon EC2 instance.

10. Select  __My Volume__.

11. In the __Actions__ menu, choose __Attach volume__.

12. Choose the __Instance__ field, then select the __Lab__ instance.

    Note that the __Device__ name is set to /dev/sdf. Notice also the message displayed that "Newer Linux kernels may rename your devices to /dev/xvdf through /dev/xvdp internally, even when the device name entered here (and shown in the details) is /dev/sdf through /dev/sdp."

13. Choose <span style="color:orange">Attach volume</span>

    The volume state is now In-use.

 
## Task 3: Connect to Your Amazon EC2 Instance

In this task, you will connect to the EC2 instance using EC2 Instance Connect which provides access to a terminal in the browser.

14. In the AWS Management Console, in the search box next to  __Services__ , search for and select __EC2__.

15. Choose __Instances__.

16. Select the __Lab__ instance, and then choose __Connect__.

17. On the __EC2 Instance Connect__ tab, choose __Connect__. 

    An EC2 Instance Connect terminal session opens and displays a $ prompt. 

 
## Task 4: Create and Configure Your File System

In this task, you will add the new volume to a Linux instance as an ext3 file system under the /mnt/data-store mount point.

18. View the storage available on your instance:

    Run the following command:

    ```bash
    df -h
    ```

    You should see output similar to:

    ```bash
    Filesystem      Size  Used Avail Use% Mounted on
    devtmpfs        4.0M     0  4.0M   0% /dev
    tmpfs           475M     0  475M   0% /dev/shm
    tmpfs           190M  2.8M  188M   2% /run
    /dev/xvda1      8.0G  1.6G  6.5G  20% /
    tmpfs           475M     0  475M   0% /tmp
    tmpfs            95M     0   95M   0% /run/user/1000
    ```

    The output shows that the original 8GB __/dev/xvda1__ disk volume mounted at / which indicates that it is the root volume. It hosts the Linux operating system of the EC2 instance. 

    The 1GB other volume that you attached to the Lab instance is not listed, because you have not yet created a file system on it or mounted the disk. Those actions are necessary so that Linux operating system can make use of the new storage space. You will take those actions next.

19. Create an ext3 file system on the new volume:

    ```bash
    sudo mkfs -t ext3 /dev/sdf
    ```

    The output should indicate that a new file system was created on the attached volume.

20. Create a directory for mounting the new storage volume:
    
	```bash
    sudo mkdir /mnt/data-store
    ```

21. Mount the new volume:

    ```bash
    sudo mount /dev/sdf /mnt/data-store
    ```

    To configure the Linux instance to mount this volume whenever the instance is started, you will need to add a line to /etc/fstab. Run the command below to accomplish that:

    ```bash
    echo "/dev/sdf   /mnt/data-store ext3 defaults,noatime 1 2" | sudo tee -a /etc/fstab
    ```

22. View the configuration file to see the setting on the last line:

    ```bash
    cat /etc/fstab
    ```

23. View the available storage again:

    ```bash
    df -h
	```

    The output will look similar to what is shown below.

    ```bash
    Filesystem      Size  Used Avail Use% Mounted on
    devtmpfs        484M     0  484M   0% /dev
    tmpfs           492M     0  492M   0% /dev/shm
    tmpfs           492M  460K  491M   1% /run
    tmpfs           492M     0  492M   0% /sys/fs/cgroup
    /dev/xvda1      8.0G  1.5G  6.6G  19% /
    tmpfs            99M     0   99M   0% /run/user/0
    tmpfs            99M     0   99M   0% /run/user/1000
    /dev/xvdf       976M  1.3M  924M   1% /mnt/data-store
    ```

    Notice the last line. The output now lists /dev/xvdf which is the new mounted volume.

24. On your mounted volume, create a file and add some text to it.

    ```bash
    sudo sh -c "echo some text has been written > /mnt/data-store/file.txt"
    ```

25. Verify that the text has been written to your volume.

    ```bash
    cat /mnt/data-store/file.txt
	```
	
	Leave the EC2 Instance Connect session running. You will return to it later in this lab.

 
## Task 5: Create an Amazon EBS Snapshot

In this task, you will create a snapshot of your EBS volume.

You can create any number of point-in-time, consistent snapshots from Amazon EBS volumes at any time. Amazon EBS snapshots are stored in Amazon S3 with high durability. New Amazon EBS volumes can be created out of snapshots for cloning or restoring backups. Amazon EBS snapshots can also be easily shared among AWS users or copied over AWS regions.

26. In the __EC2 Console__, choose __Volumes__ and select  __My Volume__.

27. In the __Actions__ menu, select  __Create snapshot__.

28. Choose __Add tag__ then configure:

    * __Key__: Name

    * __Value__: My Snapshot

    * Choose <span style="color:orange">Create snapshot</span>

29. In the left navigation pane, choose __Snapshots__.

    Your snapshot is displayed. The status will first have a state of Pending, which means that the snapshot is being created. It will then change to a state of Completed. 

    Note: Only used storage blocks are copied to snapshots, so empty blocks do not occupy any snapshot storage space.

30. In your EC2 Instance Connect session, delete the file that you created on your volume.

    ```bash
    sudo rm /mnt/data-store/file.txt
    ```
	
31. Verify that the file has been deleted.

    ```bash
    ls /mnt/data-store/
    ```

    Your file has been deleted.


## Task 6: Restore the Amazon EBS Snapshot

If you ever wish to retrieve data stored in a snapshot, you can Restore the snapshot to a new EBS volume.


### Create a Volume Using Your Snapshot

32. In the __EC2 console__, select  __My Snapshot__.

33. In the __Actions__ menu, select __Create volume from snapshot__.

34. For __Availability Zone__, select the same availability zone that you used earlier.

35. Choose __Add tag__ then configure:

    * __Key__: Name

    * __Value__: Restored Volume

    * Choose <span style="color:orange">Create volume</span>

    __Note__: When restoring a snapshot to a new volume, you can also modify the configuration, such as changing the volume type, size or Availability Zone.


### Attach the Restored Volume to Your EC2 Instance

36. In the left navigation pane, choose __Volumes__.

37. Select  __Restored Volume__.

38. In the __Actions__ menu, select __Attach volume__.

39. Choose the __Instance__ field, then select the __Lab__ instance that appears.

    Note that the __Device__ field is set to /dev/sdg. You will use this device identifier in a later task.

40. Choose <span style="color:orange">Attach volume</span>

    The volume state is now in-use.

 
### Mount the Restored Volume

41. Create a directory for mounting the new storage volume:

    ```bash
    sudo mkdir /mnt/data-store2
    ```

42. Mount the new volume:

    ```bash
    sudo mount /dev/sdg /mnt/data-store2
    ```

43. Verify that volume you mounted has the file that you created earlier.

    ```bash
    ls /mnt/data-store2/
    ```

    You should see file.txt.

 
## Submitting your work

44. To record your progress, choose __Submit__ at the top of these instructions.

45. When prompted, choose __Yes__.

    After a couple of minutes, the grades panel appears and shows you how many points you earned for each task. If the results don't display after a couple of minutes, choose __Grades__ at the top of these instructions.

    __Tip__: You can submit your work multiple times. After you change your work, choose __Submit__ again. Your last submission is recorded for this lab.

46. To find detailed feedback about your work, choose __Submission Report__.

    __Tip__: For any checks where you did not receive full points, there are sometimes helpful details provided in the submission report.


## Conclusion

Congratulations! You now have successfully:

* Created an Amazon EBS volume

* Attached the volume to an EC2 instance

* Created a file system on the volume

* Added a file to volume

* Created a snapshot of your volume

* Created a new volume from the snapshot

* Attached and mounted the new volume to your EC2 instance

* Verified that the file you created earlier was on the newly created volume


## Lab Complete

Congratulations! You have completed the lab.

47. Choose End Lab at the top of this page and then choose <span style="color:blue">Yes</span> to confirm that you want to end the lab.  

    A panel will appear, indicating that "DELETE has been initiated... You may close this message box now."

48. Choose the X in the top right corner to close the panel.

 

© 2023 Amazon Web Services, Inc. and its affiliates. All rights reserved. This work may not be reproduced or redistributed, in whole or in part, without prior written permission from Amazon Web Services, Inc. Commercial copying, lending, or selling is prohibited.