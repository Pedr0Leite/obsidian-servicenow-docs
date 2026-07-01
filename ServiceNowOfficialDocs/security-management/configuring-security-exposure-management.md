---
title: Implementing Unified Security Exposure Management
description: This section guides you through the entire process of implementing Unified Security Exposure Management \(USEM\) on your ServiceNow AI Platform instance. It provides detailed instructions on how to download the application from the ServiceNow Store, install it, and configure it to optimize your security workflows.
locale: en-US
canonical_url: https://www.servicenow.com/docs/r/security-management/configuring-security-exposure-management.html
release: australia
topic_type: concept
last_updated: "2026-03-12"
reading_time_minutes: 2
breadcrumb: [Unified Security Exposure Management, Security Operations]
tags:
  - security-management
  - type-concept
---

# Implementing Unified Security Exposure Management

This section guides you through the entire process of implementing Unified Security Exposure Management \(USEM\) on your ServiceNow AI Platform instance. It provides detailed instructions on how to download the application from the ServiceNow Store, install it, and configure it to optimize your security workflows.

## Installation overview

This section provides information on the initial setup of USEM, whether you're a new user or upgrading from an older version of [[vuln-landing-page|Vulnerability Response]] \(VR\).

-   [[sem-install-and-configure|Install Unified Security Exposure Management]]

    For new deployments starting with version 30.0 of Vulnerability Response and other related applications, follow these steps to install USEM for the first time.

-   [Migrate to Unified Security Exposure Management \(USEM\) from Vulnerability Response](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/security-management/vulnerability-response/migrate-to-usem.md)

    If you are upgrading from a version prior to 30.0 of Vulnerability Response and other related applications, refer to these instructions to successfully migrate to USEM.


## Configuration overview

Once you install USEM, you must configure rules, [[tisc-email-notifications|email notifications]], dashboards and so on to automate and streamline your exposure management.

1.  [[sem-configure-rules-manage-findings|Configure rules to manage findings]]

    Automate the prioritization and triaging of security exposure findings using configurable rules.

2.  [[sem-configure-email-notifications|Configure email notifications in Unified Security Exposure Management]]

    Set up email notifications to share critical information about important updates and activities, such as the approval or rejection of false-positive requests.

3.  [[sem-configure-email-templates|Configure email templates in Unified Security Exposure Management]]

    Create and manage preconfigured email templates for consistent and efficient communication.

4.  [[sem-configure-visualization-library|Configure Visualization library]]

    Customize the Findings view page by selecting the columns and widgets you want to display, and manage their activation status and conditions.

5.  [[sem-configure-exp-mngmt-vr|Configure Exception Management for Security Exposure Management]]

    Manage requests for exceptions and review, approve, or reject exceptions for findings or remediation tasks.

## Related

- [[sem-install-and-configure|Install Unified Security Exposure Management]]
- [[sem-configure-rules-manage-findings|Configure rules to manage findings]]
- [[sem-configure-email-notifications|Configure email notifications in Unified Security Exposure Management]]
- [[sem-configure-email-templates|Configure email templates in Unified Security Exposure Management]]
- [[sem-configure-visualization-library|Configure Visualization library]]
- [[sem-configure-exp-mngmt-vr|Configure Exception Management for Security Exposure Management]]
- [[vuln-landing-page|Vulnerability Response]]
- [[tisc-email-notifications|Email Notifications]]
