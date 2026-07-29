---
title: "Human Resources/HR: PDF document template with a field mapped to it truncates/cuts off text instead of wrapping/word wrapping to the next line"
aliases:
  - KB0819901
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0819901
kb_number: KB0819901
last_modified: 2024-04-08
---

## Human Resources/HR: PDF document template with a field mapped to it truncates/cuts off text instead of wrapping/word wrapping to the next line

  

### Issue

Human Resources/HR: PDF document template with a field mapped to it truncates/cuts off text instead of wrapping/word wrapping to the next line

### Cause

The fillable PDF file (.pdf) uploaded to be used as a document template's text box that is being used for field mapping is not a multi-line/multiline text box.

### Resolution

The PDF template needs to have a multi-line text box for the field being mapped to for word wrapping to occur.  
When the mapping field is mapped to a multiline text box, the text wrapping occurs as expected.  
The multi-line text box needs to be present on the '.pdf' file imported into the instance to be used as the template.  
This is configured on the PDF file itself, rather than through configuration on the ServiceNow instance.
