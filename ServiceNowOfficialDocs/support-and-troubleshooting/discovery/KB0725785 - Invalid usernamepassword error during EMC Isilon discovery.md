---
title: "Invalid username/password error during EMC Isilon discovery"
aliases:
  - KB0725785
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0725785
kb_number: KB0725785
last_modified: 2025-02-14
---

## Invalid username/password error during EMC Isilon discovery

  

### Issue

Invalid username/password combo errors appear throughout the pattern log when running the EMC Isilon Discovery pattern.

Response has error. Status code is 401 . error code: 3 . error message: Method failed: (\[DEVICE\_PATHS\]) with code: 401 - Invalid username/password combo.

### Release

All releases

### Cause

The EMC Isilon user account that is being used for discovery does not have the appropriate permissions on the EMC Isilon device. 

### Resolution

Provide the EMC Isilon user with the following REST capabilities:

-   "https://" + $host + ":8080/platform/3/cluster/config”
-   "https://" + $host + ":8080/platform/3/network/interfaces”
-   "https://" + $host\_ip + ":8080/platform/3/cluster/nodes/”
-   “https://” + $host + ":8080/platform/3/zones”
-   "https://" + $host + ":8080/platform/3/network/pools”
-   "https://" + host\_ip + ":8080/platform/3/cluster/nodes/”
-   "https://" + $host + ":8080/platform/3/storagepool/nodepools”
-   "https://" + $host + ":8080/platform/3/storagepool/storagepools”
-   "https://" + $host + ":8080/platform/3/protocols/nfs/exports”
-   "https://" + $host + ":8080/platform/3/protocols/smb/shares"

In addition to these capabilities, this EMC Isilon user must have the following privileges:

-   ISI\_PRIV\_LOGIN\_PAPI
-   ISI\_PRIV\_AUTH
-   ISI\_PRIV\_DEVICES
-   ISI\_PRIV\_NETWORK
-   ISI\_PRIV\_NFS
-   ISI\_PRIV\_SMARTPOOLS
-   ISI\_PRIV\_SMB

### Related Links

[EMC Isilon Discovery - Prerequisites](https://docs.servicenow.com/csh?topicname=emc-isilon-discovery.html&version=latest "EMC Isilon Discovery - Prerequisites")
