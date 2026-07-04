---
title: "Error \"PDF Header Not Found\" During Flow Execution in HR Service Delivery"
aliases:
  - KB2633825
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB2633825
kb_number: KB2633825
last_modified: 2026-01-01
---

## Error "PDF Header Not Found" During Flow Execution in HR Service Delivery

  

### Issue

During flow execution in HR Service Delivery, the error “PDF header not found” occurs.  
Attachments required for PDF conversion are inaccessible due to access denial errors.  
This may be related to Module Access Policy (MAP) configuration or encryption settings blocking attachment access.

### Release

Any Release

### Cause

-   Access to attachments is denied during PDF conversion.
-   Logs may show “crypto module access is denied for an attachment”, indicating MAP or encryption policies are restricting access.
-   Privileged accounts (admin, maint, system) may also be unable to access attachments, confirming policy restrictions.

### Resolution

1.  Check Attachment Access:

-   Navigate to the sys\_attachment table and verify if attachments can be accessed by admin or system accounts.
-   If access is denied, proceed to review MAP and encryption settings.

2.  Review Module Access Policies (MAP):

-   Go to Key Management Framework (KMF) configuration.
-   Check if MAP settings restrict access to attachments used in PDF generation.
-   Update policies to allow required access for the PDF conversion process.

3.  Verify Encryption Settings:

-   Review Field Encryption and Column Level Encryption configurations.
-   Ensure that encryption policies do not block attachment access during flow execution.

4.  Test PDF Conversion:

-   After updating MAP or encryption settings, re-run the flow to confirm that PDF generation works as expected.
