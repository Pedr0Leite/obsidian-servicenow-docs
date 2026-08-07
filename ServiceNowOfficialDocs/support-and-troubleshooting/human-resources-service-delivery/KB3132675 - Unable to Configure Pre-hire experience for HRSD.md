---
title: "Unable to Configure Pre-hire experience for HRSD"
aliases:
  - KB3132675
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB3132675
kb_number: KB3132675
last_modified: 2026-07-01
---

## Issue

  
After upgrading to the Zurich release and upgrading the Journey designer application to version 7.0, key features for the employee onboarding pre-hire experience were missing. Specifically, the Lifecycle Event activities 'Account Setup and Notification' and 'Transition pre-hire to Employee', as well as the pre-hire portal and its associated widgets, which should be available per product documentation:

[Pre-hire experience](https://www.servicenow.com/docs/r/employee-service-management/journey-designer/jny-pre-hire-experience.html?contentId=18sdLCl4dUdwAQJxqXK2WA "Pre-hire experience")

## Resolution

Repairing the Journey Designer plugin resolved the issue:

 https://<instance>.service-now.com/sn\_hr\_le\_activity\_list.do?sysparm\_query=title%3DTransition%20pre-hire%20to%20employee%5EORtitle%3DAccount%2Frole%20setup%20and%20notification&sysparm\_view=  
  
  

## Additional Information

[Pre-hire experience](https://www.servicenow.com/docs/r/employee-service-management/journey-designer/jny-pre-hire-experience.html?contentId=18sdLCl4dUdwAQJxqXK2WA "Pre-hire experience")
