---
title: "HR Case redirects to blank page with error message"
aliases:
  - KB0821183
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0821183
kb_number: KB0821183
last_modified: 2026-03-17
---

## Issue

After submitting an HR record producer form the ESC Portal, a blank page is displayed instead of the HR Case page and a with error messages are displayed:

Server JavaScript error The undefined value has no properties.  
Line number 4 (sys\_script\_include.d22e7bdbc0a8016500a18e024bfc9aa3.script)  
Script source code logged to browser console  
Failing widget: 'HRM Task Parent' (6155d8cb5b1313003bbcefe5f0f91ac8)  
  
Server JavaScript error The undefined value has no properties.  
Line number 4 (sys\_script\_include.d22e7bdbc0a8016500a18e024bfc9aa3.script)  
Script source code logged to browser console  
Failing widget: 'HRM Case Info' (ee7ed65a671f1300470f6c3b5685ef7c)

## Resolution

Revert the 'hr' Script Include to its OOB state and make sure that all HR-related Restricted Caller Access (RCA) records are in 'Allowed' state:

<Instance URL>/sys\_restricted\_caller\_access\_list.do
