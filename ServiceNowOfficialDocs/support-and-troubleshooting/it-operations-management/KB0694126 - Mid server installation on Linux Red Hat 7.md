---
title: "Mid server installation on Linux Red Hat 7"
aliases:
  - KB0694126
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0694126
kb_number: KB0694126
last_modified: 2024-04-07
---

## Mid server installation on Linux Red Hat 7

  

### Issue

# Mid server installation on Linux Red Hat 7

* * *

Installing a MID Server on Red Hat 7 had issues that were resolved in ServiceNow's London version .

Running mid server command agent/bin/mid.sh install in RHEL created a softlink in init.d to the mid.sh file wherever it is located.

However RHEL uses systemd instead of sysvinit. Systemd only allows softlinks in init.d to point to the /(root) or /usr filesystems.
