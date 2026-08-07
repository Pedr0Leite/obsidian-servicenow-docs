---
title: "Warning message when Publishing Flow Designer Action w/ Script step"
aliases:
  - KB0821171
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0821171
kb_number: KB0821171
last_modified: 2024-04-08
---

## Issue

\* Reference type field '<input variable name>' in table '' inserted with a max length of 32. Reference type fields hold the sys\_id of the reference record which is a 32-character GUID  
\* Maximum length cannot be increased on a Reference type field. Column '<input variable name>' in table 'var\_\_m\_sys\_hub\_action\_input\_<sys\_id of input variable>' not modified.

## Resolution

Steps to reproduce the issue - 

1\. Login to OOB instance as Admin.  
2\. Create a new action.  
3\. Add input variable  
first try to select type as "record.ast\_contract".  
4\. Click on save.  
5\. now again try changing the type to "reference.ast\_contract".  
6\. Click on save and publish

You can follow the below workaround which will resolve the issue.

Workaround - create a copy of the action and publish to remove the error and system will automatically set the max\_length to "32" again.  
However when creating a copy you will see the warning. Once you publish it the warning will be gone.
