---
title: "Inbound Action skipping message incorrect"
aliases:
  - KB0816008
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0816008
kb_number: KB0816008
last_modified: 2024-04-08
---

## Inbound Action skipping message incorrect

  

### Issue

User is trying to perform insert and update operations via Inbound Action and whenever the insert operation happens, it is getting captured in the email log whereas the update operation happens, the message is appearing in the email log  "Skipping ‘Inbound\_action\_name’, did not create or update incident" even though the update operation is processed.

### Cause

When user is trying to insert the record using current object 'current.insert()'and it got processed and captured successfully in the email log.

 The script shown as below:

function createNewIncident()  
  
{  
  
current.work\_notes = email.body\_text;  
  
current.insert();  
  
}

But, when they are trying to update the record, there is no current.update() within the script, as the script uses a query to locate the record to update, and does the update using it as reference. 

So even though the update is processed, the email log doesn’t captured that successful transaction instead it showing wrong message as  "Skipping ‘Inbound\_action\_name’, did not create or update incident”.

The script shown as below:

function updateTheIncident()  
  
{  
  
recentIncident.work\_notes = email.body\_text;  
  
recentIncident.update();  
  
}

### Resolution

The insert operation is happening using current object hence it got captured in the log whereas in update operation, since they are using it as reference instead of current object, it wasn't able to capture which is an expected behaviour.

So in order to capture the insert and update operations in email log, we should use current object as below.

current.insert();  
  
current.update();
