---
title: Perform link analysis and threat hunting using MITRE-ATT&amp;CK specific filters
description: Correlate and perform link analysis of observables, security incidents, and MITRE-ATT&amp;CK related information so that your organization can start hunting for threats.
locale: en-US
canonical_url: https://www.servicenow.com/docs/r/security-management/link-analysis-threat-hunt-mitre.html
release: australia
topic_type: task
last_updated: "2026-03-12"
reading_time_minutes: 2
breadcrumb: [Using MITRE-ATT&amp;CK to detect and analyze threats, MITRE-ATT&amp;CK framework overview, Threat Intelligence, Enterprise security case management applications, Security Operations]
---

# Perform link analysis and threat hunting using MITRE-ATT&amp;CK specific filters

Correlate and perform link analysis of [[c_Observables|observables]], security incidents, and MITRE-ATT&amp;CK related information so that your organization can start hunting for threats.

## Before you begin

Role required: sn\_ti.mitre\_analyst, sn\_si.read

## About this task

After you associate the security incidents with MITRE-ATT&amp;CK information, you can use the MITRE-ATT&amp;CK specific filters for threat hunting. Use the MITRE-ATT&amp;CK filters with the existing [[sir-landing-page|Security Incident Response]] filters to correlate and perform link analysis.

## Procedure

1.  Navigate to **All** &gt; **Security Incidents** &gt; **Show All Incidents**.

2.  Click **Update Personalized List** to add the MITRE columns.

3.  Select a filter condition so that you can view MITRE related information and associations with security incidents or observables:

    -   MITRE-ATT&amp;CK Adversary Group
    -   MITRE-ATT&amp;CK Data Source
    -   MITRE-ATT&amp;CK Procedure \([[threat-intelligence-malware|Malware]]\)
    -   MITRE-ATT&amp;CK Procedure \([[tools|Tools]]\)
    -   MITRE-ATT&amp;CK Tactic
    -   MITRE-ATT&amp;CK Technique
4.  Create a filter condition that is based on the above criteria and click **Run** to perform a link analysis or correlation between security incidents, observables, and MITRE-ATT&amp;CK related information.

    **Note:** The MITRE-ATT&amp;CK data is stored as a string and you can only use **contains** as the operator for filter conditions.

    For example, if you want to review that a configuration item \(CI\) is compromised, you select a CI. You then correlate the CI with techniques that are present by adding a MITRE-ATT&amp;CK Technique ID. You can then continue to build your filter criteria to correlate the information and for threat hunting.

    \[Omitted image "mitre-filter-conditions.png"\] Alt text: MITRE filter conditions for threat analysis.


**Parent Topic:**[[mitre-att-ck-features|Using MITRE-ATT&amp;CK to detect and analyze threats]]

**Related topics**  


[Associate MITRE-ATT&amp;CK information with security incidents]()

[Associate MITRE-ATT&amp;CK information with observables]()

[Associate MITRE-ATT&amp;CK information with security case]()

[Rollup MITRE-ATT&amp;CK information using [[tisc-threat-lookup|Threat Lookup]] results]()

[Rollup MITRE-ATT&amp;CK information from detection rules]()

[Rollup MITRE-ATT&amp;CK information from child security incidents]()

[MITRE-ATT&amp;CK heat map and navigator]()

[Using the MITRE-ATT&amp;CK dashboard]()

## Related

- [[mitre-att-ck-features|Using MITRE-ATT&amp;CK to detect and analyze threats]]
- [[c_Observables|Observables]]
- [[sir-landing-page|Security Incident Response]]
- [[threat-intelligence-malware|Malware]]
- [[tools|Tools]]
- [[tisc-threat-lookup|Threat Lookup]]
