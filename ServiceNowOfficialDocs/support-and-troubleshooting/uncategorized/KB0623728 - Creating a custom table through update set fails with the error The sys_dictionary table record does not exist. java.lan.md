---
title: "Creating a custom table through update set fails with the error: The sys_dictionary table record does not exist.: java.lang.IllegalStateException: Missing metadata record for table <table_name>"
aliases:
  - KB0623728
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0623728
kb_number: KB0623728
last_modified: 2024-04-07
---

## Issue

Creating a custom table through update set fails: The sys\_dictionary table record does not exist.: java.lang.IllegalStateException: Missing metadata record for table <table\_name>

Problem

* * *

Trying to create a standalone table (for example, u\_history) by committing an update set fails to create the table. The table exists in sys\_db\_object and the columns exist in sys\_dictionary, but the 'collection' record in sys\_dictionary (which is a placeholder for the table itself) is not created. Also, the table is not created in the database.  Errors are found in the localhost log during the update set commit.  

Symptoms

* * *

The error seen in the log is similar to the following example.

\==================   
2017-06-06 02:35:31 (255) Committing update set: TC - History Table 2 SYSTEM Loading repeated update (second pass) from database: sys\_dictionary\_u\_history\_u\_table\_name with update date 06/06/2017 12:   
35:24   
2017-06-06 02:35:31 (270) Committing update set: TC - History Table 2 SYSTEM SEVERE \*\*\* ERROR \*\*\* Missing metadata record for table u\_history. The sys\_dictionary table record does not exist.   
java.lang.IllegalStateException: Missing metadata record for table u\_history. The sys\_dictionary table record does not exist.   
at com.glide.update.loader.schema.TableSchemaLoader.throwExceptionForInvalidTableMetadataStateAsCouldNotRetrieveTheRecordFor(TableSchemaLoader.java:259)   
at com.glide.update.loader.schema.TableSchemaLoader.ensureBothTheCollectionAndDBObjectRecordsExist(TableSchemaLoader.java:206)   
at com.glide.update.loader.schema.TableSchemaLoader.ensureCanAlterTableOrThrowException(TableSchemaLoader.java:108)   
at com.glide.update.loader.schema.TableSchemaLoader.alterTable(TableSchemaLoader.java:89)   
at com.snc.apps.update.dictionary.DictionaryAlterer.alterTableSchema(DictionaryAlterer.java:108)   
at com.snc.apps.update.dictionary.DictionaryAlterer.alterTableSchemaWithAllPendingAlterFields(DictionaryAlterer.java:49)   
at com.glide.update.loader.DictionaryUpdateLoader.alterTableIfPendingAlterAndClearAlterState(DictionaryUpdateLoader.java:458)   
at com.glide.update.loader.DictionaryUpdateLoader.load(DictionaryUpdateLoader.java:101)   
at com.snc.apps.file.update.AbstractFileHandler.writeRecord(AbstractFileHandler.java:240)   
at com.snc.apps.file.update.FileManager.writeRecord(FileManager.java:225)   
at com.glide.update.UpdateController.loadDocument(UpdateController.java:476)   
at com.glide.update.UpdateController.loadDocument(UpdateController.java:424)   
at com.glide.update.UpdateManager2.loadDocument(UpdateManager2.java:537)   
at com.glide.update.UpdateManager2.processRecords(UpdateManager2.java:1123)   
at com.glide.update.UpdateManager2.loadItems(UpdateManager2.java:1065)   
at com.glide.update.UpdateManager2.loadSetItems(UpdateManager2.java:1023)   
at com.glide.update.UpdateManager2.commitUpdateSet0(UpdateManager2.java:933)   
at com.glide.update.UpdateManager2.commitUpdateSet(UpdateManager2.java:906)   
at com.glide.update.UpdateSetWorker.commitUpdateSet(UpdateSetWorker.java:822)   
at com.glide.update.UpdateSetWorker.startWork(UpdateSetWorker.java:132)   
at com.glide.worker.AbstractProgressWorker.startAndWait(AbstractProgressWorker.java:86)   
at com.glide.worker.HierarchicalProgressWorker.startAndWait(HierarchicalProgressWorker.java:37)   
at com.glide.worker.ProgressWorkerThread.run(ProgressWorkerThread.java:53)   
  
2017-06-06 02:35:31 (274) Committing update set: TC - History Table 2 SYSTEM Loading update 37 of 50 from database: sys\_dictionary\_u\_history\_null with update date 06/06/2017 12:35:24   
2017-06-06 02:35:31 (285) Committing update set: TC - History Table 2 SYSTEM DictionaryUpdateLoader: Table u\_history already exists - skipping the load   

Cause

* * *

A database view already exists on the target instance with the same name as the table. Creating a new database view with a name that already exists as a table\_name is not allowed, but the other way around is possible when creating the table through an update set.  

  
Resolution

* * *

Before following this procedure, confirm that the symptoms are as follows:

-   sys\_db\_object record exists
-   sys\_dictionary records exist for the columns, but not for the collection record
-   The table does not actually exist in the database
-   A database view exists with the same name as the table

If these conditions are not met, then the the following procedre will delete the records from the dictionary but not delete the physical table from the database (if it exists).

If that is the case:

1.  In Database Views, find and select the record having the same name as the table and delete it.
    
    For more information, see the product documentation topic [Database views in the base system](https://docs.servicenow.com/csh?topicname=r_DatabaseViewsInTheBaseSystem.html&version=latest).
    
2.  Navigate to **System Definition > Scripts - Background** (sys.scripts.do) and execute the following script (replace "u\_history" with the actual tablename:
    
    \---   
    var dictGR = new GlideRecord("sys\_dictionary");   
    dictGR.addQuery("name", "u\_history");   
    dictGR.query();   
    dictGR.setWorkflow(false);   
    dictGR.setUseEngines(false);   
    dictGR.deleteMultiple();   
    GlideTableManager.invalidateTable("u\_history");   
      
    var dbObjGR = new GlideRecord("sys\_db\_object");   
    dbObjGR.addQuery("name", "u\_history");   
    dbObjGR.query();   
    dbObjGR.setWorkflow(false);   
    dbObjGR.setUseEngines(false);   
    dbObjGR.deleteMultiple();   
    GlideCacheManager.flush("OBJECT\_MANAGER");   
    \--
    
3.  Verify that there are no more records in sys\_db\_object and sys\_dictionary with the name of the table.
    
4.  Try to re-create the table, preferably through a new update set where you capture creating the table on the dev instance.
    
    Do NOT capture deleting the table in that update set as well as that may lead to collisions.
