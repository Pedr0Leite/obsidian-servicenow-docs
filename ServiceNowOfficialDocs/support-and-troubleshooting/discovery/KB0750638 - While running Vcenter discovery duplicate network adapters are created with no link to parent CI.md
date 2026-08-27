---
title: "While running Vcenter discovery duplicate network adapters are created with no link to parent CI"
aliases:
  - KB0750638
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0750638
kb_number: KB0750638
last_modified: 2024-04-07
---

## While running Vcenter discovery duplicate network adapters are created with no link to parent CI

  

### Issue

# Symptoms

While running Vcenter discovery duplicate network adapters are created with no link to parent CI.

Discovery log warnings:

Multiple Guest CI's existing on this VM instance. serial\_number 42 12 8e 43 32 ab 3c xx xx xx xx xx, Mac addresses: 00:50:5X:XX:e9:8f 

# Release

All releases

# Steps to reproduce

01) Run a Vcenter discovery.

02) Check if it is creating duplicate records in the table \[cmdb\_ci\_vmware\_nic\] with no configuration item record.

03) Also check if you have below error messages from the discovery logs.

Multiple Guest CI's existing on this VM instance. serial\_number 42 12 8e 43 32 ab 3c xx xx xx xx xx, Mac addresses: 00:50:5X:XX:e9:8f 

# Cause

The issue is caused due to the existing duplicate records in the \[cmdb\_ci\_computer\] table & empty mac\_address field in the computer CI record. 

The script include VmwareVmCorrelator below handles this logic:  
/sys\_script\_include.do?sys\_id=8dddde336730120072b9f06943415ad8   
  
  
Read script lines: //282 to 290   
if (JSUtil.nil(guestCiSysId))   
return;   
  
if (duplicateCIs.length > 1)   
throw {   
"error": "VMCorrelator.DuplicateGuestsFound",   
"msg": "Multiple Guest CI's existing on this VM instance. serial\_number " + serial + ", Mac addresses: " + macs,   
"duplicateCis": duplicateCIs   
};   
  
Investigating further, discovery is considering duplicateCIs in the table (cmdb\_ci\_computer).   
  
Script lines : //244 to 246   
var guestGr = new GlideRecord('cmdb\_ci\_computer');   
guestGr.addQuery('serial\_number', \['zone-' + serial, 'vmware-' + serial\]);   
guestGr.query(); 

# Resolution

To resolve the issue, make sure that you don't have any duplicates in the computer records with empty MAC address records.
