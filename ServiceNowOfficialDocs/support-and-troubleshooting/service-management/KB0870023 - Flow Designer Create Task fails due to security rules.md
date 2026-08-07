---
title: "Flow Designer Create Task fails due to security rules"
aliases:
  - KB0870023
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0870023
kb_number: KB0870023
last_modified: 2026-03-23
---

## Flow Designer Create Task fails due to security rules

  

### Issue

Running the Flow Designer Create Task results in the following error: The requested flow operation was prohibited by security rules.

However, the user has the correct permissions to create the task.

### Release

All supported releases

### Cause

The user needs permission to run the flow.

### Resolution

To create a sc\_task record, ensure the flow runs with roles itil and catalog\_admin. 

If running the flow still fails, check that the catalog item used has any catalog variables. If so, set additional permissions.

In the following error message, notice the addVariableToTask reference:

Flow Designer: Operationxxx.Create Catalog Task) failed with error: com.snc.process\_flow.exception.OpException: The requested flow operation was prohibited by security rules.  
at com.snc.process\_flow.operation.SetCatalogVariablesOperationBase.addVariableToTask(SetCatalogVariablesOperationBase.java:47)  
at com.snc.process\_flow.operation.SetCatalogVariablesOperationBase.setCatalogVariables(SetCatalogVariablesOperationBase.java:37)

For this to work, write access is required on the sc\_item\_variables\_task table. There is currently no access control list (ACL) to do this, which means this only works if you have admin permissions.  

To resolve this error:

1.  Create an ACL for catalog\_admin.
2.  Give write access to sc\_item\_variables\_task.

Preferred fix: Run the flow in system context or with a dedicated service account so catalog variable writes don't require custom ACL changes.

Caution: Avoid creating broad write ACLs. If ACLs are required, scope them minimally to sc\_item\_variables\_task with strict conditions (least privilege) and test in a sub-production environment first.
