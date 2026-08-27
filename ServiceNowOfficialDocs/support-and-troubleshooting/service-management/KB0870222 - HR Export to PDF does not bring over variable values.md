---
title: "HR Export to PDF does not bring over variable values"
aliases:
  - KB0870222
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0870222
kb_number: KB0870222
last_modified: 2025-09-03
---

## HR Export to PDF does not bring over variable values

  

### Issue

When trying to utilize the "Export to PDF" option built-in to ServiceNow for exporting a HR Case to PDF, the HR case's Variable Editor variable values are not carrying across to the PDF. The user wanted to know why.

### Resolution

This is the Out of Box, designed behavior as only fields on the form and their values are carried over to the PDF.

It was recommended that the customer try to create a custom Business Rule to query the variables and their values and print them out to the "description" field, as this field is reliably carried over to the PDF.
