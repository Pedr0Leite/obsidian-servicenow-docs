---
title: Add artifacts to case\(s\) or case task\(s\)
description: After you have created a case, you can view or add artifacts, such as security incidents, CIs, and indicators of compromise, to the case. These artifacts act as clues in solving the case.
locale: en-US
canonical_url: https://www.servicenow.com/docs/r/security-management/threat-intelligence-security-center/add-artifacts-to-a-case-s.html
release: australia
product: Threat Intelligence Security Center
classification: threat-intelligence-security-center
topic_type: task
last_updated: "2026-03-12"
reading_time_minutes: 4
breadcrumb: [Threat Analyst Workbench, Use, Threat Intelligence Security Center, Security Operations]
---

# Add artifacts to case\(s\) or case task\(s\)

After you have created a case, you can view or add artifacts, such as security incidents, CIs, and [[c_IoCs|indicators of compromise]], to the case. These artifacts act as clues in solving the case.

## Before you begin

Role required: admin

**Note:** Artifacts are available only to the existing cases. For [[c_Observables|observables]] and [[indicator|indicators]], the artifacts can also be added or associated to a case from the import job using the Import Intelligence button. For more information on how to import see, [Import Intelligence in TISC](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/security-management/threat-intelligence-security-center/importing-threat-intelligence.md)

## Procedure

1.  Navigate to **Workspaces** &gt; **[[tisc-landing-page|Threat Intelligence Security Center]]**.

2.  Click **[[threat-analyst-workbench|Threat Analyst Workbench]]** icon.

3.  Go to **Case Management** &gt; **All Cases**.

    All the cases are displayed.

4.  Select any case or case task.

5.  Go to **Artifacts** tab.

    The associated artifacts are displayed as the related lists for that specific case or case task.

6.  Link or Unlink the records from the case or case task.

    **Note:** For more information, see [Link Threat Intel Related Records](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/security-management/threat-intelligence-security-center/link-threat-intel-releated-records.md)

    Following table lists the artifacts related lists related to the case\(s\) or case task\(s\):

<table id="table_svf_lcn_2yb"><thead><tr><th>

Related List

</th><th>

Description

</th></tr></thead><tbody><tr><td>

MITRE Techniques

</td><td>

List the MITRE techniques related to the case\(s\).MITRE techniques also displays all the associated techniques in a case.

</td></tr><tr><td>

Observable

</td><td>

List of observables related to this cases or case tasks.

</td></tr><tr><td>

Indicators

</td><td>

List of indicators related to this cases or case tasks.

</td></tr><tr><td>

[[attack-patterns|Attack Patterns]]

</td><td>

List of attack patterns that are related to this cases or case tasks.

</td></tr><tr><td>

[[threat-intelligence-campaigns|Campaigns]]

</td><td>

List the campaigns that are related to this cases or case tasks.

</td></tr><tr><td>

[[threat-intelligence-course-actions|Course of Actions]]

</td><td>

List the course of actions that are related to this cases or case tasks.

</td></tr><tr><td>

Data Components

</td><td>

List of Data Components that are related to this cases or case tasks.

</td></tr><tr><td>

[[threat-groupings|Threat Groupings]]

</td><td>

List the threat groupings that are related to this cases or case tasks.

</td></tr><tr><td>

[[threat-intelligence-identities|Identities]]

</td><td>

List the identities that are related to this cases or case tasks.

</td></tr><tr><td>

[[threat-intelligence-infrastructure|Infrastructure]]

</td><td>

List the Infrastructure such as systems, software services, and any associated physical or virtual resources that are related to this cases or case tasks.

</td></tr><tr><td>

Intrusion Sets

</td><td>

List the intrusion sets such as a set of adversarial behaviors and resources with common properties that are related to this cases or case tasks.

</td></tr><tr><td>

[[threat-intelligence-locations|Locations]]

</td><td>

List the locations records that are related to this cases or case tasks.

</td></tr><tr><td>

[[threat-intelligence-malware|Malware]]

</td><td>

List the malware source records that are related to this cases or case tasks.

</td></tr><tr><td>

[[marking-definitions|Marking Definitions]]

</td><td>

List the marking definitions records that are related to this cases or case tasks.

