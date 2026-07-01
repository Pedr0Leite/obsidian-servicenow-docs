---
title: Migrating to Field Encryption
description: Scheduled jobs migrate your keys and encrypted data from Encryption Support to Field Encryption.
locale: en-US
canonical_url: https://www.servicenow.com/docs/r/platform-security/migration-to-platform-encryption.html
release: australia
topic_type: concept
last_updated: "2026-03-10"
reading_time_minutes: 1
breadcrumb: [Configuring Field Encryption, Field Encryption, Encryption]
tags:
  - platform-security
  - type-concept
---

# Migrating to Field Encryption

Scheduled jobs migrate your keys and encrypted data from [[encryption-landing|Encryption]] Support to [[field-encryption|Field Encryption]].

When you install Field Encryption, the migration process triggers automatically. Once the key migration job completes, encryption context keys are restricted to decryption only. Use cryptographic module keys for all new encryption operations going forward.

You can review the scheduled jobs by navigating to **System Security** &gt; **[[c_HighSecuritySettings|High Security Settings]]** &gt; **Security Jobs**:

-   **autoKeyMigration**: Migrates encryption context keys to [[encryption|Key Management Framework]] \(KMF\) cryptographic module keys.
-   **autoDataMigration**: Migrates data that you already encrypted to use the KMF cryptographic module key.

You can modify when these scheduled jobs run, and can pause or restart them at any time.

Verify that the encrypted field configurations are using your newly migrated module keys by navigating to **System Security** &gt; **Field Encryption** &gt; **Encrypted Field Configurations**. Look for the following items:

-   The **Method** field is **Single Module**.
-   The **Crypto module** field is populated with the name of the cryptographic module that the system automatically creates. You can review that module and the module access policy, both of which are active and published.

-   **[[cle-migration-status-page|Field Encryption migration status page]]**  
Use the migration status page to track the migration of encryption contexts to encryption modules.

**Parent Topic:**[[configuring-column-level-encryption|Configuring Field Encryption]]

## Related

- [[cle-migration-status-page|Field Encryption migration status page]]
- [[configuring-column-level-encryption|Configuring Field Encryption]]
- [[encryption-landing|Encryption]]
- [[field-encryption|Field Encryption]]
- [[c_HighSecuritySettings|High Security Settings]]
- [[encryption|Key Management Framework]]
