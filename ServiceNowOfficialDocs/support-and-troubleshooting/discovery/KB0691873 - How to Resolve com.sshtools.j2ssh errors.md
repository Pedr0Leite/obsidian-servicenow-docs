---
title: "How to Resolve \"com.sshtools.j2ssh\" errors"
aliases:
  - KB0691873
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0691873
kb_number: KB0691873
last_modified: 2024-04-07
---

## How to Resolve "com.sshtools.j2ssh" errors

  

### Issue

How to Resolve "com.sshtools.j2ssh" Errors

# Description

* * *

When checking MID logs for issues related to SSH troubleshooting you may observe errors such as the following:

Exception from SSH: java.io.IOException; The socket is EOF

java.io.IOException: The socket is EOF

at com.sshtools.j2ssh.transport.TransportProtocolInputStream.readBufferedData(TransportProtocolInputStream.java:187)

at com.sshtools.j2ssh.transport.TransportProtocolInputStream.readMessage(TransportProtocolInputStream.java:234)

at com.sshtools.j2ssh.transport.TransportProtocolCommon.readMessage(TransportProtocolCommon.java:1340)

at com.sshtools.j2ssh.transport.kex.SshKeyExchangeFixedGroupDh.performClientExchange(SshKeyExchangeFixedGroupDh.java:162)

at com.sshtools.j2ssh.transport.TransportProtocolClient.performKeyExchange(TransportProtocolClient.java:353)

at com.sshtools.j2ssh.transport.TransportProtocolCommon.beginKeyExchange(TransportProtocolCommon.java:711)

at com.sshtools.j2ssh.transport.TransportProtocolCommon.onMsgKexInit(TransportProtocolCommon.java:1295)

at com.sshtools.j2ssh.transport.TransportProtocolCommon.startBinaryPacketProtocol(TransportProtocolCommon.java:1032)

at com.sshtools.j2ssh.transport.TransportProtocolCommon.run(TransportProtocolCommon.java:388)

at java.lang.Thread.run(Thread.java:748)

# Cause

* * *

This is caused by the deprecated j2ssh library, which may still be in use by clients who existed pre-Eureka and never manually added the necessary property to switch to the new SNC SSH library. All clients are encouraged to switch to the SNC library.

# Solution

* * *

The property can be added at the MID level or SSHProbe level. It's recommended to add the property at the probe level to prevent MID servers from somehow missing the property and causing issues. Add the use\_snc\_ssh parameter to the SSHProbe. Supporting documentation:

[https://docs.servicenow.com/csh?topicname=r\_Parameters.html&version=latest](https://docs.servicenow.com/csh?topicname=r_Parameters.html&version=latest)

# Applicable Versions

* * *

Any, if upgraded from a pre-Eureka instance.

# Additional Information

* * *

Community article explaining some of the differences between the j2ssh and sncssh:

[https://community.servicenow.com/community?id=community\_question&sys\_id=04ec0b29db9cdbc01dcaf3231f9619eb](https://community.servicenow.com/community?id=community_question&sys_id=04ec0b29db9cdbc01dcaf3231f9619eb)
