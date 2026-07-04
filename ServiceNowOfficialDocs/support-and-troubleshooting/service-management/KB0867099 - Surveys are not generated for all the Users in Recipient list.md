---
title: "Surveys are not generated for all the Users in Recipient list"
aliases:
  - KB0867099
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0867099
kb_number: KB0867099
last_modified: 2026-06-24
---

## Surveys are not generated for all the Users in Recipient list

  

### Issue

  
  
You are unable to generate Survey Instances for your Users in an associated Recipient list.

In this Case scenario you have a recipient list of 45k users.

Hitting 'Send Invitations' or 'Save and Publish' does not create the expected amount of Recipients.

### Release

N/A

### Cause

  
You have hit a transaction quota rule which killed the survey transaction which is longer than 5 mins.  
In general Survey doesn't have time limitation in creation, but system admin can set up maximum execution time, called "Transaction quota rule" which you could hit.

Below is the document of Transaction Quotas :  
https://docs.servicenow.com/bundle/paris-platform-administration/page/administer/platform-performance/concept/c\_TransactionQuotas.html

### Resolution

  
If you hit this type of issue where due to resources or timeout you get unexpected behavior with large survey recipient lists generating survey instances the workaround is to try the below:

  
1\. From the navigator there is a module called Transaction Quota Rules. Then look for UI Transactions in this record, the 'Maximum Duration (seconds)' default is 298 seconds. If we increase this to a higher limit the number of survey instances created will be more in a single time.  
  
2\. In addition consider splitting the big recipient list group into a few smaller pieces.  
  
The survey metric type's schedule period is set to "no limit" by default and this means a user can receive as many survey instances as possible. Set the schedule period for the relevant survey to 'Only Once', this ensures a survey instance is assigned only once to the survey user. Then to send out the remaining surveys, you can click the 'send invitation' UI action again. This should create remaining survey instances only for Users who haven't previously received it.  
  
3\. Another option, is to use the background scripts as well.  
  
You can run attached script from work\_around.xml file as a background job.

NOTE: You will need to alter it and use the correct survey sysID and recipient list sysID for your instance. Please test it in your subprod before running in prod instance.
