---
title: "Troubleshooting Export – Determine if there are too many records in the export set"
aliases:
  - KB0538303
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0538303
kb_number: KB0538303
last_modified: 2024-05-01
---

## Troubleshooting Export – Determine if there are too many records in the export set

  

### Issue

Export issues maybe observed by customers via the following symptoms:

-   Export takes too long
-   Data set is too large

### Cause

This issue is related to exporting data from the instance. The data set you are trying to export could be too large to export in a single transaction and the export process can be a lot slower than the simply displaying the data in a list view.

In export, all records are written out, but in a list view only a single page of data is shown at a time.

**Note** Exporting to PDF will also typically take much longer than exporting to XML, CSV, or Excel because PDF includes additional formatting, pagination, and layouts components.

### Resolution

To solve the issue, try one or more from the following list:

-   Add more filters to decrease the number of records in the results
-   Avoid using fields that have no index for filtering and sorting
-   Export to a different format. Try a more compact format, such as CSV
-   Break up the export. See [Break Up a Large Export](https://docs.servicenow.com/csh?topicname=t_BreakUpALargeExport.html&version=latest "Break Up a Large Export")
