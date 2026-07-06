---
title: "Test failed: Failed to establish SNMP connection to host 10.xx.xx.xx. Check that host is accessible and correct credentials are defined error while discovering Load Balancer"
aliases:
  - KB0697383
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0697383
kb_number: KB0697383
last_modified: 2024-04-07
---

## Test failed: Failed to establish SNMP connection to host 10.xx.xx.xx. Check that host is accessible and correct credentials are defined error while discovering Load Balancer

  

### Issue

# Symptoms 

* * *

Whenever we discover the Alteon Load Balancer, the discovery is failing in Identification phase

* * *

# Cause

1.  We investigated this issue and we see that system is unable to connect to the device.  
    
2.  On running the Pattern Debug we see below error.  
      
    **Test failed: Failed to establish SNMP connection to host 10.xx.xx.xx. Check that host is accessible and correct credentials are defined.**  
      
    
3.  In the input payload of  Windows Identify step we see below.  
      
    <system oid="1.3.6.1.2.1.1">  
    <sysName oid="1.3.6.1.2.1.1.5" type="SnmpOctetString"/> >>> SysName is empty  
    <sysUpTime oid="1.3.6.1.2.1.1.3" type="SnmpTimeTicks">668229734</sysUpTime>  
    <sysDescr oid="1.3.6.1.2.1.1.1" type="SnmpOctetString">Alteon Application Switch 5208XL</sysDescr>  
    <sysObjectID oid="1.3.6.1.2.1.1.2" type="SnmpObjectId">.1.3.6.1.4.1.1872.1.13.3.10.1</sysObjectID> 
4.  The problem is identified with the value of SysName 

# Resolution

* * *

1.   In order to fix the issue, we worked with the Network Administration team and added the value if SysName at device level.
2.  After adding the value, we run the discovery and found that device is getting identified successfully.
