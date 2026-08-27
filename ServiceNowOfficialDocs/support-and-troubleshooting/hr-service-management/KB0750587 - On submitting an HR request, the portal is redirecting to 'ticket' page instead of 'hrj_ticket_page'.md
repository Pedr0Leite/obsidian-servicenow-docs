---
title: "On submitting an HR request, the portal is redirecting to 'ticket' page instead of 'hrj_ticket_page' "
aliases:
  - KB0750587
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0750587
kb_number: KB0750587
last_modified: 2024-04-07
---

## Issue

# Symptoms

Issue: On submitting an HR request, Portal is redirecting to 'ticket' page instead of 'hrj\_ticket\_page'   
  
Business Impact: Low   
  
Steps to Reproduce:  
1\. Go to dot\_hr portal  
2\. Submit a request on for 'Ask HR"  
3\. Observe in the url that id=ticket   
  

# Release

Madrid Patch 3 Hot Fix 2

# Cause

Customized widget schema options.

For 'esc' portal, custom 'Copy HRM Catalog Item' widget is used by customer.

Under options schema, we can see it is specified to which page it should go (which is hrj\_ticket\_page) 

# Resolution

Under options schema of Custom widget of 'esc' portal, one can specify to which page it should go (which is hrj\_ticket\_page) 

![](sys_attachment.do?sys_id=85ce3ca2db0ab450e515c2230596191a)
