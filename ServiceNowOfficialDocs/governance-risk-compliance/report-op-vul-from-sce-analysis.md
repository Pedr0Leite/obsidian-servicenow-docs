---
title: Report an operational vulnerability from the Scenario analysis
description: Report an operational vulnerability from the Scenario analysis in the Operational Resilience Workspace.
locale: en-US
canonical_url: https://www.servicenow.com/docs/r/governance-risk-compliance/report-op-vul-from-sce-analysis.html
release: australia
topic_type: task
last_updated: "2026-03-12"
reading_time_minutes: 1
breadcrumb: [Reporting Operational vulnerability, Managing Operational vulnerability, Manage, Operational Resilience, Governance, Risk, and Compliance]
tags:
  - governance-risk-compliance
  - type-task
---

# Report an operational vulnerability from the Scenario analysis

Report an operational vulnerability from the Scenario analysis in the [[grc-opres-landing-page|Operational Resilience]] Workspace.

## Before you begin

Role required: sn\_oper\_res.manager

## Procedure

1.  Navigate to **Workspaces** &gt; **Operational Resilience Workspace** &gt; **Scenario analyses**.

    A list of the available scenario analyses is displayed.

2.  Select a [[scenario-analysis-ov|Scenario analysis]] record from the list.

    If you create a Scenario analysis record and save it, the Operational vulnerabilities related list is displayed.

    The Scenario analysis record with the Operational vulnerabilities related list is displayed.

3.  Check the state of the Scenario analysis record.

    If the scenario analysis is in the **Pending analysis approval** state, you cannot add or remove a vulnerability at this stage.

4.  Select **New** in the Operational vulnerabilities related list and add an [[exploring-op-vul|operational vulnerability]].

5.  On the Vulnerability New record form, fill in the fields.

    The source of the vulnerability is the Scenario analysis. Therefore, the **Source** field on the form shows the source as Scenario analysis and the **Source table** field on the form shows the table as Scenario analysis. The **Source table** field is auto-filled.

    To view more information on the fields, see the [[create-new-op-vul-form|Create Operational vulnerability form]].

6.  Select **Save**.

    The following example shows how the Scenario analysis record is displayed in the Operational vulnerabilities related list and the Operational vulnerability is associated with the Scenario analysis for critical services.

    \[Omitted image "op-vul-rel-list-sce-analysis.png"\] Alt text: Scenario analysis record.

7.  Select **Save**.

    The Scenario analysis record is saved.

## Related

- [[create-new-op-vul-form|Create Operational vulnerability form]]
- [[grc-opres-landing-page|Operational Resilience]]
- [[scenario-analysis-ov|Scenario analysis]]
- [[exploring-op-vul|Operational vulnerability]]
