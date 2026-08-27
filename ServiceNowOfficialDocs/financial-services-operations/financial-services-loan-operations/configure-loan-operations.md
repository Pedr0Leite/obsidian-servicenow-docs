---
title: Configure Financial Services Loan Operations
description: Review the components that are installed with the Financial Services Loan Operations application and modify as needed for your organization's business needs.
locale: en-US
canonical_url: https://www.servicenow.com/docs/r/financial-services-operations/financial-services-loan-operations/configure-loan-operations.html
release: australia
product: Financial Services Loan Operations
classification: financial-services-loan-operations
topic_type: task
last_updated: "2026-03-12"
reading_time_minutes: 3
breadcrumb: [Loan Operations, Banking applications, Financial Services Operations \(FSO\)]
tags:
  - financial-services-operations
  - loans
  - servicing
  - fso
  - banking
  - type-task
---

# Configure Financial Services Loan Operations

Review the components that are installed with the [[loan-ops-landing-page|Financial Services Loan Operations]] application and modify as needed for your organization's business needs.

## Before you begin

Make sure that the Financial Services Loan Operations application is installed. For more information, see [Install Financial Services Business Loan Operations](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/financial-services-operations/financial-services-loan-operations/install-fso-business-loan-ops.md) and [Install Financial Services Personal Loan Operations](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/financial-services-operations/financial-services-loan-operations/install-fso-personal-loan-ops.md).

Role required: sn\_bom\_loan\_b2b.admin, sn\_bom\_loan.b2c\_admin, and admin

## Procedure

1.  Import your financial accounts, financial products, financial institutions, and transactions data into ServiceNow tables.

    For more information, see [[import-financial-accounts-products-institutions|Import your financial data using import sets]].

2.  Review the installed components and modify them or add new ones as applicable.

    |Task|Description|
    |----|-----------|
    |**Configure service definitions**|[[configure-service-definitions|Configure service definitions]] to enable unique flows and views for loan service cases and tasks.|
    |**Configure record producers**|[[create-modify-record-producers-fso-apps|Create or modify record producers]] to define request forms.|
    |**Edit or create new flows**|[[configure-flow-designer-flows-fso-apps|Edit or create new flows]] using Workflow Studio.|
    |**Modify interceptors and workspace record type selectors**|[[configure-request-types-fso|Modify interceptors and workspace record type selectors]] to configure loan request types.|
    |**Configure playbook**|[[configure-playbooks-fso-apps|Edit or create a new playbook]] using Playbooks.|
    |**Configure workspace**|[[configure-csm-workspace-fso-apps|Configure CSM Configurable Workspace]] to enable agents to interact with customers and create and work on cases.|
    |**Configure Service Level Agreements \(SLAs\)**|[[configure-sla-definitions-fso-cases|Configure the installed SLAs]] to configure SLA timings for loan service cases and tasks.|
    |**Configure user groups**|[[configure-groups-fso|Configure user groups]] for assignment of cases and tasks. You can also assign roles to groups and users.|
    |**Configure assignment rules**|[[configure-assignment-rules-fso-applications|Configure assignment rules]] to identify cases that meet certain conditions and then route those cases to agents.|
    |**Configure Document Processor**|[[configuring-fso-document-processor|Configure Document Processor]] for document categories, document types, inbound and outbound document rules, and approval rules for document deferments and exceptions.|

## Related

- [[import-financial-accounts-products-institutions|Import your financial data using import sets]]
- [[configure-service-definitions|Configure service definitions]]
- [[create-modify-record-producers-fso-apps|Create or modify record producers]]
- [[configure-flow-designer-flows-fso-apps|Configure flows]]
- [[configure-request-types-fso|Configure request types]]
- [[configure-playbooks-fso-apps|Configure playbooks]]
- [[configure-csm-workspace-fso-apps|Configure CSM Configurable Workspace]]
- [[configure-sla-definitions-fso-cases|Configure SLA definitions]]
- [[configure-groups-fso|Configure groups]]
- [[configure-assignment-rules-fso-applications|Configure assignment rules]]
- [[configuring-fso-document-processor|Configuring Financial Services Operations Document Processor]]
- [[loan-ops-landing-page|Financial Services Loan Operations]]
