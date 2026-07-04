---
title: "Workflow activities are getting canceled unexpectedly"
aliases:
  - KB0854497
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0854497
kb_number: KB0854497
last_modified: 2026-06-29
---

## Workflow activities are getting canceled unexpectedly

  

### Issue

Workflow activities are unexpectedly canceled.

### Symptoms

-   Workflow activities show a state of Canceled without being manually stopped.
-   Workflows do not complete as expected.
-   Records on the wf\_executing table show state set to Canceled.

### Release

  All supported releases

### Cause

A script in the instance is programmatically setting the state of records on the wf\_executing table to Canceled. When a record on the wf\_executing table has its state set to Canceled, the associated workflow activity is canceled.

### Resolution

To resolve this issue, locate and remove or update the script that is setting the wf\_executing state to Canceled.

Step 1: Search for scripts modifying the wf\_executing table

Check the following locations for scripts that reference \`wf\_executing\` and set the state to \`cancelled\`:

-   Business Rules — Navigate to System Definition > Business Rules and search for scripts referencing \`wf\_executing\`.
-   Script Includes — Navigate to System Definition > Script Includes and search for \`wf\_executing\`.
-   Scheduled Jobs — Navigate to System Definition > Scheduled Jobs and review any jobs with custom scripts.
-   Workflow scripts — Open the affected workflow in the Workflow Editor and inspect any Run Script activities.

A problematic script may look similar to the following example:

var gr = new GlideRecord('wf\_executing');  
gr.addQuery('workflow\_version', workflowVersionSysId);  
gr.query();  
while (gr.next()) {  
    gr.setValue('state', 'cancelled');  
    gr.update();  
}  
  

Step 2: Confirm the affected records

To view records on the wf\_executing table that are in a Canceled state:

1\. Navigate to https://<instance-name>.service-now.com/wf\_executing\_list.do  
2\. Filter records where State is Canceled.  
3\. Note the workflow version and context to help identify the source script.

Step 3: Remove or update the script

Once you identify the script, either remove the logic that sets the state to \`cancelled\` or update it to reflect the intended behavior. If the script is required for another purpose, review the workflow design to determine whether a different approach is needed.

Step 4: Verify the fix

After updating the script, trigger the workflow again and confirm that the activities complete as expected without being canceled.
