---
title: Reporting Operational vulnerability
description: Any Operational Resilience application user can report an operational vulnerability that needs the attention of the Operational Resilience team.
locale: en-US
canonical_url: https://www.servicenow.com/docs/r/governance-risk-compliance/reporting-operational-vul.html
release: australia
topic_type: concept
last_updated: "2026-06-01"
reading_time_minutes: 2
breadcrumb: [Managing Operational vulnerability, Manage, Operational Resilience, Governance, Risk, and Compliance]
---

# Reporting Operational vulnerability

Any [[grc-opres-landing-page|Operational Resilience]] application user can report an [[exploring-op-vul|operational vulnerability]] that needs the attention of the Operational Resilience team.

Users of the Operational Resilience feature can report an operational vulnerability using one the following options:

-   To create an operational vulnerability from the [[employee-center|Employee Center]], see [[reporting-op-vul|Report operational vulnerability from the Employee Center]]. The user must have the Operational Resilience business user \[sn\_oper\_res.operational\_resilience\_business\_user\] role.
-   To create an operational vulnerability from the Operational vulnerability menu in the Operational Resilience Workspace, see [[set-up-op-vul-record|Report an operational vulnerability from the module]]. The user must have the Operational Resilience manager \[sn\_oper\_res.operational\_resilience\_manager\] role.
-   To create an operational vulnerability from the records in the Operational Resilience Workspace, see the following topics:
    -   [[create-op-vul-from-other-records-in-or-ws|Report Operational vulnerability from Importance assessment]]
    -   [[report-op-vul-from-sce-analysis|Report an operational vulnerability from the Scenario analysis]]
    -   [[report-op-vul-from-attestation|Report an operational vulnerability from the Self-attestation module]]
    -   [[report-op-vul-from-service|Report an operational vulnerability from the Service record]]

## States of the vulnerability

An operational vulnerability record moves through the following workflow states.

|States|Description|
|------|-----------|
|**New**|The vulnerability has been opened and it is in the initial stage of review.|
|**Assessment**|The vulnerability is being evaluated to determine the appropriate course of action.|
|**Treatment**|The vulnerability is being actively investigated to gather information and evidence. The course of action and treatment is being decided.|
|**Pending approval**|The vulnerability is being worked on to find a resolution.|
|**Approved**|A review of the vulnerability is being done after it is resolved.|
|**Closed**|The vulnerability is closed and is no longer active.|
|**Canceled**|The vulnerability is canceled and it is no longer being pursued.|

## Email notifications for the vulnerabilities

When the vulnerability is assigned to the users, they receive email notifications informing them about the vulnerability details, upcoming actions, and due dates. Email notifications are sent to the following users:

1.  When the vulnerability is assigned to an analyst or a user, they receive the email notifications.
2.  When the vulnerability is approved or rejected, the analyst receives the email notification.
3.  When the vulnerability is canceled, the approver, requester, analyst, and people on the watchlist receive the email notifications.

## Related

- [[reporting-op-vul|Report operational vulnerability from the Employee Center]]
- [[set-up-op-vul-record|Report an operational vulnerability from the module]]
- [[create-op-vul-from-other-records-in-or-ws|Report Operational vulnerability from Importance assessment]]
- [[report-op-vul-from-sce-analysis|Report an operational vulnerability from the Scenario analysis]]
- [[report-op-vul-from-attestation|Report an operational vulnerability from the Self-attestation module]]
- [[report-op-vul-from-service|Report an operational vulnerability from the Service record]]
- [[grc-opres-landing-page|Operational Resilience]]
- [[exploring-op-vul|Operational vulnerability]]
- [[employee-center|employee center]]
