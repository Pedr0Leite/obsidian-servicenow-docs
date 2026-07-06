---
title: "MID Server Auto-Assign IP Ranges does not populate IP Range Assignment records after initial Scan"
aliases:
  - KB0677220
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0677220
kb_number: KB0677220
last_modified: 2024-04-07
---

## MID Server Auto-Assign IP Ranges does not populate IP Range Assignment records after initial Scan

  

### Issue

MID Server Auto-Assign IP Ranges doesn't populate IP Range Assignment records after initial Scan

  
  

# Issue

* * *

Auto-Assign IP Range is a new feature introduced in Jakarta to automatically discover available IP Ranges for a MID server. However, people may find this functionality works for the 1st time but in later scans it cannot populate records in IP Range Assignment tab.

# Cause

* * *

When Auto Assignment Discovery runs, it will first discovery all the subnets. The discovered subnets can be seen in the Identified Subnets tab in a Automation Status Set record. Then it checks which subnets are not part of MID server IP ranges. MID server IP ranges can be seen in the IP Ranges tab in a MID server record. For the subnets which are not part of MID server IP ranges, they appear in AutoConfig Queue tab in a Automation Status Set record. And Discovery only tries for those subnets. If the MID server can reach any host in the subnet, Discovery marks this subnet as reachable subnet and assign it to MID server IP Ranges. If no host in the subnet is reachable then Discovery marks the subnet as unreachable subnet and not assign it to MID Server IP Ranges. 

# Solution

* * *

This is an expected result by design. The algorithm works in a way that if any identified subnet is part of MID server IP Ranges, it is not tried by Auto Assignment again.
