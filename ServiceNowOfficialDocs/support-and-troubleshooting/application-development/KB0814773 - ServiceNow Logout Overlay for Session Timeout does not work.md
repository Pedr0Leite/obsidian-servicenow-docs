---
title: "ServiceNow Logout Overlay for Session Timeout does not work"
aliases:
  - KB0814773
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0814773
kb_number: KB0814773
last_modified: 2024-04-08
---

## ServiceNow Logout Overlay for Session Timeout does not work

  

### Issue

Logout Overlay style property (glide.amb.session.logout.overlay.style) introduced in Orlando release is not working.

[https://docs.servicenow.com/csh?topicname=platform-security-rn.html&version=latest](https://docs.servicenow.com/csh?topicname=platform-security-rn.html&version=latest)

### Release

Orlando and forward

### Cause

The instance has Single Sign On (SSO) enabled

### Resolution

The Overlay feature will not work with instances that have SSO enabled, this is working as expected.
