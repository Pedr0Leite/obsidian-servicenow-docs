---
title: "Verifying your exclude table settings for cloning"
aliases:
  - KB0535341
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0535341
kb_number: KB0535341
last_modified: 2024-12-30
---

## Verifying your exclude table settings for cloning

  

### Issue

After a clone completes, a table was copied but does not contain any records.

### Symptoms

-   Clone completes but is missing records
-   Table empty after a clone
-   Records missing from table

### Release

  All release versions.

### Resolution

The excluded table data can be located under the System Clone application. To locate:  

1.  Type **Clone** into the navigation filter. 
2.  Select **Exclude tables**.
3.  Review the list to determine if the table with missing records is included. If the table is included, remove the table from the list and re-run the clone.

### Related Links

To learn more about the **Exclude tables** settings, see: [Exclude a table from cloning](https://www.servicenow.com/docs/csh?topicname=t_ExcludeATableFromCloning.html&version=latest)
