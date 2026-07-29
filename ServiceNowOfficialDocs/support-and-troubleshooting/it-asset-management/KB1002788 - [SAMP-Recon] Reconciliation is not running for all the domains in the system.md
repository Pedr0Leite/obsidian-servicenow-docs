---
title: "[SAMP-Recon] Reconciliation is not running for all the domains in the system"
aliases:
  - KB1002788
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB1002788
kb_number: KB1002788
last_modified: 2025-01-02
---

## \[SAMP-Recon\] Reconciliation is not running for all the domains in the system

  

### Summary

In an domain separated instance, you might see the reconciliation results are not generated for all the domains.

### Release

All with SAMP enabled.

### Instructions

The SAMP reconciliation job depends on the _**Domain Asset Process Settings**_ table's **_Run asset process_** flag to determine if that domains needs reconciliation. Make sure the intended domain does have the run asset process flag is set to true.

You can configure as below:

Application Navigator >> Software Asset >> Administration >> Domain Settings

![](sys_attachment.do?sys_id=1239d0d3dbc501d007ab82630596197c)

### Related Links

-   [Run software reconciliation in the workspace](https://docs.servicenow.com/bundle/rome-it-asset-management/page/product/software-asset-management2/task/run-recon-workspace.html "Run software reconciliation in the workspace")
