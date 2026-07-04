---
title: "Microsoft Entra ID integration and user provisioning with ServiceNow"
aliases:
  - KB0635951
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0635951
kb_number: KB0635951
last_modified: 2026-02-03
---

## Microsoft Entra ID integration and user provisioning with ServiceNow

  

### Issue

Learn about Microsoft Entra ID (formerly Microsoft Azure Active Directory or Azure AD) integration with ServiceNow, including single sign-on (SSO) and automatic user provisioning. This article describes common symptoms and provides resources for configuring the integration.

**Important**: Microsoft Entra ID is not a ServiceNow product. For configuration assistance, contact Microsoft Support.

### Symptoms

-   Users cannot log in when selecting the ServiceNow icon in Microsoft Entra ID.
    
-   Automatic user provisioning is not working.
    
-   Users in ServiceNow are not synchronized with users in Microsoft Entra ID.
    

**Note**: User auto-provisioning through Microsoft Entra ID is not an LDAP integration. The integration requires a multiple provider SSO (MPSSO) record in ServiceNow.

### Release

All supported releases

### Cause

Microsoft Entra ID integration requires configuration in the Microsoft Entra admin center. These settings are outside ServiceNow, so there is limited control over them from the ServiceNow instance.

### Resolution

Microsoft Entra ID integrates with the User \[sys\_user\] table using direct web services. Because this integration is managed by Microsoft, there are no settings in the ServiceNow instance that control this behavior.

To troubleshoot issues:

1.  Review system logs in your ServiceNow instance for error messages related to the integration.
2.  Verify the integration configuration in the Microsoft Entra admin center.
3.  Confirm that a multiple provider SSO (MPSSO) record exists in ServiceNow.

For configuration guidance, see the resources in the Related Links section.

Contact Microsoft Support for additional assistance with user auto-provisioning configuration.

### Related Links

[Configure ServiceNow for automatic user provisioning with Microsoft Entra ID (Microsoft)](https://docs.microsoft.com/en-us/azure/active-directory/active-directory-saas-servicenow-provisioning-tutorial)

[Auto account provisioning with Service Now & Entra ID integration (YouTube)](https://www.youtube.com/watch?v=oUIq3Ue1djE)
