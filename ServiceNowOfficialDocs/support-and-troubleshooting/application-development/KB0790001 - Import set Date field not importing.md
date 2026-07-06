---
title: "Import set Date field not importing"
aliases:
  - KB0790001
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0790001
kb_number: KB0790001
last_modified: 2024-04-08
---

## Import set Date field not importing

  

### Issue

If you upload spreadsheet with some columns having date format like 31/12/2022 , it is not importing this date to import set table.

### Release

All

### Resolution

Change the data type of the column from "Date" to "String" in the import set table. Change the format of date in the xls : DD/MM/YYYY then import again.
