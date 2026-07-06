---
title: "\"Network Switch\" Discovery pattern throws \"Abandoned due to too many errors\""
aliases:
  - KB0726444
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0726444
kb_number: KB0726444
last_modified: 2024-04-07
---

## Issue

# Symptoms

* * *

 "Network Switch" Discovery pattern throws "Abandoned due to too many errors" caused by duplicate Related items

# Release

* * *

Kingston patch 11 and lower

London Patch 4 and lower

# Environment

* * *

Network Switches, Layer 2 Discovery

# Cause

* * *

 The pattern library 'SNMP - CDP and LLDP' may get identification errors because of duplicated neighbor\_id for discovery\_device\_neighbors 

\=> In system logs, found identification error: identification\_engine : DUPLICATE\_RELATED\_PAYLOAD Found duplicate Related items (<integer> and <integer>) in the payload index <integer> using fields neighbor\_id,neighbor\_source 

\=> Discovery pattern log. Note the message contains "Found duplicate Related items (<integer> and <integer) in the payload index <integer> using fields neighbor\_id,neighbor\_source"

<date/time stamp>: Identification CI Errors:   
Abandoned due to too many errors,Abandoned due to too many errors,Abandoned due to too many errors,Abandoned due to too many errors,Abandoned due to too many errors,Abandoned due to too many errors,Abandoned due to too many errors,Abandoned due to too many errors,Abandoned due to too many errors,Abandoned due to too many errors,Abandoned due to too many errors,Abandoned due to too many errors,Abandoned due to too many errors,Found duplicate Related items (0 and 2) in the payload index 13 using fields neighbor\_id,neighbor\_source,

  
\=> In the Pattern debug, checked the variable table cdpCacheTable, there seems to be two records with the same localIfIndex value for neighbor\_id (<neighbor name). See attached screenshot.   
  
\=> The issue is also seen in cases where there are LAG interfaces.   
For example, if one of the interface discovered is actually a port-channel (LAG = Link Aggregation), which is a virtual port combining multiple physical ports, a router interface probably gets multiple CDP updates from both the physical port it is connected to and the virtual one (LAG interface). This results in a payload that appears to contain the same neighbor\_id and neighbor\_source and if the neighbor\_interface has not yet been discovered, discovery can fail as identification engine thinks the entries are duplicate. 

# Resolution

* * *

PRB1307721
