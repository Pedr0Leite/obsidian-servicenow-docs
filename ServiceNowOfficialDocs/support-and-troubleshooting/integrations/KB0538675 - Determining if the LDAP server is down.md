---
title: "Determining if the LDAP server is down"
aliases:
  - KB0538675
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0538675
kb_number: KB0538675
last_modified: 2024-05-01
---

## Determining if the LDAP server is down

  

### Issue

Determining if the LDAP server is down 

Problem

* * *

The connection between the LDAP server and the instance is failing.  

Symptoms

* * *

-   Users are unable to log in.
-   The **connection timed out** error message is displayed when using the **Test Connection** link in the **LDAP Server** record.

Causes

* * *

-   The LDAP server may not be running.
-   The firewalls or VPN may not be allowing connectivity from associated datacenters.

Resolution

* * *

-   Verify with the LDAP administrator that the server is running.
-   Verify if there have been recent changes to the firewall or VPN.

If the suggestions above did not resolve the issue, create an incident (INT) ticket, and include this information:

-   The network administrator contact information
-   The result of nslookup / host of the affected instance from the LDAP server
-   The result of ping / traceroute from the LDAP server to the instance URL, noting the start and endpoint IPs
-   The result of packet captures that can be opened in Wireshark, noting the start and endpoint IPs, and the time frames when the user authentication was requested

ServiceNow Technical Support provides the corresponding IPs for the associated datacenter pair and schedules a call between ServiceNow resource and the networking resource.

<table class="noteTable" align="left"><tbody><tr><td style="width: 50; vertical-align: middle; text-align: center;"><img style="align: baseline;" title="Note" src="/Note_25x.pngx" align="bottom" border="" hspace="" vspace=""></td><td style="vertical-align: middle; text-align: left;"><strong>Note:</strong> Make sure to include the contact information of the networking resource so that a Servicenow network engineer can help resolve the issue.&nbsp;</td></tr></tbody></table>
