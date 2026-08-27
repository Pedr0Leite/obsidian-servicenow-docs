---
title: "Use catalog variable value in an action script"
aliases:
  - KB0793381
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0793381
kb_number: KB0793381
last_modified: 2024-04-08
---

## Use catalog variable value in an action script

  

### Issue

Use catalog variable value in an action script e.g. 'send email' action and use the catalog variable value in the subject line for the email.

### Resolution

1) Use 'get catalog variables' action to select the required variable.

2) Use fd\_data.get\_catalog\_variables.<variable\_name> to capture and utilise the variable value as required.

Screenshots are attached to illustrate this with an example scenario.

[screenshot 1](sys_attachment.do?sys_id=7d4a940ddb0838d0fec4fb24399619b9 "screenshot 1")

[screenshot 2](sys_attachment.do?sys_id=f14a940ddb0838d0fec4fb24399619bb "screenshot 2")

[screenshot 3](sys_attachment.do?sys_id=b94ad40ddb0838d0fec4fb2439961913 "screenshot 3")
