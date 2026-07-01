---
title: Configure Individual Life Claims
description: Configure the components that are installed with the Individual Life Claims application to meet your organization's claims requirements. Examples include long-term care, disability, or critical illness.
locale: en-US
canonical_url: https://www.servicenow.com/docs/r/financial-services-operations/insurance-claims/configure-individual-life-claims.html
release: australia
product: Insurance Claims
classification: insurance-claims
topic_type: task
last_updated: "2026-03-12"
reading_time_minutes: 6
breadcrumb: [Configure, Individual Life Claims, Exploring insurance claims applications, Insurance applications, Financial Services Operations \(FSO\)]
---

# Configure Individual Life Claims

Configure the components that are installed with the [[individual-life-claims-landing-page|Individual Life Claims]] application to meet your organization's claims requirements. Examples include long-term care, disability, or critical illness.

## Before you begin

Make sure that the Individual Life Claims application is installed. For more information, see [Install Individual Life Claims](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/financial-services-operations/insurance-claims/install-individual-life-claims.md).

Role required: admin

## About this task

Individual Life Claims includes a death benefit claim workflow that demonstrates the ability to work on multiple policy claims from a single case. It also includes a first-notice-of-loss \(FNOL\) playbook and a customizable workspace for claims adjusters. See [Individual Life Claims workflows](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/financial-services-operations/insurance-claims/individual-life-claims-workflows.md) for more information.

## Procedure

1.  Import your insurance policies, financial products, and financial institutions into ServiceNow tables.

    For more information, see [[import-financial-accounts-products-institutions|Import your financial data using import sets]].

2.  Review the installed components and modify them, or add new ones as applicable.

<table id="choicetable_oxg_nxp_4bc"><thead><tr><th align="left" id="d54239e128">

Task

</th><th align="left" id="d54239e131">

Description

</th></tr></thead><tbody><tr><td id="d54239e137">

**Configure roles and user groups**

</td><td>

Determine the roles of the individuals that you need to work on the claim cases for your line of business. Set up the roles to support the permissions that are required to adjudicate a claim. The roles should inherit the included roles from FSO core. For more information, see [Managing roles](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/platform-administration/ua-creating-roles.md).

 Required roles include:

 -   Viewer: Included in the Individual Life Claims application and inherits the viewer role, and account or customer data viewer roles from FSO core. This role can view the customer, case, and policy information for your line of business.
-   Adjuster: Included in the Individual Life Claims application and inherits the core adjuster role, and document processor agent role, from FSO core. This role evaluates the claims for your line of business.
-   FNOL Agent: Included in the Individual Life Claims application and inherits the first-notice-of-loss \(FNOL\) representative core role. This FNOL agent role is shared across all lines of business.
-   Manager: Included in the Individual Life Claims application and inherits the death benefit claims adjuster role. This role contains the adjuster roles for all your lines of business. This role has the permission to view Performance Analytics dashboards. This role is shared across all lines of business.
-   Admin: Included in Individual Life Claims and inherits the service definition admin core role. This role performs the configurations that are required for the application. This role is shared across all your lines of business. You may not need to make any changes to this role.
 Next, configure the user groups for the assignment of cases and tasks. You can also assign roles to groups. For more information, see [[configure-groups-fso|Configure user groups]].

</td></tr><tr><td id="d54239e217">

**Set up script includes**

</td><td>

Use script includes to store JavaScript that runs on the server. By using script includes in your claims flow, you enable reusability and inheritance from the base objects. Add the following for each table that was created for your line of business:

-   An Action layer script include contains the UI-level action functions.
-   A Service layer script include contains the middle layer business logic.
-   A DAO layer script include contains the methods to perform CRUD operations.
-   Any other script includes based on your requirements.
Modify the ClaimConstants script include to reuse the object names across functions.

For more information, see [Script includes](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/api-reference/scripts/c_ScriptIncludes.md).

</td></tr><tr><td id="d54239e250">

**Configure tables and ACLs**

</td><td>

Configure the tables by reviewing the existing tables that were provided in Insurance Claim Core and the tables included in this application, and make changes according to your requirements.Configure access control lists \(ACLs\) on these tables to give the appropriate permissions to the roles and personas who work on the cases and tasks.

