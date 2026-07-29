---
title: "Troubleshooting Solaris Pattern Discovery: Global Zone Host Address Error"
aliases:
  - KB0749069
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0749069
kb_number: KB0749069
last_modified: 2025-07-30
---

## Troubleshooting Solaris Pattern Discovery: Global Zone Host Address Error

  

### Issue

Pattern discovery fails with the error message: "Solaris global zone host/address of local zone need to be discovered first. Please run quick discovery on this IP and try again." 

### Symptoms

-   Pattern discovery process stops unexpectedly
-   Error message appears during application discovery on Solaris systems
-   Discovery logs show global zone detection failures

### Release

All currently supported releases.

### Cause

Pattern discovery uses process detection to find applications on your system. Solaris systems require extra logic because they use both global and local zones.

-   The system needs to decide where to run commands (global zone versus local zone)
-   The system triggers this error when it cannot find a process in the global zone
-   Solaris systems make multiple attempts to collect process information, so discovery may still succeed

### Resolution

1\. Review your pattern discovery logs for successful detection results. If found, disregard this error message.

2\. Resolve the errors found in the process detection. Steps to resolve depend on the error returned.

3\. Set the MID Server property mid.solaris.use\_netstat\_u\_param to **true**.

If the error is not resolved, contact Support for further troubleshooting.
