---
title: "Service Mapping does not recognize the \"Nmap\" capability assigned to MID Servers used for credential-less Discovery"
aliases:
  - KB0640005
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0640005
kb_number: KB0640005
last_modified: 2025-02-25
---

## Service Mapping does not recognize the "Nmap" capability assigned to MID Servers used for credential-less Discovery

  

### Issue

When Nmap is installed on a MID Server, the installer configures the **Nmap** capability for that MID Server. Horizontal, Discovery requires this capability for any MID Server used for credential-less Discovery and will not initiate an Nmap scan using a non-compliant MID Server. Service Mapping, however, does not check for the presence of the **Nmap** capability and selects the MID Server based on the IP address only. It is therefore possible for Service Mapping to select a MID Server that does not have Nmap installed. This condition logs the following error:

Nmap is not installed on MID Server. Verify all MIDs configured to handle selected IP Address have Nmap Capability.

### Resolution

To ensure that Service Mapping does not select a MID Server without the Nmap capability, install Nmap on all MID Servers assigned to the IP address ranges on which you want credential-less Discovery to be available.
