---
title: "SFTP import fails with error \"java.io.IOException: SSH authentication failed, Timed out while waiting for TCP to connect\""
aliases:
  - KB0724520
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0724520
kb_number: KB0724520
last_modified: 2026-08-25
---

## SFTP import fails with error "java.io.IOException: SSH authentication failed, Timed out while waiting for TCP to connect"

  

### Issue

SFTP type data source fails to import and throws the error:

java.io.IOException: SSH authentication failed, Timed out while waiting for TCP to connect

### Cause

This happens when the SFTP server or the firewall before this blocks the source IPs from which the SFTP connection is initiated.

### Resolution

1.  Obtain the IP information for your instance by following the steps provided in the KB "[Finding the IP information for your instance](https://support.servicenow.com/kb_view.do?sysparm_article=KB0538621)".
2.  Share the two IP ranges (both Datacenters) specified for "Source address used for integrations into customer network with NO VPN" with your network/firewall admin to have them in the allow list.
