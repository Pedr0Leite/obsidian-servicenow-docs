---
title: "Push notifications are stuck in Pending status"
aliases:
  - KB0811754
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0811754
kb_number: KB0811754
last_modified: 2024-04-08
---

## Push notifications are stuck in Pending status

  

### Issue

Push notifications are stuck in Pending status in the sys\_push\_notification table.

### Cause

The schedule Job "Push" is not running.

### Resolution

1.  Check the sys\_trigger\_list.do table for https://instancemame.service-now.com/sys\_trigger\_list.do?sysparm\_query=name%3DPush
2.  Check If the Job 'Push' is set the next action to be set a previous date.
3.  Set the record to 'Error' State. Save the record. Change the date to the current date and time if the date and time is in the past. Save the record.  
    Set the state to 'Ready'.
