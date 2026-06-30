---
title: Run mass encryption or decryption
description: You can run mass encryption on encryption configurations, as well as a mass decryption to decrypt previously encrypted values.
locale: en-US
canonical_url: https://www.servicenow.com/docs/r/platform-security/mass-enc-dec.html
release: australia
topic_type: task
last_updated: "2026-03-12"
reading_time_minutes: 1
breadcrumb: [Encrypting fields and attachments, Using Field Encryption, Field Encryption, Encryption]
---

# Run mass encryption or decryption

You can run mass [[encryption-landing|encryption]] on encryption configurations, as well as a mass decryption to decrypt previously encrypted values.

## Before you begin

Role required: security\_admin

## About this task

You can also create scheduled jobs for mass encryption and decryption. See [[schedule-mass-jobs|Schedule mass encryption, decryption, and rekeying jobs]] for instructions.

Mass encryption and decryption are available only when an encrypted field [[sc-configuration|configuration]] uses the single cryptographic module. Mass decryption is available for both the single and multiple encryption method.

**Note:** You should run mass encryption and decryption only during non-peak hours because the operations are resource and time intensive.

## Procedure

1.  Navigate to **All** &gt; **System Security** &gt; **[[field-encryption|Field Encryption]]** &gt; **Encrypted Field Configurations**.

2.  Open the encrypted field configuration for the field you would like to mass encrypt or decrypt.

3.  Under Related Links, select an available option.

    -   **Schedule Mass Decryption job**
    -   **Schedule Mass Encryption job**
4.  Confirm your selection in the dialog.


## Result

If running a mass encryption, all values are encrypted with the encryption module defined in the encrypted field configuration record. If running a mass decryption, only fields encrypted with an encryption module you have access to are decrypted.

**Parent Topic:**[[field-encryption-key-management|Encrypting fields and attachments]]

## Related

- [[schedule-mass-jobs|Schedule mass encryption, decryption, and rekeying jobs]]
- [[field-encryption-key-management|Encrypting fields and attachments]]
- [[encryption-landing|Encryption]]
- [[sc-configuration|Configuration]]
- [[field-encryption|Field Encryption]]
