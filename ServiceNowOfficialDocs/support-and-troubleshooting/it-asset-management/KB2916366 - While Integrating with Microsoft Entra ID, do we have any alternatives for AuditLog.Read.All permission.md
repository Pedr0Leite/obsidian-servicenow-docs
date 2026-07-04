---
title: "While Integrating with Microsoft Entra ID, do we have any alternatives for AuditLog.Read.All permission? "
aliases:
  - KB2916366
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB2916366
kb_number: KB2916366
last_modified: 2026-04-02
---

## Issue

  
Due to some additional security considerations for few customers, they expect an alternative for AuditLog.Read.All permission.

## Resolution

The AuditLog.Read.All permission is required to fetch the activities of the users connected to the application in the Microsoft Azure AD portal.  
We use this API for pulling this information: [https://learn.microsoft.com/en-us/graph/api/signin-list?view=graph-rest-1.0&tabs=http](https://learn.microsoft.com/en-us/graph/api/signin-list?view=graph-rest-1.0&tabs=http)  
  
As outline in the document by Microsoft , the Least privileged permission for both Application and Delegated type of permissions is AuditLog.Read.All  
Hence this permission is necessary for us to access user activity data, specifically to capture details such as last login information.  
  
Unless Microsoft provides a lower-privileged alternative for this API, we would not be able to modify this requirement from our end.
