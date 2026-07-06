---
title: "Discover IBM HMC server return \"Active, couldn't classify\""
aliases:
  - KB0787098
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0787098
kb_number: KB0787098
last_modified: 2024-04-08
---

## Discover IBM HMC server return "Active, couldn't classify"

  

### Issue

Discover IBM HMC server return "Active, couldn't classify"

### Cause

ECC queue input for "UNIX - Classify"  
<results probe\_time="556" result\_code="0" warn="/bin/bash: PATH: readonly variable ">  
<result warn="/bin/bash: PATH: readonly variable ">  
<output>/bin/bash: line 6: vmware: command not found</output>  
</result>  
  
Because of this error, it failed in Unix classification.

### Resolution

Added the probe parameter "set\_path" to "false" in the "UNIX - OS"  
https://<INSTANCE\_NAME>.service-now.com/nav\_to.do?uri=discovery\_probes.do?sys\_id=e5e075a2a9fe1561018f2a9636d5ec39  
  
![](sys_attachment.do?sys_id=8a337ff8db8478d066e0a345ca961978)
