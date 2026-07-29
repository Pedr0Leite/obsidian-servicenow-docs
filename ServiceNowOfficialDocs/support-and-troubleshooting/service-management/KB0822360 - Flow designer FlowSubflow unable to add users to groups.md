---
title: "Flow designer Flow/Subflow unable to add users to groups"
aliases:
  - KB0822360
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0822360
kb_number: KB0822360
last_modified: 2025-12-08
---

## Issue

A Subflow can be used to function like an Active Directory process to add users to groups or assign roles.  
In the flow properties, it is configured to run as the system user, and unless the invoking user has an admin role, they will not be able to add users to groups or assign roles through this flow.

## Resolution

Because Scoped Roles are restricted and cannot be assigned by a system user, the flow properties will need to be changed from Run as 'System User' to Run as 'User who initiated the session'. This will resolve the issue and users can now be added to groups or be given roles using this Subflow.
