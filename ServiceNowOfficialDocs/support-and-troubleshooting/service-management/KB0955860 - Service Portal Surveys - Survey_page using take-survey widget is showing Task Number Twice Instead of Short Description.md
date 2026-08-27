---
title: "Service Portal Surveys - Survey_page using take-survey widget is showing Task Number Twice Instead of Short Description"
aliases:
  - KB0955860
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0955860
kb_number: KB0955860
last_modified: 2026-06-24
---

## Service Portal Surveys - Survey\_page using take-survey widget is showing Task Number Twice Instead of Short Description

  

### Issue

When opening a survey url in public mode i.e. not logged in the take-survey widget is showing the Case number twice. It is expected to show the short description.  
This behavior does not occur when you are logged in and on the take\_survey page.

see attached screenshots:

![Public Page](sys_attachment.do?sys_id=f63e396b4769c3103542f24c736d4379 "Public Page")

![Take Survey Page](sys_attachment.do?sys_id=3a3e396b4769c3103542f24c736d437f "Take Survey Page")

### Release

All

### Cause

  
This is working as expected.  
  
The reason that guest user sees case number, not description, is because guest user cannot read the case record.  
This happens not only to guest user, but also to login user if the login user cannot read the case record.  
  
The public\_survey page is build with take\_survey widget. The trigger\_desc is obtained from script include "SPSurveyAPI", with code snippet below.  
  
var trigger\_desc = titleConfig.getTitle(titleGr); // line #194  
if (!trigger\_desc)  
trigger\_desc = titleGr.getDisplayValue();  
data.trigger\_desc = trigger\_desc;

### Resolution

The reported behavior is by design.

The Description displays the Case number as guest user cannot read the Case record.
