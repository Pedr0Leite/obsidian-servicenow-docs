---
title: "Default MSSql DB On Windows Pattern used with the Microsoft SQL Server Process Classifier fails with null pointer exception"
aliases:
  - KB0816039
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0816039
kb_number: KB0816039
last_modified: 2025-07-03
---

## Default MSSql DB On Windows Pattern used with the Microsoft SQL Server Process Classifier fails with null pointer exception

  

### Issue

When using the MSSql DB On Windows Pattern on a Windows device with multiple database instances, the default pattern throws a hard error due to a null value in step 7 ("get instance\_name from WMI if empty"). This issue can occur even on a Windows server with a single database instance, where other instances may complete without issues. 

Error from Discovery Log: Failed Exploring CI Pattern, Pattern name: MSSql DB On Windows, Process ID: 2548, To Check Pattern Log Press Here Error from Discovery Pattern Log: get instance\_name from WMI if empty 2020-02-26 17:20:31: null java.lang.NullPointerException at com.snc.sw.kb.lang.closure.RunWmiQueryToVariableClosure.handleNameSpaceCollection(RunWmiQueryToVariableClosure.java:129) at com.snc.sw.kb.lang.closure.RunWmiQueryToVariableClosure.function(RunWmiQueryToVariableClosure.java:66) at com.snc.sw.kb.lang.closure.RunWmiQueryToVariableClosure.function(RunWmiQueryToVariableClosure.java:16) at com.snc.sw.kb.lang.closure.IfClosure.function(IfClosure.java:49) at com.snc.sw.kb.lang.closure.IfClosure.function(IfClosure.java:13) at com.snc.sw.pattern.AbstractPatternExecutor.executeStep(AbstractPatternExecutor.java:739) at com.snc.sw.pattern.DefaultPatternExecutor.executeStepsImpl(DefaultPatternExecutor.java:40) at com.snc.sw.pattern.AbstractPatternExecutor.executeSteps(AbstractPatternExecutor.java:680) at com.snc.sw.pattern.HorizontalDiscoveryPatternExecutor.executeIdentification(HorizontalDiscoveryPatternExecutor.java:203) at com.snc.sw.pattern.HorizontalDiscoveryPatternExecutor.runIdentific 2020-02-26 17:20:31: null java.lang.NullPointerException at com.snc.sw.kb.lang.closure.RunWmiQueryToVariableClosure.handleNameSpaceCollection(RunWmiQueryToVariableClosure.java:129) at com.snc.sw.kb.lang.closure.RunWmiQueryToVariableClosure.function(RunWmiQueryToVariableClosure.java:66) at com.snc.sw.kb.lang.closure.RunWmiQueryToVariableClosure.function(RunWmiQueryToVariableClosure.java:16) at com.snc.sw.kb.lang.closure.IfClosure.function(IfClosure.java:49) at com.snc.sw.kb.lang.closure.IfClosure.function(IfClosure.java:13) at com.snc.sw.pattern.AbstractPatternExecutor.executeStep(AbstractPatternExecutor.java:739) at com.snc.sw.pattern.DefaultPatternExecutor.executeStepsImpl(DefaultPatternExecutor.java:40) at com.snc.sw.pattern.AbstractPatternExecutor.executeSteps(AbstractPatternExecutor.java:680) at com.snc.sw.pattern.HorizontalDiscoveryPatternExecutor.executeIdentification(HorizontalDiscoveryPatternExecutor.java:203) at com.snc.sw.pattern.HorizontalDiscoveryPatternExecutor.runIdentifi 

### Release

All Environments.

### Cause

This error occurs because step 7 is trying to use the variable **$nm** in the namespace field but this variable is not set up with a value until step 15, where it is **set namespace attr** 

### Resolution

Copy the following steps and paste it after **step 2:list namespaces in SqlServer namespace,** and then delete the following steps after copying.

step 12:filter namespaces  
step 13:verify at least one namespace exists  
step 14:set our NM  
step 15:set namespace attr
