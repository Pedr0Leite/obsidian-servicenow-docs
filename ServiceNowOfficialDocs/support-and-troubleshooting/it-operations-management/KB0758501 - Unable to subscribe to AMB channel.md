---
title: "Unable to subscribe to AMB channel"
aliases:
  - KB0758501
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0758501
kb_number: KB0758501
last_modified: 2024-04-07
---

## Unable to subscribe to AMB channel

  

### Issue

**Issue:**

AMB issues using Linux Mid server.

**error from agent logs:**

Unable to subscribe to AMB channel: /mid/server/29cc65f213be67c860ee30128144b07d

**Errors in Wrapper logs**

Errors in wrapper log:2019/07/16 02:34:39 | Caused by: javax.net.ssl.SSLHandshakeException: No appropriate protocol, may be no appropriate cipher suite specified or protocols are deactivated  
2019/07/16 02:34:39 | at com.ibm.jsse2.D.c(D.java:352)  
2019/07/16 02:34:39 | at com.ibm.jsse2.as.g(as.java:383)  
2019/07/16 02:34:39 | at com.ibm.jsse2.as.c(as.java:607)  
2019/07/16 02:34:39 | at com.ibm.jsse2.as.wrap(as.java:172)

### Cause

\-This is caused by mid server using custom JRE rather than Out of the box JRE. From the stack trace in the wrapper log, it happens only when using custom JRE(IBM on Redhat)

\-Since we did not ship JRE our of the box in London, mid defaults to default JRE installed on the machine. You can confirm this by looking at wrapper-override.conf.

### Resolution

1.  Stop the mid server   
      
    2\. Download the mid server folder and copy the JRE to your Current agent folder. (Skip this step if JRE folder already exists)  
      
    3\. Navigate to the following file and comment out the following entry with wrapper.java.command(Check to see if this is pointing to custom JRE)   
      
    \-agent/conf/wrapper-override.conf   
      
    \- comment out this line so that we use default JRE  
    wrapper.java.command={your\_java\_executable} 

          4. Restart the mid server, this will start the mid with our out of the box JRE.

### Related Links

