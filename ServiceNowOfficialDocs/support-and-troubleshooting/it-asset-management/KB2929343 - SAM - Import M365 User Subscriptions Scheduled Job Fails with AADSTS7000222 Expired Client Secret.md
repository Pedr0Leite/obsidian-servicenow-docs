---
title: "SAM - Import M365 User Subscriptions Scheduled Job Fails with AADSTS7000222 Expired Client Secret"
aliases:
  - KB2929343
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB2929343
kb_number: KB2929343
last_modified: 2026-04-01
---

## Issue

The SAM - Import M365 User Subscriptions scheduled job fails with the following error:

SamImportUserSubscriptionsO365: Failed to run job. Please look into logs for more details.

System logs show an outbound HTTP 401 to login.microsoftonline.com with OAuthProblemException error invalid\_client and Microsoft error code AADSTS7000222.

## Resolution

In the Azure portal, navigate to the App Registration used by the integration and generate a new client secret

Open the Microsoft 365 Direct Integration Profile in ServiceNow and update the client secret with the newly generated value.

Click Validate Connection to confirm authentication is successful.

Re-run the SAM - Import M365 User Subscriptions job
