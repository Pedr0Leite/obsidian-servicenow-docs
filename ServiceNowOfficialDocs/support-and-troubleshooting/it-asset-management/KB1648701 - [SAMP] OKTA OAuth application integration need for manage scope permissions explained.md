---
title: "[SAMP] OKTA OAuth application integration need for manage scope permissions explained"
aliases:
  - KB1648701
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB1648701
kb_number: KB1648701
last_modified: 2024-12-13
---

## \[SAMP\] OKTA OAuth application integration need for manage scope permissions explained

  

### Summary

As per the docs for [SAMP Okta SSO Integration](https://docs.servicenow.com/bundle/washingtondc-it-asset-management/page/product/software-asset-management2/concept/integrate-okta.html), we will need to grant the following scopes to your Okta OAuth 2.0 application:

-   okta.groups.read
-   okta.eventHooks.read
-   okta.groups.manage
-   okta.eventHooks.manage
-   okta.apps.read
-   okta.users.manage
-   okta.users.read
-   okta.logs.read
-   okta.apps.manage

The reason why we need manage scope permission is that _The scopes are required to access data around last login/launch of specific apps. We inventory both groups and users who have access to the apps that the customer wants to manage via Okta in SAM. If reclamation rules are set, users can also be removed via groups if the SAM admin wants to optimise based on usage. This is the minimum access needed to meet these use cases._

### Related Links

-   [Integrating with Okta](https://docs.servicenow.com/bundle/washingtondc-it-asset-management/page/product/software-asset-management2/concept/integrate-okta.html)
