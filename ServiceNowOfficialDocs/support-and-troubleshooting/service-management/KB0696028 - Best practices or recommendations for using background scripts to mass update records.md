---
title: "Best practices or recommendations for using background scripts to mass update records"
aliases:
  - KB0696028
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0696028
kb_number: KB0696028
last_modified: 2024-04-07
---

## Best practices or recommendations for using background scripts to mass update records

  

### Issue

# Symptoms

* * *

Large delays in system functionality (as the user was running a background script during work hours to update 50,000 records). 

# Release

* * *

Kingston Patch 6

# Cause

* * *

It is recommended that when updating large amounts of records, that this be done through a Scheduled Job (and generally in off-business hours). 

# Resolution

* * *

Per the above, the user's goal of mass updating records can be best accomplished by placing the script they are currently running during the day into a Scheduled Job and having it run in batches each night, in off-business hours.  
  
Doing it this way will allow the user to chip away at the large number of records over a few days, and having the script run by a scheduled job will allow the user to run it during off-hours when no one's day-to-day work will be affected.
