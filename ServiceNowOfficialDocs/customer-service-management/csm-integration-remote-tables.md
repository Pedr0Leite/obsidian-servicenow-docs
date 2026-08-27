---
title: Using remote tables and the Salesforce spoke
description: Create Salesforce spoke actions that you can use to test the third-party data integration. Then use these actions in the remote table definition.
locale: en-US
canonical_url: https://www.servicenow.com/docs/r/customer-service-management/csm-integration-remote-tables.html
release: australia
topic_type: concept
last_updated: "2026-03-12"
reading_time_minutes: 1
breadcrumb: [Reference Salesforce integration using remote tables, Third-party data integration for CSM, CSM Configurable Workspace features, CSM Configurable Workspace, Organize agent workspaces, Configure, Customer Service Management]
tags:
  - customer-service-management
  - type-concept
---

# Using remote tables and the Salesforce spoke

Create Salesforce spoke actions that you can use to test the third-party data integration. Then use these actions in the remote table definition.

-   **[[config-csm-integration-salesforce|Using the IntegrationHub Salesforce spoke]]**  
Use the Salesforce spoke to integrate a Salesforce account with your ServiceNow instance.
-   **[[csm-integration-salesforce-spoke|Create Salesforce spoke actions to retrieve opportunities]]**  
The Salesforce spoke provides actions to retrieve metadata of the opportunity record and create a new opportunity.
-   **[[csm-remote-tables-definition|Remote tables and definition]]**  
Once you have the spoke custom actions working, you need to create a remote table that describes the schema for the data to be retrieved from the Salesforce Opportunity table.
-   **[[csm-opportunity-table-script|Example script that queries the Opportunity table]]**  
This example script queries the opportunity table using the **Get All Opportunities**, **Get Opportunities for Account Id**, and **Get Opportunity Details** custom actions.
-   **[[csm-related-list-opportunity-table|Connect Customer Account and Salesforce Opportunities using a related list]]**  
Use a related list to link the Customer Account table with Salesforce Account Id, and the Salesforce Opportunity remote table with the same Account Id.

**Parent Topic:**[[data-integration-salesforce-example|Reference Salesforce integration using remote tables]]

## Related

- [[config-csm-integration-salesforce|Using the IntegrationHub Salesforce spoke]]
- [[csm-integration-salesforce-spoke|Create Salesforce spoke actions to retrieve opportunities]]
- [[csm-remote-tables-definition|Remote tables and definition]]
- [[csm-opportunity-table-script|Example script that queries the Opportunity table]]
- [[csm-related-list-opportunity-table|Connect Customer Account and Salesforce Opportunities using a related list]]
- [[data-integration-salesforce-example|Reference Salesforce integration using remote tables]]
