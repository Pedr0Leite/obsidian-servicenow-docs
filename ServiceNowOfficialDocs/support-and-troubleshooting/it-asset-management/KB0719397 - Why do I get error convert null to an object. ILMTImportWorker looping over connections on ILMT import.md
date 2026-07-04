---
title: "Why do I get error \"convert null to an object. ILMTImportWorker : looping over connections\" on ILMT import?"
aliases:
  - KB0719397
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0719397
kb_number: KB0719397
last_modified: 2024-04-07
---

## Why do I get error "convert null to an object. ILMTImportWorker : looping over connections" on ILMT import?

  

### Issue

# Symptoms

* * *

Once you have setup connection for IBM ILMT integration, on running the scheduled job "ILMT Scheduled Data Import"

[https://xxxxxx.service-now.com/sysauto\_script.do?sys\_id=8b1be03453d003002658ddeeff7b12c4](https://xxxxxx.service-now.com/sysauto_script.do?sys_id=8b1be03453d003002658ddeeff7b12c4)

you will see the following error message in system log:

ILMTImportWorker Unhandled exception: TypeError: Cannot convert null to an object. ILMTImportWorker : looping over connections. 

# Resolution

* * *

This error occurs if the scheduled job "ILMT Scheduled Data Import" does not have a valid user. In order to set a valid user, please follow the steps:

1.  Configure the form to include field "run\_as".
2.  Add a user who has admin rights as value to the above field and update.
