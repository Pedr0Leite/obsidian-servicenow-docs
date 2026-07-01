---
title: Create a system module access policy
description: Create a module access policy \(MAP\) for a matched user to encrypt attachments when inbound email processing runs as that user.
locale: en-US
canonical_url: https://www.servicenow.com/docs/r/platform-security/fe-create-system-map.html
release: australia
topic_type: task
last_updated: "2026-04-27"
reading_time_minutes: 1
breadcrumb: [Module access policies for inbound email attachment encryption, Encrypting fields and attachments, Using Field Encryption, Field Encryption, Encryption]
---

# Create a system module access policy

[[create-module-access-policy|Create a module access policy]] \(MAP\) for a matched user to encrypt attachments when inbound [[email|email]] processing runs as that user.

## Before you begin

Role required: **security\_admin** and **sn\_kmf.crypto\_manager** \(or **sn\_kmf.admin**\)

## About this task

These instructions create a system-based MAP for the system user's role. See [[maps-for-fe|Configure module access policies for Field Encryption]] for information.

## Procedure

1.  Navigate to **All** &gt; **System Security** &gt; **[[field-encryption|Field Encryption]]** &gt; **Field Encryption Experience**.

2.  Select **Access [[ca-policies|Policies]]** in the tile of the module configured for the target table's [[encryption-landing|encryption]] [[sc-configuration|configuration]].

3.  Select **Create new**.

4.  Enter a name for your MAP in the **Policy name** field.

5.  Select **Role** in the **Type** field.

6.  In the **Target role** field, select the system user's role.

7.  Fill out the rest of the form accordingly.

    \[Omitted image "fe-system-map.png"\] Alt text: System Module Access Policy Example

8.  Select **Save**.


## Result

The system MAP has been created.

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
