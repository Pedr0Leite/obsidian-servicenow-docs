---
title: "How to debug the Identification and Reconciliation Engine using background scripts"
aliases:
  - KB0793220
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0793220
kb_number: KB0793220
last_modified: 2025-12-22
---

## How to debug the Identification and Reconciliation Engine using background scripts

  

### Summary

Troubleshoot unexpected Discovery or SCCM results by running Identification and Reconciliation Engine (IRE) API calls from background scripts to generate detailed debug information. When Discovery or integration processes do not insert or update records as expected, you can use IRE API calls in background scripts to isolate debug output from other system activity. This approach provides cleaner log data than searching the system log during active Discovery jobs.

### Release

All supported releases

### Instructions

### Before you begin

**Warning:** The scripts in this article insert or update records. Perform this troubleshooting in a **non-production instance only**. If you must debug in production, verify you have permission to insert or update records.

**Requirements**

-   IRE input payload (see Finding the IRE payload section)
-   User with admin privileges
-   Access to **System Definition** > **Scripts - Background**

**Note:** Not all users have access to background scripts or the APIs used in these examples.

**Alternative method**

You can also use the Identification Simulation module at **Configuration** \> **Identification/Reconciliation** > **Identification Simulation**. However, this module does not provide the same level of debug data that may be necessary to identify the root cause of an issue.

**Why use background scripts**

Debug information is available in the system log, but if Discovery jobs are running, the data can be difficult to isolate. Debug statements from background scripts are isolated to your session, making the output easier to analyze.

### Find the IRE payload

The IRE input payload is logged each time it is sent to the API.

1.  Go to **System Logs** > **System Log** > **All**.
2.  Search for records where Message contains "**input =**".
3.  If the payload is not found or the event occurred in the past, reprocess the ECC Queue input or rerun Discovery, then search again.

### Enable IRE debug logging

If the IRE payload is not logged, add the following system property:

-   Property name: glide.cmdb.logger.source.identification\_engine
-   Property value: info,warn,error,debug,debugVerbose

**Warning:** Revert this property to the default value of **info,warn,error** when debugging is complete.

If the IRE payload is still not found after adding this property, the process inserting or updating records is not using the IRE API.

### Run the debug script

Use the following script to run IRE API calls from background scripts:

var payload = <IRE\_Payload>;  
var discoverySource = "ServiceNow";  
var output = SNC.IdentificationEngineScriptableApi.createOrUpdateCI(discoverySource, JSON.stringify(payload));  
gs.print(output);

**Payload format**

The IRE\_Payload must be a JSON object (not a string) in the following format:

{"fld1":"val1","fld2":"val2"}

**Sample payload**

{"items":\[{"className":"cmdb\_ci\_win\_server","values":{"company":"86c1f3193790200044e0bfc8bcbe5d95","install\_status":"1","ip\_address":"10.20.30.41","location":"a63c49b037d0200044e0bfc8bcbe5dd9","mac\_address":"ABCD1234","manufacturer":"0c43c22bc611227500002515e25bf079","model\_id":"4431c26b37913000158bbfc8bcbe5d0d","name":"SNCTest Win Server 100","operational\_status":"1","ram":"2048","serial\_number":"SNC123456789"}}\]} 

### Example script with payload

The following example includes gs.trace(true) to display SQL statements. This is not necessary in every scenario but can help identify query-level issues.

var payload = {"items":\[{"className":"cmdb\_ci\_win\_server","values":{"company":"86c1f3193790200044e0bfc8bcbe5d95","install\_status":"1","ip\_address":"10.20.30.40","location":"a63c49b037d0200044e0bfc8bcbe5dd9","mac\_address":"ABCD1234","manufacturer":"0c43c22bc611227500002515e25bf079","model\_id":"4431c26b37913000158bbfc8bcbe5d0d","name":"SNCTest Win Server 100","operational\_status":"1","ram":"2048","serial\_number":"SNC123456789"}}\]};  
  
