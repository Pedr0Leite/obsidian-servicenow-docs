---
title: Configuring Financial Services Operations
description: Set up your Financial Services Operations application by importing financial services data and reviewing and configuring the components installed with the application. You can configure record producers, Workflow Studio flows, assignment groups and rules, workspace, playbooks, and service level agreement definitions for Financial Services Operations applications. These settings enable creating and managing requests and tasks for banking operations.
locale: en-US
canonical_url: https://www.servicenow.com/docs/r/financial-services-operations/setting-up-fso-applications.html
release: australia
topic_type: concept
last_updated: "2026-03-12"
reading_time_minutes: 3
breadcrumb: [Financial Services Operations \(FSO\)]
tags:
  - financial-services-operations
  - type-concept
---

# Configuring Financial Services Operations

Set up your [[fso-overview|Financial Services]] Operations application by importing financial services data and reviewing and configuring the [[components-installed-with-dispute-rules-content-pack-for-mastercard|components installed]] with the application. You can configure record producers, Workflow Studio flows, assignment groups and rules, workspace, playbooks, and service level agreement definitions for Financial Services Operations applications. These settings enable creating and managing requests and tasks for banking operations.

1.  [[import-financial-accounts-products-institutions|Planning to import your financial data]]

    Understand how to import your financial accounts, financial products, financial institutions, and financial transactions into ServiceNow [[financial-services-operations-core-data-model|Financial Services Operations Core]] tables.

2.  \(Optional\) [[enable-branch-operations|Enabling branch operation features]]

    Enable branch operations features to allow managers to view performance metrics and manage cases for the branches they oversee, helping optimize operational performance across locations.

3.  [[fso-user-management|Setting up roles and personas]]

    Configure internal and external users in Customer Service Management and the FSO application to ensure proper access. Combine Agent Connector and Contributor roles with relevant CSM Industry data model and user roles to streamline case management and support for specific accounts.

4.  [Setting up script includes](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/api-reference/scripts/c_ScriptIncludes.md)

    Create script includes to store JavaScript that runs on the server.

5.  [[data-models|Setting up Data models]]

    Create structured and flexible data models to represent the need across various industries.

6.  [Creating an ACL](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/it-service-management/t_CreateNewACL.md)

    Create an access control rule \(ACL\) to prevent the Needs review field from being modified after it has been set.

7.  [Setting up form views](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/platform-user-interface/form-configurable-workspace.md)

    Form views refer to the user interfaces or screens that allow users to input, edit, and view data related to tables.

8.  [[configure-service-definitions|Configuring service definitions]]

    Configure and modify service definitions for Financial Services Operations applications, including reviewing or adding new ones.

9.  [Creating a UI action](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/it-service-management/t_CreateNewUIAction.md)

    Create UI actions.

10. [[configure-csm-workspace-fso-apps|Setting up CSM Configurable Workspace]]

    Review the CSM Configurable Workspace in Financial Services Operations applications to ensure it meets your business needs. Customize its components as needed and set it up for agents to engage with customers, answer questions, create cases, and resolve issues.

11. [Setting up decision tables](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/application-development/decision-table.md)

    Create decision tables.

12. [Setting up approval engine](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/build-workflows/t_SetupAnApprovalEngine.md)

    Set up insurance claim core as per the business requirements.

13. [[configure-assignment-rules-fso-applications|Configuring assignment rules]]

    Configure rules to automatically assign cases to specific agents or groups based on the rule conditions. You can either modify predefined assignment rules or create new ones.

14. [[configure-flow-designer-flows-fso-apps|Configuring flows]]

    Review the available flows in Financial Services Operations applications to ensure they align with your business needs. Customize existing flows or create new ones as necessary.

## Related

- [[import-financial-accounts-products-institutions|Import your financial data using import sets]]
- [[enable-branch-operations|Enable branch operations]]
- [[fso-user-management|FSO User management]]
- [[data-models|Data Models]]
- [[configure-service-definitions|Configure service definitions]]
- [[configure-csm-workspace-fso-apps|Configure CSM Configurable Workspace]]
- [[configure-assignment-rules-fso-applications|Configure assignment rules]]
- [[configure-flow-designer-flows-fso-apps|Configure flows]]
- [[fso-overview|Financial Services]]
- [[components-installed-with-dispute-rules-content-pack-for-mastercard|Components installed]]
- [[financial-services-operations-core-data-model|Financial Services Operations Core]]
