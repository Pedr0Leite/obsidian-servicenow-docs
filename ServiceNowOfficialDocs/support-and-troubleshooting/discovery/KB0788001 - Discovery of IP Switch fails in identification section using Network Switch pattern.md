---
title: "Discovery of IP Switch fails in identification section using Network Switch pattern"
aliases:
  - KB0788001
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0788001
kb_number: KB0788001
last_modified: 2026-06-12
---

## Discovery of IP Switch fails in identification section using Network Switch pattern

  

### Issue

Discovery fails during the identification phase of the Network Switch pattern. The following error appears in the Discovery Pattern Log:

```
Identification Engine: Discovery status is FAILURE, Identification sections in pattern failed: section: discovery, error: SNMP table query failed on host.
```

The Check Processing Success step fails, preventing the switch from being discovered and added to the CMDB

### Release

ALL Release

### Cause

The MID Server's SNMP request timeout value is too low for the switch to respond within the allocated time. The default timeout may be insufficient for switches with high latency or heavy load.

### Resolution

-   Log in to the ServiceNow instance with administrator privileges.
-   Navigate to MID Servers in the left navigator.
-   Select the MID Server used for Discovery.
-   In the Related Links section, select MID Server Properties.
-   Select New to add a new parameter.
-   In the Property field, enter: `mid.snmp.request.timeout`
-   In the Value field, enter: `30000` (milliseconds, which equals 30 seconds).
-   Select Save.
-   Restart the MID Server service:
    -   Navigate to MID Servers.
    -   Select the MID Server.
    -   Select Restart MID Server (or restart the service manually on the host system).
-   Wait 2–5 minutes for the MID Server to restart and reconnect.
