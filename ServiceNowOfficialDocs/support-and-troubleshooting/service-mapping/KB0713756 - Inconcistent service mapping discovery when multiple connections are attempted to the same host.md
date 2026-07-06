---
title: "Inconcistent service mapping discovery when multiple connections are attempted to the same host"
aliases:
  - KB0713756
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0713756
kb_number: KB0713756
last_modified: 2024-04-07
---

## Inconcistent service mapping discovery when multiple connections are attempted to the same host

  

### Issue

# Overview

* * *

Business service discovery at times fails with error "Failed to recognize application" if multiple applications in the map reside on the same host. Resuming discovery often clears the error. This behavior was observed on OpenVMS servers, however could potentially affect discovery of applications residing in other operating systems. OpenVMS operating system is not listed as supported per the following document.

-   [Linux Discovery](https://docs.servicenow.com/csh?topicname=r_DataCollDiscoLinuxComputers.html&version=latest "Linux Discovery") 

# Root Cause

* * *

Review of MID server agent logs, matching at time of issue, found that connections were not accepted by the target IP address.

<time\_stamp> () SSHProtocolEngine \[#/<ip\_address>:22\] Received server DEBUG messageDEBUG: always display: true, message: Failed to allocate pty!&#13

Some environments may limit the number of concurrent connections from a source, and therefore new connection attempts will fail.

# Solution

* * *

**Note:** "Failed to recognize application" is a generic error. This solution only applies to when multiple applications are discovered at once which reside on the same host.

Two possible solution are:

1.  Contact the sysadmin managing the system so that concurrent connections from the same source are allowed.
2.  Lower the number of connections created by service map to a given host concurrently.

To control the number of connections to a given IP address by service mapping:

-   Set following MID Server property "mid.servicewatch.max\_concurrent\_connections" to the desired number, the default is 7. Set it to 1 f the system only allows for a single connection. As a result, as long as there is one ecc queue output records that's currently processing, the others ecc queue records are kept in "ready" state.

# Additional Information

* * *

For a list of available MID server properties see:

-   [MID Server properties](https://docs.servicenow.com/csh?topicname=r_MIDServerProperties.html&version=latest "MID Server properties")
