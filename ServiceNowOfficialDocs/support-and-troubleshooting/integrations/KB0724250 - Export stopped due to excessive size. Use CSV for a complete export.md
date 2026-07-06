---
title: "Export stopped due to excessive size. Use CSV for a complete export"
aliases:
  - KB0724250
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0724250
kb_number: KB0724250
last_modified: 2024-12-23
---

## Export stopped due to excessive size. Use CSV for a complete export

  

### Issue

Exporting large xlsx file, throws error "Export stopped due to excessive size. Use CSV for a complete export."

### Release

All

### Cause

Due to system property "glide.excel.max\_cells" limit

### Resolution

Excel exports are intended for relatively small exports, fewer than 500,000 cells, while CSV can handle larger exports.

Whenever you export to Excel and the resultant spreadsheet has more than 500,000 cells (by default), the export process stops and you are given the Excel file at that point. In the bottom row, there will be the following message: Export stopped due to excessive size. Use CSV for a complete export:  
The Excel export cell threshold is customizable by adding system property "glide.excel.max\_cells" property.  
Note: Increasing this threshold may cause a memory issue in your instance. The threshold is set at an appropriate level to prevent resource issues.

### Related Links

[https://docs.servicenow.com/csh?topicname=r\_AdministerReports.html&version=latest](https://docs.servicenow.com/csh?topicname=r_AdministerReports.html&version=latest)
