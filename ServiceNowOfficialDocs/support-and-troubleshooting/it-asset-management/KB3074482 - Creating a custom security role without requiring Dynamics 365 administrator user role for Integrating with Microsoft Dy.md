---
title: "Creating a custom security role without requiring \"Dynamics 365 administrator\" user role for Integrating with Microsoft Dynamics 365 and Power Apps"
aliases:
  - KB3074482
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB3074482
kb_number: KB3074482
last_modified: 2026-06-09
---

## Creating a custom security role without requiring "Dynamics 365 administrator" user role for Integrating with Microsoft Dynamics 365 and Power Apps

  

### Issue

"Integrating with Microsoft Dynamics 365 and Power App" DOC only lists 'Dynamics 365 administrator' role as the required user role to have minimal user permissions to

"Pull user activity".

### Release

Available ServiceNow releases

### Resolution

These are the minimum privileges needed for:

[Integrating with Microsoft Dynamics 365 and Power Apps](https://www.servicenow.com/docs/r/it-asset-management/saas-license-management/integrating-with-microsoft365.html "Integrating with Microsoft Dynamics 365 and Power Apps")

These can be configured on the Power Apps Admin Portal by creating a custom security role.

-   Tables (Read-only access, no Create/Write/Delete on any table)
-   Business Management
-   User (systemuser) — Read: Organization
-   Core Records
-   Activity (activitypointer) — Read: Organization
-   Sharepoint Document (sharepointdocument) — Read: Organization
-   Customization
-   Attribute (attribute) — Read: Organization
-   Entity (entity) — Read: Organization
-   Relationship Entity (relationship) — Read: Organization

Miscellaneous Privileges:  
View Audit Summary (prvReadAuditSummary) — Organization

Once this role is created, assign this custom role to the user who will be fetching the token in the ServiceNow instance.

### Related Links

[https://www.servicenow.com/docs/r/it-asset-management/saas-license-management/integrating-with-microsoft365.html](https://www.servicenow.com/docs/r/it-asset-management/saas-license-management/integrating-with-microsoft365.html)
