---
title: "Cannot upload files from the MID Server to the instance"
aliases:
  - KB0789881
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0789881
kb_number: KB0789881
last_modified: 2024-04-08
---

## Cannot upload files from the MID Server to the instance

  

### Issue

-   If one tried to import files via the Mid server what options are there to implement this?
-   One encounters the error: "Failed to open/read local data from file/application" when importing a file from a remote Server via the Mid Server

### Release

All

### Cause

The MID Server does not have an FTP Client implementation

### Resolution

Out of The Box, there is no support by the Platform to upload files from the MID Server to the instance.

In order to import a file such as a CSV file the following Datasource types are supported: FTP, SCP, HTTP  
These Datasource types can be connected to directly from the ServiceNow instance

Alternatively, customized solutions to do this may be explored however these would not be supported by ServiceNow Customer Support
