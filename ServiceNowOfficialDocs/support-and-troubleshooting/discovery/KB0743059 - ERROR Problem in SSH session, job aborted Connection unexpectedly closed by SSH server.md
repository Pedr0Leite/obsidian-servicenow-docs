---
title: "ERROR: Problem in SSH session, job aborted: Connection unexpectedly closed by SSH server"
aliases:
  - KB0743059
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0743059
kb_number: KB0743059
last_modified: 2026-05-21
---

## ERROR: Problem in SSH session, job aborted: Connection unexpectedly closed by SSH server

  

### Issue

Discovery is failing to execute few ssh commands on some Unix servers & returning below errors.

ERROR: Problem in SSH session, job aborted: Connection unexpectedly closed by SSH server

Example of failing commands:

-   sh ${file:websphere-version.sh} ${was\_install\_root}
-   cat ${filename}

### Release

All releases

### Cause

If we configure MID Server parameter "mid.ssh\_connections\_per\_host" with a number higher than what MaxSessions is configured on the target, then we will see the errors regarding SSH connection, as the connections cannot be opened.

### Explanation

The mid.ssh\_connections\_per\_host control how many session we make to the same host using the same connection.  
  
For example, if we discovery host A and set mid.ssh\_connections\_per\_host = 5 we will only have 5 sessions to host A at the same time.  
  
From Linux documentation:

MaxSessions  
Specifies the maximum number of open shell, login or subsystem  
(e.g. sftp) sessions permitted per network connection. Multiple  
sessions may be established by clients that support connection  
multiplexing. Setting MaxSessions to 1 will effectively disable  
session multiplexing, whereas setting it to 0 will prevent all  
shell, login and subsystem sessions while still permitting for-  
warding. The default is 10.

The MaxSessions on the server specifies the maximum number of open sessions permitted per network connection. The default is 10.

From ServiceNow documentation:

### SSH Discovery parameters

<table style="height: 121px;" border="2" width="825" cellspacing="4" cellpadding="2"><tbody><tr><td style="width: 150.234px;">&nbsp; MID Server SSH&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;connections per host</td><td style="width: 182.72px;">&nbsp;mid.ssh_connections_per_host&nbsp;&nbsp;</td><td style="width: 455.568px;">&nbsp; Controls the number of concurrent probes that the MID Server can run against a given host. Lowering the number of concurrent connections can slow Discovery.<ul id="r_SSHDiscoveryParameters__ul_lqt_hwy_1bb" style="list-style-position: inside;"><li>Type: integer</li><li>Default value:<br><ul id="r_SSHDiscoveryParameters__ul_arb_jwy_1bb" style="list-style-position: inside;"><li>7 for the ServiceNow client</li><li>3 for the legacy SSH client</li></ul></li></ul></td></tr></tbody></table>

### Resolution

-   The value for mid.ssh\_connections\_per\_host should be at most equals to the target server MaxSessions SSH parameter.
-   Check the mid server parameter "mid.ssh\_connections\_per\_host" value & "max sessions" on the target server.
-   If the "mid.ssh\_connections\_per\_host" value is more than max sessions(on target server), then lowering this value on the MID Server parameter may resolve this issue.
