---
title: Configure and upload your customer supplied key
description: You can use your own customer-supplied key instead of using the ServiceNow system-generated keys.
locale: en-US
canonical_url: https://www.servicenow.com/docs/r/platform-security/upload-customer-supplied-key.html
release: australia
topic_type: task
last_updated: "2026-03-12"
reading_time_minutes: 1
breadcrumb: [Using customer-supplied keys with Field Encryption Enterprise, Using Field Encryption, Field Encryption, Encryption]
tags:
  - platform-security
  - type-task
---

# Configure and upload your customer supplied key

You can use your own customer-supplied key instead of using the ServiceNow® system-generated keys.

## Before you begin

Role required: security\_admin  and sn\_kmf.cryptographic\_manager  or sn\_kmf.admin

If you’re NOT supplying your own keys, you don’t need to perform this procedure. To [[create-cryptographic-module|create a cryptographic module]] with ServiceNow® keys, go to [Create a cryptographic module](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/platform-security/platform-encryption/create-cryptographic-module.md) or [[create-PE-cryptographic-module|Create cryptographic module for Field Encryption]].

**Note:** This procedure only applies to [[now-platform-encryption|Field Encryption Enterprise]] functionality. See [[activate-platform-encryption|Activate Field Encryption]] for more information.

**Important:** You can’t revoke a customer supplied key.

## Procedure

1.  Navigate to **All** &gt; **System Security** &gt; **[[field-encryption|Field Encryption]]** &gt; **Field Encryption Experience**.

2.  Select **View module details** on the Field Encryption module.

3.  Select **[[encryption-landing|Encryption]] Keys** and **Select and Continue** for the **Bring-your-own Key** option.

4.  Select **Download wrapping key** and **Next**.

5.  Follow the required online steps and select the **I completed the online steps** box followed by **Done and continue to the next step**.

6.  Upload the wrapped encryption key and the import token downloaded with the wrapped key, enter a name for the encryption key, and select **Complete provisioning**.


## What to do next

Now that you have finished configuring your cryptographic module with your customer-supplied key, move on to [Create a module access policy](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/platform-security/platform-encryption/create-module-access-policy.md)

**Parent Topic:**[[csk-landing|Using customer-supplied keys with Field Encryption Enterprise]]

**Parent Topic:**[[csk-landing-2|Using customer supplied keys with Column Level Encryption Enterprise]]

## Related

- [[create-PE-cryptographic-module|Create cryptographic module for Field Encryption]]
- [[activate-platform-encryption|Activate Field Encryption]]
- [[csk-landing|Using customer-supplied keys with Field Encryption Enterprise]]
- [[csk-landing-2|Using customer supplied keys with Column Level Encryption Enterprise]]
- [[create-cryptographic-module|Create a cryptographic module]]
- [[now-platform-encryption|Field Encryption Enterprise]]
- [[field-encryption|Field Encryption]]
- [[encryption-landing|Encryption]]
