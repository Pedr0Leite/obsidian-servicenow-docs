---
title: "Subscription Consumption Summary for \"Salesforce Marketing Cloud\" is missing Contract start date, Contract end date, Actual monthly consumption, & Expected monthly consumption"
aliases:
  - KB2685449
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB2685449
kb_number: KB2685449
last_modified: 2026-03-27
---

## Subscription Consumption Summary for "Salesforce Marketing Cloud" is missing Contract start date, Contract end date, Actual monthly consumption, & Expected monthly consumption

  

### Issue

**Issue:**

Subscription Consumption Summary for "Salesforce Marketing Cloud" profile type doesn't populate Contract start date, Contract end date, Actual monthly consumption, & Expected monthly consumption fields.  
  
**Steps to reproduce:**

1.  Create an Integration Profile for "Salesforce Marketing Cloud Subscription" profile type.
2.  Open the Profile, then navigate to tab "Subscription Consumption Summaries".  
    The Contract start date, Contract end date, Actual monthly consumption, & Expected monthly consumption fields are not populated.  
    https://<instance\_name>.service-now.com/sam\_saas\_consumption\_summary\_list.do?sysparm\_query=subscription\_profile.display\_nameLIKESalesforce  
    ![](/sys_attachment.do?sys_id=217ed9cf473b761cb8a4aa25126d4366 "Screenshot 1.png")
3.  The job "SAM - Refresh Salesforce CRM Experience Cloud None Prod Consumption" that is responsible to collect the "Subscription Consumption Summaries" have run successful.  
    ![](/sys_attachment.do?sys_id=a17ed9cf473b761cb8a4aa25126d436b "Screenshot 2.png")

### Release

Yokohama

### Cause

Our current design does not support populating Contract start date, Contract end date, Actual monthly consumption, & Expected monthly consumption for Salesforce Marketing Cloud profile.

### Resolution

Customer to create an enhancement request on the Idea portal for our Product Management to review.

Find out more about the enhancement request process and our methods for reviewing them at [KB0755878](https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0755878)
