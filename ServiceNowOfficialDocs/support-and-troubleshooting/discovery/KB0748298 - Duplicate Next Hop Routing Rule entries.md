---
title: "Duplicate Next Hop Routing Rule entries"
aliases:
  - KB0748298
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0748298
kb_number: KB0748298
last_modified: 2024-11-14
---

## Duplicate Next Hop Routing Rule entries

  

### Issue

# Symptoms

Duplicate Next Hop Routing Rule entries

# Cause

The "SNMP - Routing" Probe is being triggered together with the pattern Network Router pattern. The pattern also collects this data, and when this happens, both of them keep creating the duplicates. 

Our documentation says it is ok:  
[https://docs.servicenow.com/csh?topicname=r\_DataCollDiscoNWRouteAndSwitch.html&version=latest](https://docs.servicenow.com/csh?topicname=r_DataCollDiscoNWRouteAndSwitch.html&version=latest)   
  
However, this has been seen a few times.

# Resolution

Option 1:

01) Disable the following probe:   
https://<instance-name>.service-now.com/discovery\_classifier\_probe\_list.do?sysparm\_query=child.nameLIKERouting   
02) Delete test CI with its associated data.   
03) Run test discoveries to confirm no more duplicates are created. 

Option 2:

01) Disable the SNMP Fields on the SNMP - Routing Probe:  
https://<instance-name>.service-now.com/discovery\_probes\_snmp.do?sys\_id=a2bada940a0a0b6100d5e020a828fdeb  
02) Delete test CI with its associated data.   
03) Run test discoveries to confirm no more duplicates are created.