var discoverySource = "ServiceWatch";  
gs.trace(true);  
var output = SNC.IdentificationEngineScriptableApi.createOrUpdateCI(discoverySource, JSON.stringify(payload));  
gs.trace(false);  
gs.print(output); 

### Example Call Output

The following output shows a typical IRE debug response. Key lines are explained after the output.

identification\_engine : IdentificationEngine::process: Pass=1  
identification\_engine : addAttempt \[{"className":"cmdb\_ci\_win\_server","values":{"operational\_status":"1","discovery\_source":"ServiceWatch","install\_status":"1","mac\_address":"ABCD1234","name":"SNCTest002","serial\_number":"SNC123456789","company":"86c1f3193790200044e0bfc8bcbe5d95","location":"a63c49b037d0200044e0bfc8bcbe5dd9","ip\_address":"10.20.30.41","model\_id":"4431c26b37913000158bbfc8bcbe5d0d","manufacturer":"0c43c22bc611227500002515e25bf079","ram":"2048"},"internal\_id":"37dadd3adbd674104a9a53ca1184b9ac","sys\_object\_source\_info":{"source\_name":"ServiceWatch"},"settings":{},"sys\_ire\_info":{"ire\_received\_time":"2021-09-03 15:33:31"}}\] - \[sys\_object\_source\] SKIPPED  
identification\_engine : addAttempt \[{"className":"cmdb\_ci\_win\_server","values":{"operational\_status":"1","discovery\_source":"ServiceWatch","install\_status":"1","mac\_address":"ABCD1234","name":"SNCTest002","serial\_number":"SNC123456789","company":"86c1f3193790200044e0bfc8bcbe5d95","location":"a63c49b037d0200044e0bfc8bcbe5dd9","ip\_address":"10.20.30.41","model\_id":"4431c26b37913000158bbfc8bcbe5d0d","manufacturer":"0c43c22bc611227500002515e25bf079","ram":"2048"},"internal\_id":"37dadd3adbd674104a9a53ca1184b9ac","sys\_object\_source\_info":{"source\_name":"ServiceWatch"},"settings":{},"sys\_ire\_info":{"ire\_received\_time":"2021-09-03 15:33:31"}}\] - \[Rule id:c12f9be8c3400200d8d4bea192d3aea6|cmdb\_ci\_hardware|cmdb\_serial\_number|\[serial\_number, serial\_number\_type\]\] SKIPPED  
identification\_engine : addAttempt \[{"className":"cmdb\_ci\_win\_server","values":{"operational\_status":"1","discovery\_source":"ServiceWatch","install\_status":"1","mac\_address":"ABCD1234","name":"SNCTest002","serial\_number":"SNC123456789","company":"86c1f3193790200044e0bfc8bcbe5d95","location":"a63c49b037d0200044e0bfc8bcbe5dd9","ip\_address":"10.20.30.41","model\_id":"4431c26b37913000158bbfc8bcbe5d0d","manufacturer":"0c43c22bc611227500002515e25bf079","ram":"2048"},"internal\_id":"37dadd3adbd674104a9a53ca1184b9ac","sys\_object\_source\_info":{"source\_name":"ServiceWatch"},"settings":{},"sys\_ire\_info":{"ire\_received\_time":"2021-09-03 15:33:31"}}\] - \[Rule id:fb27f69cc3000200d8d4bea192d3ae67|cmdb\_ci\_hardware|\[serial\_number\]\] MATCHED  
identification\_engine : createOrUpdateCI: Matched 1 records and 0 relations in 4msec  
identification\_engine : Reconciliation: update to field 'name' of CI 'a853dd72dbd674104fa1c9db1396190e' was skipped because of rules \[60d9117adbd674104fa1c9db13961986\] defined in cmdb\_reconciliation\_definition  
identification\_engine : Reconciliation: cmdb\_ci\_win\_server(name) field update skipped for Data Source ServiceWatch  
identification\_engine : Commit: UPDATE cmdb\_ci\_win\_server : a853dd72dbd674104fa1c9db1396190e  
identification\_engine : Processed 1 records and 0 relations in 4msec + 135msec (waited 0msec for mutex)  
identification\_engine : logId:\[3bda95ba17d67410854244fa7a3ee1c2\] Processed payload from ServiceWatch. Using options: {partial\_payloads:false,partial\_commits:false,deduplicate\_payloads:false,generate\_summary:false}  
identification\_engine : logId:\[3bda95ba17d67410854244fa7a3ee1c2\] Input = {"items":\[{"className":"cmdb\_ci\_win\_server","values":{"operational\_status":"1","install\_status":"1","mac\_address":"ABCD1234","name":"SNCTest002","company":"86c1f3193790200044e0bfc8bcbe5d95","location":"a63c49b037d0200044e0bfc8bcbe5dd9","serial\_number":"SNC123456789","ip\_address":"10.20.30.41","model\_id":"4431c26b37913000158bbfc8bcbe5d0d","manufacturer":"0c43c22bc611227500002515e25bf079","ram":"2048"},"sys\_object\_source\_info":{"source\_name":"ServiceWatch"},"sys\_ire\_info":{"ire\_received\_time":"2021-09-03 15:33:31"}}\]}  
identification\_engine : logId:\[3bda95ba17d67410854244fa7a3ee1c2\] Output = {"items":\[{"className":"cmdb\_ci\_win\_server","operation":"UPDATE","sysId":"a853dd72dbd674104fa1c9db1396190e","maskedAttributes":\["name"\],"identifierEntrySysId":"fb27f69cc3000200d8d4bea192d3ae67","identificationAttempts":\[{"info":"sys\_object\_source SKIPPED","identifierName":"","attemptResult":"SKIPPED","attributes":\[\],"hybridEntryCiAttributes":\[\]},{"identifierName":"Hardware Rule","attemptResult":"SKIPPED","attributes":\["serial\_number","serial\_number\_type"\],"searchOnTable":"cmdb\_serial\_number","hybridEntryCiAttributes":\[\]},{"identifierName":"Hardware Rule","attemptResult":"MATCHED","attributes":\["serial\_number"\],"searchOnTable":"cmdb\_ci\_hardware","hybridEntryCiAttributes":\[\]}\],"info":\[\],"errorCount":0,"markers":\[\],"mergedPayloadIds":\[\],"warningCount":0,"inputIndices":\[0\]}\],"additionalCommittedItems":\[\],"relations":\[\],"additionalCommittedRelations":\[\]}  
identification\_engine : Identification Engine Total execution time 146msec  
\*\*\* Script: {"items":\[{"className":"cmdb\_ci\_win\_server","operation":"UPDATE","sysId":"a853dd72dbd674104fa1c9db1396190e","maskedAttributes":\["name"\],"identifierEntrySysId":"fb27f69cc3000200d8d4bea192d3ae67","identificationAttempts":\[{"info":"sys\_object\_source SKIPPED","identifierName":"","attemptResult":"SKIPPED","attributes":\[\],"hybridEntryCiAttributes":\[\]},{"identifierName":"Hardware Rule","attemptResult":"SKIPPED","attributes":\["serial\_number","serial\_number\_type"\],"searchOnTable":"cmdb\_serial\_number","hybridEntryCiAttributes":\[\]},{"identifierName":"Hardware Rule","attemptResult":"MATCHED","attributes":\["serial\_number"\],"searchOnTable":"cmdb\_ci\_hardware","hybridEntryCiAttributes":\[\]}\],"info":\[\],"errorCount":0,"markers":\[\],"mergedPayloadIds":\[\],"warningCount":0,"inputIndices":\[0\]}\],"additionalCommittedItems":\[\],"relations":\[\],"additionalCommittedRelations":\[\],"hasError":false,"hasWarning":false}

