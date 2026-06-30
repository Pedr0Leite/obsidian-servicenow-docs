---
title: Setting up CSM integration with IT Service Management
description: Integrate Customer Service Management with IT Service Management that includes the Request, Incident, Problem, and Change Management applications. With this integration, users can create request, incident, problem, and change records from customer service cases. External users can view these records from the Customer and Consumer Service Portals.
locale: en-US
canonical_url: https://www.servicenow.com/docs/r/customer-service-management/setting-up-csm-integration-with-itsm.html
release: australia
topic_type: concept
last_updated: "2026-03-12"
reading_time_minutes: 2
breadcrumb: [Integrate with IT Service Management, Integrate, Customer Service Management]
---

# Setting up CSM integration with IT Service Management

Integrate [[c_CustomerServiceManagement|Customer Service Management]] with IT Service Management that includes the Request, Incident, Problem, and Change Management applications. With this integration, users can create request, incident, problem, and change records from customer service cases. External users can view these records from the Customer and Consumer Service Portals.

<table id="table_sqn_y5f_nlb"><thead><tr><th>

Task

</th><th>

Description

</th></tr></thead><tbody><tr><td>

[[configure-csm-sm-integration|Integrate with IT Service Management using Guided Setup]]

</td><td>

Use the Guided Setup to integrate CSM with IT Service Management.

</td></tr><tr><td>

[[install-csm-with-service-management|Install Customer Service Management with Service Management]]

</td><td>

Activate the CSM with Service Management plugin \(com.sn\_cs\_sm\) to enable the integration the following applications:

-   Incident Management
-   Problem Management
-   Change Management

</td></tr><tr><td>

[[install-csm-with-request-management|Install Customer Service Management with Request Management]]

</td><td>

Activate the CSM with Request Management plugin \(com.sn\_cs\_sm\_request\) to use the integration with the Request Management application.

</td></tr><tr><td>

[[assign-csm-itsm-integration-roles|Assigning CSM/ITSM integration roles]]

</td><td>

Assign the required roles to the customer service agents and managers who will be creating the request, incident, problem, and change records from customer service cases.

</td></tr><tr><td>

[[csm-itsm-integration-view-request|Enable external customers to access problem, change, and request records]]

</td><td>

Assign access controls \(ACLs\) to the external user roles to provide visibility to case-related request, problem, and change records from the Customer and Consumer Service Portals.

</td></tr><tr><td>

[[enable-customer-request-from-portal|Enable external customers to create requests]]

</td><td>

[[configure-data-model-roles|Assign roles]] to external customers which enable them to create requests.

</td></tr><tr><td>

[[enable-customer-request-approval|Enable external customers to approve requests and changes]]

</td><td>

Enable external customers to approve changes and requests:-   Add external users to approval groups or assign roles for approval users.
-   Add the necessary ACLs to the snc\_external role for the following table:
    -   Change Request \(change\_request\)
    -   Request \(sc\_request\)
    -   Request Item \(sc\_req\_item\)

</td></tr><tr><td>

[[enable-create-request-case-type|Enable the Create Request UI action for case types]]

</td><td>

Enable the **Create Request** UI action for case type tables that extend the Case \[sn\_customerservice\_case\] table.

</td></tr></tbody>
</table>

## Related

- [[configure-csm-sm-integration|Integrate with IT Service Management using Guided Setup]]
- [[install-csm-with-service-management|Install Customer Service Management with Service Management]]
- [[install-csm-with-request-management|Install Customer Service Management with Request Management]]
- [[assign-csm-itsm-integration-roles|Assigning CSM/ITSM integration roles]]
- [[csm-itsm-integration-view-request|Enable external customers to access problem, change, and request records]]
- [[enable-customer-request-from-portal|Enable external customers to create requests]]
- [[enable-customer-request-approval|Enable external customers to approve requests and changes]]
- [[enable-create-request-case-type|Enable the Create Request UI action for case types]]
- [[c_CustomerServiceManagement|Customer Service Management]]
- [[configure-data-model-roles|Assign roles]]
