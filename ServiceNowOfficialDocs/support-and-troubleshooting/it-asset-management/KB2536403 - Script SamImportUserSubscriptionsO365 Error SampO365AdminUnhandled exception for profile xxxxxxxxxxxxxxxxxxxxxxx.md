---
title: "Script: SamImportUserSubscriptionsO365: Error: SampO365AdminUnhandled exception for profile : xxxxxxxxxxxxxxxxxxxxxxx"
aliases:
  - KB2536403
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB2536403
kb_number: KB2536403
last_modified: 2025-09-29
---

## Issue

The Microsoft 365 subscription import job (`SamImportUserSubscriptionsO365`) fails because the Azure app registration client secret used for authentication has expired.

## Resolution

-   Work with your Azure Administrator to generate a new client secret or use certificate-based authentication for improved security.
    -   Azure documentation: [Create new client secret](https://learn.microsoft.com/en-us/entra/identity-platform/quickstart-register-app#add-a-client-secret)
    -   Azure documentation: [Certificate credentials](https://learn.microsoft.com/en-us/entra/identity-platform/certificate-credentials)
-   Update the new secret in ServiceNow:
    -   Navigate to Subscription Profile (samp\_sw\_subscription\_profile).
    -   Edit the Microsoft 365 profile in use.
    -   Replace the expired client secret with the newly generated one.
    -   Save and test the connection.
-   Re-run the O365 subscription import job to validate that the authentication succeeds and data is imported.

## Additional Information

## References

[ServiceNow Docs – Integrate with Microsoft 365](https://www.servicenow.com/docs/bundle/xanadu-it-asset-management/page/product/software-asset-management2/concept/integrate-with-microsoft.html)

Microsoft error reference: [AADSTS7000222](https://login.microsoftonline.com/error?code=7000222)
