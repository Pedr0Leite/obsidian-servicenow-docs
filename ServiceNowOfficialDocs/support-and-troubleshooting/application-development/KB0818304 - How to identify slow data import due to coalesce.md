---
title: "How to identify slow data import due to coalesce?"
aliases:
  - KB0818304
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0818304
kb_number: KB0818304
last_modified: 2026-06-29
---

## How to identify slow data import due to coalesce?

  

### Issue

One of the causes of slow transform is due to queries carried out by the coalesce fields while trying to locate matching records.

In order to determine if the queries being executed  during coalesce are impacting the import carry out the following steps while the transformation is ongoing:

1.  Identify the node running the import.
2.   Navigate to the worker thread processing the import.
3.  Periodically refresh the page i.e multiple times per second if possible.
4.  If you notice that the class com.glide.db.impex.transformer.MapTargetResolver consistently appears on the thread, then this is an indication that coalesce is part of the transform map is taking longer to process. 
5.  See sample stack trace below.

   ...  
  
        com.glide.script.GlideRecord.query(GlideRecord.java:3033)  
  
        com.glide.db.impex.transformer.MapTargetResolver.isMatchingRecordExists(MapTargetResolver.java:170)=====>> The coalesce logic is handled around here  
  
        com.glide.db.impex.transformer.MapTargetResolver.getTarget0(MapTargetResolver.java:162)  
  
        com.glide.db.impex.transformer.MapTargetResolver.getTargetAndAcquireLockOnNewRecord(MapTargetResolver.java:75)  
  
        com.glide.db.impex.transformer.Transformer.transformBatch(Transformer.java:154)  
  
        com.glide.db.impex.transformer.Transformer.transform(Transformer.java:82)  
  
        com.glide.system\_import\_set.ImportSetTransformerImpl.transformEach(ImportSetTransformerImpl.java:259)  
  
        com.glide.system\_import\_set.ImportSetTransformerImpl.transformAllMaps(ImportSetTransformerImpl.java:91)  
  
        com.glide.system\_import\_set.ImportSetTransformer.transformAllMaps(ImportSetTransformer.java:70)  
  
        com.glide.system\_import\_set.ImportSetTransformer.transformAllMaps(ImportSetTransformer.java:57)  
  
        com.glide.system\_import\_set.ImportSetTransformer.transformAllMaps(ImportSetTransformer.java:51)  
  
        com.snc.automation.ScheduledImportSetJob.runImport(ScheduledImportSetJob.java:114)  
  
        com.snc.automation.ScheduledImportSetJob.runNextImport(ScheduledImportSetJob.java:62)  
  
        com.snc.automation.ScheduledImportSetJob.runNextImport(ScheduledImportSetJob.java:74)  
  
        com.snc.automation.ScheduledImportSetJob.runNextImport(ScheduledImportSetJob.java:74)  
  
        com.snc.automation.ScheduledImportSetJob.runNextImport(ScheduledImportSetJob.java:74)  
  
        com.snc.automation.ScheduledImportSetJob.runNextImport(ScheduledImportSetJob.java:74)  
  
        com.snc.automation.ScheduledImportSetJob.runImport(ScheduledImportSetJob.java:50)  
  
        com.snc.automation.ScheduledImportJob.execute(ScheduledImportJob.java:45)  
  
        com.glide.schedule.JobExecutor.lambda$executeJob$0(JobExecutor.java:108)  
  
        com.glide.schedule.JobExecutor.executeJob(JobExecutor.java:111)  
  
        com.glide.schedule.JobExecutor.execute(JobExecutor.java:95)  
  
        com.glide.schedule\_v2.SchedulerWorkerThread.executeJob(SchedulerWorkerThread.java:329)  
  
        com.glide.schedule\_v2.SchedulerWorkerThread.lambda$process$0(SchedulerWorkerThread.java:192)  
  
        com.glide.worker.TransactionalWorkerThread.executeInTransaction(TransactionalWorkerThread.java:35)  
  
        com.glide.schedule\_v2.SchedulerWorkerThread.process(SchedulerWorkerThread.java:192)  
  
        com.glide.schedule\_v2.SchedulerWorkerThread.run(SchedulerWorkerThread.java:100)

### Release

All releases

### Cause

Slow processing of either the script in the coalesce field or the queries based on the coalesce field(s).

### Resolution

Identify and optimize the queries being executed based on the filters configured on the coalesce fields.

If the cause is the script configured in the coalesce field then the scripts needs to be optimized.
