---
title: "Why are discovery models created with 0 installs after SAM - Delete Discovery Models when using the Jamf integration"
aliases:
  - KB2989150
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB2989150
kb_number: KB2989150
last_modified: 2026-04-29
---

## Why are discovery models created with 0 installs after SAM - Delete Discovery Models when using the Jamf integration

  

### Issue

**Problem**  
Discovery models with 0 related installations were observed being re-created after the 'SAM - Delete Discovery Models if there are no related Installations' job was manually executed.

### Release

N/A

### Cause

**Root Cause**  
The SG-Jamf connector recreates Discovery Models if the software titles still exist in Jamf's managed inventory, even if no active installations are reported during the same run. This occurs because the connector operates on a scheduled push model, processing software inventory from Jamf and creating or updating Discovery Models accordingly. The 0-install state observed after re-creation is likely a timing artifact, where Discovery Models are recreated before corresponding installation records are fully ingested.  
  

### Resolution

**Steps to Resolve**  
1\. Confirm that the software titles in question still exist in Jamf's managed inventory, as this is the source of truth for the SG-Jamf connector.

2\. Understand that the recreation of Discovery Models is expected behavior when the underlying Jamf inventory reports the software title, even if no installations are currently active.

3\. Note that the 'SAM - Delete Discovery Models if there are no related Installations' job and the SG-Jamf integration may work against each other, with the job removing records and the connector recreating them based on Jamf's reporting.
