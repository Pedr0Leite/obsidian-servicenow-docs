---
title: Prevent users from attaching unencrypted files
description: Modify the com.glide.encryption.enable\_attachment\_key\_ui property to prevent your users with access to an encryption module key from attaching unencrypted attachments.
locale: en-US
canonical_url: https://www.servicenow.com/docs/r/platform-security/attach-enc-property.html
release: australia
topic_type: task
last_updated: "2026-03-12"
reading_time_minutes: 1
breadcrumb: [Configuring Field Encryption, Field Encryption, Encryption]
tags:
  - platform-security
  - type-task
---

# Prevent users from attaching unencrypted files

Modify the com.glide.[[encryption-landing|encryption]].enable\_attachment\_key\_ui property to prevent your [[users|users]] with access to an encryption module key from attaching unencrypted attachments.

## Before you begin

Role required: security\_admin

You must elevate to the [[security-admin-role|security\_admin role]] performing these steps. For instructions, see [[t_ElevateToAPrivilegedRole|Elevate to a privileged role]]

By default, users who have access to an encryption module key are able to upload unencrypted attachments. Use the **com.glide.encryption.enable\_attachment\_key\_ui** system property to change this behavior.

When attaching, your users see a UI picker on records that have a multi-module encrypted field [[sc-configuration|configuration]]. When this property is set to false, users no longer see an option not to encrypt an attachment.

## Procedure

1.  Navigate to **All** &gt; **[[ca-system-properties|System Properties]]** &gt; **All Properties**.

2.  In the system properties list, find and open the system property.

3.  Set the **value** of the property to `false`.


**Parent Topic:**[[configuring-column-level-encryption|Configuring Field Encryption]]

**Parent Topic:**[[configuring-column-level-encryption-2|Configuring Column Level Encryption]]

## Related

- [[t_ElevateToAPrivilegedRole|Elevate to a privileged role]]
- [[configuring-column-level-encryption|Configuring Field Encryption]]
- [[configuring-column-level-encryption-2|Configuring Column Level Encryption]]
- [[encryption-landing|Encryption]]
- [[users|Users]]
- [[security-admin-role|Security\_admin role]]
- [[sc-configuration|Configuration]]
- [[ca-system-properties|System properties]]
