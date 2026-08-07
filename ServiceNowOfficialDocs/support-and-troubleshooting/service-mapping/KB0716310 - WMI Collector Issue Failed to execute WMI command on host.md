---
title: "WMI Collector Issue: Failed to execute WMI command on host"
aliases:
  - KB0716310
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0716310
kb_number: KB0716310
last_modified: 2025-02-14
---

## WMI Collector Issue: Failed to execute WMI command on host

  

### Issue

Exception thrown: Failed to execute WMI command on host

### Release

All

### Cause

1.  WMI Collector by default communicates on port 8585.
2.  The traffic on this port should be allowed on the mid server host.
3.  Further, the target server should be able to receive the traffic.

### Resolution

1.  In this case, the wmi collector was running on port 8585 as configured on the mid server host.
2.  On the target host, the traffic was blocked due to firewall rules configured.
3.  After allowing the traffic on the target host, service mapping discovery completed successfully.
4.  The issue was identified by monitoring the network traffic between the mid server and target host.
