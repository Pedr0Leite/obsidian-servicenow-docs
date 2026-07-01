---
title: Configure Personal Lines Claims
description: Review the components that are installed with the Personal Lines Claims application and modify as needed for your organization's business needs.
locale: en-US
canonical_url: https://www.servicenow.com/docs/r/financial-services-operations/insurance-claims/configure-personal-lines-claims.html
release: australia
product: Insurance Claims
classification: insurance-claims
topic_type: task
last_updated: "2026-03-12"
reading_time_minutes: 3
breadcrumb: [Configure, Personal Lines Claims, Exploring insurance claims applications, Insurance applications, Financial Services Operations \(FSO\)]
---

# Configure Personal Lines Claims

Review the components that are installed with the [[personal-lines-claims-landing-page|Personal Lines Claims]] application and modify as needed for your organization's business needs.

## Before you begin

Make sure that the Personal Lines Claims application is installed. For more information, see [Install Personal Lines Claims](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/financial-services-operations/insurance-claims/install-personal-lines-claims.md).

Role required: sn\_ins\_claim\_pers.admin and admin

## Procedure

1.  Import your financial accounts, financial products, financial institutions, and transactions data into ServiceNow tables.

    For more information, see [[import-financial-accounts-products-institutions|Import your financial data using import sets]].

2.  Review the installed components and modify them or add new ones as applicable.

<table id="choicetable_jt1_44w_fvb"><thead><tr><th align="left" id="d39427e109">

Task

</th><th align="left" id="d39427e112">

Description

</th></tr></thead><tbody><tr><td id="d39427e118">

**Configure service definitions**

</td><td>

Configure service definitions to enable unique flows and views for service cases and tasks. For more information, see [[configure-service-definitions|Configure service definitions]].You can add new case types and configure service definitions for each type.

</td></tr><tr><td id="d39427e140">

**Edit or create flows**

</td><td>

Edit or create flows using Workflow Studio. For more information, see [[configure-flow-designer-flows-fso-apps|Edit or create flows]].

</td></tr><tr><td id="d39427e162">

**Configure playbook**

</td><td>

Create a playbook by using Playbooks. For more information, see [[configure-playbooks-fso-apps|Edit or create a new playbook]].

</td></tr><tr><td id="d39427e184">

**Configure CSM Configurable Workspace**

</td><td>

Configure CSM Configurable Workspace to enable agents to interact with customers and create and work on cases.For more information, see [[configure-csm-workspace-fso-apps|Configure CSM Configurable Workspace]].

</td></tr><tr><td id="d39427e218">

**Configure the Claim Workspace, Fraud score and Claim summary pages**

</td><td>

Configure Claim workspace, Fraud score, and Claim summary pages on claim cases and claim [[adjuster-tasks-workspace-pers|adjuster tasks]]. For more information, see [Enable Claim workspace, Fraud score, and Claim summary pages](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/financial-services-operations/insurance-claims/enable-fraud-score-and-claim-summary-pages.md).**Note:** The Claim workspace is accessible from an adjuster task. The Fraud score and Claim summary pages are accessible from both a claim case and an adjuster task.

</td></tr><tr><td id="d39427e236">

**Configure Service Level Agreements \(SLAs\)**

</td><td>

Configure the installed SLAs to configure SLA timings for claim service cases and tasks.For more information, see [[configure-sla-definitions-fso-cases|Configure the installed SLAs]]

</td></tr><tr><td id="d39427e257">

**Configure user groups**

</td><td>

Configure user groups for assignment of cases and tasks. You can also assign roles to groups and users.For more information, see [[configure-groups-fso|Configure user groups]].

</td></tr><tr><td id="d39427e279">

**Configure assignment rules**

</td><td>

Configure assignment rules to identify cases that meet certain conditions and then route those cases to agents. For more information, see [[configure-assignment-rules-fso-applications|Configure assignment rules]].

</td></tr><tr><td id="d39427e295">

**Configure Document Processor**

</td><td>

Configure document processor for document categories, document types, inbound and outbound document rules, and approval rules for document deferments and exceptions.For more information, see [[configuring-fso-document-processor|Configure Document Processor]].

</td></tr><tr><td id="d39427e322">

**Configure archive rules**

</td><td>

The Archive Personal Auto Claim Case rule archives personal auto claim cases that are older than a year. This rule is inactive by default.To configure archive rules, navigate to **System Archiving** &gt; **Archive Rules** and enable the **Archive Personal Auto Claim Case** rule.

</td></tr></tbody>
</table>

## Related

- [[import-financial-accounts-products-institutions|Import your financial data using import sets]]
- [[configure-service-definitions|Configure service definitions]]
- [[configure-flow-designer-flows-fso-apps|Configure flows]]
- [[configure-playbooks-fso-apps|Configure playbooks]]
- [[configure-csm-workspace-fso-apps|Configure CSM Configurable Workspace]]
- [[configure-sla-definitions-fso-cases|Configure SLA definitions]]
- [[configure-groups-fso|Configure groups]]
- [[configure-assignment-rules-fso-applications|Configure assignment rules]]
- [[configuring-fso-document-processor|Configuring Financial Services Operations Document Processor]]
- [[personal-lines-claims-landing-page|Personal Lines Claims]]
- [[adjuster-tasks-workspace-pers|Adjuster tasks]]
