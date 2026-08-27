---
title: Configuring Intelligent Servicing for Fraud
description: You can set up your implementation for the Intelligent Servicing for Fraud application by installing the application, importing financial services data, and reviewing and configuring the components that are installed with the application.
locale: en-US
canonical_url: https://www.servicenow.com/docs/r/financial-services-operations/intelligent-servicing-for-fraud/configuring-intelligent-servicing-for-fraud.html
release: australia
product: Intelligent Servicing for Fraud
classification: intelligent-servicing-for-fraud
topic_type: concept
last_updated: "2026-03-12"
reading_time_minutes: 3
keywords: [configure intelligent servicing for fraud, set up fraud application, install intelligent servicing for fraud, assign roles for fraud users, configure service definitions, configure playbooks, configure workspace, configure user groups, configure assignment rules, configure slas, service level agreements, fraud operations analyst, fraud operations manager, fraud case routing]
breadcrumb: [Intelligent Servicing for Fraud, Banking applications, Financial Services Operations \(FSO\)]
tags:
  - financial-services-operations
  - fraud
  - ai
  - detection
  - fso
  - type-concept
---

# Configuring Intelligent Servicing for Fraud

You can set up your implementation for the [[intelligent-servicing-for-fraud-landing-page|Intelligent Servicing for Fraud]] application by installing the application, importing [[fso-overview|financial services]] data, and reviewing and configuring the components that are installed with the application.

The following table provides an overview of the configuration tasks that are required for Intelligent Servicing for Fraud.

<table id="table_ksw_gpr_4nb"><thead><tr><th>

Task

</th><th>

Description

</th></tr></thead><tbody><tr><td>

[[install-intelligent-servicing-for-fraud|Install Intelligent Servicing for Fraud]].

</td><td>

Install the Intelligent Servicing for Fraud application to work on fraud cases.

 For detailed instructions on how to install the application, see [Install Intelligent Servicing for Fraud](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/financial-services-operations/intelligent-servicing-for-fraud/install-intelligent-servicing-for-fraud.md).

</td></tr><tr><td>

[[assign-roles-for-intelligent-servicing-for-fraud-users|Assign roles for Intelligent Servicing for Fraud users]].

</td><td>

Assign roles to control the actions that are available for each user.

 For detailed instructions on how to assign roles, see [Assign roles for Intelligent Servicing for Fraud users](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/financial-services-operations/intelligent-servicing-for-fraud/assign-roles-for-intelligent-servicing-for-fraud-users.md).

</td></tr><tr><td>

Configure service definitions.

</td><td>

Configure service definitions by navigating to **Fraud Operations** &gt; **Administration** &gt; **Service Definitions.**.

 For detailed instructions on how to configure service definitions, see [[configure-service-definitions|Configure service definitions]].

</td></tr><tr><td>

Configure a playbook.

</td><td>

Configure the playbook by navigating to **All** &gt; **Process Automation** &gt; **Process Automation Designer.**.

 For detailed instructions on how to edit or create flows, see [[configure-playbooks-fso-apps|Edit or create a new playbook]].

</td></tr><tr><td>

Configure CSM Configurable Workspace.

</td><td>

Configure CSM Configurable Workspace to enable agents to interact with customers and to create and work on cases.

 For detailed instructions on how to configure CSM Configurable Workspace, see [[configure-csm-workspace-fso-apps|Configure CSM Configurable Workspace.]]

</td></tr><tr><td>

Edit or create flows.

</td><td>

Edit or create flows by navigating to **All** &gt; **Process Automation** &gt; **Flow Designer.**.

 For detailed instructions on how to edit or create flows, see [[configure-flow-designer-flows-fso-apps|Configure flows]]

</td></tr><tr><td>

Configure service level agreements \(SLAs\).

</td><td>

Configure an SLA by navigating to **All** &gt; **Service Level Management** &gt; **SLA** &gt; **SLA Definitions**.

 For detailed instructions on how to configure an SLA, see [[configure-sla-definitions-fso-cases|Configure the Service Level Agreements \(SLAs\)]].

</td></tr><tr><td>

Configure user groups.

</td><td>

Configure the following user groups for case and task assignments. You can also assign roles to groups and users.

 -   Fraud operations analyst \(sn\_bom\_fraud.agent\)
-   Fraud operations investigator \(sn\_bom\_fraud.agent\)
-   Fraud operations manager \(sn\_bom\_fraud.manager and sn\_process\_optimization\_analyst\)

 For detailed instructions on how to configure user groups, see [[configure-groups-fso|Configure user groups]].

</td></tr><tr><td>

Configure assignment rules to route tasks to agents, based on their skill sets.

</td><td>

Configure the Fraud case \(sn\_bom\_fraud\_case\) assignment rule to identify cases that meet certain conditions and then route those cases to agents.

 For detailed instructions on how to configure assignment rules, see [[configure-assignment-rules-fso-applications|Configure assignment rules]]

</td></tr></tbody>
</table>

## Related

- [[configure-service-definitions|Configure service definitions]]
- [[configure-playbooks-fso-apps|Configure playbooks]]
- [[configure-csm-workspace-fso-apps|Configure CSM Configurable Workspace]]
- [[configure-flow-designer-flows-fso-apps|Configure flows]]
- [[configure-sla-definitions-fso-cases|Configure SLA definitions]]
- [[configure-groups-fso|Configure groups]]
- [[configure-assignment-rules-fso-applications|Configure assignment rules]]
- [[intelligent-servicing-for-fraud-landing-page|Intelligent Servicing for Fraud]]
- [[fso-overview|Financial Services]]
- [[install-intelligent-servicing-for-fraud|Install Intelligent Servicing for Fraud]]
- [[assign-roles-for-intelligent-servicing-for-fraud-users|Assign roles for Intelligent Servicing for Fraud users]]
