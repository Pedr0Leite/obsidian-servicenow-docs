---
title: "User with role sam_admin is not able to view health check scan data within Software Asset Workspace"
aliases:
  - KB1640608
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB1640608
kb_number: KB1640608
last_modified: 2024-04-08
---

## User with role sam\_admin is not able to view health check scan data within Software Asset Workspace

  

### Issue

User with role sam\_admin is not able to view health check scan data from Software Asset Workspace

![](/sys_attachment.do?sys_id=def583b793914610080af35d6cba10f9 "Screenshot 2024-04-08 at 7.16.54 PM.png")

### Cause

We need scan\_user role in order to view the data in the Health check.

This issue is tracked in "PRB1699550" and fixed in the "ITAM Health Check Application" 2.1.6 version of Washington DC.

As part of the fix, the scan\_user role is added to the sam\_admin role.

### Related Links

sam\_user/sam\_admin role is sufficient to view the health check page only  
  
Role needed:=  
sam\_user/sam\_admin = to view page/record  
scan\_user = to view the dashboard widget result  
  
Please provide the scan\_user role as well to the user.
