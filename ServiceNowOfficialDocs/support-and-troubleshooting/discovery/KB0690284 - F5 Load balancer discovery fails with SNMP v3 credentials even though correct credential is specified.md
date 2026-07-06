---
title: "F5 Load balancer discovery fails with SNMP v3 credentials even though correct credential is specified"
aliases:
  - KB0690284
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0690284
kb_number: KB0690284
last_modified: 2026-05-22
---

## F5 Load balancer discovery fails with SNMP v3 credentials even though correct credential is specified

  

### Issue

F5 load balancer discovery failing with the error 'SNMP probe timed out. Target is either unreachable or there are no valid credentials for it' in SNMP classify phase.

-   Credentials are valid
-   Increasing the SNMP probe timeout would not resolve the issue
-   Device is responding from the MID server

**Specific Error:**

"SNMP probe timed out. Target is either unreachable or there are no valid credentials for it."

### Release

Any

### Resolution

Check for SNMP v3 credential configuration on the device.

Set the OID configuration option to .1 to allow access to all OIDs instead of a specific OID. 

SNMP V3 agent access for F5 device:

[https://support.f5.com/csp/article/K13625](https://support.f5.com/csp/article/K13625)

### Related Links

[F5 Load Balancer REST identification pattern connection failure "HTTP request failed for credential with username"](https://support.servicenow.com/kb_view.do?sysparm_article=KB1429692 "F5 Load Balancer REST identification pattern connection failure \"HTTP request failed for credential with username\"")
