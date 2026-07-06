---
title: "Outbound SOAP/REST calls causing performance issues"
aliases:
  - KB0786227
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0786227
kb_number: KB0786227
last_modified: 2025-06-18
---

## Issue

Custom scripts that trigger outbound SOAP / REST calls can cause degraded performance. You can identify this by the stack trace of the transaction and from the OUTBOUND log message.

Examples:

2019-11-19 00:54:27 (760) worker.4 worker.4 txid=1be0a28cdb1d OUTBOUND\_HTTP: protocol=HTTP/1.1 response\_status=200 response\_time=98872 request\_length=0 response\_length=1724 app\_scope=global session\_id=glide.scheduler.worker.4 transaction\_name="events process 0 - system" user\_name=system mid\_server= source\_table=sysevent\_script\_action source\_record=935fa0dadb65a780075e6dda4b9619ea system\_id=some\_node method=GET log\_level=Basic scheme=https hostname=some\_host path=some\_path

"glide.scheduler.worker.0" #75 daemon prio=4 os\_prio=0 tid=0x0e663000 nid=0x12cd5 runnable \[0x585c7000\]  
INFO | jvm 2 | 2019/11/19 00:59:45.081 | java.lang.Thread.State: RUNNABLE  
INFO | jvm 2 | 2019/11/19 00:59:45.081 | at java.net.SocketInputStream.socketRead0(Native Method)  
INFO | jvm 2 | 2019/11/19 00:59:45.081 | at java.net.SocketInputStream.socketRead(SocketInputStream.java:116)  
INFO | jvm 2 | 2019/11/19 00:59:45.081 | at java.net.SocketInputStream.read(SocketInputStream.java:171)  
INFO | jvm 2 | 2019/11/19 00:59:45.081 | at java.net.SocketInputStream.read(SocketInputStream.java:141)  
INFO | jvm 2 | 2019/11/19 00:59:45.081 | at sun.security.ssl.InputRecord.readFully(InputRecord.java:465)  
INFO | jvm 2 | 2019/11/19 00:59:45.081 | at sun.security.ssl.InputRecord.read(InputRecord.java:503)  
INFO | jvm 2 | 2019/11/19 00:59:45.081 | at sun.security.ssl.SSLSocketImpl.readRecord(SSLSocketImpl.java:975)  
INFO | jvm 2 | 2019/11/19 00:59:45.081 | - locked <0xa9cde538> (a java.lang.Object)  
INFO | jvm 2 | 2019/11/19 00:59:45.081 | at sun.security.ssl.SSLSocketImpl.readDataRecord(SSLSocketImpl.java:933)  
INFO | jvm 2 | 2019/11/19 00:59:45.081 | at sun.security.ssl.AppInputStream.read(AppInputStream.java:105)  
INFO | jvm 2 | 2019/11/19 00:59:45.081 | - locked <0xa9cdecc0> (a sun.security.ssl.AppInputStream)  
INFO | jvm 2 | 2019/11/19 00:59:45.081 | at java.io.BufferedInputStream.fill(BufferedInputStream.java:246)  
INFO | jvm 2 | 2019/11/19 00:59:45.081 | at java.io.BufferedInputStream.read(BufferedInputStream.java:265)  
INFO | jvm 2 | 2019/11/19 00:59:45.081 | - locked <0xa9cdd948> (a java.io.BufferedInputStream)  
INFO | jvm 2 | 2019/11/19 00:59:45.081 | at org.apache.commons.httpclient.HttpParser.readRawLine(HttpParser.java:78)  
INFO | jvm 2 | 2019/11/19 00:59:45.081 | at org.apache.commons.httpclient.HttpParser.readLine(HttpParser.java:106)  
INFO | jvm 2 | 2019/11/19 00:59:45.081 | at org.apache.commons.httpclient.HttpConnection.readLine(HttpConnection.java:1116)  
INFO | jvm 2 | 2019/11/19 00:59:45.081 | at org.apache.commons.httpclient.MultiThreadedHttpConnectionManager$HttpConnectionAdapter.readLine(MultiThreadedHttpConnectionManager.java:1413)  
INFO | jvm 2 | 2019/11/19 00:59:45.081 | at org.apache.commons.httpclient.HttpMethodBase.readStatusLine(HttpMethodBase.java:1973)  
INFO | jvm 2 | 2019/11/19 00:59:45.081 | at org.apache.commons.httpclient.HttpMethodBase.readResponse(HttpMethodBase.java:1735)  
INFO | jvm 2 | 2019/11/19 00:59:45.081 | at org.apache.commons.httpclient.HttpMethodBase.execute(HttpMethodBase.java:1098)  
INFO | jvm 2 | 2019/11/19 00:59:45.081 | at org.apache.commons.httpclient.HttpMethodDirector.executeWithRetry(HttpMethodDirector.java:398)  
INFO | jvm 2 | 2019/11/19 00:59:45.081 | at org.apache.commons.httpclient.HttpMethodDirector.executeMethod(HttpMethodDirector.java:171)  
INFO | jvm 2 | 2019/11/19 00:59:45.081 | at org.apache.commons.httpclient.HttpClient.executeMethod(HttpClient.java:397)  
INFO | jvm 2 | 2019/11/19 00:59:45.081 | at org.apache.commons.httpclient.HttpClient.executeMethod(HttpClient.java:323)  
INFO | jvm 2 | 2019/11/19 00:59:45.081 | at com.glide.communications.HTTPClient.executeMethod(HTTPClient.java:336)  
INFO | jvm 2 | 2019/11/19 00:59:45.081 | at com.glide.communications.HTTPRequest.send(HTTPRequest.java:166)  
INFO | jvm 2 | 2019/11/19 00:59:45.081 | at com.glide.communications.HTTPRequest.get(HTTPRequest.java:60)  
INFO | jvm 2 | 2019/11/19 00:59:45.081 | at com.glide.rest.outbound.direct.DirectRESTRequestDispatcher.doGet(DirectRESTRequestDispatcher.java:115)  
INFO | jvm 2 | 2019/11/19 00:59:45.081 | at com.glide.rest.outbound.direct.DirectRESTRequestDispatcher.doRequest(DirectRESTRequestDispatcher.java:87)  
INFO | jvm 2 | 2019/11/19 00:59:45.081 | at com.glide.rest.outbound.direct.DirectRESTRequestDispatcher.invoke(DirectRESTRequestDispatcher.java:46)  
INFO | jvm 2 | 2019/11/19 00:59:45.081 | at com.glide.rest.outbound.RESTMessageClient.invoke(RESTMessageClient.java:100)  
INFO | jvm 2 | 2019/11/19 00:59:45.081 | at com.glide.rest.outbound.RESTMessageClient.execute(RESTMessageClient.java:78)  
INFO | jvm 2 | 2019/11/19 00:59:45.081 | at com.glide.rest.outbound.scriptable.ScriptableRESTMessageClient.jsFunction\_execute(ScriptableRESTMessageClient.java:67)  
INFO | jvm 2 | 2019/11/19 00:59:45.081 | at sun.reflect.GeneratedMethodAccessor941.invoke(Unknown Source)  
INFO | jvm 2 | 2019/11/19 00:59:45.081 | at sun.reflect.DelegatingMethodAccessorImpl.invoke(DelegatingMethodAccessorImpl.java:43)  
INFO | jvm 2 | 2019/11/19 00:59:45.081 | at java.lang.reflect.Method.invoke(Method.java:498)  
INFO | jvm 2 | 2019/11/19 00:59:45.081 | at org.mozilla.javascript.MemberBox.invoke(MemberBox.java:138)  
INFO | jvm 2 | 2019/11/19 00:59:45.081 | at org.mozilla.javascript.FunctionObject.doInvoke(FunctionObject.java:670)  
INFO | jvm 2 | 2019/11/19 00:59:45.081 | at org.mozilla.javascript.FunctionObject.call(FunctionObject.java:614)  
INFO | jvm 2 | 2019/11/19 00:59:45.081 | at org.mozilla.javascript.ScriptRuntime.doCall(ScriptRuntime.java:2582)  
INFO | jvm 2 | 2019/11/19 00:59:45.081 | at org.mozilla.javascript.optimizer.OptRuntime.callProp0(OptRuntime.java:85)  
INFO | jvm 2 | 2019/11/19 00:59:45.081 | at org.mozilla.javascript.gen.sys\_script\_include\_652fec9adb65a780075e6dda4b9619d1\_script\_10314.\_c\_anonymous\_2(sys\_script\_include.652fec9adb65a780075e6dda4b9619d1.script:13)  
INFO | jvm 2 | 2019/11/19 00:59:45.081 | at org.mozilla.javascript.gen.sys\_script\_include\_652fec9adb65a780075e6dda4b9619d1\_script\_10314.call(sys\_script\_include.652fec9adb65a780075e6dda4b9619d1.script)  
INFO | jvm 2 | 2019/11/19 00:59:45.082 | at org.mozilla.javascript.ScriptRuntime.doCall2(ScriptRuntime.java:2651)  
INFO | jvm 2 | 2019/11/19 00:59:45.082 | at org.mozilla.javascript.ScriptRuntime.doCall(ScriptRuntime.java:2590)  
INFO | jvm 2 | 2019/11/19 00:59:45.082 | at org.mozilla.javascript.optimizer.OptRuntime.call1(OptRuntime.java:32)  
INFO | jvm 2 | 2019/11/19 00:59:45.082 | at org.mozilla.javascript.gen.sysevent\_script\_action\_935fa0dadb65a780075e6dda4b9619ea\_script\_10313.\_c\_script\_0(sysevent\_script\_action.935fa0dadb65a780075e6dda4b9619ea.script:2)  
INFO | jvm 2 | 2019/11/19 00:59:45.082 | at org.mozilla.javascript.gen.sysevent\_script\_action\_935fa0dadb65a780075e6dda4b9619ea\_script\_10313.call(sysevent\_script\_action.935fa0dadb65a780075e6dda4b9619ea.script)  
INFO | jvm 2 | 2019/11/19 00:59:45.082 | at org.mozilla.javascript.gen.sysevent\_script\_action\_935fa0dadb65a780075e6dda4b9619ea\_script\_10313.exec(sysevent\_script\_action.935fa0dadb65a780075e6dda4b9619ea.script)  
INFO | jvm 2 | 2019/11/19 00:59:45.082 | at com.glide.script.ScriptEvaluator.execute(ScriptEvaluator.java:279)  
INFO | jvm 2 | 2019/11/19 00:59:45.082 | at com.glide.script.ScriptEvaluator.evaluateString(ScriptEvaluator.java:118)  
INFO | jvm 2 | 2019/11/19 00:59:45.082 | at com.glide.script.ScriptEvaluator.evaluateString(ScriptEvaluator.java:82)  
INFO | jvm 2 | 2019/11/19 00:59:45.082 | at com.glide.script.fencing.GlideScopedEvaluator.evaluateScript(GlideScopedEvaluator.java:309)  
INFO | jvm 2 | 2019/11/19 00:59:45.082 | at com.glide.script.fencing.GlideScopedEvaluator.evaluateScript(GlideScopedEvaluator.java:168)  
INFO | jvm 2 | 2019/11/19 00:59:45.082 | at com.glide.policy.ScriptActionHandler.executeScriptInScope(ScriptActionHandler.java:181)  
INFO | jvm 2 | 2019/11/19 00:59:45.082 | at com.glide.policy.ScriptActionHandler.process0(ScriptActionHandler.java:60)  
INFO | jvm 2 | 2019/11/19 00:59:45.082 | at com.glide.policy.ScriptActionHandler.process(ScriptActionHandler.java:39)  
INFO | jvm 2 | 2019/11/19 00:59:45.082 | at com.glide.policy.EventProcessor.processEventDuringNormalOperation(EventProcessor.java:213)  
INFO | jvm 2 | 2019/11/19 00:59:45.082 | at com.glide.policy.EventProcessor.processEvent(EventProcessor.java:138)  
INFO | jvm 2 | 2019/11/19 00:59:45.082 | at com.glide.policy.EventProcessor.process(EventProcessor.java:92)  
INFO | jvm 2 | 2019/11/19 00:59:45.082 | at com.glide.policy.EventManager.processEvents(EventManager.java:291)  
INFO | jvm 2 | 2019/11/19 00:59:45.082 | at com.glide.policy.EventManager.\_process(EventManager.java:166)  
INFO | jvm 2 | 2019/11/19 00:59:45.082 | at com.glide.policy.EventManager.processDelegatedEvents(EventManager.java:140)  
INFO | jvm 2 | 2019/11/19 00:59:45.082 | at com.glide.script.GlideSystem.js\_processDelegatedEvents(GlideSystem.java:731)  
INFO | jvm 2 | 2019/11/19 00:59:45.082 | at sun.reflect.GeneratedMethodAccessor299.invoke(Unknown Source)  
INFO | jvm 2 | 2019/11/19 00:59:45.082 | at sun.reflect.DelegatingMethodAccessorImpl.invoke(DelegatingMethodAccessorImpl.java:43)  
INFO | jvm 2 | 2019/11/19 00:59:45.082 | at java.lang.reflect.Method.invoke(Method.java:498)  
INFO | jvm 2 | 2019/11/19 00:59:45.082 | at org.mozilla.javascript.MemberBox.invoke(MemberBox.java:138)  
INFO | jvm 2 | 2019/11/19 00:59:45.082 | at org.mozilla.javascript.FunctionObject.doInvoke(FunctionObject.java:670)  
INFO | jvm 2 | 2019/11/19 00:59:45.082 | at org.mozilla.javascript.FunctionObject.call(FunctionObject.java:614)  
INFO | jvm 2 | 2019/11/19 00:59:45.082 | at org.mozilla.javascript.ScriptRuntime.doCall(ScriptRuntime.java:2582)  
INFO | jvm 2 | 2019/11/19 00:59:45.082 | at org.mozilla.javascript.optimizer.OptRuntime.callProp0(OptRuntime.java:85)  
INFO | jvm 2 | 2019/11/19 00:59:45.082 | at org.mozilla.javascript.gen.\_refname\_\_161.\_c\_script\_0(<refname>:1)  
INFO | jvm 2 | 2019/11/19 00:59:45.082 | at org.mozilla.javascript.gen.\_refname\_\_161.call(<refname>)  
INFO | jvm 2 | 2019/11/19 00:59:45.082 | at org.mozilla.javascript.ContextFactory.doTopCall(ContextFactory.java:563)  
INFO | jvm 2 | 2019/11/19 00:59:45.082 | at org.mozilla.javascript.ScriptRuntime.doTopCall(ScriptRuntime.java:3429)  
INFO | jvm 2 | 2019/11/19 00:59:45.082 | at org.mozilla.javascript.gen.\_refname\_\_161.call(<refname>)  
INFO | jvm 2 | 2019/11/19 00:59:45.082 | at org.mozilla.javascript.gen.\_refname\_\_161.exec(<refname>)  
INFO | jvm 2 | 2019/11/19 00:59:45.082 | at com.glide.script.ScriptEvaluator.execute(ScriptEvaluator.java:279)  
INFO | jvm 2 | 2019/11/19 00:59:45.082 | at com.glide.script.ScriptEvaluator.evaluateString(ScriptEvaluator.java:118)  
INFO | jvm 2 | 2019/11/19 00:59:45.082 | at com.glide.script.ScriptEvaluator.evaluateString(ScriptEvaluator.java:82)  
INFO | jvm 2 | 2019/11/19 00:59:45.082 | at com.glide.script.ScriptEvaluator.evaluateStringWithPrefix(ScriptEvaluator.java:66)  
INFO | jvm 2 | 2019/11/19 00:59:45.082 | at com.glide.script.Evaluator.evaluatePossiblePrefixedString(Evaluator.java:208)  
INFO | jvm 2 | 2019/11/19 00:59:45.082 | at com.glide.job.RunScriptJob.evaluateScript(RunScriptJob.java:163)  
INFO | jvm 2 | 2019/11/19 00:59:45.082 | at com.glide.job.RunScriptJob.execute(RunScriptJob.java:86)  
INFO | jvm 2 | 2019/11/19 00:59:45.082 | at com.glide.schedule.JobExecutor.lambda$executeJob$0(JobExecutor.java:108)  
INFO | jvm 2 | 2019/11/19 00:59:45.082 | at com.glide.schedule.JobExecutor$$Lambda$222/3990179.call(Unknown Source)  
INFO | jvm 2 | 2019/11/19 00:59:45.082 | at com.glide.schedule.JobExecutor.executeJob(JobExecutor.java:111)  
INFO | jvm 2 | 2019/11/19 00:59:45.082 | at com.glide.schedule.JobExecutor.execute(JobExecutor.java:95)  
INFO | jvm 2 | 2019/11/19 00:59:45.082 | at com.glide.schedule\_v2.SchedulerWorkerThread.executeJob(SchedulerWorkerThread.java:329)  
INFO | jvm 2 | 2019/11/19 00:59:45.082 | at com.glide.schedule\_v2.SchedulerWorkerThread.lambda$process$0(SchedulerWorkerThread.java:192)  
INFO | jvm 2 | 2019/11/19 00:59:45.082 | at com.glide.schedule\_v2.SchedulerWorkerThread$$Lambda$212/29705465.run(Unknown Source)  
INFO | jvm 2 | 2019/11/19 00:59:45.082 | at com.glide.worker.TransactionalWorkerThread.executeInTransaction(TransactionalWorkerThread.java:35)  
INFO | jvm 2 | 2019/11/19 00:59:45.082 | at com.glide.schedule\_v2.SchedulerWorkerThread.process(SchedulerWorkerThread.java:192)  
INFO | jvm 2 | 2019/11/19 00:59:45.082 | at com.glide.schedule\_v2.SchedulerWorkerThread.run(SchedulerWorkerThread.java:100)

## Resolution

For immediate relief, contact SN Technical Support to approve the following:

1) kill the stuck transaction  
2) set the events to error  
3) cancel the scheduled jobs  
4) restart the nodes affected by the job triggered call
