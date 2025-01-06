# AWS IAM: Best practices to follow

## What is IAM?
IAM is an AWS service that stands for Identity and Access Management. It is used to define the identity of our users. By default, we are given a root account when we first set up our AWS account. It is through IAM that we can create user accounts for accessing AWS instead and perform certain actions.

## Tip 1:
Never use the root account, always create a user account and use that account instead. The root account is simply used for account setup, and nothing else.

## Tip 2:
Enable MFA (Multi-Factor Authentication) for your root account and for your IAM users. An extra layer of security always goes a long way

## Tip 3:
Create an effective password policy for your users. You can decide on the number of characters that a user must have in their password, how often they must rotate their password, and set up many other characteristics

## Tip 4:
Never share your user's access and secret access keys with anyone! Each IAM user that you create will come with access keys, be sure to keep it private.

## Tip 5:
Be sure to add your IAM users to groups, and attach permissions to those groups. You can add permission directly to a user, but this can get chaotic and get disorganized, especially if you have a lot of users. So, be sure to group them accordingly... and assign permissions to those groups. Examples of groups may be "Administrators" or "Developers" or "Managers".