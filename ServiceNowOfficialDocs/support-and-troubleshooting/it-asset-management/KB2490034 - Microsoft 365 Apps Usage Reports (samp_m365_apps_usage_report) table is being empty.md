---
title: "Microsoft 365 Apps Usage Reports (samp_m365_apps_usage_report)  table is being empty "
aliases:
  - KB2490034
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB2490034
kb_number: KB2490034
last_modified: 2025-09-22
---

## Issue

**SAM - Collect Microsoft 365 Usage** job is designed to populate the "samp\_m365\_apps\_usage\_report" table with relevant data. However, despite the job completing successfully without any reported issues, the table remains empty.

## Resolution

Need to update the below property to include the CSV extension.  
System Property:- glide.attachment.extensions  
https://<instance-name>.service-now.com/nav\_to.do?uri=sys\_properties.do?sys\_id=650b07dbc0a80006004f95f2c929335d
