---
title: "Scheduled job \"SAM - Refresh Dynamics 365 Subscriptions\" fails with \"The requested flow operation was prohibited by security rules"
aliases:
  - KB3127941
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB3127941
kb_number: KB3127941
last_modified: 2026-06-30
---

## Issue

The scheduled job SAM - Refresh Dynamics 365 Subscriptions fails. The flow execution trace shows the Create or Update Record core action (target table samp\_purchased\_subscription\_details) in an Error state with the message:

{"Action Status":{"code":1,"message":"The requested flow operation was prohibited by security rules."}}

The Microsoft Graph API calls earlier in the sub-flow (for example GET /v1.0/subscribedSKUs and GET /v1.0/users) complete successfully with HTTP 200. Only the write-back to ServiceNow fails.

## Resolution

Clear the Run as field on the scheduled job

With no run-as user, the inner user session is not created, the flow runs in the outer system session, and the CSAP enforcement in ExecutionScopeRunner does not apply to the write operation.

Steps:

  1. Open the scheduled job record SAM - Refresh Dynamics 365 Subscriptions (sysauto\_script).

  2. Clear the Run as field

  3. Save the record.

  4. Re-run the job using Execute Now to confirm.

After applying this change, the job completes successfully
