---
title: "Failed to download AWS Billing information with error: The specified key does not exist"
aliases:
  - KB0656780
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0656780
kb_number: KB0656780
last_modified: 2025-02-14
---

## Failed to download AWS Billing information with error: The specified key does not exist

  

### Issue

#### AWS billing schedule fails with the following error in the Current Job Details field:

Downloading dataUnable to establish connection to [https://s3.amazonaws.com:](https://s3.amazonaws.com:) com.amazonaws.services.s3.model.AmazonS3Exception: The specified key does not exist.

(Service: Amazon S3; Status Code: 404; Error Code: NoSuchKey; Request ID: 27F869BDF8FD446F),

S3 Extended Request ID: EMbXszhYsIToNOfA7K1fnVPu2c+QlZFy5BzbNo3XdgpndZEmX9/VWfwoNxn2Tqe+jZxBwiib7KM=

![](/sys_attachment.do?sys_id=c5b12b071b0ec990c465ece6b04bcbad)

### Resolution

Review the following items:

-   A service account in the instance for AWS.
-   A payer account that gets billing information for all linked accounts.
-   The Amazon S3 bucket where you want AWS to publish your detailed billing reports is  designated. In addition, the credential used to access this report must have permissions to this S3 bucket.

### Related Links

[Create a cloud billing schedule](https://docs.servicenow.com/csh?topicname=cloud-configuration.html&version=latest "Create a cloud billing schedule")

[AWS Documentation](https://aws.amazon.com/documentation/ "AWS Documentation")
