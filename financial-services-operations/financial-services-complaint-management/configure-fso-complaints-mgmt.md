---
title: Configure Financial Services Complaint Management
description: Review the components that are installed with the Financial Services Complaint Management application and modify as needed for your organization's business needs.
locale: en-US
canonical_url: https://www.servicenow.com/docs/r/financial-services-operations/financial-services-complaint-management/configure-fso-complaints-mgmt.html
release: australia
product: Financial Services Complaint Management
classification: financial-services-complaint-management
topic_type: task
last_updated: "2026-03-12"
reading_time_minutes: 3
breadcrumb: [Complaint Management, Common applications, Financial Services Operations \(FSO\)]
---

# Configure Financial Services Complaint Management

Review the components that are installed with the [[fso-complaint-mgmt-landing-page|Financial Services Complaint Management]] application and modify as needed for your organization's business needs.

## Before you begin

Make sure that the Financial Services Complaint Management application is installed. For more information, see [Install Financial Services Complaint Management](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/financial-services-operations/financial-services-complaint-management/install-fso-complaints-management.md).

Role required: sn\_bom\_compl.admin and admin

## Procedure

1.  Import your financial accounts, financial products, financial institutions, and transactions data into ServiceNow tables.

    For more information, see [[import-financial-accounts-products-institutions|Import your financial data using import sets]].

2.  Review the installed components and modify them or add new ones as applicable.

    |Task|Description|
    |----|-----------|
    |**Configure service definitions**|[[configure-service-definitions|Configure service definitions]] to enable unique flows and views for complaint service cases and tasks.|
    |**Configure record producers**|[[create-modify-record-producers-fso-apps|Create or modify record producers]] to define request forms.|
    |**Modify interceptors and workspace record type selectors**|[[configure-request-types-fso|Modify interceptors and workspace record type selectors]] to configure complaint request types.|
    |**Edit or create flows**|[[configure-flow-designer-flows-fso-apps|Edit or create flows]] using Workflow Studio.|
    |**Configure playbook**|[[configure-playbooks-fso-apps|Edit or create a new playbook]] using Playbooks.|
    |**Configure workspace**|[[configure-csm-workspace-fso-apps|Configure CSM Configurable Workspace]] to enable agents to interact with customers and create and work on cases.|
    |**Define response templates**|[Define response templates](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/financial-services-operations/financial-services-complaint-management/configure-response-templates-fso-complaints.md) for complaint service case for a quick and consistent messaging to customers.|
    |**[[configure-regulation-categories-fso-complaint-mgmt|Configure regulation categories and subcategories]]**|[Configure regulation categories and subcategories](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/financial-services-operations/financial-services-complaint-management/configure-regulation-categories-fso-complaint-mgmt.md) to be used in complaint cases that have regulatory impact.|
    |**Configure Service Level Agreements \(SLAs\)**|[[configure-sla-definitions-fso-cases|Configure the installed SLAs]] to configure SLA timings for complaint service cases and tasks.|
    |**Configure user groups**|[[configure-groups-fso|Configure user groups]] for assignment of cases and tasks. You can also assign roles to groups and users.|
    |**Configure assignment rules**|[[configure-assignment-rules-fso-applications|Configure assignment rules]] to identify cases that meet certain conditions and then route those cases to agents.|

## Related

- [[import-financial-accounts-products-institutions|Import your financial data using import sets]]
- [[configure-service-definitions|Configure service definitions]]
- [[create-modify-record-producers-fso-apps|Create or modify record producers]]
- [[configure-request-types-fso|Configure request types]]
- [[configure-flow-designer-flows-fso-apps|Configure flows]]
- [[configure-playbooks-fso-apps|Configure playbooks]]
- [[configure-csm-workspace-fso-apps|Configure CSM Configurable Workspace]]
- [[configure-sla-definitions-fso-cases|Configure SLA definitions]]
- [[configure-groups-fso|Configure groups]]
- [[configure-assignment-rules-fso-applications|Configure assignment rules]]
- [[fso-complaint-mgmt-landing-page|Financial Services Complaint Management]]
- [[configure-regulation-categories-fso-complaint-mgmt|Configure regulation categories and subcategories]]