2019/07/16 02:34:39 | \[AMBClientProvider\] ERROR com.snc.glide.amb.AMBHttpClient - javax.net.ssl.SSLHandshakeException: No appropriate protocol, may be no appropriate cipher suite specified or protocols are deactivated   
2019/07/16 02:34:39 | java.util.concurrent.ExecutionException: javax.net.ssl.SSLHandshakeException: No appropriate protocol, may be no appropriate cipher suite specified or protocols are deactivated   
2019/07/16 02:34:39 | at org.eclipse.jetty.client.util.FutureResponseListener.getResult(FutureResponseListener.java:118)   
2019/07/16 02:34:39 | at org.eclipse.jetty.client.util.FutureResponseListener.get(FutureResponseListener.java:101)   
2019/07/16 02:34:39 | at org.eclipse.jetty.client.HttpRequest.send(HttpRequest.java:684)   
2019/07/16 02:34:39 | at com.snc.glide.amb.AMBHttpClient.login(AMBHttpClient.java:99)   
2019/07/16 02:34:39 | at com.snc.glide.amb.AMBHttpClient.login(AMBHttpClient.java:83)   
2019/07/16 02:34:39 | at com.snc.glide.amb.AMBClient.buildHttpClient(AMBClient.java:172)   
2019/07/16 02:34:39 | at com.snc.glide.amb.AMBClient.initializeBayeuxClient(AMBClient.java:134)   
2019/07/16 02:34:39 | at com.snc.glide.amb.AMBClient.connect(AMBClient.java:86)   
2019/07/16 02:34:39 | at com.service\_now.mid.Instance.getAMBClient(Instance.java:378)   
2019/07/16 02:34:39 | at com.service\_now.mid.amb.AMBClientProvider.connect(AMBClientProvider.java:116)   
2019/07/16 02:34:39 | at com.service\_now.mid.amb.AMBClientProvider$$Lambda$38.0000000054007900.execute(Unknown Source)   
2019/07/16 02:34:39 | at com.service\_now.mid.amb.AMBClientProvider.executeInLock(AMBClientProvider.java:191)   
2019/07/16 02:34:39 | at com.service\_now.mid.amb.AMBClientProvider.lambda$initialize$7(AMBClientProvider.java:54)   
2019/07/16 02:34:39 | at com.service\_now.mid.amb.AMBClientProvider$$Lambda$37.000000002007B930.run(Unknown Source)   
2019/07/16 02:34:39 | at java.lang.Thread.run(Thread.java:812)   
2019/07/16 02:34:39 | Caused by: javax.net.ssl.SSLHandshakeException: No appropriate protocol, may be no appropriate cipher suite specified or protocols are deactivated   
2019/07/16 02:34:39 | at com.ibm.jsse2.D.c(D.java:352)   
2019/07/16 02:34:39 | at com.ibm.jsse2.as.g(as.java:383)   
2019/07/16 02:34:39 | at com.ibm.jsse2.as.c(as.java:607)   
2019/07/16 02:34:39 | at com.ibm.jsse2.as.wrap(as.java:172)   
2019/07/16 02:34:39 | at javax.net.ssl.SSLEngine.wrap(SSLEngine.java:18)   
2019/07/16 02:34:39 | at org.eclipse.jetty.io.ssl.SslConnection$DecryptedEndPoint.flush(SslConnection.java:980)   
2019/07/16 02:34:39 | at org.eclipse.jetty.io.WriteFlusher.flush(WriteFlusher.java:429)   
2019/07/16 02:34:39 | at org.eclipse.jetty.io.WriteFlusher.write(WriteFlusher.java:323)   
2019/07/16 02:34:39 | at org.eclipse.jetty.io.AbstractEndPoint.write(AbstractEndPoint.java:380)   
2019/07/16 02:34:39 | at org.eclipse.jetty.client.http.HttpSenderOverHTTP$HeadersCallback.process(HttpSenderOverHTTP.java:268)   
2019/07/16 02:34:39 | at org.eclipse.jetty.util.IteratingCallback.processing(IteratingCallback.java:241)   
2019/07/16 02:34:39 | at org.eclipse.jetty.util.IteratingCallback.iterate(IteratingCallback.java:224)   
2019/07/16 02:34:39 | at org.eclipse.jetty.client.http.HttpSenderOverHTTP.sendHeaders(HttpSenderOverHTTP.java:62)   
2019/07/16 02:34:39 | at org.eclipse.jetty.client.HttpSender.send(HttpSender.java:212)   
2019/07/16 02:34:39 | at org.eclipse.jetty.client.http.HttpChannelOverHTTP.send(HttpChannelOverHTTP.java:85)   
2019/07/16 02:34:39 | at org.eclipse.jetty.client.HttpChannel.send(HttpChannel.java:128)   
2019/07/16 02:34:39 | at org.eclipse.jetty.client.HttpConnection.send(HttpConnection.java:201)   
2019/07/16 02:34:39 | at org.eclipse.jetty.client.http.HttpConnectionOverHTTP$Delegate.send(HttpConnectionOverHTTP.java:253)   
2019/07/16 02:34:39 | at org.eclipse.jetty.client.http.HttpConnectionOverHTTP.send(HttpConnectionOverHTTP.java:122)   
2019/07/16 02:34:39 | at org.eclipse.jetty.client.http.HttpDestinationOverHTTP.send(HttpDestinationOverHTTP.java:38)   
2019/07/16 02:34:39 | at org.eclipse.jetty.client.HttpDestination.process(HttpDestination.java:347)   
2019/07/16 02:34:39 | at org.eclipse.jetty.client.HttpDestination.process(HttpDestination.java:305)   
2019/07/16 02:34:39 | at org.eclipse.jetty.client.HttpDestination.send(HttpDestination.java:295)   
2019/07/16 02:34:39 | at org.eclipse.jetty.client.HttpDestination.succeeded(HttpDestination.java:229)   
2019/07/16 02:34:39 | at org.eclipse.jetty.client.AbstractConnectionPool.proceed(AbstractConnectionPool.java:154)   
2019/07/16 02:34:39 | at org.eclipse.jetty.client.AbstractConnectionPool$1.succeeded(AbstractConnectionPool.java:132)   
2019/07/16 02:34:39 | at org.eclipse.jetty.client.AbstractConnectionPool$1.succeeded(AbstractConnectionPool.java:124)   
2019/07/16 02:34:39 | at org.eclipse.jetty.util.Promise$Wrapper.succeeded(Promise.java:130)   
2019/07/16 02:34:39 | at org.eclipse.jetty.client.http.HttpConnectionOverHTTP.onOpen(HttpConnectionOverHTTP.java:130)   
2019/07/16 02:34:39 | at org.eclipse.jetty.io.ssl.SslConnection.onOpen(SslConnection.java:251)   
2019/07/16 02:34:39 | at org.eclipse.jetty.io.AbstractEndPoint.upgrade(AbstractEndPoint.java:440)   
2019/07/16 02:34:39 | at org.eclipse.jetty.client.HttpProxy$CreateTunnelPromise.tunnelSucceeded(HttpProxy.java:212)   
2019/07/16 02:34:39 | at org.eclipse.jetty.client.HttpProxy$CreateTunnelPromise.lambda$tunnel$0(HttpProxy.java:182)   
2019/07/16 02:34:39 | at org.eclipse.jetty.client.HttpProxy$CreateTunnelPromise$$Lambda$55.0000000070F81930.onComplete(Unknown Source)   
2019/07/16 02:34:39 | at org.eclipse.jetty.client.ResponseNotifier.notifyComplete(ResponseNotifier.java:216)   
2019/07/16 02:34:39 | at org.eclipse.jetty.client.ResponseNotifier.notifyComplete(ResponseNotifier.java:208)   
2019/07/16 02:34:39 | at org.eclipse.jetty.client.HttpReceiver.terminateResponse(HttpReceiver.java:470)   
2019/07/16 02:34:39 | at org.eclipse.jetty.client.HttpReceiver.responseSuccess(HttpReceiver.java:416)   
2019/07/16 02:34:39 | at org.eclipse.jetty.client.http.HttpReceiverOverHTTP.messageComplete(HttpReceiverOverHTTP.java:316)   
2019/07/16 02:34:39 | at org.eclipse.jetty.http.HttpParser.handleContentMessage(HttpParser.java:605)   
2019/07/16 02:34:39 | at org.eclipse.jetty.http.HttpParser.parseNext(HttpParser.java:1519)   
2019/07/16 02:34:39 | at org.eclipse.jetty.client.http.HttpReceiverOverHTTP.parse(HttpReceiverOverHTTP.java:172)   
2019/07/16 02:34:39 | at org.eclipse.jetty.client.http.HttpReceiverOverHTTP.process(HttpReceiverOverHTTP.java:135)   
2019/07/16 02:34:39 | at org.eclipse.jetty.client.http.HttpReceiverOverHTTP.receive(HttpReceiverOverHTTP.java:73)   
2019/07/16 02:34:39 | at org.eclipse.jetty.client.http.HttpChannelOverHTTP.receive(HttpChannelOverHTTP.java:133)   
2019/07/16 02:34:39 | at org.eclipse.jetty.client.http.HttpConnectionOverHTTP.onFillable(HttpConnectionOverHTTP.java:155)   
2019/07/16 02:34:39 | at org.eclipse.jetty.io.AbstractConnection$ReadCallback.succeeded(AbstractConnection.java:281)   
2019/07/16 02:34:39 | at org.eclipse.jetty.io.FillInterest.fillable(FillInterest.java:102)   
2019/07/16 02:34:39 | at org.eclipse.jetty.io.ChannelEndPoint$2.run(ChannelEndPoint.java:118)   
2019/07/16 02:34:39 | at org.eclipse.jetty.util.thread.QueuedThreadPool.runJob(QueuedThreadPool.java:762)   
2019/07/16 02:34:39 | at org.eclipse.jetty.util.thread.QueuedThreadPool$2.run(QueuedThreadPool.java:680)   
2019/07/16 02:34:39 | ... 1 more   
2019/07/16 02:34:45 | \[AMBClientProvider\] ERROR com.snc.glide.amb.AMBHttpClient - javax.net.ssl.SSLHandshakeException: No appropriate protocol, may be no appropriate cipher suite specified or protocols are deactivated   
2019/07/16 02:34:45 | java.util.concurrent.ExecutionException: javax.net.ssl.SSLHandshakeException: No appropriate protocol, may be no appropriate cipher suite specified or protocols are deactivated
