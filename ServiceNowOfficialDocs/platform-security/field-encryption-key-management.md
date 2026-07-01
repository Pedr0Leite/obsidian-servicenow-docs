---
title: Encrypting fields and attachments
description: Once cryptographic modules are created, a security admin can define the encrypted fields configuration \(EFC\) and opt to encrypt a field or attachment on a table.
locale: en-US
canonical_url: https://www.servicenow.com/docs/r/platform-security/field-encryption-key-management.html
release: australia
topic_type: concept
last_updated: "2026-03-12"
reading_time_minutes: 2
breadcrumb: [Using Field Encryption, Field Encryption, Encryption]
tags:
  - platform-security
  - type-concept
---

# Encrypting fields and attachments

Once cryptographic modules are created, a security admin can define the encrypted fields [[sc-configuration|configuration]] \(EFC\) and opt to encrypt a field or attachment on a table.

## How to encrypt fields

**Note:** Encrypted fields aren’t audited by design. This behavior isn’t configurable.

1.  Specify the key source: ServiceNow generated keys or your customer-supplied keys \(bring your own key\) in **System Security** &gt; **[[field-encryption|Field Encryption]] Settings**.
2.  After specifying the key source, [[create-cryptographic-module|create a cryptographic module]] or use an existing cryptographic module. Start with [Create a cryptographic module](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/platform-security/platform-encryption/create-cryptographic-module.md) for instructions.

    **Note:** If you use customer-supplied keys, follow the directions in [[create-PE-cryptographic-module|Create cryptographic module for Field Encryption]] and [[customer-supplied-keys|Configure properties for customer-supplied keys]].

3.  Create an encrypted field configuration to define where the [[encryption-landing|encryption]] is applied. Here, you specify the target table and choose whether to encrypt a column or attachments within the table. See [[set-encrypted-field-config|Set encrypted field configurations]] to get started.

**Note:** See [[kmf-walkthroughs-tutorials|Field Encryption Enterprise examples]] that illustrates how to encrypt fields and attachments using customer-supplied keys.

-   **[Set encrypted field configurations](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/platform-security/set-encrypted-field-config.md)**  
Configure which table columns or attachments that the system encrypts using a preconfigured cryptographic module.
-   **[[script-map|Script access for cryptographic modules]]**  
Scripts can be run to access a cryptographic module policy for a cryptographic purpose.
-   **[[schedule-mass-jobs|Schedule mass encryption, decryption, and rekeying jobs]]**  
Schedule encryption, decryption, and rekeying jobs to run at a time that is best for your instance.
-   **[[mass-enc-dec|Run mass encryption or decryption]]**  
You can run mass encryption on encryption configurations, as well as a mass decryption to decrypt previously encrypted values.
-   **[[upload-attachments-for-encryption|Upload attachments for encryption]]**  
Protect sensitive files by encrypting record attachments using Field Encryption and Row Conditions.
-   **[[fe-maps-inbound-email-attachment-encryption|Module access policies for inbound email attachment encryption]]**  
Encrypting inbound [[email|email]] attachments associated with matched records requires one or more module access [[ca-policies|policies]] \(MAPs\).

**Parent Topic:**[[using-column-level-encryption|Using Field Encryption]]

**Parent Topic:**[[using-column-level-encryption-2|Using Column Level Encryption]]

## Related

- [[create-PE-cryptographic-module|Create cryptographic module for Field Encryption]]
- [[customer-supplied-keys|Configure properties for customer-supplied keys]]
- [[set-encrypted-field-config|Set encrypted field configurations]]
- [[kmf-walkthroughs-tutorials|Field Encryption Enterprise examples]]
- [[script-map|Script access for cryptographic modules]]
- [[schedule-mass-jobs|Schedule mass encryption, decryption, and rekeying jobs]]
- [[mass-enc-dec|Run mass encryption or decryption]]
- [[upload-attachments-for-encryption|Upload attachments for encryption]]
- [[fe-maps-inbound-email-attachment-encryption|Module access policies for inbound email attachment encryption]]
- [[using-column-level-encryption|Using Field Encryption]]
- [[using-column-level-encryption-2|Using Column Level Encryption]]
- [[sc-configuration|Configuration]]
- [[field-encryption|Field Encryption]]
- [[create-cryptographic-module|Create a cryptographic module]]
- [[encryption-landing|Encryption]]
- [[email|Email]]
- [[ca-policies|Policies]]
