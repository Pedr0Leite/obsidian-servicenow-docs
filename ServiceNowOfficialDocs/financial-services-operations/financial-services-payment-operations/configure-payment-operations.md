---
title: Configure Financial Services Payment Operations
description: Review the components that are installed with the Financial Services Payment Operations application and modify as needed for your organization's business needs.
locale: en-US
canonical_url: https://www.servicenow.com/docs/r/financial-services-operations/financial-services-payment-operations/configure-payment-operations.html
release: australia
product: Financial Services Payment Operations
classification: financial-services-payment-operations
topic_type: task
last_updated: "2026-03-12"
reading_time_minutes: 2
breadcrumb: [Payment Operations, Banking applications, Financial Services Operations \(FSO\)]
tags:
  - financial-services-operations
  - payments
  - fso
  - processing
  - disputes
  - type-task
---

# Configure Financial Services Payment Operations

Review the components that are installed with the [[payment-ops-landing-page|Financial Services Payment Operations]] application and modify as needed for your organization's business needs.

## Before you begin

Make sure that the Financial Services Payment Operations application is installed.

Role required: sn\_bom\_payment.admin and admin

## Procedure

1.  Import your financial accounts, financial products, financial institutions, and transactions data into ServiceNow tables.

    For more information, see [[import-financial-accounts-products-institutions|Import your financial data using import sets]].

2.  Review the installed components and modify them or add new ones as applicable.

    |Task|Description|
    |----|-----------|
    |**Configure service definitions**|[[configure-service-definitions|Configure service definitions]] to enable unique flows and views for payment service cases and tasks.|
    |**Configure record producers**|[[create-modify-record-producers-fso-apps|Create or modify record producers]] to define request forms.|
    |**Edit or create new flows**|[[configure-flow-designer-flows-fso-apps|Edit or create new flows]] using Workflow Studio.|
    |**Modify interceptors and workspace record type selectors**|[[configure-request-types-fso|Modify interceptors and workspace record type selectors]] to configure payment request types.|
    |**Configure Service Level Agreements \(SLAs\)**|[[configure-sla-definitions-fso-cases|Configure the installed SLAs]] to configure SLA timings for payment service cases and tasks.|
    |**Configure user groups**|[[configure-groups-fso|Configure user groups]] for assignment of cases and tasks. You can also assign roles to groups and users.|
    |**Configure assignment rules**|[[configure-assignment-rules-fso-applications|Configure assignment rules]] to identify cases that meet certain conditions and then route those cases to agents.|
    |**Configure properties**|[Configure properties](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/financial-services-operations/financial-services-payment-operations/properties-installed-with-payment-operations.md) for payment operations.|

## Related

- [[import-financial-accounts-products-institutions|Import your financial data using import sets]]
- [[configure-service-definitions|Configure service definitions]]
- [[create-modify-record-producers-fso-apps|Create or modify record producers]]
- [[configure-flow-designer-flows-fso-apps|Configure flows]]
- [[configure-request-types-fso|Configure request types]]
- [[configure-sla-definitions-fso-cases|Configure SLA definitions]]
- [[configure-groups-fso|Configure groups]]
- [[configure-assignment-rules-fso-applications|Configure assignment rules]]
- [[payment-ops-landing-page|Financial Services Payment Operations]]
