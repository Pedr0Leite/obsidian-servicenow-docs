---
title: "SSH authentication fails with \"host key is invalid or was not accepted\" error during Discovery"
aliases:
  - KB0782056
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0782056
kb_number: KB0782056
last_modified: 2026-02-20
---

## SSH authentication fails with "host key is invalid or was not accepted" error during Discovery

  

### Issue

Troubleshoot SSH authentication failures that occur during Discovery on UNIX servers. Some servers complete Discovery and create configuration items (CIs) successfully, while others fail with the following warning or error:

"SSH authentication or connection failure: The host key is invalid or was not accepted!"

Credential-based connections to the affected servers succeed, which indicates the issue is not related to authentication credentials.

Error found from the MID Server log "agent.log.0":

10/08/19 18:30:17 (768) Worker-Interactive:MultiProbe-e787aa721b100c508cb8fc43cd4bcbef SEVERE \*\*\* ERROR \*\*\* Exception from SSH: com.sshtools.j2ssh.transport.kex.KeyExchangeException; The host key is invalid or was not accepted!&#13;  
com.sshtools.j2ssh.transport.kex.KeyExchangeException: The host key is invalid or was not accepted!&#13;  
at com.sshtools.j2ssh.transport.TransportProtocolClient.performKeyExchange(TransportProtocolClient.java:356)&#13;  
at com.sshtools.j2ssh.transport.TransportProtocolCommon.beginKeyExchange(TransportProtocolCommon.java:711)&#13;  
at com.sshtools.j2ssh.transport.TransportProtocolCommon.onMsgKexInit(TransportProtocolCommon.java:1295)&#13;  
at com.sshtools.j2ssh.transport.TransportProtocolCommon.startBinaryPacketProtocol(TransportProtocolCommon.java:1032)&#13;  
at com.sshtools.j2ssh.transport.TransportProtocolCommon.run(TransportProtocolCommon.java:388)&#13;  
at java.lang.Thread.run(Unknown Source)&#13;

### Release

All Supported Releases

### Resolution

This error occurs when the legacy SSH client j2ssh runs SSH commands instead of the current SSH client. To resolve the issue, update the MID Server configuration parameter `mid.ssh.use_snc`.

1.  On each MID Server used for SSH Discovery, check the value of the `mid.ssh.use_snc` parameter.
2.  If the value is false, set it to true.

Apply this change to all MID Servers used for SSH Discovery.
