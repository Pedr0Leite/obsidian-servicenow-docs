---
title: "Discovery of Vyatta Open Source Routers"
aliases:
  - KB0716621
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0716621
kb_number: KB0716621
last_modified: 2024-08-28
---

## Discovery of Vyatta Open Source Routers

  

### Issue

# Symptoms

* * *

  
Vyatta Open Source Routers and Discovery 

### Release

ALL.

### Resolution

If your Vyatta Open Source Router responds to SNMP queries, you might as well be able to use ServiceNow discovery for discovering it. However, please ensure that you have the following- 

  
1\. The corresponding MIB file for your Vyatta device added on to your instance.   
2\. You have its OID(s) listed on the SNMP OID table on your instance.   
3\. The credentials for your Vyatta device listed under Discovery>Credentials.
