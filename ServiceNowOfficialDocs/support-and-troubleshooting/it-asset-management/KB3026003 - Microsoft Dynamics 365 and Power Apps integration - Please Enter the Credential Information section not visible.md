---
title: "Microsoft Dynamics 365 and Power Apps integration - Please Enter the Credential Information section not visible"
aliases:
  - KB3026003
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB3026003
kb_number: KB3026003
last_modified: 2026-05-18
---

## Microsoft Dynamics 365 and Power Apps integration - Please Enter the Credential Information section not visible

  

### Issue

 

When following the product documentation to set up the ServiceNow instance for Microsoft Dynamics 365 and Power Apps integration, the **Please Enter the Credential Information** section referenced in Step 6 of the procedure is not visible.

### Symptoms

 

-   After selecting the preview icon next to the **Connection & Credential** field in Step 5, the **Please Enter the Credential Information** section described in Step 6 is not displayed.
-   The fields for **Tenant ID**, **OAuth Client ID**, and **OAuth Client Secret** are not visible on the page.
-   There is no apparent way to proceed with entering credential values from the current view.

### Facts

 

-   This issue occurs when setting up the ServiceNow instance for the Microsoft Dynamics 365 and Power Apps integration as part of Software Asset Management (SAM) or Software Asset Workspace (SAW).
-   The product documentation for the _Set up ServiceNow instance for Microsoft Dynamics 365 and Power Apps_ procedure is missing sub-steps under Step 5 that are required to reach the **Please Enter the Credential Information** section.
-   Step 5 in the documentation instructs users to select the preview icon next to the **Connection & Credential** field, but does not provide the additional navigation steps needed to open the credential entry dialog.
-   This is a documentation gap — the product behavior is functioning as designed.

### Release

All Releases

### Cause

 

The product documentation for _Set up ServiceNow instance for Microsoft Dynamics 365 and Power Apps_ is missing intermediate sub-steps under Step 5. After selecting the preview icon on the **Connection & Credential** field, the user must open the Connection & Credential record and then use the **Create New Connection & Credential** link under Related Links before the credential entry dialog — and its **Please Enter the Credential Information** section — becomes accessible.

Because these sub-steps are absent from the published documentation, users cannot progress past Step 5 and are unable to locate the fields described in Step 6.

![](/sys_attachment.do?sys_id=8df9d8f38774479c2d5cbbb5cebb3544 "M365DynamicsIntgMissingDocs.png")

### Resolution

 

Follow the complete procedure below. Steps 3 and 4 are the missing sub-steps not documented in the current product documentation.

1.  Navigate to the integration profile and create a new **Microsoft Dynamics 365 and Power Apps Integration Profile** record as described in the product documentation, then select **Save**.
    
2.  Under the **Download Subscription Subflow** tab, beside the **Connection & Credential** field, select the preview icon.
    
3.  In the preview panel that opens, select **Open Record** to open the Connection & Credential record.
    
4.  On the Connection & Credential record, under **Related Links**, select **Create New Connection & Credential**.
    
5.  The **Create Connection and Credential** dialog opens, displaying two sections: **Please Enter the Connection Information** and **Please Enter the Credential Information**.
    
6.  Under the **Please Enter the Credential Information** section, enter the values obtained from the Azure Active Directory setup:
    
    -   In the **Tenant ID** field, enter your Tenant ID.
    -   In the **OAuth Client ID** field, enter your OAuth Client ID.
    -   In the **OAuth Client Secret** field, enter your OAuth Client Secret key.
    
7.  Select **Create and Get OAuth Token**.
    

**Note:** The **Create and Get OAuth Token** step must be executed by a user with the Global administrator role in the Microsoft admin center.

### Related Links

 

-   [Integrating with Microsoft Dynamics 365 and Power Apps](https://docs.servicenow.com/bundle/latest-it-asset-management/page/product/software-asset-management2/concept/integrating-with-microsoft365.html)
