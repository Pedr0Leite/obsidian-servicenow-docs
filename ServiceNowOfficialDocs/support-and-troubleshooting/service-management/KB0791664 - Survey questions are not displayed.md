---
title: "Survey questions are not displayed "
aliases:
  - KB0791664
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0791664
kb_number: KB0791664
last_modified: 2025-11-13
---

## Issue

When accessing the survey URL, an empty page is displayed rather than the expected questions.

Example URL:

https://instance\_name.service-now.com/assessment\_take2.do?sysparm\_assessable\_type=b934d606dbfa3b4021171c0e049619a9

The system and debug logs might show errors like this: 

Time: 0:00:00.000 for: uxcuat\_2\[glide.29\] SELECT ... FROM asmt\_assessable\_record asmt\_assessable\_record0 WHERE asmt\_assessable\_record0.\`metric\_type\` = 'b934d606dbfa3b4021171c0e049619a9' AND asmt\_assessable\_record0.\`sys\_domain\` IN ('global' , 'ddc9c52edb86f740ce3964d3149619ed') limit 0,100000 /\*...\*/  
java.lang.NullPointerException: java.lang.NullPointerException:  
com.snc.assessment\_core.questionset.AssessmentQuestionSet.load(AssessmentQuestionSet.java:296)   
com.snc.assessment\_core.TakeAssessment.doTag(TakeAssessment.java:38)   
org.apache.commons.jelly.impl.CustomTagScript.run(CustomTagScript.java:205)   
org.apache.commons.jelly.impl.ScriptBlock.run(ScriptBlock.java:146)   
org.apache.commons.jelly.impl.StaticTagScript.run(StaticTagScript.java:66)   
org.apache.commons.jelly.impl.ScriptBlock.run(ScriptBlock.java:146)   
org.apache.commons.jelly.impl.StaticTagScript.run(StaticTagScript.java:66)   
org.apache.commons.jelly.impl.ScriptBlock.run(ScriptBlock.java:146)   
org.apache.commons.jelly.impl.StaticTagScript.run(StaticTagScript.java:66)   
org.apache.commons.jelly.impl.ScriptBlock.run(ScriptBlock.java:146)   
org.apache.commons.jelly.TagSupport.invokeBody(TagSupport.java:235)   
com.glide.ui.jelly.tags.StaticFormTag.invokeBody(StaticFormTag.java:25)   
com.glide.ui.jelly.tags.BaseStaticTag.doTag(BaseStaticTag.java:26)   
org.apache.commons.jelly.impl.CustomTagScript.run(CustomTagScript.java:205)   
org.apache.commons.jelly.TagSupport.invokeBody(TagSupport.java:235)   
com.glide.ui.jelly.tags.FileinfoTag2.doTag(FileinfoTag2.java:44)   
org.apache.commons.jelly.impl.CustomTagScript.run(CustomTagScript.java:205)   
org.apache.commons.jelly.impl.ScriptBlock.run(ScriptBlock.java:146)   
org.apache.commons.jelly.TagSupport.invokeBody(TagSupport.java:235)   
com.glide.ui.jelly.tags.FileinfoTag2.doTag(FileinfoTag2.java:44)   
org.apache.commons.jelly.impl.CustomTagScript.run(CustomTagScript.java:205)   
org.apache.commons.jelly.impl.ScriptBlock.run(ScriptBlock.java:146)   
org.apache.commons.jelly.TagSupport.invokeBody(TagSupport.java:235)   
com.glide.ui.jelly.tags.FileinfoTag2.doTag(FileinfoTag2.java:44)   
org.apache.commons.jelly.impl.CustomTagScript.run(CustomTagScript.java:205)   
org.apache.commons.jelly.impl.ScriptBlock.run(ScriptBlock.java:146)   
org.apache.commons.jelly.impl.StaticTagScript.run(StaticTagScript.java:66)   
org.apache.commons.jelly.impl.ScriptBlock.run(ScriptBlock.java:146)   
org.apache.commons.jelly.impl.StaticTagScript.run(StaticTagScript.java:66)   
org.apache.commons.jelly.impl.ScriptBlock.run(ScriptBlock.java:146)   
org.apache.commons.jelly.TagSupport.invokeBody(TagSupport.java:235)   
com.glide.ui.jelly.tags.FileinfoTag2.doTag(FileinfoTag2.java:44)   
org.apache.commons.jelly.impl.CustomTagScript.run(CustomTagScript.java:205)   
org.apache.commons.jelly.TagSupport.invokeBody(TagSupport.java:235)   
org.apache.commons.jelly.tags.core.JellyTag.doTag(JellyTag.java:84)   
org.apache.commons.jelly.impl.CustomTagScript.run(CustomTagScript.java:205)   
com.glide.ui.jelly.GlideJellyContext.run(GlideJellyContext.java:668)   
com.glide.ui.jelly.GlideJellyContext.executeCompiledScript(GlideJellyContext.java:896)   
com.glide.ui.jelly.GlideJellyContext.runScript(GlideJellyContext.java:749)   
com.glide.ui.jelly.GlideJellyContext.runScript(GlideJellyContext.java:707)   
com.glide.ui.GlideFormPhase2.generate(GlideFormPhase2.java:49)   
com.glide.ui.GlideForm.generatePopulatedForm(GlideForm.java:707)   
com.glide.ui.GlideForm.generatePopulatedForm(GlideForm.java:692)   
com.glide.ui.GlideForm.populateForm(GlideForm.java:684)   
com.glide.ui.GlideForm.getRenderedPage(GlideForm.java:228)   
com.glide.ui.NavigationTransaction.writeOutput(NavigationTransaction.java:157)   
com.glide.ui.NavigationTransaction.process(NavigationTransaction.java:128)  
com.glide.ui.GlideServletUITransaction.process(GlideServletUITransaction.java:110)   
com.glide.processors.AProcessor.runProcessor(AProcessor.java:532)   
com.glide.processors.AProcessor.processTransaction(AProcessor.java:230)   
com.glide.processors.ProcessorRegistry.process0(ProcessorRegistry.java:178)   
com.glide.processors.ProcessorRegistry.process(ProcessorRegistry.java:167)   
com.glide.ui.GlideServletTransaction.process(GlideServletTransaction.java:31)   
com.glide.sys.Transaction.run(Transaction.java:2091)   
java.util.concurrent.ThreadPoolExecutor.runWorker(ThreadPoolExecutor.java:1149)   
java.util.concurrent.ThreadPoolExecutor$Worker.run(ThreadPoolExecutor.java:624)   
java.lang.Thread.run(Thread.java:748)   
Time: 0:00:00.001 for: uxcuat\_2\[glide.4\] SELECT ... FROM asmt\_assessment\_instance asmt\_assessment\_instance0 WHERE asmt\_assessment\_instance0.\`sys\_id\` = '35775079db718814ce3964d314961949' AND asmt\_assessment\_instance0.\`sys\_domain\` IN ('global' , 'ddc9c52edb86f740ce3964d3149619ed') /\*...\*/   
Missing assessment: noquestions: no thrown error

## Resolution

Re-adding the expected dependencies **from the Survey Designer** and saving the survey fixed the issue.
