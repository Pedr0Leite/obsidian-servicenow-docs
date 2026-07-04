---
title: "When flow tries to run we get the following error: failed with error: java.lang.IllegalArgumentException: <field_name> is not a valid dot-walk for record <table_name>:<sys_id_of_record>"
aliases:
  - KB0961555
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0961555
kb_number: KB0961555
last_modified: 2025-03-13
---

## When flow tries to run we get the following error: failed with error: java.lang.IllegalArgumentException: is not a valid dot-walk for record :

  

### Issue

-   flow errors out when it tries to executes
-   we get the following sample NPE:

Flow Designer: Operation(Create A Request./start) failed with error: java.lang.IllegalArgumentException: name is not a valid dot-walk for record u\_division\_one:e94c1a583c607d0098d77544db388b98
at com.snc.process\_flow.val.transform.GRDotWalker.getElement(GRDotWalker.java:135)
at com.snc.process\_flow.val.transform.GRDotWalker.value(GRDotWalker.java:41)
at com.snc.process\_flow.val.transform.DotWalker.value(DotWalker.java:35)
at com.snc.process\_flow.val.InVal.valueReady(InVal.java:235)
at com.snc.process\_flow.val.OutVal.lambda$value$0(OutVal.java:61)
at java.lang.Iterable.forEach(Iterable.java:75)
at com.snc.process\_flow.val.OutVal.value(OutVal.java:61)
at com.snc.process\_flow.engine.DirectiveOperation.lambda$run$0(DirectiveOperation.java:18)
at com.google.common.collect.RegularImmutableMap.forEach(RegularImmutableMap.java:185)
at com.snc.process\_flow.engine.DirectiveOperation.run(DirectiveOperation.java:13)
at com.snc.process\_flow.engine.Operation.execute(Operation.java:165)
at com.snc.process\_flow.engine.ProcessEngine.executeOps(ProcessEngine.java:498)
at com.snc.process\_flow.engine.ProcessEngine.run(ProcessEngine.java:414)
at com.snc.process\_flow.engine.ProcessAutomation.run(ProcessAutomation.java:66)
at com.snc.process\_flow.engine.GlideProcessAutomation.runSync(GlideProcessAutomation.java:158)
at com.snc.process\_flow.engine.GlideProcessAutomation.runWithDomain(GlideProcessAutomation.java:261)
at com.snc.process\_flow.engine.GlideProcessAutomation.lambda$runAsUserSync$1(GlideProcessAutomation.java:239)
at com.snc.process\_flow.engine.PFSessionClone.run(PFSessionClone.java:58)
at com.snc.process\_flow.engine.GlidePFSession.runPlanAsUserSession(GlidePFSession.java:42)
at com.snc.process\_flow.engine.GlideProcessAutomation.runAsUserSync(GlideProcessAutomation.java:237)
at com.snc.process\_flow.engine.GlideProcessAutomation.messageFlow(GlideProcessAutomation.java:292)
at com.snc.process\_flow.engine.ProcessHubEventHandler.doSendMessage(ProcessHubEventHandler.java:301)
at com.snc.process\_flow.engine.ProcessHubEventHandler.process(ProcessHubEventHandler.java:77)
at com.glide.policy.EventProcessor.process(EventProcessor.java:261)
at com.glide.policy.EventProcessor.processEventDuringNormalOperation(EventProcessor.java:225)
at com.glide.policy.EventProcessor.processEvent(EventProcessor.java:149)
at com.glide.policy.EventProcessor.process(EventProcessor.java:102)
at com.glide.policy.EventManager.processEvents(EventManager.java:310)
at com.glide.policy.EventManager.\_process(EventManager.java:185)
at com.glide.policy.EventManager.processDelegatedEvents(EventManager.java:159)

### Resolution

-   the issue is due to an inline script trying to dot walk to an invalid field name
-   use the correct field name, save & publish flow
