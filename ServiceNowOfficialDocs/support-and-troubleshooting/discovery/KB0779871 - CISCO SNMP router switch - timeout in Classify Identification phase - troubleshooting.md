---
title: "CISCO SNMP router / switch - timeout in Classify/ Identification phase - troubleshooting"
aliases:
  - KB0779871
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0779871
kb_number: KB0779871
last_modified: 2024-04-07
---

## CISCO SNMP router / switch - timeout in Classify/ Identification phase - troubleshooting

  

### Issue

You might see:

Warning SNMP probe timed out. Target is either unreachable or there are no valid credentials for it. SNMP (empty) SNMP Classify w.x.y.z

Symptoms: Run discovery to switch or router get following error in discovery pattern log:  
2018-08-30 14:09:55: Error during walk from host xx.xxx.xx.xxx. TableEvent:-1. Error Message: Request timed out.  
2018-08-30 14:09:55: Failed to get SNMP scalar 1.3.6.1.2.1.4.1 from host xx.xxx.xx.xxx community: \*\*\*\*\*\*  
  

### Cause

snmp timeout  
  

### Resolution

Test the credential and whether it validates OK

Add following mid server parameters to higher value.  
mid.snmp.request.timeout  
mid.snmp.session.timeout  
  
"By default, they are 1500 millisecond. In my case, I have to increase to 6000 milliseconds in order to fix the issue."  
  
KB0712512 - Unable to discover switch or router with Identification engine error

From the Mid Server DEBUG processing the "Network Switch" pattern I can see the issue:  
  
09/16/19 15:06:25 (503) Worker-Standard:HorizontalDiscoveryProbe-be529be3db73bb00a5c7f69f2996193b DEBUG: (99)SNMPProviderImpl - Failed to get SNMP scalar 1.3.6.1.2.1.17.1.2 from host w.x.y.z USM User: null&#13;  
09/16/19 15:06:25 (503) Worker-Standard:HorizontalDiscoveryProbe-d1629be3db73bb00a5c7f69f2996192c SEVERE \*\*\* ERROR \*\*\* (107)SNMPProviderImpl - Error during walk from host w.x.y.z. TableEvent:-1. Error Message: Request timed out.&#13;  
  
Do an snmpwalk and notice the timeout for 1.3.6.1.2.1.17.1.2 from host w.x.y.z  
KB0696727 - MID Server SNMP Troubleshooting  
  
Further troubleshooting of the credential we found that if we reduced to AES128 we no longer saw the problem.  
  
There is a known issue regarding CISCO and AES256: PRB1348201 which is fixed in Madrid Patch 8, New York Patch 2, Orlando.  
The workaround is to use AES128 on the permission for CISCO Switch.
