---
title: "Missing Contextual Bar Tabs After HR Agent Workspace Upgrade"
aliases:
  - KB2642832
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB2642832
kb_number: KB2642832
last_modified: 2026-03-27
---

## Missing Contextual Bar Tabs After HR Agent Workspace Upgrade

  

### Issue

After upgrading Agent Workspace for HR Case Management to version 4.2.0 in a non-production instance, several expected menus/options (e.g., _At a glance_, _Agent Assist_, _Employee documents_, _Attachments_, _Response templates_, _Email templates_) were missing from the Contextual bar.  
Only Fulfilment instructions and Checklist were visible, while all expected menus appeared in the production instance.  
Attempts to repair the plugin did not resolve the issue.

### Release

Any

### Cause

The issue was caused by a customization in the Data Broker responsible for configuring which tabs appear in the Contextual bar.  
The Script Include `hr_ContextualSideBarUtils` had been modified from its out-of-box (OOB) implementation.  
The output object in the Data Broker referenced a `showTemplates` function, which exists in the OOB script include but not in the customized version (which only had `showResponseTemplates`).  
This mismatch prevented the output object from being created correctly, resulting in missing tabs.

### Resolution

To resolve the issue:

-   Review the Data Broker configuration for the Contextual bar.
-   Remove the faulty reference to `showTemplates` from the Data Broker output object.
-   Ensure the script include `hr_ContextualSideBarUtils` aligns with OOB logic or includes equivalent functions.
-   Validate that all expected tabs (e.g., _At a glance_, _Agent Assist_, _Employee documents_, _Attachments_, _Response templates_, _Email templates_) appear after the fix.

After removing the incorrect reference, the Contextual bar displayed all expected menus.
