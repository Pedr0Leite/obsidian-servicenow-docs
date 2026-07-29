---
title: "Unable to discover switch or router with Identification engine error"
aliases:
  - KB0712512
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0712512
kb_number: KB0712512
last_modified: 2024-04-07
---

## Unable to discover switch or router with Identification engine error

  

### Issue

# Symptoms

* * *

Run discovery to switch or router get following error in discovery pattern log:

Get ipForwarding flag  
2018-08-30 14:09:46: getting SNMP scalar 1.3.6.1.2.1.4.1 from xx.xxx.xx.xxx .Context: null/null  
2018-08-30 14:09:52: Error during walk from host xx.xxx.xx.xxx. TableEvent:-1. Error Message: Request timed out.  
2018-08-30 14:09:55: Error during walk from host xx.xxx.xx.xxx. TableEvent:-1. Error Message: Request timed out.  
2018-08-30 14:09:55: Failed to get SNMP scalar 1.3.6.1.2.1.4.1 from host xx.xxx.xx.xxx community: \*\*\*\*\*\*  
discovery  
2018-08-29 21:10:01:  
Check Processing Success  
2018-08-29 21:10:01: Identification Engine: Discovery status is FAILURE, unable to get error message.

Note: xx.xxx.xx.xxx is referring to device ip address

# Release

* * *

Kingston

# Cause

* * *

snmp timeout 

# Resolution

* * *

Add following mid server parameters to higher value.

mid.snmp.request.timeout   
mid.snmp.session.timeout

By default, they are 1500 millisecond. In my case, I have to increase to 6000 milliseconds in order to fix the issue.
