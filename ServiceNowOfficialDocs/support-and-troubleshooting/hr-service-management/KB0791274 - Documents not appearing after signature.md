---
title: "Documents not appearing after signature"
aliases:
  - KB0791274
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0791274
kb_number: KB0791274
last_modified: 2024-04-08
---

## Documents not appearing after signature

  

### Issue

When a document is signed on the HR task record the attachment is missing on both HR task and HR case.

### Resolution

-   The Document Template mappings need to be chosen from the table which is selected on the template. The pdf will be attached to the table only if all the mappings are populated on the record and all signatures of those users were complete
-   So if the customer chooses the subject person and Assigned to fields signatures in the PDF template, the pdf will be attached only when the subject person and assigned to users have signed. If the fields are not populated/empty in the record the pdf won't be created.
-   Hence the assigned\_to field on the case must be populated for the pdf to create and attach to the case.
-   This is an expected out of the box behavior

### Related Links

STEPS TO REPRODUCE :

-   Click on "create new case" under HR Case Management
-   Select an HR service
-   create New case
-   Open the HR task and sign the document 
-   Once the document is signed, the PDF is not attached to both the HR case and HR task
