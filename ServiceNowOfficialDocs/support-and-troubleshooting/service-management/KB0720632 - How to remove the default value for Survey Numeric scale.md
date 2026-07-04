---
title: "How to remove the default value for Survey Numeric scale"
aliases:
  - KB0720632
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0720632
kb_number: KB0720632
last_modified: 2025-01-01
---

## How to remove the default value for Survey Numeric scale

  

### Issue

Whenever creating a Survey with a Numeric Scale Question Type, it is by default selecting the first value when the survey page is viewed.

### Resolution

To remove the default selection for a survey question, please follow the below steps:  

1) Go to the table survey\_question\_new.

2) From the Form layout select the checkbox field. Do not select the first choice.

3) Its value is "false" by default. Setting it to "true" fixes the issue removing the default selection.

Note : This issue is seen only when using the Legacy Surveys.

For more information on the Survey Management please refer the below documentation :

[https://docs.servicenow.com/csh?topicname=r\_ServiceNowPlatform.html&version=latest](https://docs.servicenow.com/csh?topicname=r_ServiceNowPlatform.html&version=latest)
