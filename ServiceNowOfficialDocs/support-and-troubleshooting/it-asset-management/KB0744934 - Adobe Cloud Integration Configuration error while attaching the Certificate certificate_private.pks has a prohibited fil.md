---
title: "Adobe Cloud Integration Configuration error while attaching the Certificate \"certificate_private.pks has a prohibited file extension\""
aliases:
  - KB0744934
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0744934
kb_number: KB0744934
last_modified: 2026-05-21
---

## Adobe Cloud Integration Configuration error while attaching the Certificate "certificate\_private.pks has a prohibited file extension"

  

### Issue

The instructions for configuring Adobe cloud publisher pack for Software Asset Management (SAM) states that we must attach a 'pks' file to the x.509 record in ServiceNow.  
Attempting to attach a PKS file to the x.509 record prompts the error message as seen in attachment.  
  

![Screenshot of certificate\_private.pks](/sys_attachment.do?sys_id=b4d4f81b8358eed0cdbbc430feaad33c "Screenshot of certificate_private.pks has a prohibited file extension popup message.png")

### Release

### Cause

System property: '**glide.attachment.extensions**' whose value by default is empty means that we allow all file extensions as attachments by default.

When the property's value is set to certain file extensions and if **pks** is not in the value specified, we see the error as shown above.

### Resolution

1) Navigate to system properties and search for the property : **glide.attachment.extensions** 

2) In the value , add **pks** and try attaching the certificate again.

### Related Links

[KB1001915 - Adobe Integration Profile Configuration Step-By-Step | Software Asset Management](https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB1001915 "KB1001915 - Adobe Integration Profile Configuration Step-By-Step | Software Asset Management")
