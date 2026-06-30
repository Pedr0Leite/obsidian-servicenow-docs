---
title: Test an external key definition
description: Test your external encryption key to use in External Key Management Service \(EKMS\).
locale: en-US
canonical_url: https://www.servicenow.com/docs/r/platform-security/ekms-test-external-key-definition.html
release: australia
topic_type: task
last_updated: "2026-03-12"
reading_time_minutes: 1
breadcrumb: [Configuring External Key Management Service, External Key Management Service, Field Encryption, Encryption]
---

# Test an external key definition

Test your external [[encryption-landing|encryption]] key to use in [[ekms-external-key-management|External Key Management Service]] \(EKMS\).

## Before you begin

Roles required: admin, security\_admin, and sn\_kmf.cryptographic\_manager

To test an external key definition, there must be one configured in EKMS. See [[ekms-configure-external-key-definition|Configure an external key definition]].

## Procedure

1.  Navigate to **All** &gt; **System Security** &gt; **[[field-encryption|Field Encryption]]** &gt; **EKMS Configurations**.

2.  Select the EKMS integration.

3.  Select **Test EKMS Config**.


## Result

The following validation message displays when the external key is properly configured in EKMS: Validation passed for the [[sc-configuration|configuration]]. You have successfully wrapped and unwrapped the test key in EKMS.

If the test fails, the validation message shows as failed indicating the operation that was unsuccessful. Go back through the configuration process to correct the issue and run the test again. See [Configure an external key definition](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/platform-security/ekms-configure-external-key-definition.md).

**Parent Topic:**[[ekms-configuring-external-key-management|Configuring External Key Management Service]]

**Related topics**  


[[ekms-create-crypto-module|Create a cryptographic module with external key wrapping]]

[[ekms-create-encrypted-field-config|Create Encrypted Field Configurations]]

[[ekms-set-up-maps|Set up Module Access Policies]]

## Related

- [[ekms-configure-external-key-definition|Configure an external key definition]]
- [[ekms-configuring-external-key-management|Configuring External Key Management Service]]
- [[ekms-create-crypto-module|Create a cryptographic module with external key wrapping]]
- [[ekms-create-encrypted-field-config|Create Encrypted Field Configurations]]
- [[ekms-set-up-maps|Set up Module Access Policies]]
- [[encryption-landing|Encryption]]
- [[ekms-external-key-management|External Key Management Service]]
- [[field-encryption|Field Encryption]]
- [[sc-configuration|Configuration]]
