---
title: "Troubleshooting a report that does not execute"
aliases:
  - KB0535306
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0535306
kb_number: KB0535306
last_modified: 2025-02-15
---

## Troubleshooting a report that does not execute

  

### Issue

There can be a situation where a report does not execute as expected. This article provides information for addressing those issues.

### Resolution

If the report does not execute, some common causes and solutions may include: 

1.  Check whether users have access to that table.
2.  Verify that you can access the table by navigating to it in the navpage, for example, task.do.
3.  Issues with reports in a clone: Can you access the table or report in the _source_ instance? After a clone, depending on whether a table has been excluded, the user has the same permissions that they did in the source instance.
4.  Verify the credentials of the user. If this is an ITIL user, do ITIL users have access to reports?
