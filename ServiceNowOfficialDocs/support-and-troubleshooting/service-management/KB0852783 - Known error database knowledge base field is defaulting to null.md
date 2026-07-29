---
title: "Known error database knowledge base field is defaulting to null"
aliases:
  - KB0852783
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0852783
kb_number: KB0852783
last_modified: 2024-04-08
---

## Known error database knowledge base field is defaulting to null

  

### Issue

When clicking on "Create Known Error article" from a problem record, the following error is returned

Apply default values: null

Also, the Knowledge Base is not populated

### Cause

The dictionary entry or dictionary override of kb\_knowledge.kb\_knowledge\_base field was customized

This dictionary is also having a default value pointing to the property "problem.knowledgebase.known\_error\_article"

This property contains the default sys\_id for the "Known Error" knowledge base which is "c0a54bac871023000e3dd61e36cb0bcb" by default

If this sys\_id is not in your instance or you deleted the out-of-box (OOB) knowledge base, then the issue can occur

  

### Resolution

Check the dictionary entry or dictionary override entry for the field kb\_knowledge\_base in the kb\_knowledge table and revert it to OOB if customized

  
Check the property "problem.knowledgebase.known\_error\_article" and make sure that the sys\_id is pointing to an existing Known error knowledge base
