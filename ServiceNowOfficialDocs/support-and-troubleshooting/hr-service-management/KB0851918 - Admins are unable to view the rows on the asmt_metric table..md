---
title: "Admins are unable to view the rows on the asmt_metric table."
aliases:
  - KB0851918
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0851918
kb_number: KB0851918
last_modified: 2025-09-03
---

## Admins are unable to view the rows on the asmt\_metric table.

  

### Issue

When logged as an admin, the table asmt\_metric returns some records where columns are hidden .

If you set "Admin overrides" to the ACL READ "asmt\_metric.\*", the issue is fixed. 

### Cause

The system property **`glide.security.admin.override.accessterm`** is **`missing`**. As per the doc [Evaluate the admin override at the access level](https://docs.servicenow.com/csh?topicname=t_EvalAdmOverrideAccLevel.html&version=latest "Evaluate the admin override at the access level") it's included on new instances and set to true.  
  
  

### Resolution

1.  Import  glide.security.admin.override.accessterm system property attached in this article.
2.  Clear instance cache
3.  Test issue
