---
title: "How to force encoding for an CSV data source"
aliases:
  - KB0721226
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0721226
kb_number: KB0721226
last_modified: 2025-06-11
---

## How to force encoding for an CSV data source

  

### Issue

When you are importing CSV file as File Type in the data source, you can specify the encoding charset using the Properties field on the Data Source form. Properties field can be enabled in the Data Source Form by configuring the Form Layout.

The Below image shows the Properties Field:

![Properties field on the Data Source form](sys_attachment.do?sys_id=6b6771ca93462250c2513f986cba10c7 "Properties field on the Data Source form")

### Release

All

### Resolution

Steps are given:

1.  Navigate to the Data Source Form.
2.  Click the context menu icon (![Context menu icon](/sys_attachment.do?sys_id=6f6771ca93462250c2513f986cba10c4)) and select Configure > Form Layout.
3.  Using the slushbucket, select "Properties" and the order in which you want them to appear.
4.   Enter the value as "charset=utf-8" for more information please follow below documentation

[https://www.servicenow.com/docs/bundle/yokohama-integrate-applications/page/administer/import-sets/reference/r\_FileTypeDataSource.html#d268226e379](https://www.servicenow.com/docs/bundle/yokohama-integrate-applications/page/administer/import-sets/reference/r_FileTypeDataSource.html#d268226e379)

### Related Links

The default character set used for decoding the imported CSV file is WINDOWS-1252. See below :   
  
[https://en.wikipedia.org/wiki/Windows-1252](https://en.wikipedia.org/wiki/Windows-1252)   
  
Defining a specific type of encoding such as utf-8 when importing a CSV document is necessary for proper data formatting(dependent on CSV format).
