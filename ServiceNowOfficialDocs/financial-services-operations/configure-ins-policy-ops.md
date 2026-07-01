---
title: Configure Personal Lines Servicing
description: Review the components that are installed with the Personal Lines Servicing application and modify as needed for your organization's business needs.
locale: en-US
canonical_url: https://www.servicenow.com/docs/r/financial-services-operations/configure-ins-policy-ops.html
release: australia
topic_type: task
last_updated: "2026-03-12"
reading_time_minutes: 3
breadcrumb: [Personal Lines Servicing, Property and Casualty Insurance Servicing, Insurance applications, Financial Services Operations \(FSO\)]
tags:
  - financial-services-operations
  - type-task
---

# Configure Personal Lines Servicing

Review the components that are installed with the Personal Lines Servicing application and modify as needed for your organization's business needs.

## Before you begin

Make sure that the Personal Lines Servicing application is installed. For more information, see [[install-ins-policy-ops|Install Personal Lines Servicing]].

Role required: sn\_ins\_policy\_b2c.admin or admin

## Procedure

1.  Import your financial accounts, financial products, financial institutions, and transactions data into ServiceNow tables.

    For more information, see [[import-financial-accounts-products-institutions|Import your financial data using import sets]].

2.  Review the installed components and modify them or add new ones as applicable.

<table id="choicetable_ajc_kk5_z4b"><thead><tr><th align="left" id="d135558e123">

Task

</th><th align="left" id="d135558e126">

Description

</th></tr></thead><tbody><tr><td id="d135558e135">

**Configure service definitions**

</td><td>

[[configure-service-definitions|Configure service definitions]] to enable unique flows and views for policy service case and task. You should configure service definitions for:-   Personal Lines Servicing
-   Insurance Underwriting Operations


</td></tr><tr><td id="d135558e168">

**Configure record producers**

</td><td>

[[create-modify-record-producers-fso-apps|Create or modify record producers]] to define request forms.

</td></tr><tr><td id="d135558e188">

**Create flows**

</td><td>

[[configure-flow-designer-flows-fso-apps|Create flows]] using Workflow Studio.

</td></tr><tr><td id="d135558e210">

**Configure playbooks**

</td><td>

[[configure-playbooks-fso-apps|Edit or create a new playbook]] using Playbooks.

</td></tr><tr><td id="d135558e232">

**Configure CSM Configurable Workspace**

</td><td>

[[configure-csm-workspace-fso-apps|Configure CSM Configurable Workspace]] to enable requesters, contributors, and processors to interact with customers, and create and work on cases.

</td></tr><tr><td id="d135558e259">

**Modify interceptors and workspace record type selectors**

</td><td>

[[configure-request-types-fso|Modify interceptors and workspace record type selectors]] to configure policy request types.

</td></tr><tr><td id="d135558e278">

**Configure user groups**

</td><td>

[[configure-groups-fso|Configure user groups]] for assignment of cases and tasks. You can also assign roles to groups and users.

</td></tr><tr><td id="d135558e297">

**Configure assignment rules**

</td><td>

[[configure-assignment-rules-fso-applications|Configure assignment rules]] to identify cases that meet certain conditions and then route those cases to agents.

</td></tr><tr><td id="d135558e314">

**Configure Service Level Agreements \(SLAs\)**

</td><td>

[[configure-sla-definitions-fso-cases|Configure the installed SLAs]] to configure SLA timings for policy service cases and tasks.

</td></tr><tr><td id="d135558e333">

**Configure Document Processor**

</td><td>

[[configuring-fso-document-processor|Configure Document Processor]] for document categories, document types, inbound and outbound document rules, and approval rules for document deferments and exceptions.

</td></tr></tbody>
</table>
**Parent Topic:**[[fso-ins-personal-policy-ops-landing-page|Personal Lines Servicing]]

## Related

- [[install-ins-policy-ops|Install Personal Lines Servicing]]
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
- [[fso-ins-personal-policy-ops-landing-page|Personal Lines Servicing]]
