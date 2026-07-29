---
title: "Possible reasons to explain why a CI name is not updating correctly even though the correct name is in the payload."
aliases:
  - KB0782058
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0782058
kb_number: KB0782058
last_modified: 2024-04-08
---

## Possible reasons to explain why a CI name is not updating correctly even though the correct name is in the payload.

  

### Issue

There can be a few reasons as to why the name of a CI is not updated as expected after discovery, even though the payload has the correct host name. Please review the below possible causes:

### Cause

1.  Check if there are any reconciliation rules defined for the name field of the CI class using "CI Class Manager"
2.  Review the system properties for the following properties to make sure they are not preventing the host name from being updated:
    -   glide.discovery.hostname.always\_update
    -   glide.discovery.hostname.dns\_nbt\_trusted
    -   glide.discovery.hostname.wmi\_trusted
    -   glide.discovery.hostname.snmp\_trusted
    -   glide.discovery.hostname.ssh\_trusted
3.  Check the CMDB table to make sure there are no custom business rules which could prevent the name from being updated. Sometimes, customers create a business rule to prevent duplicate CI names. 

### Resolution

Please review the above information for possible causes to investigate the issue.
