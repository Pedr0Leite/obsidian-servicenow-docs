---
title: Install Vault Suite
description: Use Vault Suite to deploy ServiceNow Vault and its underlying plugins in a single step, without configuring each plugin separately.
locale: en-US
canonical_url: https://www.servicenow.com/docs/r/platform-security/install-vault-suite.html
release: australia
topic_type: task
last_updated: "2026-05-26"
reading_time_minutes: 1
keywords: [Vault Suite, install vault, vault plugins]
breadcrumb: [Configuring ServiceNow Vault, ServiceNow Vault]
tags:
  - platform-security
  - type-task
---

# Install Vault Suite

Use [[vault-suite|Vault Suite]] to deploy [[servicenow-vault-landing|ServiceNow Vault]] and its underlying plugins in a single step, without configuring each plugin separately.

## Before you begin

Your instance must have a ServiceNow Vault entitlement. Without an entitlement, the underlying plugins remain inactive after installation and the tool cards on the [[vault-dashboard|ServiceNow Vault console dashboard]] appear as inactive.

Role required: admin

## About this task

Vault Suite includes ServiceNow Vault and its premium plugins, including [[data-privacy-landing|Data Privacy]], Log [[export|Export]] Service, Zero Trust Access, [[field-encryption|Field Encryption]], and [[code-signing-landing|Code Signing]]. Installing Vault Suite activates all included plugins together.

**Note:** If ServiceNow Vault is already installed on your instance, installing Vault Suite adds the remaining plugins without affecting your existing ServiceNow Vault [[sc-configuration|configuration]].

## Procedure

1.  Navigate to **All** &gt; **Application Manager** &gt; **Vault Suite**.

2.  Select **Install**.

    Vault Suite begins installing the underlying plugins. Installation may take several minutes to complete.


## Result

Vault Suite and the following premium plugins are installed on your instance:

-   Vault Console
-   Data Privacy
-   Log Export Service
-   Zero Trust Access
-   Field Encryption
-   Code Signing

## What to do next

Navigate to the [ServiceNow Vault console dashboard](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/platform-security/vault-dashboard.md) to confirm that the tool cards are enabled. On Vault Console 2.1 or later, if your instance doesn't already have [[ca-policies|policies]] or configurations for Anonymization and Log Export Service, then ServiceNow Vault can apply ready-to-use defaults to help you get started. For more information, see [[vault-default-policies-configs|Default policies and configurations in ServiceNow Vault]].

## Related

- [[vault-dashboard|ServiceNow Vault console dashboard]]
- [[vault-default-policies-configs|Default policies and configurations in ServiceNow Vault]]
- [[vault-suite|Vault Suite]]
- [[servicenow-vault-landing|ServiceNow Vault]]
- [[data-privacy-landing|Data Privacy]]
- [[export|Export]]
- [[field-encryption|Field Encryption]]
- [[code-signing-landing|Code Signing]]
- [[sc-configuration|Configuration]]
- [[ca-policies|Policies]]
