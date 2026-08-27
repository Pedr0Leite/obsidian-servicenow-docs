---
title: "AWS Cloud Discovery Service Endpoint"
aliases:
  - KB0789845
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0789845
kb_number: KB0789845
last_modified: 2024-01-21
---

## AWS Cloud Discovery Service Endpoint

  

### Issue

If blanket allowance for “\*.amazonaws.com” cannot be provided for AWS Cloud Discovery, List of exact URL endpoints need to be whitelisted to run the AWS Cloud Discovery.

### Resolution

Use the list in below AWS documentation for service endpoints:  
[https://docs.aws.amazon.com/general/latest/gr/ec2-service.html](https://docs.aws.amazon.com/general/latest/gr/ec2-service.html)

  
Refer to the attached file "aws-general.pdf" (downloaded from [https://docs.aws.amazon.com/general/latest/gr/rande.html](https://docs.aws.amazon.com/general/latest/gr/rande.html)) for the same information at page 125.  
  
There's one more URL to add:  
https://ec2.amazonaws.com  
  
This should cover the URLs that AWS cloud discovery need.

### Related Links

Amazon Documentation:

[https://docs.aws.amazon.com/general/latest/gr/rande.html](https://docs.aws.amazon.com/general/latest/gr/rande.html)

[https://docs.aws.amazon.com/general/latest/gr/aws-service-information.html](https://docs.aws.amazon.com/general/latest/gr/aws-service-information.html)

[https://docs.aws.amazon.com/general/latest/gr/ec2-service.html](https://docs.aws.amazon.com/general/latest/gr/ec2-service.html)
