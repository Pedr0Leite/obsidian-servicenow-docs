---
title: "Unable to access Activity Sets in Lifecycle Events"
aliases:
  - KB0961915
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0961915
kb_number: KB0961915
last_modified: 2025-12-10
---

## Unable to access Activity Sets in Lifecycle Events

  

### Issue

When attempting to edit Activity Sets within a Lifecycle Event user faces error message "There was an unexpected error, refresh the page".

Steps:

1.   Manage Lifecycle Events
2.  Select Lifecycle Event Type
3.  Click Activity Sets Tab
4.  Error shows 

  

1.  ![](/sys_attachment.do?sys_id=2a63d31adb4cf050981a0b55ca961948)

### Release

Paris

### Cause

  
Script Include hr\_ActivitySet wasn't updated with latest version; old version was missing function for new updates.

  

### Resolution

  
Revert to most recent system version of the script include hr\_ActivitySet   
1\. Navigate to System Definition > Script Includes  
2\. Search for hr\_ActivitySet  
3\. Find latest version created by system   
4\. Right click > Revert to this version
