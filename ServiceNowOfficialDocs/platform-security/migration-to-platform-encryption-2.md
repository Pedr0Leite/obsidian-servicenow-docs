---
title: Migrating to Column Level Encryption
description: Scheduled jobs migrate your keys and encrypted data from Encryption Support to Column Level Encryption.
locale: en-US
canonical_url: https://www.servicenow.com/docs/r/platform-security/migration-to-platform-encryption-2.html
release: australia
topic_type: concept
last_updated: "2026-03-12"
reading_time_minutes: 1
breadcrumb: [Configuring Column Level Encryption, Column Level Encryption, Encryption]
---

# Migrating to Column Level Encryption

Scheduled jobs migrate your keys and encrypted data from [[encryption-landing|Encryption]] Support to [[column-level-encryption-landing|Column Level Encryption]].

You can review the scheduled jobs by navigating to **System Security** &gt; **[[c_HighSecuritySettings|High Security Settings]]** &gt; **Security Jobs**:

-   **autoKeyMigration**: Migrates encryption context keys to [[encryption|Key Management Framework]] \(KMF\) cryptographic module keys.
-   **autoDataMigration**: Migrates data that you already encrypted to use the KMF cryptographic module key.

You can modify when these scheduled jobs run, and can pause or restart them at any time.

Verify that the encrypted field configurations are using your newly migrated module keys by navigating to **System Security** &gt; **[[field-encryption|Field Encryption]]** &gt; **Encrypted Field Configurations**. Look for the following items:

-   The **Method** field is **Single Module**.
-   The **Crypto module** field is populated with the name of the cryptographic module that the system automatically creates. You can review that module and the module access policy, both of which are active and published.

## Column Level Encryption and system clones

If Column Level Encryption is installed on your instance, a new field encryption module encryption key is automatically generated on the target clone instance as a part of clone process. These keys are generated for all modules to which the user has access, and that does not have a key already.

Because of this, field encryption modules on the target clone instance may have two module encryption keys present:

-   An active module encryption key. This is the new key generated after clone, as long as the module is accessible to the user and has no prior keys.
-   A deactivated encryption module key \(from the automated key exchange transfer

    The active module encryption key is used to encrypt inserted data as needed on the target clone instance. The deactivated module is used to decrypt existing data that was cloned over as part of the system clone.

    To use a single key to decrypt and encrypt all data, you can run a module rekeying job. For more information about module rekeying jobs, see [[schedule-mass-jobs|Schedule mass encryption, decryption, and rekeying jobs]].


**Parent Topic:**[[configuring-column-level-encryption-2|Configuring Column Level Encryption]]

## Related

- [[schedule-mass-jobs|Schedule mass encryption, decryption, and rekeying jobs]]
- [[configuring-column-level-encryption-2|Configuring Column Level Encryption]]
- [[encryption-landing|Encryption]]
- [[column-level-encryption-landing|Column Level Encryption]]
- [[c_HighSecuritySettings|High Security Settings]]
- [[encryption|Key Management Framework]]
- [[field-encryption|Field Encryption]]
