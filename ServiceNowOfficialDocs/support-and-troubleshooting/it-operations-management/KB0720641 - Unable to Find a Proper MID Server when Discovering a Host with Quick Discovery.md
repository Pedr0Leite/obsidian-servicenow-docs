---
title: "Unable to Find a Proper MID Server when Discovering a Host with Quick Discovery"
aliases:
  - KB0720641
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0720641
kb_number: KB0720641
last_modified: 2024-04-07
---

## Unable to Find a Proper MID Server when Discovering a Host with Quick Discovery

  

### Issue

# Symptoms

* * *

When you attempt to use the Quick Discovery you get a banner error stating "Unable to find a proper MID Sever for discovering <IP\_ADDRESS>"

![](Screen%20Shot%202018-12-12%20at%2012.10.54%20PM.pngx)![](Screen%20Shot%202018-12-12%20at%2012.10.54%20PM.pngx)![](sys_attachment.do?sys_id=c6da68e6db42b450e515c22305961958)

# Release

* * *

All

# Cause

* * *

The MID Server does not meet the requirements for discovering this host. 

The MID server selection algorithm that ServiceNow uses is below:

1\. Start with all validated MID servers

2\. Select only "Up" MID servers

3\. Select MID servers configured for requesting application or "ALL"

4\. Select MID servers whose IP address of ranges include "ALL" targets

5\. Select MID servers with "ALL" required "Capabilities"

6\. If the remaining set has at least 1 MID server, use 1 randomly from that set

7\. If the remaining set is empty and there is a default MID Server that is "UP", use it

8\. If there are no MID Servers that meet the criteria, the requests to use it fail.

# Resolution

Make certain that you have a MID Server that meets the criteria above

# Additional Information

* * *

Read our documentation regarding [MID Server Selection](https://docs.servicenow.com/csh?topicname=c_MIDServerSelector.html&version=latest "MID Server Selection")
