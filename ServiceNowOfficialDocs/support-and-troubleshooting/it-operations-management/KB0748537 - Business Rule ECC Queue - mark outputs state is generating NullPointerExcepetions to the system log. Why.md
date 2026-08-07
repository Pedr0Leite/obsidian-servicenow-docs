---
title: "Business Rule \"ECC Queue - mark outputs state\" is generating NullPointerExcepetions to the system log. Why?"
aliases:
  - KB0748537
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0748537
kb_number: KB0748537
last_modified: 2024-04-07
---

## Business Rule "ECC Queue - mark outputs state" is generating NullPointerExcepetions to the system log. Why?

  

### Issue

You may start to see a lot of NullPointerExcepetions in the System Log, looking like the following:

java.lang.NullPointerException: org.mozilla.javascript.JavaScriptException: java.lang.NullPointerException: org.mozilla.javascript.Context.makeJavaScriptException(Context.java:1935)  
org.mozilla.javascript.Context.throwAsScriptRuntimeEx(Context.java:1921)  
org.mozilla.javascript.MemberBox.invoke(MemberBox.java:143)  
org.mozilla.javascript.NativeJavaMethod.call(NativeJavaMethod.java:292)  
org.mozilla.javascript.ScriptRuntime.doCall(ScriptRuntime.java:2585)  
org.mozilla.javascript.optimizer.OptRuntime.call2(OptRuntime.java:42)  
org.mozilla.javascript.gen.sys\_script\_270373260a0a0b020024aa74055d1fbf\_script\_647.\_c\_markComplete\_1(sys\_script.270373260a0a0b020024aa74055d1fbf.script:28)  
org.mozilla.javascript.gen.sys\_script\_270373260a0a0b020024aa74055d1fbf\_script\_647.call(sys\_script.270373260a0a0b020024aa74055d1fbf.script)  
org.mozilla.javascript.ScriptRuntime.doCall2(ScriptRuntime.java:2650)  
org.mozilla.javascript.ScriptRuntime.doCall(ScriptRuntime.java:2590)

### Release

Believed to be from London or Madrid

### Cause

This is most likely caused by the removal of ECC Queue table from the Table Rotation configuration.

To confirm this is the issue, navigate to **System Definition >> Table Rotations.  
**Check if the ecc\_queue table record is present. If it's not, then this is most likely the issue.  
  
The reason behind this is that the Business Rule script calls, Out of the box, for the sys\_table\_name, to get the most current rotated table name.

	if (state \== 'processing') {
		// get the real rotated table name: mutli-update does not take care of table rotation
		var sys\_table\_name \= gr.getValue('sys\_table\_name');

If we remove the table from the Rotation configuration, the script can't figure it out the name of it, and therefore, will throw NullPointerExcepetions to the log.

### Resolution

To solve those NullPointerExcepetions (NPE) errors, you should include back the ecc\_queue to the Table Rotation configuration. This is the expected OOTB configuration for the ECC Queue on new instances.

Search in Docs for "Apply table rotation" to capture the steps needed for your release and make sure it looks like an Out of the box configuration.

![](sys_attachment.do?sys_id=9d8e3862db0ab450e515c2230596193c)

### Related Links

The "ECC Queue - mark outputs state" Business rule is fixed so non-rotated ECC Queue tables still work, by PRB1368654 in the Paris release.

A Paris instance running on Oracle database will probably need the table rotation turning off to avoid PRB1429007. That should not cause this problem, but a Table Cleaner \[sys\_auto\_flush\] will need adding set at 5 days old, to keep the size of the table equivalent to if rotation was being used.
