---
title: "Excel Files Fail to Preview or Load Slowly in HR Agent Workspace Document Viewer"
aliases:
  - KB2656756
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB2656756
kb_number: KB2656756
last_modified: 2025-12-17
---

## Excel Files Fail to Preview or Load Slowly in HR Agent Workspace Document Viewer

  

### Issue

Users may experience long loading times or failures when previewing Excel files in the HR Agent Workspace document viewer. In some cases, files do not open at all or take up to 30 seconds to load. Occasionally, downloads fail and result in "Unconfirmed .crdownload" files.

### Release

Any

### Cause

The document viewer does not support Excel workbooks containing multiple sheets. Only single-sheet Excel files are supported for preview.

### Resolution

-   Confirmed that the issue occurs with multi-sheet Excel files in OOB environments.
-   Workaround:
    -   Use single-sheet Excel files for attachments in HR Agent Workspace.
    -   If the file contains multiple sheets, copy the required data into a new single-sheet Excel file before uploading.
