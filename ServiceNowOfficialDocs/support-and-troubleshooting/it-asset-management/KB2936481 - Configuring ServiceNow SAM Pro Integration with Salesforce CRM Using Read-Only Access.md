---
title: "Configuring ServiceNow SAM Pro Integration with Salesforce CRM Using Read-Only Access"
aliases:
  - KB2936481
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB2936481
kb_number: KB2936481
last_modified: 2026-05-21
---

## Configuring ServiceNow SAM Pro Integration with Salesforce CRM Using Read-Only Access

  

### Issue

Customers are unable to proceed with ServiceNow SAM Pro and Salesforce CRM integration due to security restrictions preventing the assignment of administrative-level permissions (e.g., "Customize Application", "Manage Connected Apps") to the integration user.

### Release

All supported releases of ServiceNow SAM Pro with Salesforce CRM integration

### Cause

1.  The official documentation outlines administrative permissions as part of the standard integration setup, which leads to the assumption that full admin access is mandatory.  
      
    
2.  In reality, these permissions are only required for advanced capabilities such as license reclamation and deeper configuration management. For basic license monitoring, the integration primarily depends on API access and data visibility rather than administrative privileges.

### Resolution

For license monitoring–only use cases, configure the Salesforce integration user with minimal required permissions instead of full admin access.

1\. Required Permissions:

-   View Setup and Configuration
-   API Enabled

2\. OAuth Scopes:

-   API (`api`)
-   Refresh Token (`refresh_token`)

Additional Considerations:

-   Ensure read access to relevant Salesforce objects (e.g., Users, Licenses, Subscriptions)
-   Optional permissions like "View All Users" may be required depending on data visibility constraints

This configuration allows successful data retrieval for monitoring purposes while adhering to the principle of least privilege.

* * *

### Fix

No platform defect. This is a configuration-based optimization.

Administrative permissions (e.g., "Customize Application", "Manage Connected Apps") are only required if enabling advanced features such as license reclamation.

### Related Links

[Integrating with Salesforce CRM](https://www.servicenow.com/docs/r/it-asset-management/saas-license-management/integrate-with-salesforce-crm.html)
