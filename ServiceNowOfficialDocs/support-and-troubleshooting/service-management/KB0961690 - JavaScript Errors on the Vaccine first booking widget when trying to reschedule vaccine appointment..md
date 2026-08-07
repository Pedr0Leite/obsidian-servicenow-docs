---
title: "JavaScript Errors on the Vaccine first booking widget when trying to reschedule vaccine appointment."
aliases:
  - KB0961690
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0961690
kb_number: KB0961690
last_modified: 2024-04-09
---

## Issue

When user tries to reschedule an appointment, the error messages are seen: 

  

Server JavaScript error Cannot read property "uiRenderTz" from undefined

Line number 55 (sp\_widget.ad2404f087222010420e5cdac5cb0be6.script)

Failing widget: 'Vaccine first booking' (ad2404f087222010420e5cdac5cb0be6)

  

## Resolution

  
The issue occurred as the Program centers didn't have an appointment configuration.  
  
The "center" added to the vaccine Program that is being used should have appointment configuration so that the appointments can be rescheduled.
