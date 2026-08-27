---
title: Create a cryptographic specification for Column Level Encryption
description: After you create a cryptographic module, access the corresponding cryptographic specification to define the algorithm.
locale: en-US
canonical_url: https://www.servicenow.com/docs/r/platform-security/create-crypto-spec-pe-2.html
release: australia
topic_type: task
last_updated: "2026-03-12"
reading_time_minutes: 1
breadcrumb: [Using Column Level Encryption, Column Level Encryption, Encryption]
tags:
  - platform-security
  - type-task
---

# Create a cryptographic specification for Column Level Encryption

After you [[create-cryptographic-module|create a cryptographic module]], access the corresponding cryptographic specification to define the algorithm.

## Before you begin

Role required: sn\_kmf.cryptographic\_manager or sn\_kmf\_admin and security\_admin or admin

## About this task

This procedure describes options that are available with [[column-level-encryption-landing|Column Level Encryption]] with the base system and additional [[sc-configuration|configuration]] options that become available with [[now-platform-encryption-2|Column Level Encryption Enterprise]] functionality. Column Level Encryption Enterprise functionality is available with a paid subscription. Refer to [Encryption and Key Management subscription bundle](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/platform-security/platform-encryption/encryption-sku.md) for supported features and options available with each offering. See [[activate-platform-encryption-2|Activate Column Level Encryption Enterprise]] for more information on obtaining Column Level Encryption Enterprise.

A cryptographic specification will be created by the system when you create a cryptographic module for Column Level Encryption Enterprise.

## Procedure

1.  Navigate to **System Security** &gt; **[[field-encryption|Field Encryption]] Modules** &gt; **All**.

2.  Select the cryptographic module to open the configuration options.

    Cryptographic module information is displayed at the top of the screen. A Symmetric Data Encryption/Decryption crypto specification is auto-created with an AES 256 CBC algorithm.

3.  Select the crypto specification from the table to open the Algorithm Definition.

    For Column Level Encryption Enterprise see [[adv-algorithm-cleent-2|Configure advanced algorithms for Column Level Encryption Enterprise]].

4.  Click **Next** to access the Key Lifecycle.


## What to do next

Perform one of the following operations:

-   Select an entry in the Key Lifecycle table to define key lifecycle behavior. See [Configure key lifecycle states](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/platform-security/platform-encryption/configure-key-lifecycle-states.md) for details to complete the lifecycle definition for the key.
-   Click **Next** to create a cryptographic key. For details on this process, see [Generate a ServiceNow cryptographic key](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/platform-security/platform-encryption/generate_sn_key.md).

**Parent Topic:**[[using-column-level-encryption-2|Using Column Level Encryption]]

## Related

- [[activate-platform-encryption-2|Activate Column Level Encryption Enterprise]]
- [[adv-algorithm-cleent-2|Configure advanced algorithms for Column Level Encryption Enterprise]]
- [[using-column-level-encryption-2|Using Column Level Encryption]]
- [[create-cryptographic-module|Create a cryptographic module]]
- [[column-level-encryption-landing|Column Level Encryption]]
- [[sc-configuration|Configuration]]
- [[now-platform-encryption-2|Column Level Encryption Enterprise]]
- [[field-encryption|Field Encryption]]
