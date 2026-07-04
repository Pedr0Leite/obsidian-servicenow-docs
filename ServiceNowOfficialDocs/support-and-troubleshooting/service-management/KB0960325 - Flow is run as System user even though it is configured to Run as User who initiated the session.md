---
title: "Flow is run as \"System\" user even though it is configured to Run as \"User who initiated the session\""
aliases:
  - KB0960325
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0960325
kb_number: KB0960325
last_modified: 2025-07-09
---

## Flow is run as "System" user even though it is configured to Run as "User who initiated the session"

  

### Issue

When a Flow Designer flow is connected to a catalog, it does not take into account the specific user who made the request, even if the flow properties are configured to use the "User who initiated the session". Instead, the flow runs as the system user.

### Cause

When a user creates a record in out-of-the-box and the Stage on RITM changes to "request\_approved", the "Start FlowDesigner Flow" in the same transaction BR will be activated and it will create a sys\_flow\_context using the same user ID used to initiate the flow.

The reason for the flow running as the system user is due to the customization of the Service Catalog Request out-of-the-box workflow. This customization involves introducing a timer that pushes the context creation to the system user.

### Resolution

It is recommended removing this timer, as doing so will resolve the issue.
