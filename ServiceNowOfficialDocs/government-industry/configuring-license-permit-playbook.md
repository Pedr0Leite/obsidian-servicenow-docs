---
title: Install and configure the License and Permit Playbook application
description: Install the License and Permit Playbook application, which enables public sector end users to submit and track license and permit requests and provides government agents with a pre-defined process for handling and resolving these requests. You can then configure the features available for submitting requests and routing requests to agents.
locale: en-US
canonical_url: https://www.servicenow.com/docs/r/government-industry/configuring-license-permit-playbook.html
release: australia
topic_type: concept
last_updated: "2026-03-12"
reading_time_minutes: 3
breadcrumb: [Playbooks and Solutions, Configure agent workspaces, Configure, Public Sector Digital Services \(PSDS\)]
---

# Install and configure the License and Permit Playbook application

Install the License and Permit Playbook application, which enables public sector end users to submit and track license and permit requests and provides government agents with a pre-defined process for handling and resolving these requests. You can then configure the features available for submitting requests and routing requests to agents.

As a user with the admin role, complete the following configuration tasks to set up the License and Permit Playbook, after you install the [[install-public-sector-digital-services-core|Public Sector Digital Services Core]] application.

|Task|Description|
|----|-----------|
|[[install-psds-license-permit-request-playbook|Install License and Permit Playbook for Public Sector Digital Services]]|Install License and Permit Playbook \(com.sn\_public\_sector\_digital\_services\_core\) from the ServiceNow® Store.|
|[[psds-create-service-definition-catalog-item|Configure service definition catalog items for License and Permit Playbook application]]|The Services Offered and Services Received tables have been migrated into the Service Definition table. All Services Offered data must be converted into individual Service Definitions. For more information, see [Services Offered and Services Received Migration Guidance](https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB1559449).|
|[[psds-configuring-va|Enable public sector end users to create a License or Permit request using Virtual Agent]]|Use Virtual Agent Designer to [publish](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/conversational-interfaces/publish-virtual-agent-topic.md) the pre-built conversation topic, **Start a License/Permit Application**, which enables end users to submit a license or permit request using the Virtual Agent chatbot. For more information, see [[psds-lpr-configure-va|Configure Virtual Agent for License and Permit Playbook]].|
|[[awa-psds-overview|Automatically route license and permit requests using Advanced Work Assignment]]|Use the ServiceNow Advanced Work Assignment \(AWA\) application to route and assign license and permit requests to designated agents.|
|[[psds-configure-eligibility-lpr|Configure License and Permit Eligibility Framework in License and Permit Playbook]]|Configure the pre-eligibility criteria to allow agents to confirm whether an applicant is eligible for the specific license or permit requested.|
|[[psds-configure-decision-tables|Configure decision tables for License and Permit Playbook]]|Use decisions tables to simplify the pricing configuration of a license or permit request that depends on multiple factors. Decision tables provide a single point where you can create, view, and modify pricing and dependent attributes.|
|[[psds-lpr-configure-doc-template|Create Document Templates for License and Permit Playbook]]|Use the Document Templates application to generate templates for various types of Licenses and Permits issued through the License and Permit Playbook.|

## Related

- [[install-public-sector-digital-services-core|Install Public Sector Digital Services Core]]
- [[install-psds-license-permit-request-playbook|Install License and Permit Playbook for Public Sector Digital Services]]
- [[psds-create-service-definition-catalog-item|Configure service definition catalog items for License and Permit Playbook application]]
- [[psds-configuring-va|Configure Virtual Agent for Public Sector Digital Services]]
- [[psds-lpr-configure-va|Configure Virtual Agent for License and Permit Playbook]]
- [[awa-psds-overview|Configure Advanced Work Assignment for Public Sector Digital Services]]
- [[psds-configure-eligibility-lpr|Configure License and Permit Eligibility Framework in License and Permit Playbook]]
- [[psds-configure-decision-tables|Configure decision tables for License and Permit Playbook]]
- [[psds-lpr-configure-doc-template|Create Document Templates for License and Permit Playbook]]
