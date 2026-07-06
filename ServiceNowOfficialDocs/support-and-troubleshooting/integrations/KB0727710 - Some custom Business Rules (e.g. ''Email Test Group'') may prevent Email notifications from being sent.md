---
title: "Some custom Business Rules (e.g. ''Email Test Group'') may prevent Email notifications from being sent"
aliases:
  - KB0727710
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0727710
kb_number: KB0727710
last_modified: 2024-04-26
---

## Some custom Business Rules (e.g. ''Email Test Group'') may prevent Email notifications from being sent

  

### Issue

When reviewing Emails, some Emails have a status 'SENT' but the recipients never received the Emails.

  

### Cause

It turns out that the notification was processed but behind the scene, some business rules prevented the Email from being sent based on the inclusion listing conditions created on business rules.

The inclusion-list list of Emails is typically stored in a system property named 'glide.email.test.group.custom'  
The business rule name is often ''Email Test Group''

Some business rule customizations are often added to Servicenow instances and administrators are not aware of its existence.

This business rule adds a user inclusion list functionality that lets an admin specify which users can or cannot be used as a recipient. The users can still be added but the Email does not get sent.

### Resolution

Disable the customized business rules tampering with the notification processes (e.g. "Email Test Group")

<table class="noteTable" align="left"><tbody><tr><td class="c3"><img class="c2" title="Note" src="/Note_25x.pngx" align="bottom" border="border" hspace="" vspace=""></td><td class="c4"><strong>Note</strong>: This is a customization, you need to contact the developer to fully understand the scope of this business rule and its configuration.</td></tr></tbody></table>
