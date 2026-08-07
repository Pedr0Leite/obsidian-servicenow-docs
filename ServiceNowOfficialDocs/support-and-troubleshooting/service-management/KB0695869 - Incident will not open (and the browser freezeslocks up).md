---
title: "Incident will not open (and the browser freezes/locks up)"
aliases:
  - KB0695869
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0695869
kb_number: KB0695869
last_modified: 2024-04-07
---

## Incident will not open (and the browser freezes/locks up)

  

### Issue

# Symptoms

* * *

Unable to open an incident form

# Release

* * *

Kingston Patch 7

# Cause

* * *

There are a large number of comments and work notes on the incident which are preventing the incident from being opened (continued explanation below...) 

# Resolution

* * *

On the specific incident where this behavior is seen, there are a substantial amount of journal entries. There are 41,260 comments and 80,844 work notes, a total of 122,104 entries.  
  
The sys\_audit for the incident shows 122,166 entries.   
  
It is likely that the entries on the sys\_journal\_field were created by a script (hence the unusually large amount of entries).

To resolve the behavior, on a sub-production instance, remove the sys\_journal\_field entries for the affected record.

Doing the above should allow the incident to be opened again without issue.
