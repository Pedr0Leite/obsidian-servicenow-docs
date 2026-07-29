---
title: "IBM HMC pattern does not get triggered"
aliases:
  - KB0788147
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0788147
kb_number: KB0788147
last_modified: 2025-08-07
---

## IBM HMC pattern does not get triggered

  

### Issue

When discovering an HMC Console, the initial "UNIX - Classify" returns HMC information. However, it is not triggering the associated HMC Horizontal Discovery Pattern.

### Release

All

### Cause

If one of the multiprobes, mainly the UNIX-OS probe, fails with some error then the discovery is not able to trigger the **IBM HMC Server** Pattern. 

### Resolution

Go to probe: UNIX - OS and under probe parameters, add a probe parameter "set\_path" value to 'false' (allow probe to alter the session's PATH variable or not. By default, during session setup, the PATH variable is set to /usr/sbin:/usr/bin:/bin:/sbin.Type: true | false . Default value: true).  
  
Once the parameter is added, run a quick discovery and you can see the HMC server getting discovered successfully.
