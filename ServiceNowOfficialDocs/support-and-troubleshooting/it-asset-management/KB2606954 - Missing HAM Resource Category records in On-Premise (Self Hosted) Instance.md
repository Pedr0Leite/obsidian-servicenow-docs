---
title: "Missing HAM Resource Category records in On-Premise (Self Hosted) Instance"
aliases:
  - KB2606954
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB2606954
kb_number: KB2606954
last_modified: 2026-05-12
---

## Missing HAM Resource Category records in On-Premise (Self Hosted) Instance

  

### Issue

There are no visible records on the HAM Resource Categories \[sn\_hamp\_resource\_category\] table on a On-Premise (Self Hosted) instance.

### Symptoms

-   By default for a particular resource category, the normalization functions for its associated models and the asset actions for its associated assets don't work.
-   To use the normalization functions and asset actions, customers have to opt in that resource category.
-   Without access to the resource category records, customers are unable to opt in and the normalization functions won't work.

### Facts

Self Hosted On-Premise instances need to set a comma separated list of the HAM entitlement names associated to their SKUs to the value of System Property **sn\_hamp.sn\_ham\_active\_entitlements.**

Admins can update this system property with a comma separated list of entitlements for which you have access.

The comma separated entitlements should be updated in the following format:

-   End User Computers- **ham\_computer\_license**
-   Mobile Device- **ham\_mobiledevice\_license**
-   Servers- **ham\_server\_license**
-   Network Gear- **ham\_networkgear\_license**
-   Monitors- **ham\_monitor\_license**
-   Storage- **ham\_storage\_license**
-   Printer- **ham\_printer\_license**
-   Telecom Network Inventory- **ham\_tni\_license**

### Release

All Releases

### Cause

System Property **sn\_hamp.sn\_ham\_active\_entitlements** is empty and does not list the HAM entitlement names.

### Resolution

Set a comma separated list of the HAM entitlement names associated to their SKUs to the value of System Property **sn\_hamp.sn\_ham\_active\_entitlements**

**Procedure**

**1.** Navigate to the **System Properties \[sys\_properties\]** table.

**2.** Open the record for System Property **sn\_hamp.sn\_ham\_active\_entitlements.**

**3.** Set a comma separated list of **HAM entitlement names that you're entitled to** in the property's Value field.

**Example:**

ham\_mobiledevice\_license,ham\_computer\_license,ham\_server\_license,ham\_networkgear\_license,ham\_monitor\_license,ham\_storage\_license,ham\_printer\_license,ham\_hardware\_license

**4.** **Save** the record

### Related Links

**Hardware Asset Management licensing**

[https://www.servicenow.com/docs/csh?topicname=ham-licensing.html&version=latest](https://www.servicenow.com/docs/csh?topicname=ham-licensing.html&version=latest)
