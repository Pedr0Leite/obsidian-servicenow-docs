---
title: Add artifacts to a case
description: After you have created a case, you can add artifacts, such as security incidents, CIs, and indicators of compromise, to the case. These artifacts act as clues in solving the case.
locale: en-US
canonical_url: https://www.servicenow.com/docs/r/security-management/add-records-to-cases.html
release: australia
topic_type: task
last_updated: "2026-03-12"
reading_time_minutes: 1
breadcrumb: [Create cases in Security Case Management, Security Case Management, Threat Intelligence, Enterprise security case management applications, Security Operations]
---

# Add artifacts to a case

After you have created a case, you can add artifacts, such as security incidents, CIs, and [[c_IoCs|indicators of compromise]], to the case. These artifacts act as clues in solving the case.

## Before you begin

The [[threat-intel-landing-page|Threat Intelligence]] plugin must be activated to use [[case-mgmt|Security Case Management]].

Role required: sn\_ti.case\_user\_write

## Procedure

1.  Open a case to which you want to add artifacts.

2.  Click the **Case Artifacts** related list.

    \[Omitted image "case-dossier.png"\] Alt text: Case artifacts

3.  Click the tab associated with the type of artifact you want to add to the case.

    For example, click **Configuration Items** to add one or more CIs to the case.

    \[Omitted image "cis.png"\] Alt text: Configuration items

4.  Click **Edit**.

    \[Omitted image "slushbucket.png"\] Alt text: Slushbucket

5.  Using the slushbucket and filters, locate the artifact records you want to add to the case and move them from the Collection bucket to the List bucket, and click **Save**.

    The list appears in the selected tab and the selected artifacts are added to the list.


**Parent Topic:**[[create-cases-in-case-mgmt|Create cases in Security Case Management]]

**Related topics**  


[Associate MITRE-ATT&amp;CK information with security case]()

[[add-records-to-cases-threat|Add IoCs and observables to an existing case]]

[[add-sec-inc-to-cases|Add security incidents to an existing case]]

[[add-cis-to-cases-sir|Add CIs to existing cases]]

[[add-users-to-cases-sir|Add affected users to existing cases]]

## Related

- [[create-cases-in-case-mgmt|Create cases in Security Case Management]]
- [[add-records-to-cases-threat|Add IoCs and observables to an existing case]]
- [[add-sec-inc-to-cases|Add security incidents to an existing case]]
- [[add-cis-to-cases-sir|Add CIs to existing cases]]
- [[add-users-to-cases-sir|Add affected users to existing cases]]
- [[c_IoCs|Indicators of compromise]]
- [[threat-intel-landing-page|Threat Intelligence]]
- [[case-mgmt|Security Case Management]]
