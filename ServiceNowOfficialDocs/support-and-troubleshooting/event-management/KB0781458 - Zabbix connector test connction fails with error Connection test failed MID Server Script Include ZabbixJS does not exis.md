---
title: "Zabbix connector test connction fails with error: Connection test failed: MID Server Script Include ZabbixJS does not existCredentials not found, id: <SYS ID> Caused by error in JavaScript probe 'ZabbixJS' at line 1"
aliases:
  - KB0781458
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0781458
kb_number: KB0781458
last_modified: 2024-04-07
---

## Zabbix connector test connction fails with error: Connection test failed: MID Server Script Include ZabbixJS does not existCredentials not found, id: Caused by error in JavaScript probe 'ZabbixJS' at line 1

  

### Issue

Test connector on the Zabbix connector instance fails with below error

Connection test failed: MID Server Script Include ZabbixJS doesn't exist Credentials not found, id: <SYS ID> by the error in JavaScript probe 'ZabbixJS' at line 1

### Release

Any

### Cause

Custom Zabbix Mid script include and a corrupted credential record.

### Resolution

Issue 1: MID Server Script Include ZabbixJS does not exist

Make sure the ZabbixJS script include is not customized, sometimes it may be customized or else recreated with the same name. In that case, import the OOB script include and this should resolve the first part of the issue:

MID Server Script Include ZabbixJS does not exist  
  
  

Issue 2:Credentials not found, id: <SYS ID> by error in JavaScript probe 'ZabbixJS' at line 1

It looks like the credential record is corrupted and so try recreating the credentials again.
