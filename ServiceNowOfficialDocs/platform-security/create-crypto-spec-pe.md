---
title: Create a cryptographic specification for Field Encryption
description: After you create a cryptographic module, access the corresponding cryptographic specification to define the algorithm.
locale: en-US
canonical_url: https://www.servicenow.com/docs/r/platform-security/create-crypto-spec-pe.html
release: australia
topic_type: task
last_updated: "2026-03-12"
reading_time_minutes: 1
breadcrumb: [Using Field Encryption, Field Encryption, Encryption]
tags:
  - platform-security
  - type-task
---

# Create a cryptographic specification for Field Encryption

After you [[create-cryptographic-module|create a cryptographic module]], access the corresponding cryptographic specification to define the algorithm.

## Before you begin

Role required: security\_admin  and sn\_kmf.cryptographic\_manager  or sn\_kmf.admin

## About this task

This procedure describes options that are available with [[field-encryption|Field Encryption]] with the base system and additional [[sc-configuration|configuration]] options that become available with [[now-platform-encryption|Field Encryption Enterprise]] functionality. Field Encryption Enterprise functionality is available with a paid subscription. Refer to [Encryption and Key Management subscription bundle](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/platform-security/platform-encryption/encryption-sku.md) for supported features and options available with each offering. See [[activate-platform-encryption|Activate Field Encryption]] for more information on obtaining Field Encryption Enterprise.

A cryptographic specification will be created by the system when you create a cryptographic module for Field Encryption Enterprise.

## Procedure

1.  Navigate to **System Security** &gt; **Field Encryption** &gt; **Field Encryption Experience**.

2.  Select **View module details** from the **Field Encryption overview** to open the module record you want to configure.

    **Note:** The names displayed in the list are appended with the scope, for example, `global.[your Field Encryption Module name ]`.

3.  Select **Manage Specifications Settings** from the **Cryptographic Specification**.

    For Field Encryption Enterprise see [[adv-algorithm-cleent|Configure advanced algorithms for Field Encryption Enterprise]].


## What to do next

Perform one of the following operations:

-   Select an entry in the Key Lifecycle table to define key lifecycle behavior. See [Configure key lifecycle states](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/platform-security/platform-encryption/configure-key-lifecycle-states.md) for details to complete the lifecycle definition for the key.
-   Click **Next** to create a cryptographic key. For details on this process, see [Generate a ServiceNow cryptographic key](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/platform-security/platform-encryption/generate_sn_key.md).

**Parent Topic:**[[using-column-level-encryption|Using Field Encryption]]

## Related

- [[activate-platform-encryption|Activate Field Encryption]]
- [[adv-algorithm-cleent|Configure advanced algorithms for Field Encryption Enterprise]]
- [[using-column-level-encryption|Using Field Encryption]]
- [[create-cryptographic-module|Create a cryptographic module]]
- [[field-encryption|Field Encryption]]
- [[sc-configuration|Configuration]]
- [[now-platform-encryption|Field Encryption Enterprise]]
