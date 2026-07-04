---
title: "Intent and usage of the field \"Suspended For\""
aliases:
  - KB0961910
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0961910
kb_number: KB0961910
last_modified: 2025-09-03
---

## Intent and usage of the field "Suspended For"

  

### Issue

The field is labeled "Suspended For" but does not seem to get set when using the suspended case functionality.   
  

### Resolution

The product team has provided the following information related to the "Suspended For" field:  
  
The sla\_suspended\_for field was added when we moved over functionality from the old pre-scoped order functionality. It is a legacy field that some customer may wish to use.  
  
Currently, I found the usage of this field only 'Tuition Reimbursement' workflow where it is setting the sla\_suspend\_for field with a value of 'Awaiting transcripts after course end date'. Except this usage, we do not have any other usages of this field.
