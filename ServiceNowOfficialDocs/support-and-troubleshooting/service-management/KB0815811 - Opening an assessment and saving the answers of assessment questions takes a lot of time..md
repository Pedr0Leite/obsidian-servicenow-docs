---
title: "Opening  an assessment and saving the answers of assessment questions takes a lot of time."
aliases:
  - KB0815811
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0815811
kb_number: KB0815811
last_modified: 2024-04-08
---

## Opening an assessment and saving the answers of assessment questions takes a lot of time.

  

### Issue

-   Opening an assessment and saving the answers of assessment questions takes a lot of time. You receive the error message: "There was an unexpected failure with this assessment, invalid type provided", after saving the assessment.

### Release

-   Madrid Patch 9a

### Cause

-   From stats, it showed the below:

com.glide.script.glide\_elements.GlideElementViewable.queryAttachment(GlideElementViewable.java:204)  
com.glide.script.glide\_elements.GlideElementViewable.getAttachmentID(GlideElementViewable.java:78)  
com.glide.script.glide\_elements.GlideElementUserImage.getAttachmentID(GlideElementUserImage.java:122)  
com.glide.script.glide\_elements.GlideElementUserImage.getDisplayValue(GlideElementUserImage.java:55)  
com.glide.script.glide\_elements.GlideElementViewable.getDisplayValue(GlideElementViewable.java:48)  
com.glide.script.GlideRecord.getDisplayValue(GlideRecord.java:7852)  
com.snc.assessment\_core.questionset.AssessmentTemplateQuestionSet.initJellyVariables(AssessmentTemplateQuestionSet.java:265)  
com.glideapp.questionset.Question.initJellyVariables(Question.java:244)  
com.snc.assessment\_core.questionset.AssessmentTemplateQuestionSet.render(AssessmentTemplateQuestionSet.java:222)  
com.glideapp.questionset.QuestionSet.renderList(QuestionSet.java:139)  
com.glideapp.questionset.QuestionSet.render(QuestionSet.java:53)  
com.snc.assessment\_core.TakeAssessment.doTag(TakeAssessment.java:41)

-   It will take time for page to load form that HTML and add data to it, there is a huge amount of data being loaded and I would say this as expected behavior.

### Resolution

-   It is an expected behavior because of a lot of questions for every category.

### Related Links

