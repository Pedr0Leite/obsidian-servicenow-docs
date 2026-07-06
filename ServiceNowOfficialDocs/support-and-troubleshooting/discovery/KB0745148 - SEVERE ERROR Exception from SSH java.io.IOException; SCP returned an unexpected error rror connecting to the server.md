---
title: "SEVERE *** ERROR *** Exception from SSH: java.io.IOException; SCP returned an unexpected error: rror connecting to the server"
aliases:
  - KB0745148
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0745148
kb_number: KB0745148
last_modified: 2024-04-07
---

## SEVERE \*\*\* ERROR \*\*\* Exception from SSH: java.io.IOException; SCP returned an unexpected error: rror connecting to the server

  

### Issue

# Symptoms

SEVERE \*\*\* ERROR \*\*\* Exception from SSH: java.io.IOException; SCP returned an unexpected error: rror connecting to the server

# Steps to reproduce

01) Add MID server parameter mid.ssh.debug and set value to true.

02) Then run discovery on the Linux server.

You will see below errors from the mid server logs.

02/05/19 22:14:30 (248) Worker-Interactive:MultiProbe-5088248c1ba32f846ca087386e4bcb0a SSH DEBUG: Opened channel 0&#13;   
02/05/19 22:14:30 (654) Worker-Interactive:MultiProbe-5088248c1ba32f846ca087386e4bcb0a SEVERE \*\*\* ERROR \*\*\* Exception from SSH: java.io.IOException; SCP returned an unexpected error: rror connecting to the server&#13;   
java.io.IOException: SCP returned an unexpected error: rror connecting to the server&#13;   
at com.sshtools.j2ssh.ScpClient$ScpChannel.waitForResponse(ScpClient.java:590)&#13;   
at com.sshtools.j2ssh.ScpClient$ScpChannel.access$000(ScpClient.java:321)&#13;   
at com.sshtools.j2ssh.ScpClient.put(ScpClient.java:197)&#13; 

# Cause

This is because of MID Server using the older version of SSH called j2ssh and thus error has been not encountered. You can refer to the following article about Migration from j2ssh to sncssh.   
[https://community.servicenow.com/community?id=community\_question&sys\_id=04ec0b29db9cdbc01dcaf3231f9619eb](https://community.servicenow.com/community?id=community_question&sys_id=04ec0b29db9cdbc01dcaf3231f9619eb) .   
Error might mean that the set of algorithms the client offers are unacceptable to the server.

# Resolution

Following below mentioned steps can help you get rid of this error.   
1\. Go to MID Servers.   
2\. Add property "mid.ssh.use\_snc"   
3\. Set the property to true.
