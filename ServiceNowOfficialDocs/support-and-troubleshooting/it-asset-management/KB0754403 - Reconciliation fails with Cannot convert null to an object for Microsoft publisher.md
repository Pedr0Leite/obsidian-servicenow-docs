---
title: "Reconciliation fails with \"Cannot convert null to an object\" for Microsoft publisher"
aliases:
  - KB0754403
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0754403
kb_number: KB0754403
last_modified: 2024-04-07
---

## Reconciliation fails with "Cannot convert null to an object" for Microsoft publisher

  

### Issue

When running reconciliation for Microsoft, the reconciliation result is a failure. The following error is seen in system log:

\----------------------  
TypeError: Cannot convert null to an object.  
\---------------------  
at sys\_script\_include.c3361a0d0b9232001a17650d37673a27.script:1363 (anonymous)  
at sys\_script\_include.6761b0dd0b1232001a17650d37673a77.script:1201 (anonymous)  
at sys\_script\_include.6761b0dd0b1232001a17650d37673a77.script:1291 (anonymous)  
at sys\_script\_include.6761b0dd0b1232001a17650d37673a77.script:1138 (anonymous)  
at sys\_script\_include.6761b0dd0b1232001a17650d37673a77.script:203 (anonymous)  
at sys\_script\_include.6761b0dd0b1232001a17650d37673a77.script:62 (anonymous)  
at <refname>:3 (sampSoftwareLicenseReconciliation)  
at <refname>:1

### Cause

When reconciliation runs, data from the table Software Installations(cmdb\_sam\_sw\_install) is fetched to account for the field "Installed On". If this field is  empty you will see the following error message.

### Resolution

Please make sure that software installations(cmdb\_sam\_sw\_install) table does not have any records with field "Installed On" as empty. If you do have a few records, you can configure a table cleanup job as below to delete them: 

1.  Navigate to  system maintenance > Table Cleanup   
    2\. Create new with the following details:
    -   Table Cleanup:cmdb\_sam\_sw\_install 
    -   Age in Seconds in 1 
    -   Condition - installed on isempty 
    -   uncheck the cascade delete
    -   Name:Delete Software Install record with empty Installed On field

Please make sure you have unchecked the cascade delete box.
