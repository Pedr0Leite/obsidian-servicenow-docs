---
title: "Create New Entitlement' is displaying blank window in the Software Asset Workspace"
aliases:
  - KB1641483
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB1641483
kb_number: KB1641483
last_modified: 2024-10-28
---

## Issue

'Create New Entitlement' is displaying blank window in the Software Asset Workspace.

![](/sys_attachment.do?sys_id=0885c9554721921048cb2920326d4349)

## Resolution

This missing is a symptom of a wider plugin activation problem:  
PRB1776398 Family Upgrade, and activating store app, is not installing conditional content

That is fixed from Washington Patch 7. 

Once upgraded, if com.sn\_sam\_playbook is installed, then repairing the com.snc.samp.core plugin should bring the file back.

If that is not possible, import the attached script include: PlaybookDomainUtils \[sys\_script\_include\_87b7548373b220107e88ef66fbf6a716.xml\] to resolve the issue, however that will be treated as a customisation, so should be reverted to the out of box version.
