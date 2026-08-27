---
title: "IT Service Management for Microsoft 365 - Authorization failed: AADSTS50097"
aliases:
  - KB2406476
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB2406476
kb_number: KB2406476
last_modified: 2026-04-21
---

## IT Service Management for Microsoft 365 - Authorization failed: AADSTS50097

  

### Issue

Customer is setting up the integration between ServiceNow and IT Service Management for Microsoft 365  
  
The plugin to be installed is sn\_now\_teams\_it  
![](/sys_attachment.do?sys_id=dd8d715093d3aa1c057c7de86cba101f "Screenshot 2025-08-07 at 15.59.55.png")  
  
Once the plugin is installed, customer installs Azure Apps in All > ServiceNow for Microsoft > Install Azure Apps  
![](/sys_attachment.do?sys_id=809d359493d3aa1c057c7de86cba10af "Screenshot 2025-08-07 at 16.00.20.png")  
  
In the installation process there's option to authorize 'Request based Chat' and 'SSO and Activity Notification'  
![](/sys_attachment.do?sys_id=1b9df15893d3aa1c057c7de86cba1072 "Screenshot 2025-08-07 at 16.00.34.png")  
  
When clicking on any of the authorize buttons, error is displayed:  
  
Request Based chat: Authorization failed. AADSTS50097: Device authentication is required. Trace ID:   
  
SSO: Authorization failed. AADSTS50097: Device authentication is required. Trace ID:

### Release

Vancouver and onwards

### Cause

This error happens when a conditional access policy is applied to the resource you are accessing, which required that the device from which the token is acquired be managed by the organization, and that MSAL.NET proves this identity.

This is a conditional access policy applied by the tenant admin.

### Resolution

This is a Microsoft error code and customer should contact the Microsoft admin providing the following documentation:  
[https://learn.microsoft.com/en-us/entra/msal/dotnet/advanced/exceptions/device-authentication-errors](https://learn.microsoft.com/en-us/entra/msal/dotnet/advanced/exceptions/device-authentication-errors)  
  
  
Once the Microsoft admin fixes the issue by following the documentation the authorization should work.
