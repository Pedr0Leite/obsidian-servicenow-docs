---
title: "The CI hostname keeps changing or the CI record seems to be merging"
aliases:
  - KB0744540
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0744540
kb_number: KB0744540
last_modified: 2025-07-24
---

## The CI hostname keeps changing or the CI record seems to be merging

  

### Issue

During discovery, the physical host name keeps changing. The configuration item (CI) and asset records do not look correct; the CI hostname and hardware information appear to be merging between two or more CIs.

### Symptoms

undefined

### Release

All releases

### Cause

ServiceNow discovery is agentless discovery. It uses multiple probes or sensors to query the the CI for information. 

The main two probes that can cause this issue are the Classify and Identity probes. 

-   Classify gets the host information
-   Identity gets the IP address and serial number information

One of the first hardware rule identifiers is the serial\_number/serial\_number\_type. 

-   Classify scans system\_one and gets it hostname
-   Identity scans system\_two and gets it serial\_number

Since it is able to match the CI by serial number, the updated CI is the combination of hostname (system\_one) and serial\_number (system\_two).  

The following table illustrates this process.

<table style="width: 452px;" border="0" width="452" cellspacing="0" cellpadding="0"><colgroup><col style="width: 108.208px;" span="3" width="87"><col style="width: 126px;" width="104"></colgroup><tbody><tr><td width="87" height="21">&nbsp;</td><td width="87"><strong>Hostname</strong></td><td width="87"><strong>ipaddress</strong></td><td width="104"><strong>serial_number</strong></td></tr><tr><td height="21">Original CI</td><td>system_one</td><td>10.1.1.3</td><td>54321ABCD</td></tr><tr><td height="21">Original CI</td><td>system_two</td><td>10.1.1.4</td><td>ABCD54321</td></tr><tr><td height="21">New CI</td><td>system_one</td><td>10.1.1.4</td><td>ABCD54321</td></tr></tbody></table>

Other possible causes include:

1.  Multiple servers that sit behind a load balancer VIP.  It's possible that the load balancer is forwarding the request to different CIs during classify and identity.
2.  If the DHCP lease time is too short, and discovery is running very slow. System\_one picks up 10.1.1.4 and Discovery picked it up during classify. Then System\_one dropped off the network. System\_two came online and was given the same IP address, 10.1.1.4, and then discovery scans for identity.  This could also happen when using VPN when the there is a small number of IP ranges, and the user can quickly obtain the same IP address.
3.  Multiple systems have the same serial\_number
4.  The host system has multiple homes and multiple NICs.  

### Resolution

1.  If you know that the IP address you're scanning is a Virtual IP (VIP) on a load balancer, you can set the IP address in the exclude range so they will not be scanned.  Most likely you can scan the system with its direct IP address. 
2.  Increase the lease time on DHCP or add more MID Servers. This speeds up the discovery run time, shortening the time for classify and identity on different systems.   
    You can also exclude these IP address from the discovery schedule since the IP address is reused too frequently.  
3.  Multiple systems shouldn't have the same serial number.  Check to see if your system admin can address this issue.  If there are no way to change this, you need to use another method of identifying the CI in the hardware rule. 
4.  The host name can change frequently if you're scanning two different IP addresses on the same host that uses DNS as a host name.  Depending upon which IP address you scan, the host name will change to that DNS name.  You can deselect DNS as the trusted host name in the discovery properties.  This does not cause merge records but names can change frequently.

### Related Links

For more information, see the following product documentation:

[CI lookup rules for identifying configuration items](https://docs.servicenow.com/csh?topicname=ci-identifier-rules.html&version=latest)
