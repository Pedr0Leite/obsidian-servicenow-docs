---
title: Remediation view
description: The Remediation view in the Security Exposure Management workspace provides remediation owners and vulnerability managers with a consolidated view of remediation tasks, findings \(vulnerable items and configuration test results\), and assets \(configuration items\) that are associated with exposure findings.
locale: en-US
canonical_url: https://www.servicenow.com/docs/r/security-management/sem-workspaces-ui-remediation-module.html
release: australia
topic_type: concept
last_updated: "2026-03-12"
reading_time_minutes: 1
breadcrumb: [Security Exposure Management Workspace, Explore, Unified Security Exposure Management, Security Operations]
tags:
  - security-management
  - type-concept
---

# Remediation view

The Remediation view in the [[sem-workspace-user-interface|Security Exposure Management workspace]] provides remediation owners and vulnerability managers with a consolidated view of remediation tasks, findings \(vulnerable items and configuration test results\), and assets \(configuration items\) that are associated with exposure findings.

## Locating the Remediation view

Remediation owners and vulnerability managers can view remediation tasks and findings for multiple applications from a single [[location|location]] using filters. The data available on this page can help remediation owners prioritize their work, and vulnerability managers can monitor overall remediation progress for specific types of exposure findings.

Navigate to **Workspaces** &gt; **Security Exposure Management** &gt; **Remediation**. What you can see and do in the view depends on your role and the applications you have installed.

## Features of the overview page

-   **Assigned to me**

    Toggle between findings and remediation tasks that are assigned to you and your groups.

-   **Tabs**

    View remediation task, finding, or asset records.

-   **Widgets**

    Select the data visualizations to filter records by remediation tasks, findings, or asset records. These widgets must be activated in the [[sem-visualization-library|Visualization library]] to display data on this page.

    -   Remediation tasks - Filter records by remediation status, state, or risk rating.
    -   Findings - Filter records by impacted configuration items, by state, risk rating.
    -   Assets - Filter records by configuration items and their associated security exposures.
-   **Exposure Type**

    Filter remediation tasks and findings records by the type of security exposure, host findings \(VIT\), application findings \(AVIT\), and so on. These records are available based on the applications that you have installed and the roles you have assigned:

    -   [[avr-landing|Application Vulnerability Response]] - AVITs and AVULs.
    -   [[cvr-landing|Container Vulnerability Response]] - CVITs and CVUL records.
    -   Host [[vuln-landing-page|Vulnerability Response]] VITs and VUL records.
    -   Test results [[vr-config-compliance-landing|Configuration Compliance]] CTRs and CRG records.

## Related

- [[sem-workspace-user-interface|Security Exposure Management Workspace]]
- [[location|Location]]
- [[sem-visualization-library|Visualization library]]
- [[avr-landing|Application Vulnerability Response]]
- [[cvr-landing|Container Vulnerability Response]]
- [[vuln-landing-page|Vulnerability Response]]
- [[vr-config-compliance-landing|Configuration Compliance]]
