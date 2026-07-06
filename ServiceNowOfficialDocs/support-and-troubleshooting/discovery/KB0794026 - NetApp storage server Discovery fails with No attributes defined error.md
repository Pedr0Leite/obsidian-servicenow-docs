---
title: "NetApp storage server Discovery fails with \"No attributes defined\" error"
aliases:
  - KB0794026
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0794026
kb_number: KB0794026
last_modified: 2026-02-26
---

## NetApp storage server Discovery fails with "No attributes defined" error

  

### Issue

Resolve NetApp storage server Discovery failures caused by the "No attributes defined" error. This error occurs when basic authentication credentials are missing or do not have the right permissions. The NetApp Storage Cluster-Mode pattern is used for this Discovery.

### Release

All Supported Releases

### Cause

This error occurs when one of the following conditions exists:

-   Basic authentication credentials are missing in the instance.
-   Basic authentication credentials do not have enough permissions to query the NetApp storage server.

### Resolution

When you debug the NetApp Storage Cluster-Mode pattern, the following error appears in the identification section:

setAttribute(phys\_interface\_info,<error>  
error  
Failed connecting to device.  
Please verify you have valid credentials and the device is reachable via the MID server.      
</error>)

To resolve this issue, complete the following steps:

1.  Create a [basic authentication](https://www.servicenow.com/docs/r/platform-security/connections-and-credentials/r_BasicAuthCredentialsForm.html "basic authentication") credential to use when identifying and exploring the NetApp server.
2.  On the NetApp server, the credential must use the authentication method of "password" and the user may have a read-only role with default access. 
3.  After the credentials are configured, re-run Discovery. Verify that Discovery completes without errors.
