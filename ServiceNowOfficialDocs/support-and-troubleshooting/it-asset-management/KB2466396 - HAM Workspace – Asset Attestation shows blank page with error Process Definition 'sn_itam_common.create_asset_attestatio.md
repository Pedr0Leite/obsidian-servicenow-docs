---
title: "HAM Workspace – Asset Attestation shows blank page with error \"Process Definition 'sn_itam_common.create_asset_attestation' is missing or inactive\""
aliases:
  - KB2466396
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB2466396
kb_number: KB2466396
last_modified: 2025-12-17
---

## HAM Workspace – Asset Attestation shows blank page with error "Process Definition 'sn\_itam\_common.create\_asset\_attestation' is missing or inactive"

  

### Issue

When creating a new Asset Attestation from HAM Workspace, the page shows blank with system log error:

"Process Definition 'sn\_itam\_common.create\_asset\_attestation' is missing or inactive"

### Symptoms

HAM Workspace → Inventory → Asset Attestation → _Create New_ → blank Playbook page.

System logs show `PlaybookInvalidInputException` referencing the missing or inactive process definition.

Only “start” and “end” steps appear in playbook, with no activities.

### Release

Yokohama Patch 6 Hot Fix 1

### Resolution

1\. Set the system property 'sn\_itam\_common.enable\_asset\_attestation\_playbook' value to false. This will prevent the playbook from being invoked and allow the Asset Attestation record to be created directly from the form view, enabling the functionality to work as expected.  
2\. Import the file sys\_pd\_process\_definition\_1451a9bd7f3f121015742fab1d86652b to resolve the issue with the entire playbook 'Create asset attestation'.
