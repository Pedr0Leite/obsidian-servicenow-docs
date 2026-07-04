---
title: "Confluence Cloud Integration Profile Link Missing"
aliases:
  - KB0993112
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0993112
kb_number: KB0993112
last_modified: 2024-08-28
---

## Confluence Cloud Integration Profile Link Missing

  

### Issue

When setting up a SaaS Integration Profile following steps outlined in ["Integrating with Confluence Cloud"](https://docs.servicenow.com/bundle/quebec-it-asset-management/page/product/software-asset-management2/concept/integrate-with-confluence-cloud.html "\"Integrating with Confluence Cloud\""), you cannot find the Confluence Cloud Integration Profile from the choice list. 

The Procedure section on ["Integrating with Confluence Cloud"](https://docs.servicenow.com/bundle/quebec-it-asset-management/page/product/software-asset-management2/concept/integrate-with-confluence-cloud.html "\"Integrating with Confluence Cloud\"") outlines the step to create the integration profile:

**From your ServiceNow instance, navigate to SaaS License > Administration > Direct Integration Profiles and then click New.**  
**Select Confluence Cloud Integration Profile.**

But you cannot find the Confluence profile from the choice list:

![](sys_attachment.do?sys_id=a5c89f6adb69bc10f77799ead396196e)

### Release

All current release from Quebec

### Cause

The Confluence SaaS Integration is part of a store release and was introduced from version 4.0.0.  In this case, the current store application version installed in the instance is 2.0.0.  Please refer to the product release notes [here](https://docs.servicenow.com/bundle/store-release-notes/page/release-notes/store/it-asset-management/store-rn-itam-sam-saas-license-mgmt-integrations.html "here").

### Resolution

Store Applications are not normally included in your Instance platform upgrades. These applications needs to be manually updated. Please check this [link](https://docs.servicenow.com/bundle/quebec-application-development/page/build/applications/task/t_InstallUpdates.html "link") about how to update Store Applications. Search for "Software Asset Management - SaaS License Management Integrations", there may be two records, please choose the one where it indicates "Store" in the lower right-hand corner. Choose any version from 4.0.0 Q to 5.0.2 Q. Then click update.

Note this may apply to other Integration Profiles that are missing.  Always check the release notes [here.](https://docs.servicenow.com/bundle/store-release-notes/page/release-notes/store/it-asset-management/store-rn-itam-sam-saas-license-mgmt-integrations.html "here.")
