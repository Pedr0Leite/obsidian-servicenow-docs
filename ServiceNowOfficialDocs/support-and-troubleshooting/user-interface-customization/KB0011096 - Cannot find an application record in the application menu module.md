---
title: "Cannot find an application record in the application menu module"
aliases:
  - KB0011096
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0011096
kb_number: KB0011096
last_modified: 2026-04-21
---

## Cannot find an application record in the application menu module

  

### Issue

An application record cannot be found in the System Definition > Application Menu module even when searching by name.  
  
![Application module set to true](sys_attachment.do?sys_id=55ff134f475cc35877748d01426d4376 "Application module set to true")

### Symptoms

The application does not appear in the Application Menu module list.  
Searching by application name returns no results.  
The application exists but is not visible in the navigator.

### Release

  All releases

### Cause

The Application Menu module filters out inactive applications by default. If an application has its Active field set to false, it will not appear in the list.

### Resolution

To view and reactivate an inactive application record:  
1\. Navigate to System Definition > Application Menu.  
2\. Locate the Active = true filter at the top of the list.  
3\. Click the X icon next to the Active = true filter to remove it. All application records, including inactive ones, will now be displayed.  
4\. Search for and open the desired application record.  
5\. Set the Active field to true.  
6\. Click Save to apply the change.

The application will now appear in the application navigator.
