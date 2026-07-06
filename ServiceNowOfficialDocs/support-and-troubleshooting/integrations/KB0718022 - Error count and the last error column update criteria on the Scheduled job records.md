---
title: "Error count and the last error column update criteria on the Scheduled job records"
aliases:
  - KB0718022
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0718022
kb_number: KB0718022
last_modified: 2025-01-07
---

## Error count and the last error column update criteria on the Scheduled job records

  

### Issue

**Overview**

When are the “error count” and “last error columns” updated in the scheduled job records under sys trigger table

**Description**

Under System scheduler application , we do have scheduled job records which have 2 columns for each record – Error count and Last error. Observe that these columns are not always populated for every Job failure. This solution talks about when these columns are updated for a scheduled Job failures

![](/sys_attachment.do?sys_id=5f2a6026db42b450e515c2230596190b)

**Solution**

* * *

The columns are updated only when the error reported in the logs for a scheduled job is popped up by a Java throwable class like Java threads. Ex: Thread.java

In the event a job failed catastrophically and an error bubbles up, the scheduler throw an event and re-queue.   
Note this is a departure from previous behavior that uses to set the state to error after two failures in a row

Based on the internal code, we can’t expect the above mentioned columns to get updated for every scheduled job failure
