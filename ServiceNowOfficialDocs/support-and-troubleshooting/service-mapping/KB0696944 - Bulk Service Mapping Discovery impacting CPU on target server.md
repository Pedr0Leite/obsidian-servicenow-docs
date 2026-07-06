---
title: "Bulk Service Mapping Discovery impacting CPU on target server"
aliases:
  - KB0696944
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0696944
kb_number: KB0696944
last_modified: 2024-04-07
---

## Bulk Service Mapping Discovery impacting CPU on target server

  

### Issue

# Symptoms

* * *

After bulk service mapping discovery is initiated, some servers received a large number of probes causing the CPU of these machines to spike to almost 100%.

# Release

* * *

From Kingston 

# Cause

* * *

MID server is sanding too many concurrent tasks sent to an individual host

# Resolution

* * *

Please configure following parameter for MID server that sent the requests:  
  
mid.servicewatch.max\_concurrent\_connections  
  
This parameter defines the maximum number of concurrent tasks sent to an individual host by a single MID Server. Default value is 7, try to set value 3.

# Additional Information

* * *

[MID Server properties](https://docs.servicenow.com/csh?topicname=r_MIDServerProperties.html&version=latest "MID Server properties")
