---
title: "Work Notes are not saved when added to Software Removal Candidates  -- Exclude listed Installations"
aliases:
  - KB0718621
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0718621
kb_number: KB0718621
last_modified: 2024-04-07
---

## Work Notes are not saved when added to Software Removal Candidates -- Exclude listed Installations

  

### Issue

# Symptoms

* * *

  
Issue: The worknotes are not getting updated on the table samp\_sw\_reclamation\_candidate 

# Release

* * *

All Releases

# Cause

* * *

  
Root Cause: Here the worknotes are getting updated but we are not seeing it on the activity. Reason for this is the auditing not enabled in this table field. 

# Resolution

* * *

  
Solution: Simplest method the auditing can be enabled as below:   
\- Add the "additional comments" on the form layout under the Activity section.   
\- Later I removed it from the form layout.  

#
