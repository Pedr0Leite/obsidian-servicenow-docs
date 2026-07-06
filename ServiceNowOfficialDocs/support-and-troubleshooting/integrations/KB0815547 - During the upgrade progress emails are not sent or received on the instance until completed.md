---
title: "During the upgrade progress emails are not sent or received on the instance until completed"
aliases:
  - KB0815547
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0815547
kb_number: KB0815547
last_modified: 2024-04-10
---

## Issue

When the upgrade is happening no emails are triggered or received during the progress and sends the emails after the upgrade is completed.

## Resolution

-   Go to the Scheduled Job (sys\_trigger) under the System Scheduler.
-   Since the upgrade safe is marked as false, the event processing job has not run during the upgrade.
-   Due to which the mails not sent during the upgrade as the events are not processed.  
      
    Please make sure the upgrade safe field is "true". By default in the Out Of Box instance, the upgrade safe is set as "true".
