---
title: "Troubleshooting export - Determine if the configured maximum rows to export is too low"
aliases:
  - KB0538324
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0538324
kb_number: KB0538324
last_modified: 2025-03-05
---

## Troubleshooting export - Determine if the configured maximum rows to export is too low

  

### Issue

This issue is related to exporting data from the instance while obtaining only a subset of the data from the expected results.

## Symptoms

-   Not all data is exported
-   Records are missing from export

### Cause

The setting for the maximum rows to export for the file type (CSV, XML, Excel, or PDF) is too low.

For Excel, another cause can be the setting for the maximum number of cells to export is too low. For more information, see [Export Limit/Max Overview (Excel, CSV, PDF, Database Views)](https://support.servicenow.com/kb_view.do?sysparm_article=KB0518655 "Export Limit/Max Overview (Excel, CSV, PDF, Database Views)")

### Resolution

To solve the issue, set the limit property for the file type to a higher value.

For example, by default, the limit for CSV export is 10,000 records. If you need to export 15,000 records, you can set (or add if not exists) the _**'glide.csv.export.limit'**_ system property to change the limit to 15,000 which is mentioned in [KB0695242](https://support.servicenow.com/kb_view.do?sysparm_article=KB0695242 "KB0695242"). Details about other glide.csv, glide.excel and glide.pdf system properties can be found [here](https://docs.servicenow.com/csh?topicname=r_AvailableSystemProperties.html&version=latest "here").

For more information about export limits and how to override them, see [Export Limits](https://docs.servicenow.com/bundle/latest-platform-administration/page/administer/exporting-data/concept/c_ExportLimits.html "Export Limits")
