---
title: "SNMP Switch Discovery Schedule- In few cases makes multiple updates  on IP address and class fields"
aliases:
  - KB0755296
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0755296
kb_number: KB0755296
last_modified: 2024-04-07
---

## SNMP Switch Discovery Schedule- In few cases makes multiple updates on IP address and class fields

  

### Issue

# Symptoms

The IP address and class (sometimes) field changes multiple times while running a discovery schedule for IP switches/ Routers

# Release

Any

# Cause

If all the ports on a switch are open for port 161, in that case, that switch will have multiple IPs (one for each port) but serial number for all the ports will be the same.

And as per OOB CI identifier: Hardware rule, CI identification is performed based on Serial number and so the same record will be updated every time instead of creating a new record.

Let's say we have a switch with serial number: 123, name: XYZ and having 10 ports (each port has a different IP, each port has port 161 SNMP open and few of them might have routing capabilities).   
We are having a discovery schedule over a specific IP range and all these 10 ports fall in this range, when discovery runs on port 1 it will create a record in the CMDB with   
  
Name:xyz,serial:123 and class: IP switch, IP: x.x.x.1   
  
During the same time, discovery sends commands to port 2 (Which has routing capability) of the same switch and this returns data as below   
  
Name: xyz, serial:123 and class: IP router, IP:x.x.x.2   
  
As per the identifier rule, CI identification looks for the serial number and since there is an existing record in the CMDB with that serial it will update that record and so the record in the CMDB will be updated from   
  
Name:xyz,serial:123 and class: IP switch, IP: x.x.x.1   
  
to   
  
Name: xyz, serial:123 and class: IP router, IP:x.x.x.2   
  
Similarly, if we have multiple ports for that switch with port 161 open the IP address and class for that record keeps on changing. 

# Resolution

Make sure we have only one port open on the IP switch for port 161.
