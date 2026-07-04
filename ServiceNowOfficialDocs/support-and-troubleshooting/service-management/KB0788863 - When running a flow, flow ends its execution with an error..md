---
title: "When running a flow, flow ends its execution with an error."
aliases:
  - KB0788863
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0788863
kb_number: KB0788863
last_modified: 2024-04-08
---

## Issue

Open the flow, click on "test" and run the flow.

You will see below error or something similar in the logs - 

Flow Designer: Operation(MX Child Count.If$1.evalConditions) failed with error: com.snc.process\_flow.exception.OpException: unable to evaluate condition for /if/\_0\_a0852cb2dba1c0109e7424f405961962 = is not a valid conditional expression  
at com.snc.process\_flow.engine.ConditionalBranchOperation.run(ConditionalBranchOperation.java:36)  
at com.snc.process\_flow.engine.Operation.execute(Operation.java:106)  
at com.snc.process\_flow.engine.ProcessEngine.executeOps(ProcessEngine.java:407)  
at com.snc.process\_flow.engine.ProcessEngine.run(ProcessEngine.java:355)  
at com.snc.process\_flow.engine.ProcessAutomation.run(ProcessAutomation.java:55)  
at com.snc.process\_flow.engine.GlideProcessAutomation.runSync(GlideProcessAutomation.java:126)  
at com.snc.process\_flow.engine.GlideProcessAutomation.lambda$runAsUserSync$1(GlideProcessAutomation.java:213)  
at com.snc.process\_flow.engine.GlidePFSession.runPlanAsUserSession(GlidePFSession.java:26)  
at com.snc.process\_flow.engine.GlideProcessAutomation.runAsUserSync(GlideProcessAutomation.java:205)  
at com.snc.process\_flow.engine.GlideProcessAutomation.messageFlow(GlideProcessAutomation.java:242)  
at com.snc.process\_flow.engine.GlideProcessAutomation.\_start(GlideProcessAutomation.java:364)  
at com.snc.process\_flow.engine.GlideProcessAutomation.access$400(GlideProcessAutomation.java:82)  
at com.snc.process\_flow.engine.GlideProcessAutomation$StartBuilder.start(GlideProcessAutomation.java:898)  
at com.glide.flow\_trigger.engine.TestButtonTriggerRunner.run(TestButtonTriggerRunner.java:168)  
at com.glide.flow\_trigger.engine.TestButtonTriggerRunner.test(TestButtonTriggerRunner.java:172)  
at com.glide.flow.providers.FlowGlideProvider.testFlow(FlowGlideProvider.java:992)  
at com.glide.flow\_design.rest.FlowService.testRunFlow(FlowService.java:573)  
at sun.reflect.NativeMethodAccessorImpl.invoke0(Native Method)  
at sun.reflect.NativeMethodAccessorImpl.invoke(NativeMethodAccessorImpl.java:62)  
at sun.reflect.DelegatingMethodAccessorImpl.invoke(DelegatingMethodAccessorImpl.java:43)  
at java.lang.reflect.Method.invoke(Method.java:498)  
at com.glide.rest.handler.impl.ServiceHandlerImpl.invokeService(ServiceHandlerImpl.java:44)  
at com.glide.rest.processors.RESTAPIProcessor.process(RESTAPIProcessor.java:290)  
at com.glide.processors.AProcessor.runProcessor(AProcessor.java:553)  
at com.glide.processors.AProcessor.processTransaction(AProcessor.java:240)  
at com.glide.processors.ProcessorRegistry.process0(ProcessorRegistry.java:177)  
at com.glide.processors.ProcessorRegistry.process(ProcessorRegistry.java:166)  
at com.glide.ui.GlideServletTransaction.process(GlideServletTransaction.java:31)  
at com.glide.sys.Transaction.run(Transaction.java:2203)  
at java.util.concurrent.ThreadPoolExecutor.runWorker(ThreadPoolExecutor.java:1149)  
at java.util.concurrent.ThreadPoolExecutor$Worker.run(ThreadPoolExecutor.java:624)  
at java.lang.Thread.run(Thread.java:748)  
Caused by: com.snc.process\_flow.model.InvalidProcessException: is not a valid conditional expression  
at com.snc.process\_flow.val.transform.ConditionalExpression.parseTerm(ConditionalExpression.java:124)  
at com.snc.process\_flow.val.transform.ConditionalExpression.parseTerms(ConditionalExpression.java:106)  
at com.snc.process\_flow.val.transform.ConditionalExpression.lambda$parseSet$3(ConditionalExpression.java:90)  
at java.util.stream.MatchOps$1MatchSink.accept(MatchOps.java:90)  
at java.util.Spliterators$ArraySpliterator.tryAdvance(Spliterators.java:958)  
at java.util.stream.ReferencePipeline.forEachWithCancel(ReferencePipeline.java:126)  
at java.util.stream.AbstractPipeline.copyIntoWithCancel(AbstractPipeline.java:498)  
at java.util.stream.AbstractPipeline.copyInto(AbstractPipeline.java:485)  
at java.util.stream.AbstractPipeline.wrapAndCopyInto(AbstractPipeline.java:471)  
at java.util.stream.MatchOps$MatchOp.evaluateSequential(MatchOps.java:230)  
at java.util.stream.MatchOps$MatchOp.evaluateSequential(MatchOps.java:196)  
at java.util.stream.AbstractPipeline.evaluate(AbstractPipeline.java:234)  
at java.util.stream.ReferencePipeline.allMatch(ReferencePipeline.java:454)  
at com.snc.process\_flow.val.transform.ConditionalExpression.parseSet(ConditionalExpression.java:89)  
at com.snc.process\_flow.val.transform.ConditionalExpression.lambda$value$1(ConditionalExpression.java:83)  
at java.util.stream.MatchOps$1MatchSink.accept(MatchOps.java:90)  
at java.util.Spliterators$ArraySpliterator.tryAdvance(Spliterators.java:958)  
at java.util.stream.ReferencePipeline.forEachWithCancel(ReferencePipeline.java:126)  
at java.util.stream.AbstractPipeline.copyIntoWithCancel(AbstractPipeline.java:498)  
at java.util.stream.AbstractPipeline.copyInto(AbstractPipeline.java:485)  
at java.util.stream.AbstractPipeline.wrapAndCopyInto(AbstractPipeline.java:471)  
at java.util.stream.MatchOps$MatchOp.evaluateSequential(MatchOps.java:230)  
at java.util.stream.MatchOps$MatchOp.evaluateSequential(MatchOps.java:196)  
at java.util.stream.AbstractPipeline.evaluate(AbstractPipeline.java:234)  
at java.util.stream.ReferencePipeline.anyMatch(ReferencePipeline.java:449)  
at com.snc.process\_flow.val.transform.ConditionalExpression.value(ConditionalExpression.java:82)  
at com.snc.process\_flow.engine.ConditionalBranchOperation.run(ConditionalBranchOperation.java:30)  
... 31 more

## Resolution

You will see above errors in the logs due to an empty condition defined in one of the activity on a flow.

This is considered a bug and there is a PRB opened for the issue.  
Please find the PRB number here - PRB1368903  
  
Deleting the condition should help if fixing the issue.
