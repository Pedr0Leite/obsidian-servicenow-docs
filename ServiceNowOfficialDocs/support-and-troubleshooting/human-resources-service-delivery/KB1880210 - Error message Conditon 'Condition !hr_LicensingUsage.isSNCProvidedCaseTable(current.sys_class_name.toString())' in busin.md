---
title: "Error message \"Conditon 'Condition: !hr_LicensingUsage.isSNCProvidedCaseTable(current.sys_class_name.toString())' in business rule 'HR Case Custom COE Usage Tracking' on {coe}: {hr_case_number} evaluated to null; skipping business rule\""
aliases:
  - KB1880210
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB1880210
kb_number: KB1880210
last_modified: 2026-03-16
---

## Issue

After submitting a new HR Case, the following error might be displayed:

**_Conditon 'Condition: !hr\_LicensingUsage.isSNCProvidedCaseTable(current.sys\_class\_name.toString())' in business rule 'HR Case Custom COE Usage Tracking' on {coe}: {hr\_case\_number} evaluated to null; skipping business rule_**

![](/sys_attachment.do?sys_id=a67d06eb932ffe10f538fb2d6cba10c0 "Screenshot - error message.png")

This issue is non-impacting and does not interrupt the case creation process.  
  

## Resolution

To resolve this issue, run a **repair** of the **Human Resources Scoped App: Core** \[sn\_hr\_core\] plugin. This will update the Script Include **hr\_LicensingUsage** and solve the issue.
