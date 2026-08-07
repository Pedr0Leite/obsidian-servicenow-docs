---
title: "Microsoft 365 integration and subscription reclamation is not getting genreated when the user is missing"
aliases:
  - KB2989176
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB2989176
kb_number: KB2989176
last_modified: 2026-05-20
---

## Microsoft 365 integration and subscription reclamation is not getting genreated when the user is missing

  

### Issue

**Problem**  
The scheduled job for generating removal candidates is being executed manually and/or via schedule, but removal candidates are only being generated for a few subscriptions (2–3 users). Other eligible subscriptions (meeting the inactivity criteria) are not being processed. Steps to reproduce include navigating to Microsoft 365 subscription data in ServiceNow, identifying users with last activity date older than 30 days, executing the scheduled job, and observing that only a subset of eligible subscriptions are processed. The user field on software subscription records is often empty, and manually associating users with subscriptions sometimes resolves the issue for specific records.  
  

### Release

N/A

### Cause

**Root Cause**  
1\. The user field on software subscription records is empty due to mismatched User Principal Name (UPN) and email address values in the environment, preventing automatic user association.

2\. The script uses a pre-filter to evaluate subscription age (creation date) and staleness (last activity date), and some records may not meet both criteria, resulting in incomplete reclamation candidate generation.  
  

### Resolution

**Steps to Resolve**  
1\. Associate the appropriate users with their corresponding software subscriptions in the samp\_sw\_subscription table.

2\. Re-run the reclamation job after ensuring the user field is populated for eligible subscriptions.

3\. Verify that the User Principal Name (UPN) matches the user's email address or adjust user resolution rules if necessary.

4\. Review the script logic for age gate and staleness checks to ensure subscriptions meet both creation date and last activity date thresholds.
