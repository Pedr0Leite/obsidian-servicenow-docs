---
title: "Enable JSON coding of Shazzam payloads for upgraded instances to prevent out of memory issues"
aliases:
  - KB0687626
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0687626
kb_number: KB0687626
last_modified: 2025-01-03
---

## Enable JSON coding of Shazzam payloads for upgraded instances to prevent out of memory issues

  

### Issue

The **glide.discovery.shazzam\_ranges\_json** system property in the London release converts Shazzam payloads into JSON strings, which dramatically reduces their size. When enabled, this property prevents nodes from running out of memory when a single schedule discovers large numbers of IP ranges. In upgraded instances, starting prior to the versions below, this property is set to **false** and is not visible in the sys\_properties table:

-   London
-   Kingston Patch 6
-   Jakarta Patch 9

To enable JSON coding for Shazzam payloads in an upgraded instance, import the update set attached to this article. The update set configures the following:

-   Adds the **glide.discovery.shazzam\_ranges\_json** property to the sys\_properties table.
-   Sets the property value to **true**.
-   Exposes the property in the **Discovery Definition > Properties** module.
