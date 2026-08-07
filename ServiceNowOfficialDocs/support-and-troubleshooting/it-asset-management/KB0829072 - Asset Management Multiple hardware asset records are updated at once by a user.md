---
title: "Asset Management:  Multiple hardware asset records are updated at once by a user"
aliases:
  - KB0829072
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0829072
kb_number: KB0829072
last_modified: 2024-08-28
---

## Asset Management: Multiple hardware asset records are updated at once by a user

  

### Issue

There are multiple hardware asset (alm\_hardware) records that were updated at the same time and it shows that they were updated by a user. Also these hardware asset records that got updated in bulk are associated to the same model

### Cause

The user updated the "name" field on the model record which is associated with the assets.

This update triggers the "Calculate display\_name" Business rule on cmdb\_model, and updates the display name on the model record:

https://<instancename>.service-now.com/nav\_to.do?uri=sys\_script.do?sys\_id=b5113661d7131100bbc783e80e61035b

Then this business rule "Update asset display names" was triggered, which updates all the assets associated with the model:

https://<instancename>.service-now.com/nav\_to.do?uri=sys\_script.do?sys\_id=2f636cf0eb3321005ecfa9bcf106fe81
