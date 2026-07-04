---
title: "Software Asset Management – ILMT v2 Scheduled Job"
aliases:
  - KB2954983
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB2954983
kb_number: KB2954983
last_modified: 2026-05-01
---

## Software Asset Management – ILMT v2 Scheduled Job

  

### Issue

When the ILMT v2 scheduled job runs in SAM Pro, the number of servers retrieved is lower than the total number of servers visible in the ILMT console.

For example: ILMT may display 200 servers, but SAM Pro imports only 50.

### Release

ALL.

### Cause

The scheduled job retrieves server data by calling the ILMT REST API endpoint

 /api/sam/v2/license\_usage\_per\_server. 

This endpoint does not return a full server inventory  it returns only servers that have active license usage or capacity data recorded against them in ILMT, such as PVU consumption records or recent scan activity.

If a server exists in ILMT but has no associated usage or capacity data, it will not appear in the API response and will therefore not be imported into SAM Pro. This is expected API behavior and is not a defect in the SAM Pro integration.

To verify, compare the total server count in the ILMT console against the number returned by the API. Any servers missing from the import should be checked in ILMT to confirm whether they have PVU consumption, capacity records, or scan activity assigned to them.

### Resolution

This behavior is by design. To include additional servers in the import, ensure they have license usage/capacity data recorded against them in ILMT. Servers with no usage data will not be returned by this API endpoint.
