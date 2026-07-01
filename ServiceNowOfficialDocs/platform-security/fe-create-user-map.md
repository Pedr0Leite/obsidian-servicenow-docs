---
title: Create a user module access policy
description: Create a module access policy \(MAP\) for a matched user to encrypt attachments when inbound email processing runs as that user.
locale: en-US
canonical_url: https://www.servicenow.com/docs/r/platform-security/fe-create-user-map.html
release: australia
topic_type: task
last_updated: "2026-04-28"
reading_time_minutes: 1
breadcrumb: [Module access policies for inbound email attachment encryption, Encrypting fields and attachments, Using Field Encryption, Field Encryption, Encryption]
tags:
  - platform-security
  - type-task
---

# Create a user module access policy

[[create-module-access-policy|Create a module access policy]] \(MAP\) for a matched user to encrypt attachments when inbound [[email|email]] processing runs as that user.

## Before you begin

Role required: admin

## About this task

These instructions create a role-based MAP for the matched user. A role-based MAP requires impersonation to be enabled so that the user has access to the cryptographic module. Other MAP types, such as script or scope, can also be used to grant the user access to the cryptographic module, but don't include an impersonation option. See [[maps-for-fe|Configure module access policies for Field Encryption]] for information on all available MAP types.

## Procedure

1.  Navigate to **All** &gt; **System Security** &gt; **[[field-encryption|Field Encryption]]** &gt; **Field Encryption Experience**.

2.  Select **Access [[ca-policies|Policies]]** in the tile of the module configured for the target table's [[encryption-landing|encryption]] [[sc-configuration|configuration]].

3.  Select **Create new**.

4.  Enter a name for your MAP in the **Policy name** field.

5.  Select **Role** in the **Type** field.

6.  In the **Target role** field, select the role of the user that the attachment transfer process impersonates.

7.  Select **Impersonation** so that the MAP enables access when that user is impersonated.

8.  Fill out the rest of the form accordingly.

    \[Omitted image "fe-user-map.png"\] Alt text: User Module Access Policy Example

9.  Select **Save**.


## Result

The user MAP has been created.

**Encrypted attachments and missing metadata**

When you encrypt an attachment, the hash and state fields on the sys\_attachment record aren't populated. This is by design.

The hash field stores a SHA-256 fingerprint of an attachment's content. Even though a file is encrypted, a hash is a deterministic and stable identifier. The same file produces an identical hash value. Storing the hash would enable an attacker who has a copy of the file to confirm that it exists in your system and can weaken encryption.

Because of this, duplicate detection doesn't work for encrypted attachments, since ServiceNow uses the hash field to prevent identical attachments from being added to a record.

**Parent Topic:**[[fe-maps-inbound-email-attachment-encryption|Module access policies for inbound email attachment encryption]]

## Related

- [[maps-for-fe|Configure module access policies for Field Encryption]]
- [[fe-maps-inbound-email-attachment-encryption|Module access policies for inbound email attachment encryption]]
- [[create-module-access-policy|Create a module access policy]]
- [[email|Email]]
- [[field-encryption|Field Encryption]]
- [[ca-policies|Policies]]
- [[encryption-landing|Encryption]]
- [[sc-configuration|Configuration]]
