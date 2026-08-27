---
title: Code Signing Health and Status Dashboard
description: The Code Signing Health and Status dashboard provides a centralized, user-friendly view of your Code Signing environment's health and configuration. Use it to identify issues, verify configuration accuracy, and support secure, uninterrupted code-signing operations.
locale: en-US
canonical_url: https://www.servicenow.com/docs/r/platform-security/code-signing-health-and-status-dashboard.html
release: australia
topic_type: concept
last_updated: "2026-06-25"
reading_time_minutes: 1
breadcrumb: [Code Signing, Platform Security]
tags:
  - platform-security
  - type-concept
---

# Code Signing Health and Status Dashboard

The Code Signing Health and Status dashboard provides a centralized, user-friendly view of your Code Signing environment's health and [[sc-configuration|configuration]]. Use it to identify issues, verify configuration accuracy, and support secure, uninterrupted code-signing operations.

The Code Signing Health and Status dashboard highlights configuration issues and includes intuitive guidance to help you resolve them quickly, reducing the need for escalation. You can use the dashboard to verify that Code Signing configurations are set up correctly and performing securely. It helps you identify potential issues that could lead to failures and enables you to provide accurate guidance to the stakeholders involved.

The dashboard lets you search, filter, and rescan the following parameters:

-   Configurations
-   Certificate status
-   Plugin details
-   Signature verification certificate
-   MID Server setup

To access the Code Signing Health and Status Dashboard, go to **All** &gt; **Code Signing** &gt; **System Health** &gt; **Dashboard**.

-   **[[overview|Overview Dashboard]]**  
The Overview dashboard provides a centralized view of your Code Signing environment, offering real-time insights into key components and their status.
-   **[[signature-verification-status|Signature Verification Status]]**  
View the status of valid, invalid, and missing signatures across different applications to assess code signing coverage. Use this information to identify areas that may require additional attention or action.
-   **[[code-signing-mid-server-configuration|Code Signing MID Server Configuration]]**  
Manage and configure the trust relationships and certificate settings for MID Servers.
-   **[[code-signing-certificates|Key Pair and Certificates]]**  
The Key Pair and Certificates dashboard displays details about the cryptographic keys and digital [[c_Certificates|certificates]] used for Code Signing. It includes information such as key type, certificate issuer, expiration date, and validity status. Use this dashboard to manage code signing certificate credentials, verify their validity, and help ensure secure and trusted Code Signing operations.
-   **[[code-signing-configuration|Code Signing Configuration]]**  
The Code Signing Configuration dashboard displays the [[ca-system-properties|system properties]] and key settings that control Code Signing in your environment, including flags and enforcement [[ca-policies|policies]]. These settings enable features, enforce signature validation, and define trusted sources.

**Parent Topic:**[[code-signing-landing|Code Signing]]

## Related

- [[overview|Overview Dashboard]]
- [[signature-verification-status|Signature Verification Status]]
- [[code-signing-mid-server-configuration|Code Signing MID Server Configuration]]
- [[code-signing-certificates|Key Pair and Certificates]]
- [[code-signing-configuration|Code Signing Configuration]]
- [[code-signing-landing|Code Signing]]
- [[sc-configuration|Configuration]]
- [[c_Certificates|Certificates]]
- [[ca-system-properties|System properties]]
- [[ca-policies|Policies]]
