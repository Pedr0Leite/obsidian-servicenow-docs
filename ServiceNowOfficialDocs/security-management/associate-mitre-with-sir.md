---
title: Associate MITRE-ATT&amp;CK information with security incidents
description: Associate the MITRE-ATT&amp;CK tactics and techniques to the security incident for better security incident and threat analysis.You can now associate MITRE-ATT&amp;CK tactics and techniques to the closed security incidents for better security incident and threat analysis.You can use the MITRE-ATT&amp;CK card to see the MITRE-ATT&amp;CK related information in a security incident.
locale: en-US
canonical_url: https://www.servicenow.com/docs/r/security-management/associate-mitre-with-sir.html
release: australia
topic_type: task
last_updated: "2026-03-12"
reading_time_minutes: 4
breadcrumb: [Using MITRE-ATT&amp;CK to detect and analyze threats, MITRE-ATT&amp;CK framework overview, Threat Intelligence, Enterprise security case management applications, Security Operations]
tags:
  - security-management
  - type-task
---

# Associate MITRE-ATT&amp;CK information with security incidents

Associate the MITRE-ATT&amp;CK tactics and techniques to the security incident for better security incident and threat analysis.

## Before you begin

Role required: sn\_si.analyst

## About this task

Add the MITRE-ATT&amp;CK tactics and techniques information to the security incident so that you can correlate your security incident and threat information for better analysis. For example, your organization may be receiving tactics, techniques, and procedures \(TTP\)-related information from your third-party sources, such as [[threat-intel-landing-page|Threat Intelligence]] reports or other sources outside of the [[sir-landing-page|Security Incident Response]]. You then add this information back to SIR for better correlation and threat analysis.

You can choose to roll up the MITRE-ATT&amp;CK information automatically from the [[tisc-threat-lookup|threat lookup]] auto-extraction results, from [[c_Observables|observables]], or from a child security incident to a security incident. For automatic roll up to security incidents, [[configure-mitre-att-ck-properties|enable the system property]]. Alternatively, you can roll up the information manually for each individual threat lookup or [[associate-mitre-observables|observable]].

## Procedure

1.  Navigate to **All** &gt; **Security Incidents** &gt; **Show All Incidents**.

2.  Select the security incident that you want to enrich with the MITRE-ATT&amp;CK information.

3.  Click the **Associate MITRE ATT&amp;CK Technique** related link.

    The Associate MITRE ATT&amp;CK Technique pane appears.

    This illustration shows how to navigate to the related list and look for Associate MITRE-ATT&amp;CK Technique, review the source Enterprise ATT&amp;CK, add a tactic Impact, and add a technique System Shutdown/Reboot.

4.  Select **Source**.

    **Note:** Only the [[setup-mitre-profile|collections]] and [[view-mitre-collection|matrices]] that have been activated appear in the source list.

    The tactics and techniques that are associated with the source are available for selection. You can also associate multiple sources.

5.  Select the **Tactic** and **Techniques**.

6.  Review the information based on the relevance with the security incident and do the following:

    -   To completely remove the association, click the bin icon. Clicking this icon deletes the source and its associated tactics and techniques.
    -   To remove a tactic, click the minus icon next to the tactic.
    -   To remove a technique, click the x icon next to the technique.
7.  Click **Save**.


## Result

The MITRE-ATT&amp;CK information is associated with the security incident. You can now view the associated information in the **MITRE ATT&amp;CK Card**.

**Parent Topic:**[[mitre-att-ck-features|Using MITRE-ATT&amp;CK to detect and analyze threats]]

**Related topics**  


[Associate MITRE-ATT&amp;CK information with observables]()

[Associate MITRE-ATT&amp;CK information with security case]()

[Rollup MITRE-ATT&amp;CK information using Threat Lookup results]()

[Rollup MITRE-ATT&amp;CK information from detection rules]()

[Rollup MITRE-ATT&amp;CK information from child security incidents]()

[Perform link analysis and threat hunting using MITRE-ATT&amp;CK specific filters]()

[MITRE-ATT&amp;CK heat map and navigator]()

[Using the MITRE-ATT&amp;CK dashboard]()

## Associate MITRE-ATT&amp;CK information with closed security incidents

You can now associate MITRE-ATT&amp;CK tactics and techniques to the closed security incidents for better security incident and threat analysis.

## Using the MITRE-ATT&amp;CK Card to see related information in a security incident

You can use the MITRE-ATT&amp;CK card to see the MITRE-ATT&amp;CK related information in a security incident.

After the information is rolled up from a threat lookup, an observable, or a SIEM integration, it is added to the security incident. Then, the aggregated information is presented in the MITRE-ATT&amp;CK Card. The **MITRE ATT&amp;CK Card** provides two views:

-   Navigator view: This view, which is similar to the MITRE-ATT&amp;CK navigator, shows all the techniques that have been manually added or rolled up from the observable or threat lookup tables. **Show origin of techniques** displays the source of the technique if it has been manually rolled up or through a Source. **Show ID** displays the technique ID.

    The following illustration shows how to navigate to the **MITRE ATT&amp;CK Card** navigator view. By clicking any of the available links, the information opens in the Threat Intelligence module.

-   List view: This view shows the data in a list or table format. You can see all the data that is spread across different tables and groups in this view.

    The following illustration shows how to navigate to the MITRE ATT&amp;CK Card list view. By clicking any of the available links, the information opens in the Threat Intelligence module.

## Related

- [[configure-mitre-att-ck-properties|Review the MITRE-ATT&amp;CK system properties]]
- [[associate-mitre-observables|Associate MITRE-ATT&amp;CK information with observables]]
- [[setup-mitre-profile|Set up the MITRE-ATT&amp;CK framework]]
- [[view-mitre-collection|Manage matrices]]
- [[mitre-att-ck-features|Using MITRE-ATT&amp;CK to detect and analyze threats]]
- [[threat-intel-landing-page|Threat Intelligence]]
- [[sir-landing-page|Security Incident Response]]
- [[tisc-threat-lookup|Threat Lookup]]
- [[c_Observables|Observables]]
