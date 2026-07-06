---
title: "Determining if the user has an older version of SAML"
aliases:
  - KB0538786
tags:
  - servicenow
  - support-kb
  - saml
  - sso
  - script-include
  - upgrade
  - authentication
area: access-controls-authentication
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0538786
kb_number: KB0538786
last_modified: 2024-05-19
---

## Issue

Troubleshooting: Determining if the user has an older version of SAML

  

# Problem

* * *

A SAML plugin upgrade has failed.

# Symptoms

* * *

-   The deep linking is not working.
-   The SAML plugin upgrade failed.

# Cause

* * *

There are a couple of deep linking-related fixes in the SAML2\_Update1 script include. SNC may fail to upgrade the script includes if a customer has made customizations and still uses the old version of SAML.

# Resolution

* * *

To solve the issue:

1.  Check if the SAML2\_update1 script include is upgraded properly.
2.  If not, check with an administrator to determine what type of customization has been made. 
3.  Revert to the current version of SAML, and then incorporate the customizations, if needed.
4.  Try upgrading again.

## Related

- [[KB0539112 - Troubleshooting SAML or SSO issues in ServiceNow]] - master SAML/SSO troubleshooting checklist
- [[KB0538769 - Determining if SAML issues are occurring due to customer scripts no longer working after upgrade]]
- [[t_TroubleshootScriptIssuesWithSAML]] - official docs on troubleshooting SAML script issues
- [[t_UpdateExistingSAML2.0Integration]] - official docs on updating an existing SAML 2.0 integration
