---
title: "HR Service are not loading on Case Creation Page and displays a \"No matches found\" message"
aliases:
  - KB0815775
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0815775
kb_number: KB0815775
last_modified: 2026-03-09
---

## Issue

In the HR 'Create New Case' page, the "HR Service" drop down is empty and only the "No matches found" message is displayed.

Steps to Reproduce:

1\. Navigate HR Case Management > Create New Case  
2\. Select any user  
3\. Select a COE

Expected behaviour: In the 'HR Service' drop down menu, the correct HR Services are listed

Actual behaviour: In the 'HR Service' drop down menu, no HR Services are displayed

## Resolution

Revert Script Include 'hr\_Utils' to its OOB version:

[https://instance\_name.service-now.com/nav\_to.do?uri=sys\_script\_include.do?sys\_id=f65370019f22120047a2d126c42e7000](https://instance_name.service-now.com/nav_to.do?uri=sys_script_include.do?sys_id=f65370019f22120047a2d126c42e7000)
