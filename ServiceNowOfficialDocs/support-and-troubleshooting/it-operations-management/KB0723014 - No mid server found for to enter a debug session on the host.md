---
title: "No mid server found for to enter a debug session on the host"
aliases:
  - KB0723014
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0723014
kb_number: KB0723014
last_modified: 2024-04-07
---

## No mid server found for to enter a debug session on the host

  

### Issue

# Overview

* * *

Error "No mid server found for to enter a debug session on the host" is thrown when trying to debug a pattern.![](Error.pngx)

# Root Cause

* * *

A MID server is automatically selected when debugging a pattern. The mid server selection algorithm is the same used for service mapping, as patterns were originally used for service mapping. In future version, the user will be able to select what MID server to be used.

The following criteria is used to determine what MID server should be used for the debug session:

-   The Service Mapping or ALL application must be specified on the MID Server.
-   The endpoint IP address must fall within the IP range that you configure on the MID Server, or the ALL option must be selected on the MID Server.
-   One of the supported Service Mapping capabilities (for new installs) must be configured on the MID Server, or the MID Server capability must be set to ALL.

If there are no MID servers found based on the above criteria, the error will be thrown.

# Solution

* * *

1.  Open the MID server to be used for debugging and add proper IP Range (All or specific IP), Supported Application (All or Service Mapping), and Capability (All).

# Additional Information

* * *

Search docs.servicenow.com for "MID Server selection" to find the most recent MID server selection algorithms.

The following is for the London release:

-   [MID Server selection](https://docs.servicenow.com/csh?topicname=c_MIDServerSelector.html&version=latest "MID Server selection")
