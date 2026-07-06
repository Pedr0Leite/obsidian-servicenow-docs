---
title: "Discovery not populating IP address field for vCenter ESX server CIs"
aliases:
  - KB0750033
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0750033
kb_number: KB0750033
last_modified: 2025-07-30
---

## Discovery not populating IP address field for vCenter ESX server CIs

  

### Issue

vCenter Discovery runs successfully but some or all ESX server CIs do not get the IP Address field updated.

### Symptoms

IP Address field on ESX server CIs not updating after successful Discovery 

### Facts

DNS Lookup is required to allow vCenter Discovery to collect the IP address information from the ESX servers. 

### Release

All

### Cause

If DNS lookup is not active Discovery will be unable to discover the in use IP addresses and will not populate the IP Address field.  

This issue is commonly seen in DMZ environments where some resources do not respond to DNS lookups. 

### Resolution

DNS lookup must be allowed on CIs that you would like to discover as a pre-requisite for ESX host IP address collection.
