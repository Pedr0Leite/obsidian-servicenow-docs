---
title: "vCenter discovery shows warning:  Active, couldn't classify: No WMI connec....."
aliases:
  - KB0696857
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0696857
kb_number: KB0696857
last_modified: 2025-01-03
---

## vCenter discovery shows warning: Active, couldn't classify: No WMI connec.....

  

### Issue

  

# Description

* * *

When discovering a vCenter system, if no Windows / SSH credential is provided, but there is valid VMware credential,

then once discovery completes, in the Discovery Status, under Devices tab, there is a warning:

"Active, couldn't classify: No WMI connec....."

This is expected.

The reason is that the "Completed activity" column on Devices tab (in the Discovery Status) only applies to the host, while vCenter is discovered as a running process / application instead of a host.

Thus, even if vCenter is successfully discovered, since the host is not discovered, the "Completed activity" column still shows "Active, couldn't classify: No WMI connec....."

# How to verify whether vCenter discovery is working when there is no host credential

* * *

When there is no host credential, but there is valid VMware credential, then once discovery completes, under Devices tab, the CMDB CI column shows the vCenter system discovered:

![](/sys_attachment.do?sys_id=068e7862db0ab450e515c2230596194e)

(Note if there is host credential, the CMDB CI will be the host system instead of the vCenter system)

On the other hand, when the VMware credential fails, the CMDB CI column is empty.

![](/sys_attachment.do?sys_id=468e7862db0ab450e515c22305961953) 

Additionally, if the VMware credential fails, under Discovery Log, there will be warning below:

![](/sys_attachment.do?sys_id=468e7862db0ab450e515c22305961958)

# Applicable Versions

* * *

Jakarta, Kingston
