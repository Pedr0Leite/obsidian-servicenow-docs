---
title: "When creating new Application Service for Service Mapping, \"Discoverable by Service Mapping\" option does not show up"
aliases:
  - KB0814653
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0814653
kb_number: KB0814653
last_modified: 2024-04-08
---

## When creating new Application Service for Service Mapping, "Discoverable by Service Mapping" option does not show up

  

### Issue

When creating new Application Service for Service Mapping, "Discoverable by Service Mapping" option does not show up.

Expected screen when creating new Application Service:

![](/sys_attachment.do?sys_id=38f768811b047414f34d33bc1d4bcb26)

Unexpected screen:

![](/sys_attachment.do?sys_id=bcf768811b047414f34d33bc1d4bcb27)

### Cause

Domain Separation must be configured on the affected instance, and your current user session is in a domain that has child domain.

As stated in below doc, the selected domain must be a domain without any child domains.

[Create entry point types for Service Mapping](https://docs.servicenow.com/csh?topicname=t_CreateEntryPoint.html&version=latest "Create entry point types for Service Mapping")

### Resolution

Please pick a domain that has no child domain as in the sample below:

![](/sys_attachment.do?sys_id=34f768811b047414f34d33bc1d4bcb29)
