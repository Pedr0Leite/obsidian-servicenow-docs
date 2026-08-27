---
title: "User unable to switch to default view on Employee relations case"
aliases:
  - KB2105903
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB2105903
kb_number: KB2105903
last_modified: 2025-09-03
---

## User unable to switch to default view on Employee relations case

  

### Issue

Open an employee relations case as HR admin or admin, try to switch to the default view from the menu, it comes back to the previous view, and never switch to default view.

![](/sys_attachment.do?sys_id=24a19887975966d024a7739c1253aff7 "Switching to default view in employee relations case.png")

### Release

All

### Cause

This is working as per design. 

### Resolution

To modify this behaviour, you need to follow the customisation below.  
  
Disable auto redirection to Self-service view: 

  
1\. Open Navigation Handler for sn\_hr\_er\_case table by navigating to /nav\_to.do?uri=sys\_navigator.do?sys\_id=265cce91eb7130101d4e509ba85228eb  
2\. Modify the code in the script field as per your business needs.   
3\. Save the Navigation Handler.
