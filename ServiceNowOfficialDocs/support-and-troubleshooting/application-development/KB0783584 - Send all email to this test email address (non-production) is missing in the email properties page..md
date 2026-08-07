---
title: "\"Send all email to this test email address (non-production)\" is missing in the email properties page."
aliases:
  - KB0783584
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0783584
kb_number: KB0783584
last_modified: 2024-04-20
---

## "Send all email to this test email address (non-production)" is missing in the email properties page.

  

### Issue

The field "Send all email to this test email address (non-production)" is missing in the email properties page.

### Release

All versions.

### Cause

This is caused because of the fact that the glide.email.test.user property is missing the category in the categories related list.

### Resolution

To fix this :

1) Delete the glide.email.test.user property  
2) Export the glide.email.test.user property and the sys\_properties\_category\_m2m entry from a working instance of same version.  
3) Import the exported records to the non working instance.
