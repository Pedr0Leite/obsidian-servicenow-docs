---
title: Mitigation controls policies
description: The Security Posture Control and the Mitigation Controls applications are required to view the mitigation controls and mitigation controls policies in the SPC. Both applications are available from the ServiceNow Store.
locale: en-US
canonical_url: https://www.servicenow.com/docs/r/security-management/spc-mitigation-policies.html
release: australia
topic_type: concept
last_updated: "2026-03-12"
reading_time_minutes: 1
breadcrumb: [Use mitigation controls, Security Posture Control, Security Operations]
---

# Mitigation controls policies

The [[spc-landing|Security Posture Control]] and the Mitigation Controls applications are required to view the mitigation controls and mitigation controls policies in the SPC. Both applications are available from the ServiceNow Store.

Refer to the following topics for more information about downloading and installing applications from the ServiceNow® Store.

-   [[download-app-first-time|Download an application from the ServiceNow Store for the first time]]
-   [[install-non-core-apps|Install a Security Operations integration]]

To view the mitigation controls policies, users in the SPC Admin Group and SPC Analyst Group can navigate to **Workspaces** &gt; **Security Posture Control** &gt; **Policies and findings** &gt; **All** in the SPC Workspace navigation panel.

The following mitigation controls policies are included with the application and are displayed along with the other SPC policies:

-   SEH Overwrite
-   Heap spray
-   CrowdStrike NULL Page Allocation
-   CrowdStrike Force DEP
-   CrowdStrike Force ASLR
-   Microsoft Defender Control Flow Guard
-   Microsoft Defender force ASLR
-   Microsoft Defender Mandatory ASLR and Bottom-up ASLR
-   SentinelOne Application Control
-   SentinelOne Data Files
-   SentinelOne Executables
-   SentinelOne Exploits
-   SentinelOne IDR
-   SentinelOne Detect Interactive Threat
-   SentinelOne Detect Lateral Movement
-   SentinelOne Static AI
-   SentinelOne Static AI - suspicious
-   SentinelOne Potentially unwanted applications
-   SentinelOne Remote shell
-   SentinelOne Reputation

## Mitigation controls categories

The following categories of mitigation controls are currently supported with the SPC.

-   [[spc-controls-policies-for-edr|Mitigation controls and policies required for Exploit Protection \(EDR\) mitigation controls]].
-   [[spc-controls-policies-for-exploit-waf|Exploit Protection \(WAF\) mitigation controls]]. You must create policies for AWS WAF. See [[spc-create-AWS-WAF-policy|Create a policy for the AWS WAF integration for mitigation controls monitoring]] for more information.

## Related

- [[download-app-first-time|Download an application from the ServiceNow Store for the first time]]
- [[install-non-core-apps|Install a Security Operations integration]]
- [[spc-controls-policies-for-edr|Mitigation controls and policies required for Exploit Protection \(EDR\) mitigation controls]]
- [[spc-controls-policies-for-exploit-waf|Exploit Protection \(WAF\) mitigation controls]]
- [[spc-create-AWS-WAF-policy|Create a policy for the AWS WAF integration for mitigation controls monitoring]]
- [[spc-landing|Security Posture Control]]
