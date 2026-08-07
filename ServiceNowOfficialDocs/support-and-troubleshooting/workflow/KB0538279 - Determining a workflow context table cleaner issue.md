---
title: "Determining a workflow context table cleaner issue"
aliases:
  - KB0538279
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0538279
kb_number: KB0538279
last_modified: 2025-07-31
---

## Determining a workflow context table cleaner issue

  

### Issue

This article helps to determine if an upgraded instance presents a workflow context table cleaner issue from legacy versions.  
  

### Symptoms

-   Workflow not found
-   Workflow restarted

### Release

All

### Resolution

### How the workflow engine executes against a current during a glide transaction

The workflow engine is a script engine that executes in a specific order. When the workflow engine executes against a current during a glide transaction, it follows these steps:

-   Checks for the existence of a workflow on that table.
-   If the engine finds a workflow, it checks for the existence of a wf\_context.
-   If a wf\_context is found and it is active, the engine executes the context.
-   If the engine does not find a wf\_context, the engine creates and executes a wf\_context.

If the table cleaner has removed a wf\_context that is older than 180 days, and then a user examines an old current and clicks **Update**, a new workflow starts executing on that current.

For more information, see [Execution Order of Scripts and Engines](https://docs.servicenow.com/csh?topicname=r_ExecutionOrderScriptsAndEngines.html&version=latest "Execution Order of Scripts and Engines") in the ServiceNow product documentation.

### Workflows re-attached to old records

Some users have reported that workflows re-attach or re-start on old records. If a workflow context is deleted and the original current that was attached to that context is updated, then a new workflow attaches to that current. There are several ways a workflow context can be deleted. For example, a system administrator can delete a workflow context at any time.

In Calgary and earlier releases, there is an entry in the table cleaner that removes wf\_context records older than 180 days. To remove this entry in record cleaner, follow these steps:

1.  In the navigation menu search box, type sys\_auto\_flush.list.  
     
2.  Find the entry on the table, wf\_context.  
     
3.  Clear the **Active** option on the record.
