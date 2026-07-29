---
title: "Amazon EC2 spoke - Actions throw runtime error: The request must contain the parameter AWSAccessKeyId"
aliases:
  - KB0829920
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0829920
kb_number: KB0829920
last_modified: 2024-04-08
---

## Amazon EC2 spoke - Actions throw runtime error: The request must contain the parameter AWSAccessKeyId

  

### Issue

After AWS credentials is configured, when running Amazon EC2 spoke Flows / Actions, below error is received:

"The request must contain the parameter AWSAccessKeyId"

### Resolution

The issue can be caused by empty "Authentication Algorithm".

  

Open the AWS Credential, make sure "Authentication Algorithm" field is showing on the form.

Pick "AmazonEC2AuthAlgo", then update.

![](/sys_attachment.do?sys_id=3ee5304ddb8478d0fec4fb2439961984)

  

### Related Links

[Setup the Amazon EC2 spoke](https://docs.servicenow.com/csh?topicname=setup-amazon-ec2.html&version=latest#setup-amazon-ec2 "Setup the Amazon EC2 spoke")
