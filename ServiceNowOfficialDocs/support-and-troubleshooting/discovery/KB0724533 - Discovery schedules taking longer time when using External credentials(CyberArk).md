---
title: "Discovery schedules taking longer time when using External credentials(CyberArk)"
aliases:
  - KB0724533
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0724533
kb_number: KB0724533
last_modified: 2024-04-07
---

## Discovery schedules taking longer time when using External credentials(CyberArk)

  

### Issue

# Symptoms

* * *

\-Discovery schedules stuck or getting cancelled when using external credentials.

# Release

* * *

All Releases

# Cause

* * *

\-If you have too many credential ID's in your credentials table,  all the credential ID's will be tested for your discovery. There is only one credential resolver proxy that will test these credentials against Cyberark. Having too many credential ID's associated with all the mid servers will lock this thread and eventually cause delay in processing the schedule. 

\-There may be connectivity issues between Mid server to cyberArk that may cause delay in reading the data from CyberArk.

\-Sample thread Dump

"Worker-Standard:HorizontalDiscoveryProbe" #137 daemon prio=5 os\_prio=0 tid=0x0000000022595800 nid=0x7a4 runnable \[0x0000000027c3e000\]&#13; 

2019/01/02 12:58:49 | java.lang.Thread.State: RUNNABLE&#13;   
2019/01/02 12:58:49 | at java.net.SocketInputStream.socketRead0(Native Method)&#13;   
2019/01/02 12:58:49 | at java.net.SocketInputStream.socketRead(SocketInputStream.java:116)&#13;   
2019/01/02 12:58:49 | at java.net.SocketInputStream.read(SocketInputStream.java:171)&#13;   
2019/01/02 12:58:49 | at java.net.SocketInputStream.read(SocketInputStream.java:141)&#13;   
2019/01/02 12:58:49 | at sun.nio.cs.StreamDecoder.readBytes(StreamDecoder.java:284)&#13;   
2019/01/02 12:58:49 | at sun.nio.cs.StreamDecoder.implRead(StreamDecoder.java:326)&#13;   
2019/01/02 12:58:49 | at sun.nio.cs.StreamDecoder.read(StreamDecoder.java:178)&#13;   
2019/01/02 12:58:49 | - locked &lt;0x0000000771ceaef8&gt; (a java.io.InputStreamReader)&#13;   
2019/01/02 12:58:49 | at java.io.InputStreamReader.read(InputStreamReader.java:184)&#13;   
2019/01/02 12:58:49 | at java.io.BufferedReader.fill(BufferedReader.java:161)&#13;   
2019/01/02 12:58:49 | at java.io.BufferedReader.read1(BufferedReader.java:212)&#13;   
2019/01/02 12:58:49 | at java.io.BufferedReader.read(BufferedReader.java:286)&#13;   
2019/01/02 12:58:49 | - locked &lt;0x0000000771ceaef8&gt; (a java.io.InputStreamReader)&#13;   
2019/01/02 12:58:49 | at java.io.Reader.read(Reader.java:140)&#13;   
2019/01/02 12:58:49 | at d.c.b(c.java:71)&#13;   
2019/01/02 12:58:49 | at k.l.c(l.java:4)&#13;   
2019/01/02 12:58:49 | at k.g.a(g.java:107)&#13;   
2019/01/02 12:58:49 | at k.i.a(i.java:53)&#13;   
2019/01/02 12:58:49 | at javapasswordsdk.PasswordSDK.getPassword(PasswordSDK.java:1)&#13;   
2019/01/02 12:58:49 | at com.service\_now.mid.services.credential.cyberark.CyberArkPasswordAccess.getPassword(CyberArkPasswordAccess.java:26)&#13;   
2019/01/02 12:58:49 | at com.service\_now.mid.services.credential.cyberark.CyberArkAccess.getCred(CyberArkAccess.java:216)&#13;   
2019/01/02 12:58:49 | at com.service\_now.mid.services.credential.cyberark.CredentialResolver.resolve(CredentialResolver.java:88)&#13;   
2019/01/02 12:58:49 | at com.service\_now.mid.services.CredentialResolverProxy.resolve(CredentialResolverProxy.java:227)&#13;   
2019/01/02 12:58:49 | - locked &lt;0x00000006c386b8e0&gt; (a com.service\_now.mid.services.CredentialResolverProxy)&#13;   
2019/01/02 12:58:49 | at com.service\_now.mid.creds.provider.standard.HighSecurityCredential.callResolver(HighSecurityCredential.java:43)&#13;   
2019/01/02 12:58:49 | at com.service\_now.mid.creds.provider.standard.HighSecurityCredential.&lt;init&gt;(HighSecurityCredential.java:33)&#13;   
2019/01/02 12:58:49 | at com.service\_now.mid.creds.provider.standard.StandardCredentialsProvider.iterator(StandardCredentialsProvider.java:153)&#13;   
2019/01/02 12:58:49 | - locked &lt;0x00000006c0428f08&gt; (a com.service\_now.mid.creds.provider.standard.StandardCredentialsProvider)&#13;   
2019/01/02 12:58:49 | at com.snc.sw.providers.DiscoveryProviderFactory.getApplicativeCredentials(DiscoveryProviderFactory.java:105)&#13;   
2019/01/02 12:58:49 | at com.snc.sw.context.ExecutionContextFactory.create(ExecutionContextFactory.java:79)&#13;   
2019/01/02 12:58:49 | at com.snc.sw.context.ExecutionContextFactory.createAppDiscovery(ExecutionContextFactory.java:129)&#13;   
2019/01/02 12:58:49 | at com.snc.sw.context.ExecutionContextFactory.createAppDiscovery(ExecutionContextFactory.java:137)&#13;   
2019/01/02 12:58:49 | at com.snc.sw.context.ExecutionContextFactory.createAppDiscovery(ExecutionContextFactory.java:143)&#13;   
2019/01/02 12:58:49 | at com.service\_now.mid.probe.HorizontalDiscoveryProbe.runProbe(HorizontalDiscoveryProbe.java:81)&#13;   
2019/01/02 12:58:49 | at com.service\_now.mid.probe.ServiceWatchProbe.probe(ServiceWatchProbe.java:35)&#13;   
2019/01/02 12:58:49 | at com.service\_now.mid.probe.AProbe.process(AProbe.java:84)&#13;   
2019/01/02 12:58:49 | at com.service\_now.mid.queue\_worker.AWorker.runWorker(AWorker.java:125)&#13;   
2019/01/02 12:58:49 | at com.service\_now.mid.queue\_worker.AWorkerThread.run(AWorkerThread.java:20)&#13;   
2019/01/02 12:58:49 | at java.util.concurrent.ThreadPoolExecutor.runWorker(ThreadPoolExecutor.java:1149)&#13;   
2019/01/02 12:58:49 | at java.util.concurrent.ThreadPoolExecutor$Worker.run(ThreadPoolExecutor.jav

# Resolution

* * *

\-Always make sure the credentials ID's are configured properly with respective mid servers.

\-Check to see if there is in delay in reading the data from CyberArk or if the thread is stuck reading the data.
