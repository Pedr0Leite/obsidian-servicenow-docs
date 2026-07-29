---
title: "Attachment table/record attachment tab 'Updated By' field will have a value of 'system' when attaching a document to a record"
aliases:
  - KB0817964
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0817964
kb_number: KB0817964
last_modified: 2024-01-28
---

## Attachment table/record attachment tab 'Updated By' field will have a value of 'system' when attaching a document to a record

  

### Issue

When a user attaches a document to a record, the sys\_attachment table or the attachment tab section with the form 'Updated By' field value will display as 'System'.

### Release

Madrid and onwards.

### Cause

This is due to the ServiceNow Antivirus Program (com.glide.snap) plugin. This plugin is activated by default starting with Madrid instances.

When an attachment is added to a record, the antivirus will run a scan on this attachment, a job record is created by the antivirus scan job. This, therefore, sets the 'Updated By' field value to 'System'.

### Resolution

This is expected behaviour.

If you prefer, so that the 'Updated By' field value does not display 'System' you can disable the antivirus scan job. However, this would not be recommended.

Please take a look at the ServiceNow documentation for more information on antivirus scan in the platform:  
  
[https://docs.servicenow.com/csh?topicname=antivirus-protection.html&version=latest](https://docs.servicenow.com/csh?topicname=antivirus-protection.html&version=latest)
