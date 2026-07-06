---
title: "Virtualized relationships not being updated on the server record when VM-instance is moved to different ESX server"
aliases:
  - KB0718102
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0718102
kb_number: KB0718102
last_modified: 2024-04-07
---

## Virtualized relationships not being updated on the server record when VM-instance is moved to different ESX server

  

### Issue

# Symptoms

* * *

Virtualized relationship between the server and Hypervisor(ESX) not being updated when the VMware instance moves from one ESX to other.

# Release

* * *

All releases

# Cause

* * *

\-"Virtual Computer check" is the business rule that is responsible for creating these virtualized relationships between the server and the ESX host. This business rule will run only when the record is inserted or when the serial number changes. When the VM instance moves from one instance to the other, none of these conditions will be satisfied and the business rule logic to correct the Server to VM instance relationship will not be triggered.

\-Registered on relationship will be updated when discovery is re-run on the Vcenter and this will update the relationship between vm-instance and ESX. But the virtualized relationship is not touched here as the business rule will be run on the cmdb\_ci\_computer record when discovered via Ip address. 

// only process rec if just inserted or serial\_number changed AND serial\_number is non-nil

if (!(current.serial\_number.changes() && JSUtil.notNil(current.serial\_number)))

# Resolution

* * *

\-Navigate to business rule "Virtual Computer Check", modify the condition from

if (!(current.serial\_number.changes() && JSUtil.notNil(current.serial\_number)))

to

if (!(JSUtil.notNil(current.serial\_number)))

\-Re-run the discovery on the Ip address and this will correct the relationship between the Server and Hypervisor(ESX)
