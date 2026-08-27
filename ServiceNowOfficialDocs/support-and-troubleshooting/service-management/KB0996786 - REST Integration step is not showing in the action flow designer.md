---
title: "REST Integration step is not showing in the action flow designer"
aliases:
  - KB0996786
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0996786
kb_number: KB0996786
last_modified: 2025-01-02
---

## Issue

Getting an error "To enable Action steps for integrations, the IntegrationHub plugin is required" when trying to create an action flow with a REST integration steps, although the IntegrationHub plugin is activated.

![](sys_attachment.do?sys_id=1a42da67db7eb05480073ca8f4961913)

## Resolution

Check if any of the below IntegrationHub Installer packs are present.

-   ServiceNow IntegrationHub Starter Pack Installer \[com.glide.hub.integrations\]
-   ServiceNow IntegrationHub Standard Pack Installer \[com.glide.hub.integrations.standard\]
-   ServiceNow IntegrationHub Professional Pack Installer \[com.glide.hub.integrations.professional\]
-   ServiceNow IntegrationHub Enterprise Pack Installer \[com.glide.hub.integrations.enterprise\]

If none of the installer packs are available, please raise a new request for activating any of the above IntegrationHub Starter pack based on your business requirement.

Also check the following document which has a detailed explanation on [IntegrationHub installer packs.](https://docs.servicenow.com/bundle/quebec-servicenow-platform/page/administer/flow-designer/concept/request-ih-overview.html?cshalt=yes "IntegrationHub installer packs")

## Additional Information

KB on Plugin Activation overview <https://support.servicenow.com/kb?id=kb\_article\_view&sysparm\_article=KB0695388>
