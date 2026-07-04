---
title: "Password reset error with message cannot reset your AD password through Service-Now password reset application"
aliases:
  - KB0634698
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0634698
kb_number: KB0634698
last_modified: 2025-08-01
---

## Password reset error with message cannot reset your AD password through Service-Now password reset application

  

### Issue

With the Password Reset Orchestration Add-on plugin enabled, a user tries to reset their password and sees the following error: 

**@@@**  
  
**Password Reset Error**  
  
**You cannot reset your AD password through Service-Now password reset application.**   
  
**Please contact your administrator for instructions on how to change your AD password.**  
  
**@@@**

### Facts

\- The Password Reset Orchestration Add-on plugin is built on top of Orchestration AD activities and allows connections to Active Directory (AD) and Remote (SOAP) Instance credential store types to reset passwords. 

### Release

All

### Resolution

The root cause of the issue is the use of the existing Password reset processes, using **Default Self Service** and changing the credential store to other credential store instead of **Local ServiceNow Instance**.

A new password reset process needs to be created instead of using the existing **Default Self Service**. There is a logic within the code restricting the password reset process, **Default Self Service**, to be used by another credential store. For example, AD credential store.

### Related Links

[Request the Password Reset Windows App plugin](https://www.servicenow.com/docs/csh?topicname=t_ActPassRstOrchAddOn.html&version=latest "Request the Password Reset Windows App plugin")
