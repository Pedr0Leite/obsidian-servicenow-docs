---
title: "Incident closed with \"Knowledge\" checked, but no knowledge article was created"
aliases:
  - KB0715926
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0715926
kb_number: KB0715926
last_modified: 2024-04-07
---

## Incident closed with "Knowledge" checked, but no knowledge article was created

  

### Issue

An incident was closed with "Knowledge" check-box checked, yet no new knowledge article was created in "draft" state

### Release

Kingston Patch 7

### Cause

The user who closed the incident did so via an e-mail response. Therefore, this is expected, OOB (Out of Box) behavior.

### Resolution

As mentioned above, the behavior seen is the same in an OOB (Out of Box) instance. When an incident is closed via an e-mail response, even with "Knowledge" checked, no new knowledge article will be created.  
  
To avoid this behavior, the user who is closing the incident should be at a desktop or laptop and logged in and authenticated to the Platform. Then they can manually close out the incident and the expected knowledge article will be created.

#
