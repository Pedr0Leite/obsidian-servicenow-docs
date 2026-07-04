---
title: "\"Invalid URL\" thrown when Survey Link is used "
aliases:
  - KB0813680
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0813680
kb_number: KB0813680
last_modified: 2024-04-08
---

## "Invalid URL" thrown when Survey Link is used

  

### Issue

when using the Survey URL from the Survey Definition record, an error is thrown:

![](sys_attachment.do?sys_id=b35f5cc9db0c70905a959c41ba9619d3)

### Release

All

### Cause

customization

### Resolution

go to the service portal page "take\_survey" and make sure the SP instance record is using the out-of-the-box widget "Take Survey" (/sp\_widget.do?sys\_id=d65e4495c3331200e44574e1c1d3aeb2)
