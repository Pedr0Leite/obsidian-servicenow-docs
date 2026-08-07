---
title: "SCCM Permission Issue even after configuring the application admin Role in SCCM"
aliases:
  - KB0752231
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0752231
kb_number: KB0752231
last_modified: 2024-04-07
---

## SCCM Permission Issue even after configuring the application admin Role in SCCM

  

### Issue

# Symptoms

Trying to run an SCCM Activity of Adding a device to an Collection in the instance , however the workflow activity won't complete due the the error below:

"Operation could not complete because the currently connected account does not have the required security rights to perform this operation.Stack Trace:"

# Release

Any release

# Environment

Microsoft SCCM 

# Cause

The security scope of the service account was set to "all Instance of the object that are related to the assigned security roles" to fix this issue.

# Resolution

In SCCM, ensure the security scope "All instances of the objects that are related to the assigned security roles" is set for the service account

1\. In the Configuration Manager console, choose Administration.  
2\. In the Administration workspace, expand Security, and then choose Administrative Users.  
3\. Select the administrative user that you want to modify.  
4\. On the Home tab, in the Properties group, choose Properties.  
5\. In the Security Scopes tab, confirm that the administrative user is configured for All instances of the objects that are related to the assigned security roles.

# Additional Information

Microsoft SCCM Documentation
