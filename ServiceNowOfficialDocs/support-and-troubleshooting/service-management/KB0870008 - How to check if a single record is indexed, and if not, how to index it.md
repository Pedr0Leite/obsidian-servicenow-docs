---
title: "How to check if a single record is indexed, and if not, how to index it"
aliases:
  - KB0870008
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0870008
kb_number: KB0870008
last_modified: 2026-05-18
---

## How to check if a single record is indexed, and if not, how to index it

  

### Issue

In this particular scenario, the user was not able to search against a specific user when creating a new HR Case either via the Platform or HR Agent Workspace. They wanted to know why.

### Release

All 

### Cause

The user's sys\_user record was not properly indexed. Hence, it was not searchable.

### Resolution

After noting that this was only affecting one user, a check was made against the sys\_user record to ensure that it was properly indexed. This was done via a sample script like the below:

For ZING:

`// Test to see if the record is indexed - this should return some result if it is. Else, not.`

`var tsDebug = new GlideTSUtil();   var table = "_table_name_";   var doc = "_sys_id_of_record_";`

`tsDebug.dumpDocument(table,doc);`

For AIS:

`// Test to see if the record is indexed - this should return some result if it is. Else, not.`

`new sn_ais.AisUtil().dumpDocument('kb_knowledge', '1234asdf1234asdf1234asdf');`

Then, once it was found that the record was not properly indexed, something like the below sample script was run to index the single record properly:

For ZING:

`// Index the targeted record`

`var table = "_table_name_";`  
`var sysID = "_sys_id_of_record_";`  
`new GlideTSUtil().indexDocument(table, sysID);`

For AIS:

`// Index the targeted record`

`new sn_ais.IndexEvent().indexRecord(‘<table_name>’, ‘<sys_id>’);`

Running the above script in Scripts - Background resolved the issue, and the user was then searchable for the creation of HR Cases in both the Platform UI and HR Agent Workspace.

The above sample scripts should be tailored to each use case and tested thoroughly in a sub-Production instance before being used in a live Production environment.
