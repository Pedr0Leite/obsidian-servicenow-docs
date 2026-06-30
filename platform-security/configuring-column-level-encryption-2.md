---
title: Configuring Column Level Encryption
description: Learn how to activate and configure Column Level Encryption and manage migration from Encryption Support.
locale: en-US
canonical_url: https://www.servicenow.com/docs/r/platform-security/configuring-column-level-encryption-2.html
release: australia
topic_type: concept
last_updated: "2026-03-12"
reading_time_minutes: 1
breadcrumb: [Column Level Encryption, Encryption]
---

# Configuring Column Level Encryption

Learn how to activate and configure Column Level Encryption and manage migration from [[encryption-landing|Encryption]] Support.

-   **[[activate-platform-encryption-2|Activate Column Level Encryption Enterprise]]**

    Learn how to active either Column Level Encryption or [[now-platform-encryption-2|Column Level Encryption Enterprise]].

-   **Roles Required for Configuring Column Level Encryption**

    Learn about the roles required to configure Column Level Encryption.


## Migration from encryption support

Use Scheduled jobs to migrate your keys and encrypted data from legacy Encryption Support to Column Level Encryption. See details for this process at [[migration-to-platform-encryption-2|Migrating to Column Level Encryption]]

## Change attachment encryption settings

Improve security by preventing [[users|users]] from attaching unencrypted files. For details, see [[attach-enc-property|Prevent users from attaching unencrypted files]].

-   **[Activate Column Level Encryption Enterprise](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/platform-security/activate-platform-encryption-2.md)**  
With subscription to Column Level Encryption Enterprise, an admin can activate the com.glide.now.platform.encryption plugin.
-   **[Migrating to Column Level Encryption](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/platform-security/migration-to-platform-encryption-2.md)**  
Scheduled jobs migrate your keys and encrypted data from Encryption Support to Column Level Encryption.
-   **[Prevent users from attaching unencrypted files](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/platform-security/attach-enc-property.md)**  
Modify the com.glide.encryption.enable\_attachment\_key\_ui property to prevent your users with access to an encryption module key from attaching unencrypted attachments.

**Parent Topic:**[[column-level-encryption-landing|Column Level Encryption]]

## Related

- [[activate-platform-encryption-2|Activate Column Level Encryption Enterprise]]
- [[migration-to-platform-encryption-2|Migrating to Column Level Encryption]]
- [[attach-enc-property|Prevent users from attaching unencrypted files]]
- [[column-level-encryption-landing|Column Level Encryption]]
- [[encryption-landing|Encryption]]
- [[now-platform-encryption-2|Column Level Encryption Enterprise]]
- [[users|Users]]
