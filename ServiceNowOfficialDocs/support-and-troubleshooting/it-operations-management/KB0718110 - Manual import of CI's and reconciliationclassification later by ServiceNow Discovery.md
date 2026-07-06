---
title: "Manual import of CI's and reconciliation/classification later by ServiceNow Discovery"
aliases:
  - KB0718110
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0718110
kb_number: KB0718110
last_modified: 2025-01-03
---

## Manual import of CI's and reconciliation/classification later by ServiceNow Discovery

  

### Issue

# Description

* * *

If you are manually planning to import CI's into ServiceNow, and planning to run Discovery on them later, you would need to import them into proper tables so that the Identification rules apply correctly and duplicates are avoided

# Procedure

* * *

For example, when we insert a CI record into cmdb\_ci table. We only give it a name field. When we run discovery, it creates a duplicate CI with the same name under cmdb\_ci\_computer.

Instead when we create a CI record on cmdb\_ci\_hardware table, after running discovery, the class of the existing CI changes from hardware to computer and there will be no duplicate.

Based on this, if you would like to do a manual import, it would be best to know what class the CI's might fall into. All the servers, network devices fall under cmdb\_ci\_hardware so you can import them under this table.

Regarding other CI's, you would need to make sure you know the class before importing. This will help prevent duplicates

# Applicable Versions

* * *

All versions
