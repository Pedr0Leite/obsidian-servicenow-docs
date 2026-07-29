---
title: "[Error] Service Analytics group alerts using RCA/Alert Aggregation"
aliases:
  - KB0778315
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0778315
kb_number: KB0778315
last_modified: 2024-04-08
---

## Issue

Event management RCA/Alert Aggregation job throws following Null Pointer error in the system logs:

java.lang.NullPointerException  
Caused by error in <refname> at line 2  
com.snc.sa.analytics.processor.ServiceAnalyticsProcessor.query(ServiceAnalyticsProcessor.java:434)  
com.snc.sa.analytics.processor.ServiceAnalyticsProcessor.jsFunction\_query(ServiceAnalyticsProcessor.java:151)  
sun.reflect.GeneratedMethodAccessor321.invoke(Unknown Source)  
sun.reflect.DelegatingMethodAccessorImpl.invoke(DelegatingMethodAccessorImpl.java:43)  
java.lang.reflect.Method.invoke(Method.java:498)  
org.mozilla.javascript.MemberBox.invoke(MemberBox.java:138)  
org.mozilla.javascript.FunctionObject.doInvoke(FunctionObject.java:670)  
org.mozilla.javascript.FunctionObject.call(FunctionObject.java:614)  
org.mozilla.javascript.ScriptRuntime.doCall(ScriptRuntime.java:2582)  
org.mozilla.javascript.optimizer.OptRuntime.callProp0(OptRuntime.java:85)  
org.mozilla.javascript.gen.\_refname\_\_3501.\_c\_script\_0(<refname>:2)  
org.mozilla.javascript.gen.\_refname\_\_3501.call(<refname>)  
org.mozilla.javascript.ContextFactory.doTopCall(ContextFactory.java:563)  
org.mozilla.javascript.ScriptRuntime.doTopCall(ScriptRuntime.java:3429)  
org.mozilla.javascript.gen.\_refname\_\_3501.call(<refname>)  
org.mozilla.javascript.gen.\_refname\_\_3501.exec(<refname>)  
com.glide.script.ScriptEvaluator.execute(ScriptEvaluator.java:279)  
com.glide.script.ScriptEvaluator.evaluateString(ScriptEvaluator.java:118)  
com.glide.script.ScriptEvaluator.evaluateString(ScriptEvaluator.java:82)  
com.glide.script.ScriptEvaluator.evaluateString(ScriptEvaluator.java:73)  
com.glide.script.Evaluator.evaluateString(Evaluator.java:91)  
com.snc.automation.ScriptJob.execute(ScriptJob.java:43)  
com.glide.schedule.JobExecutor.lambda$executeJob$306(JobExecutor.java:108)  
com.glide.schedule.JobExecutor.executeJob(JobExecutor.java:111)  
com.glide.schedule.JobExecutor.execute(JobExecutor.java:95)  
com.glide.schedule.GlideScheduleWorker.executeJob(GlideScheduleWorker.java:236)  
com.glide.schedule.GlideScheduleWorker.lambda$process$304(GlideScheduleWorker.java:165)  
com.glide.worker.TransactionalWorkerThread.executeInTransaction(TransactionalWorkerThread.java:35)  
com.glide.schedule.GlideScheduleWorker.process(GlideScheduleWorker.java:165)  
com.glide.schedule.GlideScheduleWorker.run(GlideScheduleWorker.java:75)

## Resolution

1) Make sure that the following hash record on sa\_hash table is present:

last\_alert\_update\_sa

-   If it does not exist create it with that name OR import it from an instance where it does exist.
-   Ensure the time set in the 'Hash' field is before current time (can be set to one minute before)

2) Ensure that scheduled job "Service Analytics group alerts using RCA/Alert Aggregation" is OOTB.

3) Toggle the following system property to 'false' and 'true' again:

sa\_analytics.rca\_enabled

4) Go back to the scheduled job in step 2 above and click Execute Now.
