---
title: "Flows fail when initiated by a non-admin user"
aliases:
  - KB0823951
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0823951
kb_number: KB0823951
last_modified: 2026-01-05
---

## Flows fail when initiated by a non-admin user

  

### Issue

Flows initiated by non-admin users fail with the error "_Unable to load connection with alias ID <connection alias sys\_id>_"

### Release

All

### Cause

A flow can fail if the non-admin user who initates it does not have access to the http\_connection table where the flow is stored. 

### Resolution

Run the flow as a system user because the flow requires access to the connections and credentials.

In the Flow properties, set the **Run as** as the **System user**.
