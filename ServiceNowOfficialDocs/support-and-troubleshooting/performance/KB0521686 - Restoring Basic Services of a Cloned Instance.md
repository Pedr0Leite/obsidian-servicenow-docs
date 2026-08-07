---
title: "Restoring Basic Services of a Cloned Instance"
aliases:
  - KB0521686
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0521686
kb_number: KB0521686
last_modified: 2024-04-30
---

## Restoring Basic Services of a Cloned Instance

  

### Issue

Restoring Basic Services of a Cloned Instance

  
  
Symptoms

* * *

-   My cloned instance is not sending email.
-   My cloned instance is not receiving email.
-   Scheduled jobs are not running after my clone.

Cause

* * *

-   Email service is disabled.
-   Scheduled jobs are running on nodes from the original source instance.

Resolution

* * *

This section details the steps involved to restore email functionality and to ensure that all scheduled jobs are running on proper nodes after cloning an instance. Once a clone request is complete, the clone's email service is disabled to prevent it from sending duplicate or unwanted email. In addition, you may need to reassign scheduled jobs to the clone's nodes. 

 To restore basic service of a cloned instance:

1.  1.  Email notifications use the email properties that are defined in the **System Properties > Email** module. If emails are not sending or receiving from the cloned instance, the instance may not have its email sending/receiving checkboxes turned on.
    2.  To ensure uninterrupted service, scheduled jobs must be running on the proper nodes. For example, scheduled jobs must run on the nodes of the cloned instance, not the nodes of the original instance.

**Important**: Your ServiceNow administrator should understand the effects of changing scheduled jobs to different nodes before performing these steps. Contact customer support if you have questions.
