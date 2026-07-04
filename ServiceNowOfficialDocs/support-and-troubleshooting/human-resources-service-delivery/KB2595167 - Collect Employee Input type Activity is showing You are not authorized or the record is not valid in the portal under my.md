---
title: "Collect Employee Input type Activity is showing \"You are not authorized or the record is not valid\" in the portal under my tasks."
aliases:
  - KB2595167
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB2595167
kb_number: KB2595167
last_modified: 2025-10-31
---

## Collect Employee Input type Activity is showing "You are not authorized or the record is not valid" in the portal under my tasks.

  

### Issue

Hr task which has the hr task type as Collect Employee Input, it is not displaying any value and throwing a message "You are not authorized or the record is not valid".

### Release

All releases

### Resolution

This issue typically occurs when the category is missing in the \`asmt\_assessable\_record\` related to the survey definition. To resolve this, follow these steps:

1\. \*\*Check the Survey Definition:\*\* Review the survey definition that is experiencing the issue by accessing the following link:  
   \[Survey Definition\](https://<instance>.service-now.com/asmt\_metric\_type\_list.do)

2\. \*\*Review Assessable Record:\*\* Open the related survey and navigate to the "Assessable Record" related list. Access the specific record present in the Assessable Record list.  
   \[Assessable Record List\](https://<instance>.service-now.com/nav\_to.do?uri=asmt\_assessable\_record\_list.do?sys\_id=)

3\. \*\*Edit and Add Category:\*\* Click on "Edit" and add the appropriate category. This action will resolve the issue for new records moving forward. Please note that this will not rectify the category for existing records.

4\. \*\*Visibility in HR Task:\*\* Remember that when the HR task is in a "Work in Progress" state, the records will be visible.
