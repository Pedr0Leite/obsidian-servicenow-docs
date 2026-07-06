---
title: "Unable to classify pfSense firewall devices correctly because of EMC Isilon classification"
aliases:
  - KB0761173
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0761173
kb_number: KB0761173
last_modified: 2024-04-08
---

## Unable to classify pfSense firewall devices correctly because of EMC Isilon classification

  

### Issue

Out of box, the EMC Isilon storage servers use the OID of 1.3.6.1.4.1.12325.1.1.2.1.1.

If you are creating a classification for pfSense firewalls, you may find that those devices have the same OID as the above classification. This can cause discovery to run the wrong patterns due to incorrect classification of the pfSense firewall and vice versa.

### Cause

The EMC Isilon and the pfSense firewall both share the same OID as configured by their respective manufacturers.

OID: 1.3.6.1.4.1.12325.1.1.2.1.1  
  

### Resolution

Our developers have investigated this issue and confirmed that the EMC Isilon devices return the OID of "1.3.6.1.4.1.12325.1.1.2.1.1" during discovery.

Our devs have decided against changing the the out of box OID classification for EMC Isilon because it will affect other customer's who are using discovery for that device with those OIDs.

The only way to truly resolve this problem is for the publishers (EMC and owners of pfSense) to make the OIDs unique.  
  
This means that if you are in a situation where the OID for EMC Isilon devices and the pfSense firewall that you are using have the same OID you will need to disable the classification for EMC Isilon if you want to correctly discover your pfSense firewall.
