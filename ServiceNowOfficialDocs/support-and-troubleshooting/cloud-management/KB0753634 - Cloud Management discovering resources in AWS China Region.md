---
title: "Cloud Management discovering resources in AWS China Region"
aliases:
  - KB0753634
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0753634
kb_number: KB0753634
last_modified: 2024-11-21
---

## Issue

AWS China (Beijing) Region and AWS China (Ningxia) Region are the two AWS Regions located within China. When attempting to run Cloud Discovery on AWS China regions the following error is displayed:

"The credentials can't be used with the account ID provided Pattern name: Amazon AWS Service account"

## Resolution

-   In order to support AWS China regions, user had to create scripted API's using Cloud API for the China regions. As for the China region, the URL is different for each service eg. ec2.cn-northwest-1.amazonaws.com.cn and for the global services it goes like this - ec2.region.amazonaws.com.
-   The latest version of Discovery and Service Mapping Patterns supports discovering AWS services in the China region. You can discover these services on the Now Platform, starting from Xanadu Patch 3 and Washington DC Patch 9 instances.
-   Previously the support was provided only for AWS Global and AWS GovCloud (US) regions

Note : Use the datacenter URL like : [https://organizations.cn-northwest-1.amazonaws.com.cn](https://organizations.cn-northwest-1.amazonaws.com.cn) , while configuring the master account & that should resolve the error.

## Additional Information

For more information check the documentation : [Amazon AWS Cloud components discovery using patterns](https://www.servicenow.com/docs/csh?topicname=data-discovered-aws-patterns.html&version=latest)
