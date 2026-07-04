---
title: "Unable toTrigger Survey for Request table in Production"
aliases:
  - KB0786481
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0786481
kb_number: KB0786481
last_modified: 2024-04-08
---

## Unable toTrigger Survey for Request table in Production

  

### Issue

  
Surveys in Production are not being triggered however they trigger fine in Dev and Test.  
The survey configuration was moved from Test to Prod via update sets.

### Cause

Most Probable Cause:  
The assessable record associated with the Survey seems to have been corrupted during the update set move.  
  
We tested by manually attempting to generate an Assessment instance from the Survey using the UI Action 'Assign Survey', however this failed and generated an error.  
We therefore deleted the existing Assessable record (after taking a backup) and again manually assigned a Survey.  
This generated automatically a new assessable record and successfully created an Assessment Instance.  
  
Thereafter we tested triggering the Survey and it was also successful.

### Resolution

  
Regenerating the Assessable record on the Production instance resolved the issue.
