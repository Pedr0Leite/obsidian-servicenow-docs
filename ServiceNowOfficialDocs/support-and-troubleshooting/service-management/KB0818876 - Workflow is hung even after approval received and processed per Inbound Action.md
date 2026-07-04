---
title: "Workflow is hung even after approval received and processed per Inbound Action"
aliases:
  - KB0818876
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0818876
kb_number: KB0818876
last_modified: 2024-09-20
---

## Workflow is hung even after approval received and processed per Inbound Action

  

### Issue

The user has some workflows which are hung even after receiving approval via an Inbound Action.

### Resolution

The issue is that even though Joe Employee is an approver on the Finance Request (FR) record, he actually has no visibility of the record (to see this demonstrated, the user can grab the URL to the record, impersonate Joe Employee, and try to view that record - they will get a "Record not found" error).  
  
Here's what is seen in the logs, which is the root of the issue:  
  

```
`2020-02-27 16:27:26 (476) worker.1 worker.1 txid=cb445e60db13 WARNING * WARNING * Get for non-existent record: sn_sm_finance_request:5dbb4a6cdb5f8050dea5760a689619a0, initializing`
```

  
The WorkflowApprovalUtils Script Include is trying to do a get() on the current record and then send an update to the workflow(s). If that get, fails workflows won't be updated.  
  

```
var gr = new GlideRecord(table);if (gr.get(id)) {            new Workflow().broadcastEventToCurrentsContexts(gr, 'update', null);    }}
```

  
Because Joe Employee has no visibility of the record, the `gr.get()` fails, and the approval is not broadcasted to the workflow. This will happen in any similar situation.  
  
To remedy this, the user should ensure that any approver on a record should have visibility to view the record they are approving.
