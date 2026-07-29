---
title: "Include sys_id field in Excel export for a table or record"
aliases:
  - KB0691394
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0691394
kb_number: KB0691394
last_modified: 2026-06-30
---

## Include sys\_id field in Excel export for a table or record

  

### Issue

Add the sys\_id field to an Excel export file when exporting a table or record from ServiceNow.

### Release

All Releases

### Resolution

Prerequisites:  
\- Access to the ServiceNow instance list view URL.

Add a URL parameter to include sys\_id in an Excel export

1.  Navigate to the list view for the table you want to export (for example, the Incident list).
2.  Copy the current URL from the browser address bar.
3.  Add the following parameter to the end of the URL:
    
       &EXCEL&sysparm\_default\_export\_fields=all
    
       Example: https://<instancename>.service-now.com/incident\_list.do?sysparm\_query=state%3D1&sysparm\_view=&EXCEL&sysparm\_default\_export\_fields=all
4.  Press Enter to run the export.

**Note:** This parameter exports all fields from the table, not only sys\_id.

### Related Links

More on exporting data with Sys IDs in this blog post on the Developer site: [Exporting data with Sys IDs](https://developer.servicenow.com/blog.do?p=/post/exporting-data-with-sys-ids/ "Exporting data with Sys IDs")

[Export data from a list](https://www.servicenow.com/docs/r/platform-administration/table-administration-and-data-management/export-list-data.html "Export data from a list")
