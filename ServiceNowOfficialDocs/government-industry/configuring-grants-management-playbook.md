---
title: Configuring Grants Management
description: Install the Grants Management application, which enables users to submit and track grants management requests and provides government agents with a predefined process for handling and resolving these requests. You can then configure the features available for submitting requests and routing requests to agents.
locale: en-US
canonical_url: https://www.servicenow.com/docs/r/government-industry/configuring-grants-management-playbook.html
release: australia
topic_type: concept
last_updated: "2025-07-31"
reading_time_minutes: 3
breadcrumb: [Playbooks and Solutions, Configure agent workspaces, Configure, Public Sector Digital Services \(PSDS\)]
tags:
  - government-industry
  - type-concept
---

# Configuring Grants Management

Install the Grants Management application, which enables users to submit and track grants management requests and provides government agents with a predefined process for handling and resolving these requests. You can then configure the features available for submitting requests and routing requests to agents.

As a user with the admin role, complete the following configuration tasks to set up Grants Management, after you install the [[install-public-sector-digital-services-core|Public Sector Digital Services Core]] application.

<table id="table_cmk_mdm_fwb"><thead><tr><th>

Task

</th><th>

Description

</th></tr></thead><tbody><tr><td>

[[psds-install-grants-management|Install Grants Management for Public Sector Digital Services]]

</td><td>

Install Grants Management from the ServiceNow® Store.

</td></tr><tr><td>



</td><td>

Enable publishing of grant programs, as well as authorized representative activities.

</td></tr><tr><td>

[[psds-config-gmp-fdtn-doc-template-rca|Configure Restricted Caller Access \(RCA\) for Document Templates]]

</td><td>

Allow secure, controlled access for generating results letters.

</td></tr><tr><td>

[[psds-config-gmp-assign-user-roles-responsibilities|Assign user personas, roles, groups, and responsibilities in Grants Management]]

</td><td>

Assign roles to members of your grants organization Grants Management application so that your users can have delegated access to Grants Management features, capabilities, and data.

</td></tr><tr><td>

[[psds-config-gmp-pace|Configure PaCE Eligibility Framework Engine for use with Grants Management]]

</td><td>

Configure the eligibility framework engine, powered by PaCE, to allow agents to confirm whether an applicant is eligible for the specific grant being requested.

</td></tr><tr><td>

[[psds-config-reviewer-service-portal|Configure the Reviewer Service Portal]]

</td><td>

Configure the Grants Management [[psds-rsp-overview|Reviewer Service Portal]] for merit reviewers to track, score, and review grants proposals.

</td></tr><tr><td>

[[psds-config-gmp-grant-pgr|Set up a grant program in Grants Management]]

</td><td>

Set up and configure the details of a new grant program using Grants Management.

</td></tr><tr><td>

[[psds-using-grants-management-playbook|Create a test grant program and grant proposal]]

</td><td>

Verify the newly-configured grant program setup and grant proposal playbooks are working as expected by creating a new grant program and test grant proposal using the Grants Management.

</td></tr></tbody>
</table>## Key capabilities that support the Grants Management Workflows

The main ServiceNow capabilities that are leveraged to support the Grants Management workflows are:

-   Document Processor​: Manage internal docs with version control, security, &amp; workflow integration. Request and verify docs from applicants​.
-   [[playbooks-psds-exploring|Playbooks]]​: Provide a visual, step-by-step guide for applicants and agents to complete key processes.​
-   [Policy as Code Engine \(PaCE\)](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/servicenow-platform/pace-managing-policies.md): Streamline the creation, maintenance, and use of screening criteria with a low-code rules engine.
-   Configurable Portal Widgets: Use pre-built UI components for easy portal set up and modification.
-   [[psds-config-gmp-smart-assessment-engine|Smart Assessment]]: Improve the creation and maintenance of application questions.
-   [[psds-config-gmp-config-pre-eligibility|Decision Trees]]: Provide a structured, step-by-step approach for pre-screening potential applicants.​​​

## Related

- [[install-public-sector-digital-services-core|Install Public Sector Digital Services Core]]
- [[psds-install-grants-management|Install Grants Management for Public Sector Digital Services]]
- [[psds-config-gmp-fdtn-doc-template-rca|Configure Restricted Caller Access \(RCA\) for Document Templates]]
- [[psds-config-gmp-assign-user-roles-responsibilities|Assign user personas, roles, groups, and responsibilities in Grants Management]]
- [[psds-config-gmp-pace|Configure PaCE Eligibility Framework Engine for use with Grants Management]]
- [[psds-config-reviewer-service-portal|Configure the Reviewer Service Portal]]
- [[psds-config-gmp-grant-pgr|Set up a grant program in Grants Management]]
- [[psds-using-grants-management-playbook|Using Grants Management]]
- [[playbooks-psds-exploring|Playbooks for Public Sector Digital Services]]
- [[psds-config-gmp-smart-assessment-engine|Configure the Smart Assessment Engine for Grants Management]]
- [[psds-config-gmp-config-pre-eligibility|Configure pre-eligibility questions in Grants Management]]
- [[psds-rsp-overview|Reviewer Service Portal]]
