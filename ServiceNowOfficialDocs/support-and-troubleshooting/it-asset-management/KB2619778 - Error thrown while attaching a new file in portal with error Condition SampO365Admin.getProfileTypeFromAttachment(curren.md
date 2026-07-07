---
title: "Error thrown while attaching a new file in portal with error \"Condition: SampO365Admin.getProfileTypeFromAttachment(current.table_sys_id\"
aliases:
  - KB2619778
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB2619778
kb_number: KB2619778
last_modified: 2025-11-12
---

## Issue

When we trying to upload attachment in portal we get attached error:

`Conditon 'Condition: SampO365Admin.getProfileTypeFromAttachment(current.table_sys_id) === 'microsoft_office_365' && gs.nil(SampO365Admin.parseCSVFileDateTime(current.file_name)); Filter Condition: table_name=samp_sw_subscription_profile^file_nameSTARTSWITHVisio^ORfile_nameSTARTSWITHCopilot^ORfile_nameSTARTSWITHProject^EQ' in business rule 'Validate M365 attachments' on sys_attachment: sc_cat_item (sys_idSTARTSWITHebe9027fc3ffae5487f63fbf05013192).xml evaluated to null; skipping business rule`

## Resolution

1.  Please ensure the script include [SampO365Admin](https://instance_name.service-now.com/nav_to.do?uri=sys_script_include.do?sys_id=f2081222eb203110a50ea51ef1522821)  is OOB
2.  Please check if there is different scope.
