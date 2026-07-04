---
title: "Unable to dot walk to reference field in Flow Designer. Fields or referenced field are not displayed"
aliases:
  - KB0870208
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0870208
kb_number: KB0870208
last_modified: 2024-02-26
---

## Unable to dot walk to reference field in Flow Designer. Fields or referenced field are not displayed

  

### Issue

Unable to dot walk to reference field in Flow Designer. Fields or referenced field are not displayed. Other reference fields work correctly.

### Cause

Check if there are two fields with the same label. Flow Designer UI is not case sensitive, so even if you have two fields with labels which use different case (for example 'Requested For' vs 'Requested for') it cannot handle this. If you have two fields with the same label it cannot display the fields.

### Resolution

You can't have two fields with the same label. You have to change the label for one of them.
