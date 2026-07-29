---
title: "Fillable PDF is not editable for the user."
aliases:
  - KB0998546
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0998546
kb_number: KB0998546
last_modified: 2025-09-03
---

## Fillable PDF is not editable for the user.

  

### Issue

Unable to edit the fillable pdf in the employee on-boarding form

### Resolution

  
We reached out to development team and according to them -  
  
To configure fillable pdf, please follow below steps  
1\. Create a pdf document template with Participants.   
2\. Map the created participants to the fields in "Pdf template Mapping" related list, A participant can fill only these mapped fields  
3\. Now we need to map this Document template to our HR Service. To do this, first Open the HR service in HR service configuration and configure Document template in Service table fields of HR Service Additional Information section and also in case options select 'Automatically Initiate Document 'tasks option.  
4\. after that open the Template associated with the HR service and add the pdf document template created in step-1.   
  
For this to work, both HR template and Document template should be configured on same table.
