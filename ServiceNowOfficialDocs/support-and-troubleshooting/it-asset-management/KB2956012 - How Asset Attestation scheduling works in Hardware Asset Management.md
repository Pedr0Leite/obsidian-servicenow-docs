---
title: "How Asset Attestation scheduling works in Hardware Asset Management?"
aliases:
  - KB2956012
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB2956012
kb_number: KB2956012
last_modified: 2026-04-14
---

## How Asset Attestation scheduling works in Hardware Asset Management?

  

### Summary

**SYMPTOMS:**   
\- Asset Attestation scheduled runs include all assigned assets on every execution, including assets previously confirmed by the user   
\- Users receive attestation notifications for assets they have already attested in a prior run   
\- Attestation schedule re-prompts for the full hardware portfolio each time it runs   
  
**\[-\] Cause:**  
Asset Attestation is designed as a periodic full-portfolio audit. Each scheduled run re-evaluates all in-scope assets regardless of prior attestation state. The script uses two layers:  
  
1\. A scheduled job runs daily and checks the sn\_itam\_common\_attestation\_schedule table for schedule records whose next\_run date has arrived.   
2\. Each schedule record defines a user filter, model categories, and a frequency. When a schedule is due, the system creates a new attestation run for all matching users and all their assigned assets matching the model category criteria.   
  
The method that builds the asset list (AssetAttestationUtils.processAttestationCreation) queries alm\_asset filtered on:  
\- assigned\_to matching the schedule's user filter   
\- model\_category matching the schedule's categories   
\- sys\_class\_name = alm\_hardware (when HAMP is active)   
  
This query does not filter on prior attestation state. The fields last\_attestation\_date and last\_attestation\_state on alm\_asset which are write-only, populated when a user responds but never read when building the next run's asset list.   
  
Each scheduled run:   
\- Creates a new attestation record (state = in\_progress)   
\- Creates new m2m records for ALL in-scope assets (status = open)   
\- Closes any prior open m2m records as closed\_incomplete   
\- Sends notification to each user with open items   
  
Assets excluded from a run:   
\- Assets whose parent is a bundle or pallet   
\- Assets with an open remediation task   
\- Assets with excluded\_from\_ham = true   
  
There is no incremental mode, no delta mode, and no attestation cycle concept that prevents re-prompting within a window.
