---
title: "Connect multiple Microsoft Dynamics tenants using integration profiles in SAM Pro"
aliases:
  - KB2651615
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB2651615
kb_number: KB2651615
last_modified: 2026-05-21
---

## Connect multiple Microsoft Dynamics tenants using integration profiles in SAM Pro

  

### Issue

Resolve an issue in which a second Connection & Credential record cannot be added to the same integration profile when connecting to multiple Microsoft Dynamics tenants in SAM Pro.

### Release

Any

### Resolution

Adding multiple Connection & Credential records to the same integration profile is not supported in the base system.

To connect to multiple Microsoft Dynamics tenants, create a separate integration profile for each tenant. Use child aliases to manage different configurations — such as client ID and client secret — for each profile.For steps to create a child alias and set up multiple integration profiles, see the Related Links section.

  
  

### Related Links

-   [Integrate SAM Pro with Microsoft 365](https://www.servicenow.com/docs/r/zurich/it-asset-management/saas-license-management/integrating-with-microsoft365.html)
-   [Create a child alias to set up multiple integration profiles in SAM Pro](https://www.servicenow.com/docs/r/zurich/it-asset-management/saas-license-management/create-child-alias-saas.html)
