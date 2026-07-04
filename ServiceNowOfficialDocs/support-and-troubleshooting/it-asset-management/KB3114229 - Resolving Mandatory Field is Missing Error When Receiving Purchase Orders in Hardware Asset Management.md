---
title: "Resolving \"Mandatory Field is Missing\" Error When Receiving Purchase Orders in Hardware Asset Management"
aliases:
  - KB3114229
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB3114229
kb_number: KB3114229
last_modified: 2026-06-24
---

## Resolving "Mandatory Field is Missing" Error When Receiving Purchase Orders in Hardware Asset Management

  

### Issue

When submitting a purchase order receipt in the po\_receive form, users encounter a validation error stating "Mandatory field is missing for \[asset name\]" even though all visible form fields appear to be completed.

### Symptoms

-   Error message displays: "Mandatory field is missing for \[asset name\]"
-   The error banner appears at the top of the po\_receive form
-   No mandatory field in the form visibly indicates it is missing or empty
-   Submit button cannot proceed past the error  
      
    ![image (2).png](https://support.servicenow.com/3c72548f476d47dcb6a52545d36d4352.iix)

### Release

All current releases with Hardware Asset Management and Vendor Management Workspace functionality.

### Cause

The po\_receive form requires asset tag details before finalizing the purchase order receipt. The Capture Asset Tag button (identified by a document icon) next to the Receiving Quantity field must be clicked and completed before the form can be submitted. If this step is skipped, the system rejects the form submission with a mandatory field error, even though the error message does not explicitly reference the asset tag capture requirement.

### Resolution

1.  Locate the Capture Asset Tag button: Next to the Receiving Quantity field in the po\_receive form, locate the button with a document icon.
2.  Click the Capture Asset Tag button: This opens a dialog box where you can enter required asset information.
3.  Enter asset details: Provide at least one of the following asset identifiers:
    -   Serial Number
    -   Asset Tag
    -   MAC Address
4.  Confirm your entries: Click Done to close the asset capture dialog.
5.  Submit the form: Click Submit to complete the purchase order receive action.

After these steps, the form should submit successfully without the "Mandatory field is missing" error.  
  
![](/sys_attachment.do?sys_id=0b621bef97a5c7500ed83bbe2153afd5)
