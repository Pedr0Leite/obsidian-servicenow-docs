---
title: "There is over 19 000 000 records on sys_import_set_row table"
aliases:
  - KB0812527
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0812527
kb_number: KB0812527
last_modified: 2024-11-25
---

## Issue

It may happen that there are too many records in the sys\_import\_set\_row table, and the table cleaner job does not seem to work properly.

## Resolution

**We do not advise to truncate the table manually, because of all the dependencies.**

The best is to clean the table with the cleaner job: The 'Import Set Deleter' job has a sysauto\_script in its job context. if you navigate to sysauto\_script.list, and look for the sys\_id in the job context, you will find the scheduled script.

Our OOB setting is: delete import data older than 7 days ; maybe you have it set to more days, and that's why it's grown big? Otherwise, you may also lower it to 3 days, for instance.

Please find here a link about the best practices: [https://community.servicenow.com/community?id=community\_blog&sys\_id=52cdbec6dbd57fc8d58ea345ca9619ea](https://community.servicenow.com/community?id=community_blog&sys_id=52cdbec6dbd57fc8d58ea345ca9619ea)

## Additional Information
