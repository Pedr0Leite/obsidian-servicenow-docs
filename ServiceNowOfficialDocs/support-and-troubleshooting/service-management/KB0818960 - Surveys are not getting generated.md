---
title: "Surveys are not getting generated"
aliases:
  - KB0818960
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0818960
kb_number: KB0818960
last_modified: 2024-04-08
---

## Surveys are not getting generated

  

### Issue

Survey emails are not triggered and surveys are not generated.  
Error on the form when survey is assigned "Instance could not be created"

### Cause

Possible reasons and fixes to check :  
When the category is missing for the assessable record, it leads to the error: "Instance could not be created"  
On the table : asmt\_m2m\_category\_assessment, category was missing for the assessable record : On creating that , the issue is resolved.  
Things to check in the case of similar error :  
\-asmt\_assessable\_record  
\-asmt\_m2m\_category\_assessment  
\-asmt\_metric\_type  
  
Also check if OOB Script include:AssessmentUtils is as per OOB.

### Resolution

When we create a new record in asmt\_m2m\_category\_assessment table issue is resolved
