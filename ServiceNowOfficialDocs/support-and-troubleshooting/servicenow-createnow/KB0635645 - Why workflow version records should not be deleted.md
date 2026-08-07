---
title: "Why workflow version records should not be deleted"
aliases:
  - KB0635645
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0635645
kb_number: KB0635645
last_modified: 2026-01-06
---

## Why workflow version records should not be deleted

  

### Issue

On the ServiceNow Platform, the Workflow Editor within the Workflow module allows users to create new and update existing workflows for each application. An example reason that a workflow might be implemented is for Incident Management or Change Management.

Processes change over time, and therefore the platform uses versioning to update workflows without affecting existing running workflows within the platform. Workflow versions are stored in a table called wf\_workflow\_version.

However, in-flight records, such as Change Requests and Incidents, are using the older wf\_workflow\_version as a reference to run the workflow. The in-flight workflows are stored in a table called wf\_context.

Deleting records within the wf\_workflow\_version table causes in-flight records, such as Change Requests and Incidents, to lose reference to their version. Therefore any approvals and tasks scheduled to be created by the in-flight workflow are not created, and therefore from an end-user point of view, the related record associated to the wf\_context does not complete its execution.

Therefore do not delete wf\_workflow\_version records as this causes a huge impact to a ServiceNow instance.

### Symptoms

The symptoms of a wf\_workflow\_version record being deleted are the following:

-   Empty value in the reference field Workflow Version on the wf\_context table
-   Approvals and Tasks not being created on in-flight records

### Release

### Cause

Due to the security enhancements in the platform, System Administrators cannot delete wf\_workflow\_version records if there is a reference that exists in the wf\_context table, where the state of the wf\_context is Executing.

However, the main cause of the deletion of wf\_workflow\_version records is when a user runs a background script to perform this action. 

Please note that ServiceNow Support does not advise nor support the use of a script to delete a wf\_workflow\_version.

### Resolution

If you do not wish for a wf\_workflow\_version to be used for new records, set a wf\_workflow\_version inactive by performing the following steps:

1\. Navigate to **Workflow > Workflow Editor**  
2\. Open any workflow. For example, Change Request - Normal  
3\. On the title bar, click on the menu icon and select Set **Inactive**

Important: The **Set Inactive** option is only available if the version of the workflow is not referenced in an executing wf\_context record.
