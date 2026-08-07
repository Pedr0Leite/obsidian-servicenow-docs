---
title: "MID agent log error: Problem creating JMX JMXMP connector"
aliases:
  - KB0639494
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0639494
kb_number: KB0639494
last_modified: 2024-04-07
---

## MID agent log error: Problem creating JMX JMXMP connector

  

### Issue

MID agent log error: Problem creating JMX JMXMP connector

# Issue

* * *

mid.jmx.enabled [MID Server connection parameter](https://docs.servicenow.com/csh?topicname=mid-server-parameters.html&version=latest "MID Server connection parameter") is set; however the following error is thrown in the MID Server agent log:

10/11/17 19:00:00 (811) StartupSequencer SEVERE \*\*\* ERROR \*\*\* Problem creating JMX JMXMP connector

java.net.BindException: Address already in use: JVM\_Bind

# Solution

* * *

Another process bound to the same port.

You can use [TCPView](http://technet.microsoft.com/en-us/sysinternals/bb897437) (Windows only) from [Windows Sysinternals](http://technet.microsoft.com/en-US/sysinternals) to help identify which processes are listening on which port. It also provides a convenient context menu to either kill the process or close the connection that is getting in the way.

Alternatively, if JMX server is not being used, you can set the _**mid.jmx.enabled**_ MID Server property to false. See the product documentation topic [Add a MID Server Parameter](https://docs.servicenow.com/csh?topicname=mid-server-parameters.html&version=latest "Add a MID Server Parameter") for more information.
