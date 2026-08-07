---
title: "SNMP discovery may fail in classifaction and failing to get the sysObjectID or some OID related information during the classification even though we increase the timeout"
aliases:
  - KB0761047
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0761047
kb_number: KB0761047
last_modified: 2024-04-08
---

## SNMP discovery may fail in classifaction and failing to get the sysObjectID or some OID related information during the classification even though we increase the timeout

  

### Issue

Sometimes the SNMP related device (like switches, routers) discovery may fail in classification. And indeed it might be failing in getting the sysObjectID information. But if we run the "Test Probe" of the SNMPWalk then we may get the OID information with no issues.

### Release

All releases.

### Cause

-   Sometimes the data we are getting might be timed-out or messed-up.
-   There might be some latency or delay between the MID Server and the target device (especially with proxy) that might be causing the issue.

### Resolution

-   Increase the SNMP timeout by setting the properties as given in [SNMP parameters.](https://docs.servicenow.com/csh?topicname=r_SNMPProbeParameters.html&version=latest "SNMP parameters.")
-   If this did not work then try adding the the probe parameter [use\_getscalar](https://docs.servicenow.com/csh?topicname=r_SNMPProbeParameters.html&version=latest "use_getscalar") in "SNMP - Classify" probe. If you still find any issues try to increase the SNMP timeout and/or use [use\_getbulk](https://docs.servicenow.com/csh?topicname=r_SNMPProbeParameters.html&version=latest "use_getbulk").
-   Then add the OID (as in sysObjectID) in the OIDs table.
