---
title: "No image / Broken image in the survey email"
aliases:
  - KB0812581
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0812581
kb_number: KB0812581
last_modified: 2025-02-27
---

## Issue

There is no image or a broken image in the survey email sent to the user.

## Resolution

If the user wants that no image (no broken image) should be sent to the user in the email notification, then they need to:

1.  Open the affected survey
2.  Choose any reference record in the "Sample metric" field, wait until the popup shows and then click the 'ok' button. (Do not save the form)
3.  Clear sample metric field by deleting the contents in the "Sample Metric" field.
4.  Now save the form.

  
BUT, If the user wants that an image should be sent to the user in the email notification, then they need to:

1.  Open the affected survey
2.  Choose any reference record in the "Sample metric" field, wait until the popup shows and then click the 'ok' button.
3.  Now save the form.
4.  After this, the "Sample Metric" field is not empty and the email should contain the image link as expected.

Note: It will automatically create a file in the sys\_attachment with the file name having a prefix as sample\_metric\_image and the table name as ZZ\_YYasmt\_metric\_type.
