---
title: "hrm_ticket_page shows 'Ask a question' though glide.connect.chat.disabled is set to true"
aliases:
  - KB0830842
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0830842
kb_number: KB0830842
last_modified: 2024-04-08
---

## hrm\_ticket\_page shows 'Ask a question' though glide.connect.chat.disabled is set to true

  

### Issue

'Ask A question' still shows on hrm\_ticket\_pages when the property glide.connect.chat.disabled is set to true

### Release

New York / Orlando

### Cause

The issue is because by setting the property 'glide.connect.chat.disabled' the widget is disabled.

When the property 'glide.connect.chat.disabled' is set to false

![](/sys_attachment.do?sys_id=17d270451b487414f34d33bc1d4bcb02)

When the property 'glide.connect.chat.disabled' is set to true

![](/sys_attachment.do?sys_id=d7d230451b487414f34d33bc1d4bcbf4)

However, the HTML component 'Ask a question' is something that is hard-coded in the client script of the widget 'HRM Info Tabs' (lines 35 - 41 of client script).

### Resolution

To remove the HTML component of 'Ask a question' the only way is to either comment the code in HTML script or remove the lines in client script.
