---
title: Secrets Management dashboard
description: Use the Secrets Management dashboard to review the secret groups configured on your instance and learn about any security issues.
locale: en-US
canonical_url: https://www.servicenow.com/docs/r/platform-security/secrets-dashboard.html
release: australia
topic_type: concept
last_updated: "2026-04-30"
reading_time_minutes: 2
breadcrumb: [Secrets Management, Platform Security]
---

# Secrets Management dashboard

Use the Secrets Management dashboard to review the secret groups configured on your instance and learn about any security issues.

## Secret Group Overview

\[Omitted image "sm\_dash.png"\] Alt text: Secrets management dashboard

The **Secret Group Overview** tab displays information about your configured secret groups. Use this tab to see information about the secrets groups configured on your instance.

-   **Secret Group by Type**

    Displays a pie chart showing secret groups installed on your instance, grouped by secret type \(instance side of client side\).

-   **Secret Group by Criterion Type**

    Displays a pie chart showing secret groups with criteria configured on your instance by the type of criteria used.

-   **Number of Inactive Secrets Groups**

    Displays a count of the inactive secret groups configured on your instance.

-   **Number of Dedicated Secrets**

    Displays a count of secrets within basic secret groups.


## Secret Group Warnings

\[Omitted image "sm\_dash\_2.png"\] Alt text: Secrets management dashboard

The **Secret Group Warnings** tab displays warnings related to your secret groups and [[identity-landing|identity]] groups.

-   **Instance Accessible Secret Groups- Warnings**

    This card displays warnings if there are secret groups with no active access [[ca-policies|policies]] in place. Select a secret group name to view that record.

-   **Client Accessible Secret Groups- Warnings**

    This card displays warnings if there are client accessible secret groups that don’t have an active identity module access policy \(MAP\). Select a secret group name to view that record.

-   **Identity Groups- Warnings**

    This card displays warnings if there are identity groups that don’t have group members configured. Select the identity group name to view the record.


**Note:** The Secrets Management Dashboard is a part of Secrets Management Enterprise. Secrets Management Enterprise is a Secrets Management Enterprise. Secrets Management ServiceNow's production instance.

-   **[[roles-sec-man|Secrets Management roles]]**  
Secrets Management adds these roles.
-   **[[create-sm-crypto-module|Create a secret group cryptographic module]]**  
Create a secret group cryptographic module to perform [[encryption-landing|encryption]] and decryption.
-   **[[sm-create-basic-group|Create a basic secret group]]**  
Create a basic secret group to group any secrets, regardless of their criteria.
-   **[[sm-create-criteria-group|Create a secret group with criteria]]**  
[[client-access-example-3|Create a secret group with criteria]] to organize secrets entered in Password2 fields automatically when they share a common criteria, such as table, scope, or application.
-   **[[sm-upload-key|Upload a public key for Secrets Management]]**  
Upload a public key to encrypt your secrets in Secrets Management.
-   **[[sm-security-jobs|Run Secrets Management security jobs]]**  
Schedule a Secrets Management job to perform encryption tasks on secrets fields on your instance.

**Parent Topic:**[[secrets-management|Secrets Management]]

## Related

- [[roles-sec-man|Secrets Management roles]]
- [[create-sm-crypto-module|Create a secret group cryptographic module]]
- [[sm-create-basic-group|Create a basic secret group]]
- [[sm-create-criteria-group|Create a secret group with criteria]]
- [[sm-upload-key|Upload a public key for Secrets Management]]
- [[sm-security-jobs|Run Secrets Management security jobs]]
- [[secrets-management|Secrets Management]]
- [[identity-landing|Identity]]
- [[ca-policies|Policies]]
- [[encryption-landing|Encryption]]
- [[client-access-example-3|Create a secret group with criteria]]
