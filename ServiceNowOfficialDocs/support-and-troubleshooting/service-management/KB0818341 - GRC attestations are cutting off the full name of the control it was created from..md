---
title: "GRC attestations are cutting off the full name of the control it was created from."
aliases:
  - KB0818341
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0818341
kb_number: KB0818341
last_modified: 2024-04-08
---

## GRC attestations are cutting off the full name of the control it was created from.

  

### Issue

When an attestation is created, the name on the survey page appears to be character limited on the attestation.

### Cause

PRB1364400

### Resolution

Workaround :

1) Open the Dictionary for the asmt\_assessable\_record table  
2) Go into the record for the column name 'name' field of asmt\_assessable\_record  
3) You will see that the max length for the 'name' field is 100; please try to set this to a higher number (i.e 250)  
  
The title gets truncated since the max length for the name field in asmt\_assessable\_record is shorter than the GRC source record.
