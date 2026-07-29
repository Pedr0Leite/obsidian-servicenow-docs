---
title: Download a GRC application from the ServiceNow Store for the first time
description: Downloading an application from the ServiceNow Store for the first time involves several easy steps. Some steps are performed on the ServiceNow Store and some in your ServiceNow AI Platform instance.
locale: en-US
canonical_url: https://www.servicenow.com/docs/r/governance-risk-compliance/download-grc-first-time.html
release: australia
topic_type: task
last_updated: "2026-03-12"
reading_time_minutes: 1
breadcrumb: [GRC and the ServiceNow Store, Governance, Risk, and Compliance]
tags:
  - governance-risk-compliance
  - type-task
---

# Download a GRC application from the ServiceNow Store for the first time

Downloading an application from the ServiceNow Store for the first time involves several easy steps. Some steps are performed on the ServiceNow Store and some in your ServiceNow AI Platform instance.

## Before you begin

Role required: admin

## About this task

The ServiceNow Store allows you to download core products and applications. A product contains one or more applications that are licensed as a group.

Dependency plugins are automatically installed when you activate these GRC core applications:

-   [[c_GRCAudits|Audit Management]]
-   [[r_PolicyComplianceMgmt|Policy and Compliance Management]]
-   Risk Management

For example, when you activate the Risk Management application, the Risk Management Dependencies plugin is also activated.

**Important:** Vendor Risk Management, you must first activate the Vendor Risk Management Dependencies plugin before activating the Vendor Risk Management application. For more information, see [[activate-entitled-grc-app|Activate an entitled GRC ServiceNow Store application]].

## Procedure

1.  Ensure that you have entitlements \(or licenses\) to the application and its dependent applications.

2.  Activate the application and run it on your instance.


**Related topics**  


[List of plugins](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/governance-risk-compliance/policy-and-compliance-management/t_ActivateGRCPandC.md)

## Related

- [[activate-entitled-grc-app|Activate an entitled GRC ServiceNow Store application]]
- [[c_GRCAudits|Audit Management]]
- [[r_PolicyComplianceMgmt|Policy and Compliance Management]]
