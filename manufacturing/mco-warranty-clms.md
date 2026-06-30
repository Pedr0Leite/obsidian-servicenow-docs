---
title: Repair claim
description: In the Repair claims workflow, the customer approaches the dealer with issues related to one or more products. The dealer diagnoses and fixes the issue​ and raises the reimbursement for the repair work performed.
locale: en-US
canonical_url: https://www.servicenow.com/docs/r/manufacturing/mco-warranty-clms.html
release: australia
topic_type: concept
last_updated: "2026-03-12"
reading_time_minutes: 3
breadcrumb: [MCO core, Explore, Manufacturing Commercial Operations]
---

# Repair claim

In the Repair claims workflow, the customer approaches the dealer with issues related to one or more products. The dealer diagnoses and fixes the issue​ and raises the reimbursement for the repair work performed.

\[Omitted image "repair-claim-wf.png"\] Alt text: Decorative

1.  Initiate claim: The dealer initiates the warranty or recall claim.
2.  Search serial number: Dealer can search the claim details based on the serial number.
3.  Enter claim job details: The dealer enters the job details in the [[mco-dealer-portal|dealer portal]].
4.  Enter parts and labor, misc services, attachments: The dealer enters the labor code and parts in the dealer portal.
5.  Submit claim: The dealer submits the claims request to the OEM.
6.  Review claim: OEM reviews the claims request submitted by the dealer.
7.  Approve claim: OEM reviews the claims and either approves, rejects, partially approves, or sends back the claim.
8.  Generate expense line: The claims agent processes the expense line and is generated only for approved or partially approved claims.

## Working with repair claim

Use the following to configure, use, and manage recall campaigns in MCO.

Review the entities and relationships within the [[repair-claims|Repair claims data model]], including tables added or modified by the [[mco-use-repair-claim|repair claim]] plugin.

1.  Configure repair claims: Complete the following tasks to set up the repair claims in your environment.
    1.  Install Manufacturing repair claim management \[sn\_repr\_claim\_mgmt\]: [Installing applications, plugins, and products](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/platform-administration/installing-apps-app-manager.md).
    2.  Set up product models and parts: [[mco-product-models|Configuring product models]].
    3.  Set up assets and install base items: [[mco-assets|Configuring assets]] and [[mco-create-install-base-item|Create an install base item]].
    4.  Set up dealer hierarchy: [[mco-create-channel-partner|Create a channel partner]] and [[mco-create-internal-business-location|Create an internal business location]].

        **Note:** Use the Partner Relationship Management [[data-model|data model]] to set up channel partners \(external entities\) and dealers \(external trading partners to the OEM\). Model company-owned dealer outlets as internal service organizations using the Service Model Foundation.

    5.  Set up dealers: [[set-up-dealer|Set up dealer]].
    6.  Assign repair claim roles: [[assign-mco-roles|Assign roles]]
2.  Work with repair claims \(OEM\): Use the Agents \(CSM/FSM\) workspace to create and manage repair campaigns, phases, and claims.
    1.  Create a repair claim: [[mco-create-repair-claim|Create a repair claim manually]].
    2.  Review repair claims: [[mco-approve-repair-claims|Reviewing and approving repair claims]].
3.  Work with repair claim \(Dealer\): Use the Dealer portal to submit and track repair claims.
    1.  Submit a repair claim for warranty: [[mco-submit-repair-claim|Submit a repair claim for warranty]].
    2.  Submit a repair claim for recall: .

## Related

- [[repair-claims|Repair claims data model]]
- [[mco-product-models|Configuring product models]]
- [[mco-assets|Configuring assets]]
- [[mco-create-install-base-item|Create an install base item]]
- [[mco-create-channel-partner|Create a channel partner]]
- [[mco-create-internal-business-location|Create an internal business location]]
- [[set-up-dealer|Set up dealer]]
- [[assign-mco-roles|Assign roles]]
- [[mco-create-repair-claim|Create a repair claim manually]]
- [[mco-approve-repair-claims|Reviewing and approving repair claims]]
- [[mco-submit-repair-claim|Submit a repair claim for warranty]]
- [[mco-dealer-portal|Dealer portal]]
- [[mco-use-repair-claim|Repair claim]]
- [[data-model|Data model]]
