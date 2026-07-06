---
title: "Discovery - SNMP credentials having username beyond 32 characters would lead Test Credentials to fail."
aliases:
  - KB0788324
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0788324
kb_number: KB0788324
last_modified: 2024-04-08
---

## Discovery - SNMP credentials having username beyond 32 characters would lead Test Credentials to fail.

  

### Issue

SNMP credentials having username beyond 32 characters would lead Test Credentials to fail.

### Release

All Releases. 

### Cause

  
User name exceeding the security limit which is 32.  
  
  
After going through the input payload that was run you will see this stack trace.  
com.snc.automation\_common.integration.exceptions.UnknownException: User 'snmp-server xxxxxxxxxx xxxxxxxxx RW' not added because of its too long security name with length 33  
at com.snc.core\_automation\_common.util.AKeyedConnectionFactory.getConnection(AKeyedConnectionFactory.java:146)  
at com.snc.core\_automation\_common.util.AKeyedConnectionFactory.getConnection(AKeyedConnectionFactory.java:110)  
at com.service\_now.mid.pipeline.command.TestCredentialCommandImpl.executeRawCommand(TestCredentialCommandImpl.java:120)  
at com.snc.core\_automation\_common.pipeline.ACommand.execute(ACommand.java:114)  
at com.service\_now.mid.probe.CommandPipeline.probe(CommandPipeline.java:63)  
at com.service\_now.mid.probe.AProbe.process(AProbe.java:96)  
at com.service\_now.mid.queue\_worker.AWorker.runWorker(AWorker.java:121)  
at com.service\_now.mid.queue\_worker.AWorkerThread.run(AWorkerThread.java:20)  
at java.util.concurrent.ThreadPoolExecutor.runWorker(ThreadPoolExecutor.java:1149)  
at java.util.concurrent.ThreadPoolExecutor$Worker.run(ThreadPoolExecutor.java:624)  
at java.lang.Thread.run(Thread.java:748)  
Caused by: java.lang.IllegalArgumentException: User 'snmp-server community pomeroy2 RW' not added because of its too long security name with length 33  
at org.snmp4j.security.USM.addUser(USM.java:858)  
at org.snmp4j.security.USM.addUser(USM.java:824)  
at com.service\_now.mid.probe.snmp.api.Snmp4jSessionFactory.getSnmpV3Session(Snmp4jSessionFactory.java:135)  
at com.service\_now.mid.probe.snmp.api.Snmp4jSessionFactory.getConnection(Snmp4jSessionFactory.java:101)  
at com.service\_now.mid.probe.snmp.api.Snmp4jSessionFactory.getConnection(Snmp4jSessionFactory.java:52)  
at com.snc.core\_automation\_common.util.AKeyedConnectionFactory.getConnectionUseOneCred(AKeyedConnectionFactory.java:216)  
at com.snc.core\_automation\_common.util.AKeyedConnectionFactory.getConnectionIterateOverCreds(AKeyedConnectionFactory.java:170)  
at com.snc.core\_automation\_common.util.AKeyedConnectionFactory.getConnection(AKeyedConnectionFactory.java:123)  
... 10 more  
" probe\_time="0" result\_code="900000">

  
Looks like there is a limitation on how many characters can be given to SNMP credentials. Here is the stack overflow discussion I found.  
  
[https://stackoverflow.com/questions/6290580/net-snmp-security-name-too-long-what-is-the-max-length-of-security-name#6298039](https://stackoverflow.com/questions/6290580/net-snmp-security-name-too-long-what-is-the-max-length-of-security-name#6298039)  
  
  

### Resolution

Please reduce the username to have less than 32 characters for SNMP credentials that should fix the issue.
