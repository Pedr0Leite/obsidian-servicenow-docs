---
title: "SAM - Request SAP data job fails when an SAP connection is still processing an earlier request and SAP returns Data Ready = N"
aliases:
  - KB2716620
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB2716620
kb_number: KB2716620
last_modified: 2026-01-14
---

## Issue

→ The scheduled job SAM - Request SAP data reports Failed because ServiceNow cannot submit a new request for an SAP connection that is still marked as processing an earlier request

## Resolution

Is this expected behavior  
→ Yes, this is expected behavior  
→ ServiceNow relies on the SAP response value <EIsDataReady>Y or N</EIsDataReady> to determine whether the connection is ready for a new request  
→ When SAP returns N, ServiceNow intentionally does not submit another request for that same connection and logs “processing an earlier request” to prevent overlapping requests

What to do next  
→ Correlate the failed job run with the ECC Queue response for the same SAP connection and timestamp  
→ If the ECC Queue shows <EIsDataReady>N</EIsDataReady> with lock-related comments, the remediation is on the SAP side  
→ Ask the SAP team to review why the relevant table is locked during the job schedule window for that specific connection and address the locking or reschedule the conflicting SAP process  
→ Once SAP returns <EIsDataReady>Y</EIsDataReady>, the next job run should proceed successfully
