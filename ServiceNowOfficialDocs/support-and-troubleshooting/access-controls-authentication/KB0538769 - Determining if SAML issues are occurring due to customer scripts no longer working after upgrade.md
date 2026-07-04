---
title: "Determining if SAML issues are occurring due to customer scripts no longer working after upgrade"
aliases:
  - KB0538769
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0538769
kb_number: KB0538769
last_modified: 2025-10-21
---

## Issue

After a recent instance upgrade, users cannot log in.

### Symptoms

-   No user can log in to the system.
-   One user cannot log in to the system.
-   The user cannot validate SAML response.
-   The deep linking is not working.
-   SAML is not correctly setting CMS redirection.

## Resolution

1.  Check if this occurs after a recent system upgrade.
2.  If so, confirm that the SAML2 scripts are up to date by checking the history.
3.  If any scripts were not upgraded, check with the administrator to determine what changes have been made to the scripts. 
4.  Revert to OOB scripts and apply the necessary changes or customizations, if needed.
5.  Ask users to try to log in again.
