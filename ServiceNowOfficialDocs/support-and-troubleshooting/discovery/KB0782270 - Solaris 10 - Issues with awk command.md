---
title: "Solaris 10 - Issues with \"awk\" command"
aliases:
  - KB0782270
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0782270
kb_number: KB0782270
last_modified: 2024-04-08
---

## Solaris 10 - Issues with "awk" command

  

### Issue

Solaris 10 - Issues with "awk" command

### Cause

UNIX VERITAS cluster library pattern using awk instead of nawk.

### Resolution

Similar to how certain legacy probes swap between awk and nawk for Linux and Solaris devices respectively, the UNIX VERITAS Cluster library pattern was updated to use nawk when running on Solaris devices and awk for other varieties of UNIX.

### Related Links

PRB1368838 is assigned to our pattern development team to implement this as a permanent solution in a future patch.
