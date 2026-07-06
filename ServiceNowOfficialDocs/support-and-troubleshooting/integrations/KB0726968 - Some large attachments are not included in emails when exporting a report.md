---
title: "Some large attachments are not included in emails when exporting a report "
aliases:
  - KB0726968
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0726968
kb_number: KB0726968
last_modified: 2026-04-20
---

## Some large attachments are not included in emails when exporting a report

  

### Issue

When exporting a report containing a large attachment, like a .csv file larger than 25 MB, the following dialog box displays with a **Mail it** option.

![Dialog box showing mail it option for email export](sys_attachment.do?sys_id=8bba0fa693ceaa507c79b36d6cba10e5 "Dialog box showing mail it option for email export")

However, selecting the Mail it option does not include the expected attachments. 

### Cause

The failure to include some attachments is due to the attachment file size and the outbound email attachment size limitations of the ServiceNow infrastructure.

### Resolution

For exports with large file attachments, instead of selecting the **Mail it** option, download the reports by selecting **Wait for it**.

Alternatively, you can increase the value of the system property by updating this record: glide.email.outbound.max\_total\_attachment\_size\_bytes.

**Note:** If using the ServiceNow mail infrastructure to send these emails, there is a hard limit of 25 MB that cannot be changed. This limit includes the total size of the email, including body and all attachments. You can use your own email infrastructure if you need to send attachments larger than 25 MB.
