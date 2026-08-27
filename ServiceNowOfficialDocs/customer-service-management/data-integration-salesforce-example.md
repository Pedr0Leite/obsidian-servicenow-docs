---
title: Reference Salesforce integration using remote tables
description: In this example, the Customer Account table is extended to include an associated Salesforce Account ID which, in turn, is used to retrieve Salesforce opportunities associated with this account. The remote table is used to hold the retrieved opportunity data.
locale: en-US
canonical_url: https://www.servicenow.com/docs/r/customer-service-management/data-integration-salesforce-example.html
release: australia
topic_type: concept
last_updated: "2026-03-12"
reading_time_minutes: 1
breadcrumb: [Third-party data integration for CSM, CSM Configurable Workspace features, CSM Configurable Workspace, Organize agent workspaces, Configure, Customer Service Management]
tags:
  - customer-service-management
  - type-concept
---

# Reference Salesforce integration using remote tables

In this example, the Customer Account table is extended to include an associated Salesforce Account ID which, in turn, is used to retrieve Salesforce opportunities associated with this account. The remote table is used to hold the retrieved opportunity data.

Use the steps and the examples in the following topics to create a reference Salesforce integration using remote tables.

-   [[config-csm-integration-salesforce|Using the IntegrationHub Salesforce spoke]].
-   [[csm-integration-remote-tables|Using remote tables and the Salesforce spoke]]. Identify or create an IntegrationHub action that you can use to test the third-party data integration. Then use this action in the remote table definition.
-   [[csm-related-list-opportunity-table|Using a related list to create the connection between the customer account and the Salesforce opportunities]].

-   **[Using remote tables and the Salesforce spoke](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/customer-service-management/csm-integration-remote-tables.md)**  
Create Salesforce spoke actions that you can use to test the third-party data integration. Then use these actions in the remote table definition.

**Parent Topic:**[[c_CustomerServiceManagement|Customer Service Management]]

## Related

- [[config-csm-integration-salesforce|Using the IntegrationHub Salesforce spoke]]
- [[csm-integration-remote-tables|Using remote tables and the Salesforce spoke]]
- [[csm-related-list-opportunity-table|Connect Customer Account and Salesforce Opportunities using a related list]]
- [[c_CustomerServiceManagement|Customer Service Management]]