**Key observations from this output:**

-   The serial\_number identification rule matched an existing record
-   The name field was not updated because a reconciliation rule prevented the update
-   The final operation was UPDATE (not INSERT), confirming the record was found

### Troubleshooting examples

#### **Example 1: SCCM creates duplicate records instead of updating existing record**

**Scenario:** A Computer record exists with Serial Number "ABCDE12345". When the SCCM transformation runs, it should match the existing record. Instead, it creates a duplicate. Subsequent runs match the newly created record.

**Analysis:** After retrieving the IRE payload from the system log and running the script with gs.trace(true), review the SQL query generated when evaluating the Serial Number identifier:

SELECT cmdb0.sys\_id, cmdb0.sys\_mod\_count, cmdb0.sys\_class\_name, cmdb0.serial\_number FROM (cmdb cmdb0 INNER JOIN cmdbpar1cmdbpar1 cmdb par1cmdbpar10 ON cmdb0. sys\_id = cmdb$par10.sys\_id ) WHERE cmdb0.sys\_class\_path LIKE '/!!/!2%' AND ((cmdb0.serial\_number = 'ABCDE12345')) AND cmdb$par10.duplicate\_of IS NULL

**Root cause:** The condition duplicate\_of IS NULL caused the query to fail. The existing record was marked as a duplicate of another record at some point, so the duplicate\_of field was not empty. IRE could not find the existing record and created a new one.

