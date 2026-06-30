---
title: Configure Financial Services Card Operations
description: Review the components that are installed with the Financial Services Card Operations application and modify as needed for your organization's business needs.
locale: en-US
canonical_url: https://www.servicenow.com/docs/r/financial-services-operations/financial-services-card-operations/set-up-card-operations.html
release: australia
product: Financial Services Card Operations
classification: financial-services-card-operations
topic_type: task
last_updated: "2026-03-12"
reading_time_minutes: 2
breadcrumb: [Card Operations, Banking applications, Financial Services Operations \(FSO\)]
---

# Configure Financial Services Card Operations

Review the components that are installed with the [[card-ops-landing-page|Financial Services Card Operations]] application and modify as needed for your organization's business needs.

## Before you begin

Make sure that the Financial Services Card Operations application is installed.

Role required: sn\_bom\_credit\_card.admin and admin

## About this task

You can set up your implementation for Financial Services Card Operations by installing the Financial Services Card Operations application, importing [[fso-overview|financial services]] data, and reviewing and configuring the [[components-installed-with-dispute-rules-content-pack-for-mastercard|components installed]] with the application.

## Procedure

1.  Import your financial accounts, financial products, financial institutions, and transactions data into ServiceNow tables.

    For more information, see [[import-financial-accounts-products-institutions|Import your financial data using import sets]].

2.  Review the installed components and modify them or add new ones as applicable.

    |Task|Description|
    |----|-----------|
    |**Configure service definitions**|[[configure-service-definitions|Configure service definitions]] to enable unique flows and views for card service cases and tasks.|
    |**Configure record producers**|[[create-modify-record-producers-fso-apps|Create or modify record producers]] to define request forms.|
    |**Edit or create new flows**|[[configure-flow-designer-flows-fso-apps|Edit or create new flows]] using Workflow Studio.|
    |**Modify interceptors and workspace record type selectors**|[[configure-request-types-fso|Modify interceptors and workspace record type selectors]] to configure payment request types.|
    |**Configure Service Level Agreements \(SLAs\)**|[[configure-sla-definitions-fso-cases|Configure the installed SLAs]] to configure SLA timings for card service cases and tasks.|
    |**Configure user groups**|[[configure-groups-fso|Configure user groups]] for assignment of cases and tasks. You can also assign roles to groups and users.|
    |**Configure assignment rules**|[[configure-assignment-rules-fso-applications|Configure assignment rules]] to identify cases that meet certain conditions and then route those cases to agents.|
    |**Configure properties**|[Configure properties](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/financial-services-operations/financial-services-card-operations/properties-installed-card-ops.md) for card operations.|

## Related

- [[import-financial-accounts-products-institutions|Import your financial data using import sets]]
- [[configure-service-definitions|Configure service definitions]]
- [[create-modify-record-producers-fso-apps|Create or modify record producers]]
- [[configure-flow-designer-flows-fso-apps|Configure flows]]
- [[configure-request-types-fso|Configure request types]]
- [[configure-sla-definitions-fso-cases|Configure SLA definitions]]
- [[configure-groups-fso|Configure groups]]
- [[configure-assignment-rules-fso-applications|Configure assignment rules]]
- [[card-ops-landing-page|Financial Services Card Operations]]
- [[fso-overview|Financial Services]]
- [[components-installed-with-dispute-rules-content-pack-for-mastercard|Components installed]]
