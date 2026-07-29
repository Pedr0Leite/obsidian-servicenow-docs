---
title: "Form email does not load when opened by a user"
aliases:
  - KB0785278
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0785278
kb_number: KB0785278
last_modified: 2024-04-08
---

## Form email does not load when opened by a user

  

### Issue

When a user goes to form record and clicks the three dots to see more options in the top right header bar

![](/sys_attachment.do?sys_id=cf6f0081db8c7890dc2beeb5ca9619bc)

Clicking on Email to bring the email option

![](/sys_attachment.do?sys_id=4b6f0081db8c7890dc2beeb5ca9619c0)

The email function does seem to load correctly

![](/sys_attachment.do?sys_id=c36f0081db8c7890dc2beeb5ca9619bf)

### Release

Observed in Madrid+

### Cause

The cause of this was related to Email Client Canned Messages (sys\_email\_canned\_message) having a variable declared but the canned messages itself does not have a table that can be selected hence you will see an error in the node logs that looks something like this:

SEVERE \*\*\* ERROR \*\*\* null:1078:41: <g2:get\_canned\_messages> For input string: "</p>

This can also be caused by having HTML tags inside of the ${variable} declaration. For example: ${<span style="color:#000000;">variable</span>}

### Resolution

  
Removing the offending ${variable} variable allow the email to load correctly.  
  

In the case where HTML tags are present inside of the ${variable} declaration, move the HTML outside of the ${variable} to allow this to function properly.
