---
title: "SAM Reconciliation Fails with \"No Match Found\" Error in samp_sw_publisher Table"
aliases:
  - KB0783403
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0783403
kb_number: KB0783403
last_modified: 2026-06-11
---

## SAM Reconciliation Fails with "No Match Found" Error in samp\_sw\_publisher Table

  

### Issue

When running Software Asset Management (SAM) reconciliation for all publishers or a specific publisher, a Reconciliation Result record (RR_xxxxx_) is created, and the status immediately changes to Failed. The system log displays the following errors:

SAM:ReconciliationEngine: undefined: no thrown error  
Error: No Match found for <sys\_id> in samp\_sw\_publisher  
SAM:ReconciliationEngine: Error: No Match found for <sys\_id> in samp\_sw\_publisher: no thrown error

### Release

ALL

### Cause

When reconciliation runs for all publishers or a specific publisher selected from the publisher field drop-down list, the reconciliation engine searches for that publisher in the Software Publishers \[samp\_sw\_publisher\] table. If the record does not exist in this table, the ReconciliationEngine throws an error and stops processing. The missing record may have been deleted, or the scheduled job that pulls data from the source content service may not have completed successfully.

### Resolution

##### Option 1 — Restore the missing publisher record from a non-production instance

Use this option if the issue is not occurring on any of your non-production instances.

1.  Log in to an unaffected non-production instance.
2.  Navigate to the Software Publishers \[samp\_sw\_publisher\] table list view.
3.  Search for the record using the sys\_id value shown in the error message (for example, the value shown after "No Match found for" in the log).
4.  Export the record as XML. For instructions, see [Exporting data](https://docs.servicenow.com/csh?topicname=c_ExportData.html&version=latest) in the ServiceNow product documentation.
5.  Log in to the affected instance.
6.  Import the exported XML file using the Import XML UI action. For instructions, search for "Import a record as XML data" in the ServiceNow product documentation.
7.  Re-run the reconciliation and verify that the Reconciliation Result record completes with a status other than Failed.

##### Option 2 — Contact ServiceNow Support

Use this option if Option 1 is not applicable or does not resolve the issue.

Create a support case and request that the ServiceNow Support team inspect the weekly scheduled jobs responsible for pulling source data from the content services. If these jobs were interrupted or did not complete successfully, the SAMP Software Content Library or related tables may be incomplete, which can cause this error.

When creating the case, include the following information:

-   The full error text from the system log
-   The sys\_id value shown in the error
-   The name of the publisher for which reconciliation was run
-   Whether the issue affects all publishers or a specific publisher only
