---
title: Using Column Level Encryption
description: Use Column Level Encryption to manage access to encrypted data on your instances.
locale: en-US
canonical_url: https://www.servicenow.com/docs/r/platform-security/using-column-level-encryption-2.html
release: australia
topic_type: concept
last_updated: "2026-03-12"
reading_time_minutes: 1
breadcrumb: [Column Level Encryption, Encryption]
tags:
  - platform-security
  - type-concept
---

# Using Column Level Encryption

Use Column Level Encryption to manage access to encrypted data on your instances.

Use the related links to find information on common [[field-encryption|Field Encryption]] tasks.

-   **[[create-PE-cryptographic-module-2|Create cryptographic module for Column Level Encryption]]**  
Create a Field Encryption cryptographic module to define the mechanisms used for cryptographic operations.
-   **[[encrypt-data-using-multiple-modules-feature|Encrypt data using the Multiple Modules feature]]**  
Encrypt data with more than one [[encryption-landing|encryption]] module permitting the user to determine which keys are used for specific rows within the encrypted data.
-   **[[create-crypto-spec-pe-2|Create a cryptographic specification for Column Level Encryption]]**  
After you [[create-cryptographic-module|create a cryptographic module]], access the corresponding cryptographic specification to define the algorithm.
-   **[[adv-algorithm-cleent-2|Configure advanced algorithms for Column Level Encryption Enterprise]]**  
[[create-crypto-spec|Create a cryptographic specification]] to define the algorithm for a cryptographic module. Customize the encryption specifications with advanced options that are available for [[now-platform-encryption-2|Column Level Encryption Enterprise]].
-   **[[csk-landing-2|Using customer supplied keys with Column Level Encryption Enterprise]]**  
You can use your own customer-supplied key instead of using the ServiceNow® system-generated keys.
-   **[[field-encryption-key-management|Encrypting fields and attachments]]**  
Once cryptographic modules are created, a security admin can define the encrypted fields [[sc-configuration|configuration]] \(EFC\) and opt to encrypt a field or attachment on a table.
-   **[[kmf-walkthroughs-tutorials-2|Column Level Encryption Enterprise examples]]**  
These examples walk you through the encryption of fields and attachments using customer-supplied keys.

**Parent Topic:**[[column-level-encryption-landing|Column Level Encryption]]

**Related topics**  


[Create cryptographic module for Column Level Encryption](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/platform-security/create-PE-cryptographic-module-2.md)

[Create a cryptographic specification for Column Level Encryption](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/platform-security/create-crypto-spec-pe-2.md)

[Configure advanced algorithms for Column Level Encryption Enterprise](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/platform-security/adv-algorithm-cleent-2.md)

[[customer-supplied-keys|Configure properties for customer-supplied keys]]

[Encrypting fields and attachments](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/platform-security/field-encryption-key-management.md)

## Related

- [[create-PE-cryptographic-module-2|Create cryptographic module for Column Level Encryption]]
- [[encrypt-data-using-multiple-modules-feature|Encrypt data using the Multiple Modules feature]]
- [[create-crypto-spec-pe-2|Create a cryptographic specification for Column Level Encryption]]
- [[adv-algorithm-cleent-2|Configure advanced algorithms for Column Level Encryption Enterprise]]
- [[csk-landing-2|Using customer supplied keys with Column Level Encryption Enterprise]]
- [[field-encryption-key-management|Encrypting fields and attachments]]
- [[kmf-walkthroughs-tutorials-2|Column Level Encryption Enterprise examples]]
- [[column-level-encryption-landing|Column Level Encryption]]
- [[customer-supplied-keys|Configure properties for customer-supplied keys]]
- [[field-encryption|Field Encryption]]
- [[encryption-landing|Encryption]]
- [[create-cryptographic-module|Create a cryptographic module]]
- [[create-crypto-spec|Create a cryptographic specification]]
- [[now-platform-encryption-2|Column Level Encryption Enterprise]]
- [[sc-configuration|Configuration]]