**Note:** The claims data model supports working on a single case with either a single policy, or multiple policies, or beneficiaries.

For more information, see [[data-models|Data Models]] and [Components installed with Individual Life Claims](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/financial-services-operations/insurance-claims/components-installed-individual-life-claims.md).

</td></tr><tr><td id="d54239e282">

**Configure form views**

</td><td>

Set up any required views for any new tables according to your business requirements.You can use the included case views and task views in this application for reference.

</td></tr><tr><td id="d54239e294">

**Configure service definitions**

</td><td>

Configure service definitions to enable unique flows and views for your service cases and tasks. For example, the services for a claim could be reporting a new claim, appealing a claim, or reopening a claim.Define the new services for each case type table in your model.

You can also define the services for task tables to create different flows for your tasks. Examples include a claim validation task flow or a claim closure task flow.

For more information, see [[configure-service-definitions|Configure service definitions]].

</td></tr><tr><td id="d54239e318">

**Set up UI actions**

</td><td>

Define the actions that the user can take on the table record in a form. Examples include New, Save, Update, Assign to me, and Cancel.-   The case tables inherit the UI actions from CSM.
-   The task tables inherit the UI actions from Financial Task.
Override or hide the actions according to your business requirements.

For more information, see [Defining UI actions](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/platform-administration/c_UIActions.md) and [[fso-core-banking-tables|FSO Core Banking tables]].

</td></tr><tr><td id="d54239e353">

**Configure workspaces**

</td><td>

Configure the workspaces for your defined personas to interact with the customers and create and work on cases.Use the provided landing pages and workspaces as a reference, or create your own using UI Builder.

For more information, see [Enable the claim workspace for Individual Life Claims](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/financial-services-operations/insurance-claims/enable-claim-workspace-for-individual-life-claims.md).**Note:** The claim workspace is accessible from an adjuster task.

For more information, see [[configure-csm-workspace-fso-apps|Configure CSM Configurable Workspace]] and [UI Builder](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/application-development/ui-builder-overview.md).

</td></tr><tr><td id="d54239e402">

**Configure decision tables**

</td><td>

Set up the decision tables that are specific to your business requirements.Refer to the included claim triage decision table for the rules to triage the severity of a claim.

 If the input parameters, rules, and other elements vary, new tables may be needed for each line of business.

For more information, see [Decision Tables](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/application-development/decision-table.md).

</td></tr><tr><td id="d54239e422">

**Configure the approval engine**

</td><td>

Update the approval engine properties as required at **Insurance claim operations** &gt; **Properties**.For reserves and payments, review and update the Claim reserves and payments rules decision table with your desired parameters and values.

For more information, see [[insurance-claims-core-roles-and-properties|Insurance claims core properties]].

</td></tr><tr><td id="d54239e450">

**Configure assignment rules**

</td><td>

Configure the assignment rules to identify the cases that meet certain conditions and then route those cases to agents. For more information, see [[configure-assignment-rules-fso-applications|Configure assignment rules]].

</td></tr><tr><td id="d54239e467">

**Edit or create flows**

</td><td>

Edit or create flows by using Workflow Studio. For more information, see [[configure-flow-designer-flows-fso-apps|Edit or create flows]].

</td></tr></tbody>
</table>
**Parent Topic:**[Setting up Individual Life Claims](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/financial-services-operations/insurance-claims/setting-up-individual-life-claims.md)

## Related

- [[import-financial-accounts-products-institutions|Import your financial data using import sets]]
- [[configure-groups-fso|Configure groups]]
- [[data-models|Data Models]]
- [[configure-service-definitions|Configure service definitions]]
- [[fso-core-banking-tables|FSO Core Banking tables]]
- [[configure-csm-workspace-fso-apps|Configure CSM Configurable Workspace]]
- [[insurance-claims-core-roles-and-properties|Insurance Claims Core roles and properties]]
- [[configure-assignment-rules-fso-applications|Configure assignment rules]]
- [[configure-flow-designer-flows-fso-apps|Configure flows]]
- [[individual-life-claims-landing-page|Individual Life Claims]]
