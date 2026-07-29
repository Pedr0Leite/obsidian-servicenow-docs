---
title: "Global Search results showing only sys_id's if Default views are missing"
aliases:
  - KB0639324
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0639324
kb_number: KB0639324
last_modified: 2026-06-06
---

## Global Search results showing only sys\_id's if Default views are missing

  

### Issue

When the Default view of a table does not exist, the global search shows only a sys\_id. [PRB1204046](https://support.servicenow.com/problem.do?sys_id=8b311b03dbe18f445a4af85e0f9619b0 "PRB1204046") notes that the Default view for a table is deleted if someone views a public report of that table without being authenticated, which was fixed in Geneva and Helsinki (see [KB0597466](https://support.servicenow.com/kb_view.do?sys_kb_id=8c0a9fa1dba5aa04852c7a9e0f96199f "KB0597466") for more information). However, this issue has re-occurred in Istanbul and Jakarta. 

  
Symptoms:

The new Global search shows a sys\_id for the result record and all of the other fields are missing. Also, the default list view for the table showing a sys\_id is gone. To verify this, go to sys\_ui\_list.list and search for table = <table\_name> and Title = Default view

![](sys_attachment.do?sys_id=adc23022db0bc1d0b5d6e6be1396197f)

### Resolution

Re-create the Default view for the list of that table. For more information about formatting the global search results, see the product documentation topic [Text search views format search results](https://docs.servicenow.com/csh?topicname=text-search-view-formats-results.html&version=latest "Text search views format search results").

To prevent this issue from occurring again, make all public reports from type list not public so that they can be accessed only when the user is authenticated.
