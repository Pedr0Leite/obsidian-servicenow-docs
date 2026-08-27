---
title: "Attachment Icon in HR Case is not visible to Requestor"
aliases:
  - KB0864049
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0864049
kb_number: KB0864049
last_modified: 2026-02-12
---

## Attachment Icon in HR Case is not visible to Requestor

  

### Issue

Attachment Icon in HR Case is not visible to Requestor

1\. Create a Record Producer on the HR Case table or any of its extended tables

2\. Populate yourself as a requestor and attach a file.

3\. Submit it to create the HR record

It will redirect you to the HR record created

Expected behaviour: After submission, you should still be able to attach additional files in the HR record

Actual behaviour: You cannot attach additional files in the HR record even if you are the requestor

### Release

All release

### Cause

Missing or failing Human Resource (HR) ACL in the instance

### Resolution

Debug ACL and check which ACL is failing 

If you have an out-of-box (OOB) or successful instance, compare all the ACLs on the HR Case and \[sys\_attachment\] tables to see if some ACLs are missing