**Resolution**: Clear the **duplicate\_of** field on the original record, or merge the duplicate records.

#### Example 2: Discovery does not update CI name in SQL Instance class

**Scenario:** MSSQL server Discovery using modified patterns should populate the SQL Instance name per company requirements. However, the SQL Instance name is not updated after Discovery runs.

**Analysis:** Retrieve the IRE payload and run it from background scripts. The debug output shows:

identification\_engine : Reconciliation: update to field 'tcp\_port' of CI '6bce7dcfdb08b7c479cca9a5ca961910' was skipped because of rules \[3104a82e9f503200c7445f9bc32e7054, a0d77a059311020062281f10077ffb32\] defined in cmdb\_reconciliation\_definition identification\_engine : Reconciliation: update to field 'name' of CI '6bce7dcfdb08b7c479cca9a5ca961910' was skipped because of rules \[3104a82e9f503200c7445f9bc32e7054\] defined in cmdb\_reconciliation\_definition identification\_engine : Reconciliation: cmdb\_ci\_db\_mssql\_instance(tcp\_port) field update skipped for Data Source Service-now identification\_engine : Reconciliation: cmdb\_ci\_db\_mssql\_instance(name) field update skipped for Data Source Service-now identification\_engine : Commit: UPDATE cmdb\_ci\_db\_mssql\_instance : 6bce7dcfdb08b7c479cca9a5ca961910

**Root cause:** No reconciliation rules exist for the legacy "Service-now" Discovery source. The update to the existing SQL Instance record was blocked.

**Resolution:** Create reconciliation rules that include the "Service-now" Discovery source, or update the Discovery source name to match existing reconciliation rules.

#### **Example 3: Review business rules executed during script**

To see which business rules are triggered when the script runs:

1.  Go to **System Diagnostics** > **Script Debugger**.
2.  Select the **Session Log** tab.
3.  Select **Settings** and enable **Business Rule debug**.  
    ![](sys_attachment.do?sys_id=4f2cdc649342b6908960fb2d6cba10e8)
4.  In a separate browser tab, go to **System Definition** > **Scripts - Background** and run your script.
5.  Return to the Script Debugger and review the session log for the business rules that were run.  
    ![](sys_attachment.do?sys_id=cb2cdc649342b6908960fb2d6cba10df)
6.  Review the script output for IRE debug information.  
    ![](sys_attachment.do?sys_id=4b2cdc649342b6908960fb2d6cba10e4)

**Note**: You can enable additional session debug settings by selecting the corresponding checkboxes.
