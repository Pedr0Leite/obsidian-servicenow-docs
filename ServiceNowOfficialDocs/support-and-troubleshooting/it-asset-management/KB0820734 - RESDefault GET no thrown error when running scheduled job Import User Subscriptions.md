---
title: "RES/Default GET: no thrown error  when running scheduled job Import User Subscriptions"
aliases:
  - KB0820734
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0820734
kb_number: KB0820734
last_modified: 2024-04-08
---

## Issue

After setting up the Microsoft office 365 profile on running the scheduled job SAM - Import User Subscriptions, the following error in system log:

SAM:SAM - Import User Subscriptions: Microsoft Office 365 - Unhandled exception: com.glide.communications.ProcessingException: Error constructing REST Message/Method: ###########\_RES/Default GET: no thrown error

## Resolution

When an O365 integration is created, the following business rules run:

1.  Create OAuth app and REST message - this creates the rest message.
2.  Create REST verb methods - this creates the default HTTP method with name "Default GET"
3.  Validate name on table sys\_rest\_message\_fn, which creates the “GET Reports” and “GET Users”  
      
    If there is any customization that blocks these from creation, the rest message is not constructed properly then the integration will fail. In this case, the error was due to the default Get method not being built correctly due to customization.

Please revert any customization to OOB files and recreate the integration profile.
