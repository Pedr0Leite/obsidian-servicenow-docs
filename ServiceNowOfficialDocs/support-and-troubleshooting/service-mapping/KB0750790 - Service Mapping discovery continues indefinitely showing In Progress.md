---
title: "Service Mapping discovery continues indefinitely showing \"In Progress\""
aliases:
  - KB0750790
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0750790
kb_number: KB0750790
last_modified: 2026-05-21
---

## Service Mapping discovery continues indefinitely showing "In Progress"

  

### Issue

 

On individual Service Maps, the discovery process appears stuck with a spinning cog wheel animation that continues indefinitely. The discovery does not stop automatically, requiring manual intervention by selecting Stop Discovery on the topology map.

Before troubleshooting, verify if discovery is actually complete:

1.  Go to the sa\_endpoint\_status table and look for records with status other than completed. If found, discovery is still running.
2.  Check the ecc\_queue records with topic ServiceDiscoveryProbe. If any records show states other than processed or error, discovery is not complete.

![discovery in progress showing stuck discovery indicator](sys_attachment.do?sys_id=bf1eb86d938b2650101833527cba1073)

### Release

Any release

### Cause

The system relies on a scheduled job called Update Business Service Status to automatically mark discovery as complete. This job runs periodically and updates the business service discovery status after all discovery tasks finish.

When this job becomes inactive or gets stuck, the discovery status never updates to complete, even though all endpoints have finished processing.

### Resolution

Follow these steps to resolve the issue:

1.  Verify the scheduled job is active:
    -   Go to **System Definition** > **Scheduled Jobs.**
    -   Find **Update Business Service Status.**
    -   Ensure the **Active** field is set to **true.**
2.  If the job is stuck:
    -   Go to the sys\_trigger table.
    -   Delete the stuck **Update Business Service Status** job record.
    -   Rerun the job manually.
