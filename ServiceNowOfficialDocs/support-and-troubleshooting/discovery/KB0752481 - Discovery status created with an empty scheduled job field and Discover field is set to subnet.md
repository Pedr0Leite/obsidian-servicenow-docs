---
title: "Discovery status created with an empty scheduled job field and Discover field is set to subnet"
aliases:
  - KB0752481
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0752481
kb_number: KB0752481
last_modified: 2024-04-07
---

## Discovery status created with an empty scheduled job field and Discover field is set to subnet

  

### Issue

Discovery status created with an empty scheduled job field and Discover field is set to subnet as in the below screenshot.

![](sys_attachment.do?sys_id=dd6d60e2db82b450e515c22305961955)

  

### Cause

These discovery status are created by scheduled job "Subnet Discovery".  
  

```
https://<instance-name>.service-now.com/nav_to.do?uri=sysauto_script.do?sys_id=b969b06bdb213340e1c3c3af299619d3
```

  
This scheduled job calls the script include "SubnetAcceleratorManager" which triggers the subnet discoveries.  
  

```
https://<instance-name>.service-now.com/nav_to.do?uri=sys_script_include.do?sys_id=b28f1a37c3d20300e412bea192d3ae33
```

  
This below table has more information on the data collected in the discoveries.  
  

```
https://<instance-name>.service-now.com/automation_status_set_list.do 
```

### Resolution

Disable the scheduled job if you do not want the jobs to run.
