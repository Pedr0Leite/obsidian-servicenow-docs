---
title: "All Import sets fail when run automatically;  re-processing them manually works"
aliases:
  - KB0754968
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0754968
kb_number: KB0754968
last_modified: 2024-04-07
---

## All Import sets fail when run automatically; re-processing them manually works

  

### Issue

# Symptoms

\- Import sets get processed by the Transform Map scripts but noting is processed:  
updated=0, inserted=0. skipped=0, ignored=0   
\- When re-running manually ("Execute Now" button), this always works 

# Cause

The staging tables are not given a "pending" state because the default value (pending) was somehow cleared from dictionary record. 

# Resolution

1\. For Dictionary Entries where table = sys\_import\_set\_row and column = sys\_import\_state   
2\. Modify the'Default value' field to pending
