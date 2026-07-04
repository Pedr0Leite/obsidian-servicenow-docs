---
title: "Old Password Reset Request records disappear or cannot be found due to system automatic clean up"
aliases:
  - KB0647713
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0647713
kb_number: KB0647713
last_modified: 2024-09-19
---

## Old Password Reset Request records disappear or cannot be found due to system automatic clean up

  

### Issue

Password Reset Request records more than three months old are no longer in the instance and cannot be found anywhere. This has caused confusion as to why these records were gone and where they went because Password Reset Request records contained user data.

### Cause

Instances by default have an auto flush function activated for table pwd\_reset\_request and pwd\_reset\_activity. Table pwd\_reset\_request and pwd\_reset\_activity contain the records for Password Reset Requests and Password Reset Activity history. These auto flush configurations are in the table sys\_auto\_flush. By default, the auto flush function would automatically delete the records older than 90 days in these two tables.

### Resolution

If you don't want to delete any Password Reset history records, you can find the related records in table sys\_auto\_flush and disable them to stop the automatic clean up. You can also change the field **Age in seconds** from the default 7,776,000 seconds (90 days) to a longer period to keep more records.
