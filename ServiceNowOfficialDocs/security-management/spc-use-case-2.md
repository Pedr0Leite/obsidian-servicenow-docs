---
title: Security Posture Control use case: Detecting assets missed by vulnerability assessment tools
description: To detect assets missed by vulnerability assessment tools, the following pre-requisites are required.
locale: en-US
canonical_url: https://www.servicenow.com/docs/r/security-management/spc-use-case-2.html
release: australia
topic_type: concept
last_updated: "2026-03-12"
reading_time_minutes: 1
breadcrumb: [Reference, Security Posture Control, Security Operations]
tags:
  - security-management
  - type-concept
---

# Security Posture Control use case: Detecting assets missed by vulnerability assessment tools

To detect assets missed by vulnerability assessment [[tools|tools]], the following pre-requisites are required.

For each Service Graph Connector in the list, you can see if that connector is required for monitoring on-prem assets or cloud assets. Depending on your use case, you can choose to activate only the required connectors.

1.  Activate at least one Service Graph Connector from the Vulnerability Assessment category.
2.  Activate at least one Service Graph Connector for ONE of the following categories.
    1.  Directory Services \(Microsoft Active Directory\).
    2.  Endpoint Management: Microsoft Intune or Jamf Device and Endpoint Management.
    3.  Configuration and Patch Management: Microsoft SCCM or IBM Bigfix.
    4.  Cloud Provider: Amazon AWS Cloud, Microsoft Azure, GCP.

        **Note:** If Cloud Discovery is activated, these service graph connector products are not required.

3.  \[Optional\] You can activate Service Graph Connectors for any of the following categories to improve overall coverage, that is, the number of assets that are reported and monitored by [[spc-landing|Security Posture Control]].
    1.  Network Security .
    2.  Networking.
    3.  [[threat-intelligence-infrastructure|Infrastructure]] Monitoring.
    4.  Application Performance Monitoring .

After you verify you have met these prerequisites, you must activate the following policy, Assets not scanned for [[vulnerabilities|vulnerabilities]]. For more information on policies, please refer to [[spc-policies-overview|Policies for Security Posture Control]].

## Related

- [[spc-policies-overview|Policies for Security Posture Control]]
- [[tools|Tools]]
- [[spc-landing|Security Posture Control]]
- [[threat-intelligence-infrastructure|Infrastructure]]
- [[vulnerabilities|Vulnerabilities]]
