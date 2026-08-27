---
title: "HR Multi Instance Integration known limitations"
aliases:
  - KB1808151
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB1808151
kb_number: KB1808151
last_modified: 2025-09-03
---

## HR Multi Instance Integration known limitations

  

HR multi instance integration has following limitations 

-   Below HR service configuration changes such as case options, fultillment type, and COEs are restricted on remote HR services. 
    -   Restricted Case Options:
        -   Add manager to Watchlist
        -   Agent Can Add An Approval
        -   User cannot cancel
        -   Automatically Initiate Document Tasks
        -   Automatically move attachments
    -   Restricted COEs
        -   sn\_hr\_le\_case
        -   sn\_hr\_er\_case
    -   Restricted fulfillment types
        -   Lifecycle event
        -   Journey
    -   Restricted states on remote HR Case
        -   Awaiting Approval
        -   Awaiting Acceptance
        -   Suspended
-   Approvals (via flow or adhoc) must not be used for remote case or remote hr service configurations.
-   On the consumer employee portal, a catalog must be submitted on ones own behalf not for others. Only then a remote case can be created on a provider instance or a third party service can be availed.
-   HR Multi instance integration doesn't offer mobile support for remote catalogs.
