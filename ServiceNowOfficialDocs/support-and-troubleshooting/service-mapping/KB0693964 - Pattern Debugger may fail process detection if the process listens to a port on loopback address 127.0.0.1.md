---
title: "Pattern Debugger may fail process detection if the process listens to a port on loopback address 127.0.0.1"
aliases:
  - KB0693964
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0693964
kb_number: KB0693964
last_modified: 2026-05-22
---

## Pattern Debugger may fail process detection if the process listens to a port on loopback address 127.0.0.1

  

### Issue

The Pattern Debugger fails in process detection if the process listens to a port on 127.0.0.1

### Release

Any

### Resolution

In order to identify if the process listens to a port on 127.0.0.1. please follow the next steps: 

1.  Navigate to instanceName.service-now.com/**SaCmdManager.do**
2.  Run Command # **sudo netstat -lntup | grep process\_id**

If the target process listens to a port on 127.0.0.1. the '**Alternate Management IP**' option should be checked and add **127.0.0.1** and click Connect.
