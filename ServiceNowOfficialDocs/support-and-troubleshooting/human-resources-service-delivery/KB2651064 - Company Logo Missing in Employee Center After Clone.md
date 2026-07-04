---
title: "Company Logo Missing in Employee Center After Clone"
aliases:
  - KB2651064
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB2651064
kb_number: KB2651064
last_modified: 2026-01-01
---

## Company Logo Missing in Employee Center After Clone

  

### Issue

After cloning, the company logo in Employee Center was not visible and displayed the default ServiceNow logo. Attempts to update the logo did not reflect on the front end.

### Release

Any

### Cause

The clone was performed with “Exclude attachment data” enabled, which caused the logo file to be missing or corrupted between PROD and TEST instances.

### Resolution

·  Use the Branding Editor in the affected instance to upload and apply the correct company logo.

·  Avoid selecting “Exclude attachment data” during future clone operations if branding assets need to be retained.

·  Validate that the logo displays correctly on the Employee Center portal after applying changes.
