---
title: "External customers are unable to view attachments on Portal via Document viewer"
aliases:
  - KB0855835
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0855835
kb_number: KB0855835
last_modified: 2024-09-26
---

## External customers are unable to view attachments on Portal via Document viewer

  

### Issue

When logged in as an external customer on CSM/CSP portal, if you click on an attachment,

Either the document viewer might NOT open

OR

the document viewer opens but the article is NOT rendered (its blank).

### Release

Orlando. 

  

### Cause

There are 2 reasons for it.

1\. System property that enables document viewer for service portal is FALSE

2\. The script that renders the document viewable only allowed to be run for Internal.

### Resolution

1\. Create the below system property (if doesn't exist) and set it to TRUE

glide.knowman.use\_document\_viewer

sn\_km\_portal.glide.knowman.serviceportal.use\_document\_viewer

![](/sys_attachment.do?sys_id=78e10265dbcfd490fb115583ca9619f9)

  

2\. Create below ACL for the given process to make sure snc\_external / sn\_esm\_user are allowed to run that process.

![](/sys_attachment.do?sys_id=441f39e5db8fd490fb115583ca9619b2)
