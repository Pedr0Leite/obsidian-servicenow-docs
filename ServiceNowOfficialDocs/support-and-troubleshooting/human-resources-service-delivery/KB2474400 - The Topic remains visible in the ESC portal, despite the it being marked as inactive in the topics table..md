---
title: "The Topic remains visible in the ESC portal, despite the it being marked as inactive in the topics table."
aliases:
  - KB2474400
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB2474400
kb_number: KB2474400
last_modified: 2025-09-01
---

## The Topic remains visible in the ESC portal, despite the it being marked as inactive in the topics table.

  

### Issue

The Topic remains visible in the ESC portal, despite the it being marked as inactive in the topics table.  
  

### Release

Not specific to the releases.

### Resolution

1\. Inspect the topic path in the XML of the topic to identify incorrect paths causing the issue. This ensures subsequent corrections are made to the correct path.

2\. Identify the incorrect path and import the XML file from working instance or make necessary changes directly to the topic record to correct the path. This requires attention to detail.

3\. Perform indexing again for both the catalog item table and knowledge table after making corrections. This ensures changes take effect and are reflected in the system.

4\. Log out and log back in to verify changes have taken effect and are not temporary. Finally, check if the topic is no longer visible in the ESC portal to confirm the issue is resolved.
