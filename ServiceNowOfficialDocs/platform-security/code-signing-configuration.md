---
title: Code Signing Configuration
description: The Code Signing Configuration dashboard displays the system properties and key settings that control Code Signing in your environment, including flags and enforcement policies. These settings enable features, enforce signature validation, and define trusted sources.
locale: en-US
canonical_url: https://www.servicenow.com/docs/r/platform-security/code-signing-configuration.html
release: australia
topic_type: concept
last_updated: "2026-06-25"
reading_time_minutes: 1
breadcrumb: [Health and Status Dashboard, Code Signing, Platform Security]
tags:
  - platform-security
  - type-concept
---

# Code Signing Configuration

The Code Signing Configuration dashboard displays the [[ca-system-properties|system properties]] and key settings that control [[code-signing-landing|Code Signing]] in your environment, including flags and enforcement [[ca-policies|policies]]. These settings enable features, enforce signature validation, and define trusted sources.

The Code Signing Configuration dashboard displays the following reports:

|Title|Type|Description|
|-----|----|-----------|
|Setting|Text field|Name of a specific [[sc-configuration|configuration]] property that controls a feature or behavior related to code signing. Each setting defines how the system should handle aspects like signature validation, enforcement, or trusted sources.|
|Value|Text field|Current state or input assigned to a specific setting. It determines how the setting behaves. For example, whether Code Signing is enabled \(true\) or disabled \(false\). The value directly affects the system’s Code Signing operations and enforcement.|
|Last Updated|Text field|Most recent date and time when the setting was modified in the following format: `DD/MM/YY/H:S (Day/Month/Year/Hour:Minute)`|

**Parent Topic:**[[code-signing-health-and-status-dashboard|Code Signing Health and Status Dashboard]]

## Related

- [[code-signing-health-and-status-dashboard|Code Signing Health and Status Dashboard]]
- [[ca-system-properties|System properties]]
- [[code-signing-landing|Code Signing]]
- [[ca-policies|Policies]]
- [[sc-configuration|Configuration]]
