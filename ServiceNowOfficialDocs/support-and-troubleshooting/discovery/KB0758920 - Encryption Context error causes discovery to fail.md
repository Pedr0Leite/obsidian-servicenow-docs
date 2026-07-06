---
title: "Encryption Context error causes discovery to fail"
aliases:
  - KB0758920
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0758920
kb_number: KB0758920
last_modified: 2024-04-07
---

## Issue

If running discovery and the result of the pattern is multi-page and of of the inputs for that multi-page errors and has the following stacktrace:

Stack:   
com.snc.sw.resulthandlers.delete.hd.SnapshotOutputItem.hashCode(SnapshotOutputItem.java:58)   
java.util.HashMap.hash(HashMap.java:339)   
java.util.HashMap.put(HashMap.java:612)   
java.util.HashSet.add(HashSet.java:220)   
com.snc.sw.resulthandlers.delete.hd.data.SaPagedPayloadDAO.mergeOutputPayload(SaPagedPayloadDAO.java:80)   
com.snc.sw.resulthandlers.HorizontalDiscoveryResultHandler.jsFunction\_runDeleteHandler(HorizontalDiscoveryResultHandler.java:372)   
sun.reflect.NativeMethodAccessorImpl.invoke0(Native Method)   
sun.reflect.NativeMethodAccessorImpl.invoke(NativeMethodAccessorImpl.java:62)   
sun.reflect.DelegatingMethodAccessorImpl.invoke(DelegatingMethodAccessorImpl.java:43)   
java.lang.reflect.Method.invoke(Method.java:498)   
org.mozilla.javascript.MemberBox.invoke(MemberBox.java:138)   
org.mozilla.javascript.FunctionObject.doInvoke(FunctionObject.java:670)   
org.mozilla.javascript.FunctionObject.call(FunctionObject.java:614)   
org.mozilla.javascript.ScriptRuntime.doCall(ScriptRuntime.java:2582)   
org.mozilla.javascript.optimizer.OptRuntime.call2(OptRuntime.java:42)   
org.mozilla.javascript.gen.discovery\_sensor\_2f32f7899f230200fe2ab0aec32e706a\_13792.\_c\_anonymous\_2(discovery\_sensor.2f32f7899f230200fe2ab0aec32e706a:143)   
org.mozilla.javascript.gen.discovery\_sensor\_2f32f7899f230200fe2ab0aec32e706a\_13792.call(discovery\_sensor.2f32f7899f230200fe2ab0aec32e706a)   
org.mozilla.javascript.ScriptRuntime.doCall2(ScriptRuntime.java:2650)

...

com.glide.schedule.GlideScheduleWorker.run(GlideScheduleWorker.java:75)   
Message:   
  
\----------------------------- (sys\_script\_include.778011130a0a0b2500c4595ad1d1d768.script; line 53) 

If there is no multi-page and discovery fails, in the node logs you will see the following stacktrace error and logs like the following:

08/15/19 08:38:17 (958) glide.scheduler.worker.5 Attempt to get cipher for encryption context '4cf466dadbbb1300a75df1f51d96197e' without authorization   
08/15/19 08:38:17 (958) glide.scheduler.worker.5 Error while creating cipher for encryption context.: no thrown error   
08/15/19 08:38:17 (960) glide.scheduler.worker.5 java.lang.NullPointerException: java.lang.NullPointerException: com.glide.encryption.PlatformEncrypterDecrypter.encrypt(PlatformEncrypterDecrypter.java:63)   
com.glide.encryption.PlatformEncrypterDecrypter.getEncryptedValue(PlatformEncrypterDecrypter.java:39)   
com.glide.element.decorator.GEPlatformEncryptedValueDecorator.decorateSetDisplayValue(GEPlatformEncryptedValueDecorator.java:67)   
com.glide.script.GlideElement.setDisplayValue(GlideElement.java:1322)   
com.glide.script.GlideElement.setDefaultValue(GlideElement.java:1437)   
com.glide.script.GlideRecord.applyDefault(GlideRecord.java:1220)   
com.glide.script.GlideRecord.applyDefaults(GlideRecord.java:1172)   
com.glide.script.GlideRecord.insert(GlideRecord.java:4773)   
com.glide.script.GlideRecord.insert(GlideRecord.java:4712)   
com.snc.cmdb.identify\_reconcile.RecordCommitter.commitInner(RecordCommitter.java:299)   
com.snc.cmdb.identify\_reconcile.RecordCommitter.commit(RecordCommitter.java:246)   
com.snc.cmdb.identify\_reconcile.IdentificationEngine.process(IdentificationEngine.java:1005)   
com.snc.cmdb.identify\_reconcile.IdentificationEngine.execute(IdentificationEngine.java:510)   
com.snc.cmdb.identify\_reconcile.IdentificationEngine.executeAndGenerateOutput(IdentificationEngine.java:448)   
com.snc.cmdb.identify\_reconcile.IdentificationEngine.execute(IdentificationEngine.java:424)   
com.snc.cmdb.identify\_reconcile.IdentificationEngine.createOrUpdateCI(IdentificationEngine.java:373) 

...

08/15/19 08:38:17 (961) glide.scheduler.worker.5 Background message, type:error, message: Invalid attempt. Encrypted data could not be saved 

## Resolution

Add mid\_server role to the read ACL for the table "sys\_encryption\_context"
