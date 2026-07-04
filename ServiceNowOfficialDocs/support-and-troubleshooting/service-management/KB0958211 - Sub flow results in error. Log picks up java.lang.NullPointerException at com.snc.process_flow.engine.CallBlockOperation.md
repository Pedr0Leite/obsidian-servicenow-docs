---
title: "Sub flow results in error. Log picks up:  java.lang.NullPointerException at com.snc.process_flow.engine.CallBlockOperation.lambda$run$0(CallBlockOperation.java:72)"
aliases:
  - KB0958211
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0958211
kb_number: KB0958211
last_modified: 2024-02-28
---

## Sub flow results in error. Log picks up: java.lang.NullPointerException at com.snc.process\_flow.engine.CallBlockOperation.lambda$run$0(CallBlockOperation.java:72)

  

### Issue

A subflow results in error state. If you check the logs it records a nullpointer exception:

  

Flow Designer: Operation ... failed with error: java.lang.NullPointerException

at com.snc.process\_flow.engine.CallBlockOperation.lambda$run$0(CallBlockOperation.java:72)

at com.google.common.collect.RegularImmutableMap.forEach(RegularImmutableMap.java:185)

### Cause

It fails when the subflow is finished and the output is passed back to the main flow. It loops through all the outputs, if it can't process it this error will be thrown.

  

  

  

### Resolution

You need to check the outputs of the subflow and see if there are any problems here. For example, an ouput could have type Records but not actually reference a record. This would result in this error.