2020-02-26 09:23:34 (204) Default-thread-4 AE54E744DB97005083685CEFDF961987 txid=6099e7c4dbd7 WARNING \*\*\* WARNING \*\*\* GlideOutputWriter@23162440: Large amount of data has been streamed: 10,485,889 bytes  
java.lang.Thread.getStackTrace(Thread.java:1559)  
com.glide.size\_aware.StreamingBytesSizeHandler.streamedBytes(StreamingBytesSizeHandler.java:72)  
com.glide.ui.io.GlideOutputWriter.reportTotalBytesWritten(GlideOutputWriter.java:121)  
com.glide.ui.io.GlideOutputWriter.write(GlideOutputWriter.java:100)  
java.io.Writer.write(Writer.java:157)  
org.dom4j.io.XMLWriter.writeEscapeAttributeEntities(XMLWriter.java:1720)  
org.dom4j.io.XMLWriter.writeAttribute(XMLWriter.java:1522)  
org.dom4j.io.XMLWriter.writeAttributes(XMLWriter.java:1511)  
org.dom4j.io.XMLWriter.startElement(XMLWriter.java:686)  
org.apache.commons.jelly.XMLOutput.startElement(XMLOutput.java:410)  
org.apache.commons.jelly.impl.StaticTagScript.run(StaticTagScript.java:65)  
org.apache.commons.jelly.impl.ScriptBlock.run(ScriptBlock.java:146)  
org.apache.commons.jelly.impl.StaticTagScript.run(StaticTagScript.java:66)  
org.apache.commons.jelly.impl.ScriptBlock.run(ScriptBlock.java:146)  
org.apache.commons.jelly.impl.StaticTagScript.run(StaticTagScript.java:66)  
org.apache.commons.jelly.impl.ScriptBlock.run(ScriptBlock.java:146)  
org.apache.commons.jelly.impl.StaticTagScript.run(StaticTagScript.java:66)  
org.apache.commons.jelly.impl.ScriptBlock.run(ScriptBlock.java:146)  
org.apache.commons.jelly.TagSupport.invokeBody(TagSupport.java:235)  
org.apache.commons.jelly.tags.core.ForEachTag.doTag(ForEachTag.java:150)  
org.apache.commons.jelly.impl.CustomTagScript.run(CustomTagScript.java:205)  
org.apache.commons.jelly.impl.ScriptBlock.run(ScriptBlock.java:146)  
org.apache.commons.jelly.impl.StaticTagScript.run(StaticTagScript.java:66)  
org.apache.commons.jelly.impl.ScriptBlock.run(ScriptBlock.java:146)  
org.apache.commons.jelly.TagSupport.invokeBody(TagSupport.java:235)  
org.apache.commons.jelly.tags.core.IfTag.doTag(IfTag.java:88)  
org.apache.commons.jelly.impl.CustomTagScript.run(CustomTagScript.java:205)  
org.apache.commons.jelly.impl.ScriptBlock.run(ScriptBlock.java:146)  
org.apache.commons.jelly.impl.StaticTagScript.run(StaticTagScript.java:66)  
org.apache.commons.jelly.impl.ScriptBlock.run(ScriptBlock.java:146)  
org.apache.commons.jelly.impl.StaticTagScript.run(StaticTagScript.java:66)  
org.apache.commons.jelly.impl.ScriptBlock.run(ScriptBlock.java:146)  
org.apache.commons.jelly.impl.StaticTagScript.run(StaticTagScript.java:66)  
org.apache.commons.jelly.impl.ScriptBlock.run(ScriptBlock.java:146)  
org.apache.commons.jelly.impl.StaticTagScript.run(StaticTagScript.java:66)  
org.apache.commons.jelly.impl.ScriptBlock.run(ScriptBlock.java:146)  
org.apache.commons.jelly.impl.StaticTagScript.run(StaticTagScript.java:66)  
org.apache.commons.jelly.impl.ScriptBlock.run(ScriptBlock.java:146)  
org.apache.commons.jelly.impl.StaticTagScript.run(StaticTagScript.java:66)  
org.apache.commons.jelly.impl.ScriptBlock.run(ScriptBlock.java:146)  
org.apache.commons.jelly.impl.StaticTagScript.run(StaticTagScript.java:66)  
org.apache.commons.jelly.impl.ScriptBlock.run(ScriptBlock.java:146)  
org.apache.commons.jelly.TagSupport.invokeBody(TagSupport.java:235)  
org.apache.commons.jelly.tags.core.JellyTag.doTag(JellyTag.java:84)  
org.apache.commons.jelly.impl.CustomTagScript.run(CustomTagScript.java:205)  
com.glide.ui.jelly.GlideJellyContext.run(GlideJellyContext.java:668)  
com.glide.ui.jelly.GlideJellyContext.runScript(GlideJellyContext.java:805)  
com.glide.ui.jelly.tags.BaseTag.invokerNoRef(BaseTag.java:141)  
com.glide.ui.jelly.tags.BaseTag.invoker(BaseTag.java:121)  
com.snc.assessment\_core.questionset.AssessmentTemplateQuestionSet.render(AssessmentTemplateQuestionSet.java:223)  
com.glideapp.questionset.QuestionSet.renderList(QuestionSet.java:139)  
com.glideapp.questionset.QuestionSet.render(QuestionSet.java:53)  
com.snc.assessment\_core.TakeAssessment.doTag(TakeAssessment.java:41)  
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
com.glide.processors.AProcessor.runProcessor(AProcessor.java:531)  
com.glide.processors.AProcessor.processTransaction(AProcessor.java:229)  
com.glide.processors.ProcessorRegistry.process0(ProcessorRegistry.java:188)  
com.glide.processors.ProcessorRegistry.process(ProcessorRegistry.java:177)  
com.glide.ui.GlideServletTransaction.process(GlideServletTransaction.java:31)  
com.glide.sys.Transaction.run(Transaction.java:2136)  
java.util.concurrent.ThreadPoolExecutor.runWorker(ThreadPoolExecutor.java:1149)  
java.util.concurrent.ThreadPoolExecutor$Worker.run(ThreadPoolExecutor.java:624)  
java.lang.Thread.run(Thread.java:748)
