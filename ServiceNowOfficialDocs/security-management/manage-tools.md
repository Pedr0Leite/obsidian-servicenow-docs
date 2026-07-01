---
title: Manage tools
description: Manage the tools information that you imported from the MITRE TAXII collections. Tools are legitimate software that are used by threat actors to perform attacks.
locale: en-US
canonical_url: https://www.servicenow.com/docs/r/security-management/manage-tools.html
release: australia
topic_type: task
last_updated: "2026-03-12"
reading_time_minutes: 5
breadcrumb: [MITRE-ATT&amp;CK administration, MITRE-ATT&amp;CK framework overview, Threat Intelligence, Enterprise security case management applications, Security Operations]
tags:
  - security-management
  - type-task
---

# Manage tools

Manage the [[tools|tools]] information that you imported from the MITRE TAXII collections. Tools are legitimate software that are used by [[threat-actors|threat actors]] to perform attacks.

## Before you begin

Role required:

-   sn\_ti.admin: delete access
-   sn\_ti.read: read access
-   sn\_ti.write: create, write access

## About this task

Tools enable you to know how and when threat actors use them for executing [[threat-intelligence-campaigns|campaigns]]. Unlike [[threat-intelligence-malware|malware]], these tools or software packages are often found on a system and have legitimate purposes for power users, administrators, network administrators, or even normal users.

## Procedure

1.  Navigate to **All** &gt; **[[threat-intel-landing-page|Threat Intelligence]]** &gt; **MITRE ATT&amp;CK Repository** &gt; **Tools**.

    You can view the listed tools.

2.  Click a tool to view all the associated information.

    In the following illustration, you can view the details for the CARROTBALL tool, its ID, source, and other related information.\[Omitted image "mitre-tools-overview.gif"\] Alt text: View the details for the tools and their related information.

3.  To view how these objects are related, click **Show [[stix-relationships|Relationships]]**.


## What to do next

Use the [[view-techniques|techniques module]] to add or modify the tools data.

**Parent Topic:**[[mitre-att-ck-administration|MITRE-ATT&amp;CK administration]]

**Related topics**  


[Get started with MITRE-ATT&amp;CK framework]()

[Understand the MITRE to STIX data model]()

[Domain separation and MITRE-ATT&amp;CK]()

[Set up the MITRE-ATT&amp;CK framework]()

[Manage matrices]()

[Manage techniques]()

[Manage mitigations]()

[Manage groups]()

[Manage malware]()

[Manage MITRE relationships]()

[Manage CVE and technique mapping]()

[Extend the MITRE-ATT&amp;CK data]()

[Define the data source and detection tool mapping]()

[Define the data source and [[data-component|data component]] mapping]()

[Define the technique detection coverage]()

[Map your technique detection coverage to a technique]()

[Define the mitigation coverage]()

[Map your mitigation coverage to a technique]()

[Create and map detection rules]()

[Auto-extract technique rules for importing MITRE-ATT&amp;CK information]()

[Review threat group and MITRE-ATT&amp;CK techniques mapping]()

[Threat group to technique heatmap definition]()

[Review the MITRE-ATT&amp;CK system properties]()

## Related

- [[view-techniques|Manage techniques]]
- [[mitre-att-ck-administration|MITRE-ATT&amp;CK administration]]
- [[tools|Tools]]
- [[threat-actors|Threat actors]]
- [[threat-intelligence-campaigns|Campaigns]]
- [[threat-intelligence-malware|Malware]]
- [[threat-intel-landing-page|Threat Intelligence]]
- [[stix-relationships|Relationships]]
- [[data-component|Data Component]]
