---
title: Configuring Field Encryption
description: Learn how to activate and configure Field Encryption and manage migration from Encryption Support.
locale: en-US
canonical_url: https://www.servicenow.com/docs/r/platform-security/configuring-column-level-encryption.html
release: australia
topic_type: concept
last_updated: "2026-03-12"
reading_time_minutes: 2
breadcrumb: [Field Encryption, Encryption]
---

# Configuring Field Encryption

Learn how to activate and configure Field Encryption and manage migration from [[encryption-landing|Encryption]] Support.

-   **[[activate-platform-encryption|Activate Field Encryption]]**

    Learn how to active either Field Encryption or [[now-platform-encryption|Field Encryption Enterprise]].

-   **Roles Required for Configuring Field Encryption**

    Learn about the roles required to configure Field Encryption.


## Migration from encryption support

Use Scheduled jobs to migrate your keys and encrypted data from legacy Encryption Support to Field Encryption Enterprise. See details for this process at [[migration-to-platform-encryption|Migrating to Field Encryption]]

## Change attachment encryption settings

Improve security by preventing [[users|users]] from attaching unencrypted files. For details, see [[attach-enc-property|Prevent users from attaching unencrypted files]].

-   **[Activate Field Encryption](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/platform-security/activate-platform-encryption.md)**  
Activate either Field Encryption Starter or Field Encryption Enterprise.
-   **[[fe-roles|Role requirements for Field Encryption]]**  
Learn about the roles required to configure Field Encryption.
-   **[[configure-fe-modules|Configure Field Encryption modules]]**  
Learn how to configure Field Encryption modules.
-   **[[configure-fe-crypto-specs|Cryptographic specifications for Field Encryption]]**  
Use cryptographic specifications to define the purpose, algorithm, key length, mode, and origin of your encryption key.
-   **[[fe-module-keys|Module keys for Field Encryption]]**  
The Module Keys tab shows you summary level information about your Field Encryption Data Encryption Key\(s\). You can view the Key alias, Key type, Algorithm, Key lifecycle state, and Key version.
-   **[[module-lifecycle-policy-exceptions-for-fe|Module lifecycle policy exceptions for Field Encryption]]**  
Use module lifecycle policy exceptions to customize the lifecycle of your module keys.
-   **[[fe-config-customer-supplied-keys|Configure Customer-supplied keys for Field Encryption Enterprise]]**  
Bring your own data encryption key to the platform instead of using the one that ServiceNow generates.
-   **[[configure-fe-fields-attachments|Configure encrypted field configurations for fields or attachments]]**  
Create an encrypted field [[sc-configuration|configuration]] to specify which fields are encrypted on a table, and whether that table's attachments are encrypted.
-   **[[multi-module-fe-config|Configure multi-module encrypted field configurations]]**  
Create an encrypted field configuration that uses more than one encryption module.
-   **[[maps-for-fe|Configure module access policies for Field Encryption]]**  
[[create-module-access-policy|Create a module access policy]] to control which users, scripts, or system processes can encrypt or decrypt data encrypted by a field encryption module.
-   **[Migrating to Field Encryption](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/platform-security/migration-to-platform-encryption.md)**  
Scheduled jobs migrate your keys and encrypted data from Encryption Support to Field Encryption.
-   **[[migrate-ee-to-fe|Migrate from Edge Encryption to Field Encryption]]**  
Migrate from Edge Encryption to Field Encryption to take advantage of the latest security features.
-   **[[fe-system-clones|Field Encryption and system clones]]**  
Cloning an instance with Field Encryption installed automatically generates new field encryption module encryption keys on the target clone instance.
-   **[Prevent users from attaching unencrypted files](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/platform-security/attach-enc-property.md)**  
Modify the com.glide.encryption.enable\_attachment\_key\_ui property to prevent your users with access to an encryption module key from attaching unencrypted attachments.

**Parent Topic:**[[field-encryption|Field Encryption]]

## Related

- [[activate-platform-encryption|Activate Field Encryption]]
- [[migration-to-platform-encryption|Migrating to Field Encryption]]
- [[attach-enc-property|Prevent users from attaching unencrypted files]]
- [[fe-roles|Role requirements for Field Encryption]]
- [[configure-fe-modules|Configure Field Encryption modules]]
- [[configure-fe-crypto-specs|Cryptographic specifications for Field Encryption]]
- [[fe-module-keys|Module keys for Field Encryption]]
- [[module-lifecycle-policy-exceptions-for-fe|Module lifecycle policy exceptions for Field Encryption]]
- [[fe-config-customer-supplied-keys|Configure Customer-supplied keys for Field Encryption Enterprise]]
- [[configure-fe-fields-attachments|Configure encrypted field configurations for fields or attachments]]
- [[multi-module-fe-config|Configure multi-module encrypted field configurations]]
- [[maps-for-fe|Configure module access policies for Field Encryption]]
- [[migrate-ee-to-fe|Migrate from Edge Encryption to Field Encryption]]
- [[fe-system-clones|Field Encryption and system clones]]
- [[field-encryption|Field Encryption]]
- [[encryption-landing|Encryption]]
- [[now-platform-encryption|Field Encryption Enterprise]]
- [[users|Users]]
- [[sc-configuration|Configuration]]
- [[create-module-access-policy|Create a module access policy]]
