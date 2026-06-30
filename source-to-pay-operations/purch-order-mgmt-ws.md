---
title: Source-to-Pay Workspace
description: The Purchase Order Management page in the Source-to-Pay Workspace enables you to manage and work on tasks related to purchase order exceptions.
locale: en-US
canonical_url: https://www.servicenow.com/docs/r/source-to-pay-operations/purch-order-mgmt-ws.html
release: australia
topic_type: concept
last_updated: "2026-03-12"
reading_time_minutes: 1
keywords: [source-to-pay workspace, purchase order management landing page]
breadcrumb: [Explore, Purchase Order Management, Source-to-Pay Operations, Finance and Supply Chain]
---

# Source-to-Pay Workspace

The [[purchase-order-mgmt-landing-page|Purchase Order Management]] page in the Source-to-Pay Workspace enables you to manage and work on tasks related to [[purchase-order-table|purchase order]] exceptions.

The Source-to-Pay Workspace provides a Purchase Order Management dashboard and tools that enable you to do the following:

-   Manage purchase order exceptions
-   View and manage [[purchase-order-exception-table|purchase order exception]] tasks​
-   Approve purchase order exceptions

The Source-to-Pay Workspace includes a landing page and a list view that enables you to work on various aspects of the purchase order exception management process.

For more information about Purchase Order Management landing page, see [POM landing page](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/source-to-pay-operations/source-to-pay-workspace/purch-order-mgmt-tab-s2pws.md).

For more information about Purchase Order Management list view, see [POM list page](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/source-to-pay-operations/source-to-pay-workspace/pom-list-page.md).

For more information about the Source-to-Pay Workspace, see [Source-to-Pay Workspace](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/source-to-pay-operations/source-to-pay-workspace/source-to-pay-ws-overview.md).

## End user and roles

|End user and goal|Required role|
|-----------------|-------------|
|Operational buyer: View and manage purchase order exceptions and tasks.|sn\_poem\_core.operational\_buyer|
|Purchase order management viewer: View purchase order exceptions.|sn\_poem\_core.viewer|
|Purchase order management admin: Local admin for the application and its settings.|sn\_poem\_core.admin|
|Purchase order management collaborator: View assigned purchase order exceptions and tasks.|sn\_poem\_core.collaborator|
|Fulfiller for Now Assist for POM: Role assigned to an operational buyer to access [[now-assist-for-purch-order-magmt|Now Assist for Purchase Order Management \(POM\)]].|sn\_poem\_gen\_ai\_now\_assist\_fulfiller|

-   **[[view-purch-order-exception|View a purchase order exception]]**  
As an Operational Buyer, view a purchase order exception in the Purchase Order Management landing page for further processing.
-   **[[purch-order-exception-details|Purchase order exception Details page]]**  
The Details page is displayed when you select the link of a purchase order exception.
-   **[[view-po-exception-task|View a purchase order exception task]]**  
View the purchase order exception record in Source-to-Pay Workspace to take action on your assigned task.

**Parent Topic:**[[explore-purch-order-mgmt|Explore Purchase Order Management]]

## Related

- [[view-purch-order-exception|View a purchase order exception]]
- [[purch-order-exception-details|Purchase order exception Details page]]
- [[view-po-exception-task|View a purchase order exception task]]
- [[explore-purch-order-mgmt|Explore Purchase Order Management]]
- [[purchase-order-mgmt-landing-page|Purchase Order Management]]
- [[purchase-order-table|Purchase order]]
- [[purchase-order-exception-table|Purchase Order Exception]]
- [[now-assist-for-purch-order-magmt|Now Assist for Purchase Order Management \(POM\)]]
