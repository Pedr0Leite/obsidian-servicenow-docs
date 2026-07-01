---
title: Set up predefined Playbooks for Portals
description: Set up predefined Playbooks for Portals to provide end users with the playbook experience on your service portal.
locale: en-US
canonical_url: https://www.servicenow.com/docs/r/customer-service-management/setup-onb-playbks-for-portals.html
release: australia
topic_type: concept
last_updated: "2026-03-12"
reading_time_minutes: 3
breadcrumb: [Playbooks for Portals, Playbooks in Customer Service Management, Agent tools, Organize agent workspaces, Configure, Customer Service Management]
tags:
  - customer-service-management
  - type-concept
---

# Set up predefined Playbooks for Portals

Set up predefined Playbooks for Portals to provide end users with the playbook experience on your service portal.

## Overview of Playbooks

Playbooks guide users through complex processes and enable them to save their progress and resume their work when convenient. They can also get the information that they need for each stage of the flow and its associated activities with the [[c_CustomerServiceManagement|Customer Service Management]] \(CSM\) playbooks on service portals.

You can activate Playbooks for Portals if you have the admin role. The base system is delivered in an inactive state. You must activate it in the Playbooks \(PAD\) for the user to see it.

Plugins required:

-   Playbooks for Customer Service Management: sn\_csm\_playbook
-   Playbook Experience: sn\_playbook\_exp
-   [[csm-case-type-onboarding|Case Playbook for Onboarding]]: sn\_onboarding \(required if you need the predefined playbook experience\)
-   [[csm-playbook-product-support|Case Playbook for Product Support]]: sn\_product \(required if you want to use the product case playbook and record generator\)

Plugins are available from the ServiceNow® Store. For more information, see [[customer-service-case-playbooks|Playbook plugins]].

## Summary of steps for setting up predefined Playbooks for Portals

You can set up Playbooks for Portals using the following high level steps.

1.  Activate the draft state in the [[onboarding-case-type-overview|onboarding case type]] state. For more information, see [[activate-the-draft-state-in-the-onboarding-case-type-state|Activate the draft state for the onboarding case type]].
2.  [[activate-the-record-generator|Activate the record generator]]
3.  [[activate-a-new-onboarding-playbook-with-self-service-in-pad|Activate a new onboarding playbook with self-service]]
4.  Activate guided onboarding in the playbook content items. For more information, see [[activate-guided-onboarding-in-playbook-content-items|Activate guided onboarding in Playbook content items]].
5.  Add a **Process** tab to the Portal so that users can see where they are in the Playbook process. See [[add-process-tab-portal|Add the Process tab to the portal]] for more information.

**Related topics**  


[[activate-playbooks-for-portals|Set up custom Playbooks for Portals]]

[[playbooks-for-portals|Playbooks for Portals]]

[[using-playbooks-for-portals|Using Playbooks for Portals]]

[[create-an-onboarding-case-with-portal-playbook|Creating an onboarding case with Playbooks for Portals]]

[Activate the record generator](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/customer-service-management/activate-the-record-generator.md)

## Related

- [[customer-service-case-playbooks|Playbook capabilities]]
- [[activate-the-draft-state-in-the-onboarding-case-type-state|Activate the draft state for the onboarding case type]]
- [[activate-the-record-generator|Activate the record generator]]
- [[activate-a-new-onboarding-playbook-with-self-service-in-pad|Activate a new onboarding playbook with self-service]]
- [[activate-guided-onboarding-in-playbook-content-items|Activate guided onboarding in Playbook content items]]
- [[add-process-tab-portal|Add the Process tab to the portal]]
- [[activate-playbooks-for-portals|Set up custom Playbooks for Portals]]
- [[playbooks-for-portals|Playbooks for Portals]]
- [[using-playbooks-for-portals|Using Playbooks for Portals]]
- [[create-an-onboarding-case-with-portal-playbook|Creating an onboarding case with Playbooks for Portals]]
- [[c_CustomerServiceManagement|Customer Service Management]]
- [[csm-case-type-onboarding|Case Playbook for Onboarding]]
- [[csm-playbook-product-support|Case Playbook for Product Support]]
- [[onboarding-case-type-overview|Onboarding case type]]
