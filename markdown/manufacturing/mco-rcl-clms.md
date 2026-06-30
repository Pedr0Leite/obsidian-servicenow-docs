---
title: Recall campaign
description: A recall process is a structured procedure launched by Original Equipment Manufacturers \(OEM\) to fix defects or issues in their manufactured products that are sold to the customers. Dealers can submit repair claims for work performed as part of recall campaigns, while OEM assessors benefit from a playbook-guided experience that simplifies and standardizes claim resolution.
locale: en-US
canonical_url: https://www.servicenow.com/docs/r/manufacturing/mco-rcl-clms.html
release: australia
topic_type: concept
last_updated: "2026-03-12"
reading_time_minutes: 3
breadcrumb: [MCO core, Explore, Manufacturing Commercial Operations]
---

# Recall campaign

A recall process is a structured procedure launched by Original Equipment Manufacturers \(OEM\) to fix defects or issues in their manufactured products that are sold to the customers. Dealers can submit repair claims for work performed as part of recall campaigns, while OEM assessors benefit from a playbook-guided experience that simplifies and standardizes claim resolution.

\[Omitted image "recall-claim-wf.png"\] Alt text: Recall campaign workflow

1.  Create recall campaign: The Recall manager creates the recall campaign.
2.  Corrective action and charges: The dealer enters the parts and software asset details for which the claim is raised.
3.  Add impacted: The Recall manager adds the assets that are impacted for the recall campaign.
4.  Create campaign phases: The Recall manager creates the campaign phases based on the location or the dealer.
5.  Select dealers included: OEM selects the dealers who are impacted by the recall campaign.
6.  Publish the campaign to dealers: Recall phase owners sends the campaigns to the dealers.
7.  View recall campaign details: Dealers can view the recall campaign details created by the recall manager.
8.  Submit recall claims: The Dealer submits the recall claims.
9.  Close campaigns: The Recall manager closes the recall campaigns.

## Phases and sub-phases

The MCO agent portal enables manufacturers to manage recall campaigns through a structured workflow. The portal provides capabilities to create campaign phases and sub-phases, select target assets for recall, launch campaigns, and notify affected dealers.

## Working with recall campaign

Use the following to configure, use, and manage recall campaigns in MCO.

Review the entities and relationships within the [[recall-claims|Recall campaign data model]], including tables added or modified by the recall claim plugin.

1.  Configure recall campaign: Complete the following tasks to set up the recall campaign in your environment.
    1.  Install Manufacturing recall claim management \[sn\_rcl\_claim\_mgmt\]: [Installing applications, plugins, and products](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/platform-administration/installing-apps-app-manager.md).
    2.  Set up product models and parts: [[mco-product-models|Configuring product models]]
    3.  Set up assets and install base items: [[mco-assets|Configuring assets]] and [[mco-create-install-base-item|Create an install base item]]
    4.  Set up dealers: [[set-up-dealer|Set up dealer]]
    5.  Assign recall roles: [[assign-mco-roles|Assign roles]]
2.  Work with recall campaign \(OEM\): Use the Agents \(CSM/FSM\) workspace to create and manage recall campaigns, phases, and claims.
    1.  Create a recall campaign: [[mco-rc-my-campaigns|Create a campaign]]
    2.  Define corrective action and charges: [[mco-corrective-actions|Corrective actions]]
    3.  Import impacted asset: [[mco_importing_impacted_assets|Importing impacted assets]]
    4.  Create and manage campaign phases: [[mco-recall-campaign-phases|Recall a campaign phase]]
    5.  Create phases and sub-phases: [[mco_phases_sub-phases|Create a phase and sub-phase in a recall campaign]]
3.  Work with recall campaign \(Dealer\): Use the [[mco-dealer-portal|Dealer portal]] to submit and track recall claims. .

## Related

- [[recall-claims|Recall campaign data model]]
- [[mco-product-models|Configuring product models]]
- [[mco-assets|Configuring assets]]
- [[mco-create-install-base-item|Create an install base item]]
- [[set-up-dealer|Set up dealer]]
- [[assign-mco-roles|Assign roles]]
- [[mco-rc-my-campaigns|Create a campaign]]
- [[mco-corrective-actions|Corrective actions]]
- [[mco_importing_impacted_assets|Importing impacted assets]]
- [[mco-recall-campaign-phases|Recall a campaign phase]]
- [[mco_phases_sub-phases|Create a phase and sub-phase in a recall campaign]]
- [[mco-dealer-portal|Dealer portal]]
