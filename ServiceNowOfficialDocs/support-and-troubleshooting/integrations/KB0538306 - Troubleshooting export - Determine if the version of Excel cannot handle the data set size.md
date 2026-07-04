---
title: "Troubleshooting export - Determine if the version of Excel cannot handle the data set size"
aliases:
  - KB0538306
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0538306
kb_number: KB0538306
last_modified: 2024-05-01
---

## Troubleshooting export - Determine if the version of Excel cannot handle the data set size

  

### Issue

This issue is related to exporting data from the instance into an Excel file. When opening the Excel file, not all records are shown.

### Symptoms

-   Not all data exported
-   Records are missing from export

### Cause

The number of records exported is higher than the number of rows that Excel can show. So, even though all records have been exported successfully into the Excel file, Excel can only show a certain number of rows.

**Note:** Until Office 2007, Excel had a maximum of 65,000 rows. In Office 2007 and later, the limit is 1,048,576 rows.

### Resolution

To solve the issue and display more than 65,000 records in Excel, upgrade to Excel version 2007 or higher.

**Note:** To export and view more than 1,048,576 rows, export into a different file type such as CSV or XML.
