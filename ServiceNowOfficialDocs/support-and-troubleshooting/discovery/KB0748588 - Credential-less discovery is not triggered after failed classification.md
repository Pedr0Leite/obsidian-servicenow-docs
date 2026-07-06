---
title: "Credential-less discovery is not triggered after failed classification"
aliases:
  - KB0748588
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0748588
kb_number: KB0748588
last_modified: 2026-07-02
---

## Credential-less discovery is not triggered after failed classification

  

### Issue

 

Credential-less discovery is not triggered on a discovered device after failed classification. Credential-less discovery is used as a fallback to discover CIs when standard classification of a CI is not successful.

### Release

All currently supported releases.

### Cause

Credential-less discovery is used as a fallback to discover CIs when "standard" classification of a CI is not successful.  

For example, if discovery of a linux server fails, because no valid credentials are available to discover the device, then credential-less discovery would be triggered to try and determine what the device is.

See following documents on credential-less discovery for more information:

-   [Credential-less Discovery with Nmap](https://docs.servicenow.com/csh?topicname=nmap-credential-less-discovery.html&version=latest "Credential-less Discovery with Nmap")
-   [Credential-less host Discovery](https://docs.servicenow.com/csh?topicname=credential-less-host-discovery.html&version=latest "Credential-less host Discovery")

Credential-less discovery is used as a fallback. Therefore, discovery checks if there already exists a CI with such ip address before triggering credential-less discovery for the IP. If a CI already exists, then credential-less discovery is not triggered.

### Resolution

**Check if ip exists:**

Check that the cmdb\_ci\_ip\_address table has the ip address for which discovery did not trigger credential-less discovery. If yes, it is expected behavior that discovery would not trigger credential-less discovery. The matching ip addresses can be removed to trigger credential-less discovery on the next discovery attempt.

**Check discovery log for error messages:**

Review the discovery log. Look for any error messages that contain "MID" or "nmap". An error containing "MID" or "nmap" will be added to the discovery status log in most cases If a valid mid server is not found to trigger credential-less discovery with. if such errors are found, ensure there are valid mid servers which can be used for credential-less discovery.

Some of the requirements for triggering credential-less discovery are:

-   System propery mid.discovery.credentialless.enable = true.
-   A mid server with nmap capability, discovery application, and ip range configured.

### Related Links

[Credential-less Discovery with Nmap](https://docs.servicenow.com/csh?topicname=nmap-credential-less-discovery.html&version=latest) 

[Credential-less host discovery](https://docs.servicenow.com/csh?topicname=credential-less-host-discovery.html&version=latest)
