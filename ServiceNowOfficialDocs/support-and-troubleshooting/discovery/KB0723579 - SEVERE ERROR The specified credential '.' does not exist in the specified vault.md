---
title: "SEVERE *** ERROR *** The specified credential '.' does not exist in the specified vault"
aliases:
  - KB0723579
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0723579
kb_number: KB0723579
last_modified: 2026-05-21
---

## SEVERE \*\*\* ERROR \*\*\* The specified credential '.' does not exist in the specified vault

  

### Issue

Discovery using cyberark credentials fail with the below error found in mid server logs :

SEVERE \*\*\* ERROR \*\*\* The specified credential '.' does not exist in the specified vault

### Release

Kingston patch 12 and later

### Cause

The fix of PRB1304580 involved changing code related to CyberArk; modifying old behavior. This PRB was fixed in Kingston patch 12. Prior to Kingston patch 12, if the credentialID is in the format "<safename>:.", mid server will try to find the credential lookup via IP.

Credential lookup via IP will be done, if the credential ID is in the format "<safename>:" from Kingston patch 12. 

If the instance is still configured to use the format "<safename>:.", the mid server will consider the "." as a credential name and throws the error: "SEVERE \*\*\* ERROR \*\*\* The specified credential '.' does not exist in the specified vault"

### Resolution

For the credential lookup via IP to be successful, change the credential ID format from "<safename>:." to "<safename>:"

### Related Links

"For credential lookups in versions at Kingston Patch 12 and later, the MID Server finds the credential by matching the credential identifier to a name in vault, which must be unique. If the Credential identifier field is blank, then the MID Server finds the credential by IP address." - [CyberArk integration configuration](https://docs.servicenow.com/csh?topicname=c_CyberArkIntegrationConfiguration.html&version=latest)
