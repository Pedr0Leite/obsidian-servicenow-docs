---
title: "\"Is Virtual\" flag is not set for virtual machine CI record"
aliases:
  - KB0748509
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0748509
kb_number: KB0748509
last_modified: 2026-05-04
---

## "Is Virtual" flag is not set for virtual machine CI record

  

### Issue

The CI record of a virtual machine does not have "Is Virtual" flag set.

### Release

All

### Resolution

To troubleshoot the reason behind this, you will need to follow the below steps:

1- First, check if the VM should have the flag set. Out of the box, we set "Is Virtual" flag for the following types:

-   **Amazon AWS VM**: This is set through the AWS Cloud Management discovery and the population of the relationships
-   **Azure VM**: This is set through Azure Cloud Management discovery and the population of the relationships
-   **SolarisZone**: Through 'Virtual Computer Check' Business Rule
-   **HyperV**: Through 'Virtual Computer Check' Business Rule
-   **VMware**: Through 'Virtual Computer Check' Business Rule

Business rule (BR):  
https://<instance-name>.service-now.com/nav\_to.do?uri=sys\_script.do?sys\_id=dd6ea51f0a0a0b7800561c3567d869bf

2- Now, if the VM is one of the types checked by the BR:

-   Make sure that the conditions for running the BR are met. It is triggered if:

current.serial\_number.changes() || current.serial\_number.hasValue() || current.correlation\_id.changes() || current.correlation\_id.hasValue() || current.ip\_address.changes() || current.ip\_address.hasValue()

-   If the above conditions are met, then check the conditions for setting each VM type to virtual as follows:
    -   For **SolarisZone:** The CI needs to have a serial\_number that starts with **"zone-"**
    -   For **VMware:** The CI needs to have a serial\_number that starts with **"vmware-"**
    -   For **HyperV:** The serial number/s of the VM must match the serial number/s of the discovered HyperV instance/s
