---
title: "Replacing characters in an inbound email to use key-value pairs."
aliases:
  - KB0815882
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0815882
kb_number: KB0815882
last_modified: 2024-04-08
---

## Replacing characters in an inbound email to use key-value pairs.

  

### Issue

ServiceNow Inbound Actions provide many ways to process an email and use the content of the email to populate information in cases, tasks, change requests etc.

One of the ways to get this achieved is by using key-value pairs: [https://docs.servicenow.com/csh?topicname=r\_SetFieldValsFromTheEmailBody.html&version=latest](https://docs.servicenow.com/csh?topicname=r_SetFieldValsFromTheEmailBody.html&version=latest)

To use this feature efficiently, the content of the email should be in this format **key: value**

If the content is in a different format, the Inbound Action would not pick the key-value pairs.

### Resolution

This needs to be handled in 2 parts:  
1\. Replace the characters  
2\. Process Inbound Action  
  
It has to be done in that order to ensure the email body is updated before the Inbound action is run.  
  
1\. Replace the characters:  
Write a Before business rule on /sys\_email table that runs on 'insert' to replace the characters   
For example, a business rule, before, insert, on sys\_email table to check for the character '`='` and replace it with '`:'`

`(function executeRule(current, previous /*null when async*/) {  	current.body = current.body.replace(/=/g, ':'); 	 })(current, previous);`

  
2\. Process Inbound Action  
Write an Inbound Action to process the email using the concepts mentioned in:  
https://docs.servicenow.com/csh?topicname=r\_SetFieldValsFromTheEmailBody.html&version=latest  
  
  
Note:  
Please keep in mind that the business rule is being written on a base system table (sys\_email) and this may cause overhead on email processing.