</td></tr><tr><td>

[[threat-intelligence-threat-notes|Threat Notes]]

</td><td>

List the marking definitions records that are related to this cases or case tasks.

</td></tr><tr><td>

[[threat-intelligence-observed-data|Observed Data]]

</td><td>

List the observed data that are related to this cases or case tasks.

</td></tr><tr><td>

[[threat-opinions|Threat Opinions]]

</td><td>

List the threat opinions that are related to this cases or case tasks.

</td></tr><tr><td>

[[threat-reports|Threat Reports]]

</td><td>

List the threat reports that are related to this cases or case tasks.

</td></tr><tr><td>

[[indicator-sightings|Sightings]]

</td><td>

List of sightings that are related to this cases or case tasks.

</td></tr><tr><td>

[[threat-actors|Threat Actors]]

</td><td>

List the threat actors that are related to this cases or case tasks.

</td></tr><tr><td>

[[tools|Tools]]

</td><td>

List the tools that are related to this cases or case tasks.

</td></tr><tr><td>

[[vulnerabilities|Vulnerabilities]]

</td><td>

If the observable is an IP address, this list shows any resources \(configuration items\) that have a matching IP address that are related to this cases or case tasks.

</td></tr><tr><td>

Related Cases

</td><td>

Lists the related cases.

</td></tr><tr><td>

Related Case Tasks

</td><td>

Lists the related case tasks.

</td></tr><tr><td>

Security Incidents

</td><td>

List the security incidents that are related to this cases or case tasks.

</td></tr><tr><td>

Affected Configuration Items

</td><td>

List the affected configurations items that are related to this cases or case tasks.

</td></tr><tr><td>

Affected Services

</td><td>

List the affected services that are related to this cases or case tasks.

</td></tr><tr><td>

Affected Assets

</td><td>

List the affected assets that are related to this cases or case tasks.

</td></tr><tr><td>

Vulnerability Entries

</td><td>

List the vulnerability entries that are related to this cases or case tasks.

</td></tr></tbody>
</table>
-   **[Roll up of MITRE Techniques from Artifacts to Case](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/security-management/threat-intelligence-security-center/roll-up-mitre-case.md)**  
When intelligence records are added to a case, all associated MITRE Techniques are automatically rolled up to the case level.
-   **[Show MITRE ATT&amp;CK Framework for a Case\(s\)](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/security-management/threat-intelligence-security-center/tisc-show-mitre-fw.md)**  
Displays all the associated techniques of a case on the MITRE ATT&amp;CK framework.

**Parent Topic:**[Threat Analyst Workbench](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/security-management/threat-intelligence-security-center/threat-analyst-workbench.md)

**Related topics**  


[Workbench Overview]()

[Creating cases using Threat Analyst Workbench]()

[Creating case task using Threat Analyst Workbench]()

[Working with Investigation Canvas]()

[Run Enrichment Actions within a case]()

[View Case Reports]()

[Create a security incident from a TISC case]()

[Upload Secure File Attachments]()

[Using playbooks]()

## Related

- [[c_IoCs|Indicators of compromise]]
- [[c_Observables|Observables]]
- [[indicator|Indicators]]
- [[tisc-landing-page|Threat Intelligence Security Center]]
- [[threat-analyst-workbench|Threat Analyst Workbench]]
- [[attack-patterns|Attack patterns]]
- [[threat-intelligence-campaigns|Campaigns]]
- [[threat-intelligence-course-actions|Course of actions]]
- [[threat-groupings|Threat groupings]]
- [[threat-intelligence-identities|Identities]]
- [[threat-intelligence-infrastructure|Infrastructure]]
- [[threat-intelligence-locations|Locations]]
- [[threat-intelligence-malware|Malware]]
- [[marking-definitions|Marking definitions]]
- [[threat-intelligence-threat-notes|Threat notes]]
- [[threat-intelligence-observed-data|Observed data]]
- [[threat-opinions|Threat opinions]]
- [[threat-reports|Threat reports]]
- [[indicator-sightings|Sightings]]
- [[threat-actors|Threat actors]]
- [[tools|Tools]]
- [[vulnerabilities|Vulnerabilities]]
