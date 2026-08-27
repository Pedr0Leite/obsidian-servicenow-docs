---
title: "Email Client shows \"showing 1 through 10 of 10\" for autocomplete"
aliases:
  - KB0779306
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0779306
kb_number: KB0779306
last_modified: 2025-01-03
---

## Email Client shows "showing 1 through 10 of 10" for autocomplete

  

### Summary

When you type a recipient email address in the Email Client, autocomplete shows only 10 results by default. See screenshot below:

![](sys_attachment.do?sys_id=adf1ac451b407414f34d33bc1d4bcbf4)![](sys_attachment.do?sys_id=a4fbca641bc84c50ada243f6fe4bcb6f)

  

Customer may request to change this autocomplete result count.

In order to change this count, change the integer value of system property "**glide.ui.email\_client.autocomplete.count**" to any required number from 10.
