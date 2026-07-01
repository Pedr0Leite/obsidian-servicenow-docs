---
title: Configure Group Life Servicing
description: Review the components that are installed with the Group Life Servicing application and modify as needed for your organization's business needs.
locale: en-US
canonical_url: https://www.servicenow.com/docs/r/financial-services-operations/configure-group-life-servicing.html
release: australia
topic_type: task
last_updated: "2026-03-12"
reading_time_minutes: 3
breadcrumb: [Configure, Group Life Servicing, Life Insurance Servicing, Insurance applications, Financial Services Operations \(FSO\)]
tags:
  - financial-services-operations
  - type-task
---

# Configure Group Life Servicing

Review the components that are installed with the [[group-life-servicing|Group Life Servicing]] application and modify as needed for your organization's business needs.

## Before you begin

Make sure that the Group Life Servicing application is installed. For more information, see [[install-group-life-servicing|Install Group Life Servicing]].

Role required: sn\_ins\_group\_life.admin or admin

## Procedure

1.  Import your financial accounts, financial products, financial institutions, and transactions data into ServiceNow tables.

    For more information, see [[import-financial-accounts-products-institutions|Import your financial data using import sets]].

2.  Review the installed components and modify them or add new ones as applicable.

<table><thead><tr><th align="left" id="d36584e103">

Task

</th><th align="left" id="d36584e106">

Description

</th></tr></thead><tbody><tr><td id="d36584e115">

**Configure service definitions**

</td><td>

[[configure-service-definitions|Configure service definitions]] to enable unique flows and views for policy service case and task. You should configure service definitions for:-   Group Life and Disability Servicing
-   Group Life and Disability Underwriting


</td></tr><tr><td id="d36584e147">

**Configure record producers**

</td><td>

[[create-modify-record-producers-fso-apps|Create or modify record producers]] to define request forms.

</td></tr><tr><td id="d36584e167">

**Create flows**

</td><td>

[[configure-flow-designer-flows-fso-apps|Create flows]] using Workflow Studio.

</td></tr><tr><td id="d36584e189">

**Configure playbooks**

</td><td>

[[configure-playbooks-fso-apps|Edit or create a new playbook]] using Playbooks.

</td></tr><tr><td id="d36584e211">

**Configure CSM Configurable Workspace**

</td><td>

[[configure-csm-workspace-fso-apps|Configure CSM Configurable Workspace]] to enable requesters, contributors, and processors to interact with customers, and create and work on cases.

</td></tr><tr><td id="d36584e238">

**Modify interceptors and workspace record type selectors**

</td><td>

[[configure-request-types-fso|Modify interceptors and workspace record type selectors]] to configure policy request types.

</td></tr><tr><td id="d36584e257">

**Configure user groups**

</td><td>

[[configure-groups-fso|Configure user groups]] for assignment of cases and tasks. You can also assign roles to groups and users.

</td></tr><tr><td id="d36584e276">

**Configure assignment rules**

</td><td>

[[configure-assignment-rules-fso-applications|Configure assignment rules]] to identify cases that meet certain conditions and then route those cases to agents.

</td></tr><tr><td id="d36584e293">

**Configure Service Level Agreements \(SLAs\)**

</td><td>

[[configure-sla-definitions-fso-cases|Configure the installed SLAs]] to configure SLA timings for policy service cases and tasks.

</td></tr><tr><td id="d36584e312">

**Configure Document Processor**

</td><td>

[[configuring-fso-document-processor|Configure Document Processor]] for document categories, document types, inbound and outbound document rules, and approval rules for document deferments and exceptions.

</td></tr></tbody>
</table>

## Related

- [[install-group-life-servicing|Install Group Life Servicing]]
- [[import-financial-accounts-products-institutions|Import your financial data using import sets]]
- [[configure-service-definitions|Configure service definitions]]
- [[create-modify-record-producers-fso-apps|Create or modify record producers]]
- [[configure-flow-designer-flows-fso-apps|Configure flows]]
- [[configure-playbooks-fso-apps|Configure playbooks]]
- [[configure-csm-workspace-fso-apps|Configure CSM Configurable Workspace]]
- [[configure-request-types-fso|Configure request types]]
- [[configure-groups-fso|Configure groups]]
- [[configure-assignment-rules-fso-applications|Configure assignment rules]]
- [[configure-sla-definitions-fso-cases|Configure SLA definitions]]
- [[configuring-fso-document-processor|Configuring Financial Services Operations Document Processor]]
- [[group-life-servicing|Group Life Servicing]]
