---
title: "Troubleshooting export - Determine whether the encoding setting is wrong"
aliases:
  - KB0538309
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0538309
kb_number: KB0538309
last_modified: 2024-05-01
---

## Troubleshooting export - Determine whether the encoding setting is wrong

  

### Issue

-   Export results are formatted with the wrong encoding
-   Non-English characters (for example, Russian, Hebrew) are replaced by question marks

### Cause

The setting for the export encoding is missing or it has the wrong value. This issue is related to exporting data using the CSV format from the instance.

### Resolution

To solve the issue, set the correct encoding using the system property **_glide.export.csv.charset_**

**Note**: By default, ServiceNow exports all CSV files in Windows-1252 encoding. If you need to export translated data, set the _**glide.export.csv.charset**_ system property to UTF-8 (starting with the Calgary release).
