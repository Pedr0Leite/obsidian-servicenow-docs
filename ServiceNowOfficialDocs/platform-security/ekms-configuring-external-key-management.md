---
title: Configuring External Key Management Service
description: Set up External Key Management Service \(EKMS\) to control the encryption of your ServiceNow data using your Amazon Web Service Key Management System \(AWS KMS\).
locale: en-US
canonical_url: https://www.servicenow.com/docs/r/platform-security/ekms-configuring-external-key-management.html
release: australia
topic_type: concept
last_updated: "2026-03-12"
reading_time_minutes: 2
breadcrumb: [External Key Management Service, Field Encryption, Encryption]
tags:
  - platform-security
  - type-concept
---

# Configuring External Key Management Service

Set up External Key Management Service \(EKMS\) to control the [[encryption-landing|encryption]] of your ServiceNow data using your Amazon Web Service Key Management System \(AWS KMS\).

## Configuration Overview

Configuring External Key Management Service \(EKMS\) involves installing the plugin, connecting to AWS KMS, and setting up encryption for specific fields. Complete these tasks to establish external key management for your ServiceNow data.

## Configuration Workflow

1.  Activate the EKMS plugin and assign required user roles
2.  Configure the AWS KMS key definition with connection credentials
3.  Create cryptographic modules that use external key wrapping
4.  Specify which table fields should be encrypted
5.  Set up access [[ca-policies|policies]] to control data visibility
6.  Test encryption and [[sc-access-control|access control]] to verify the [[sc-configuration|configuration]]

## Prerequisites

Before configuring EKMS, verify that you have:

-   AWS KMS access through your organization's [[c_requestAPI|request]] process
-   Created or identified an AWS KMS key
-   [[identity-landing|Identity]] and [[access-management-landing|Access Management]] \(IAM\) user credentials with KMS permissions
-   IAM user configured with at least these permissions: kms:DescribeKey, kms:Encrypt, and kms:Decrypt
-   admin, security\_admin, and sn\_kmf.cryptographic\_manager roles in ServiceNow

-   **[[ekms-activate-external-key-management|Activate External Key Management Service]]**  
Install the External Key Management Service \(EKMS\) plugin and configure user permissions to enable external key management functionality.
-   **[[ekms-configure-external-key-definition|Configure an external key definition]]**  
Configure your external encryption key to use in External Key Management Service \(EKMS\).
-   **[[ekms-create-crypto-module|Create a cryptographic module with external key wrapping]]**  
[[create-cryptographic-module|Create a cryptographic module]] that uses external Amazon Web Services Key Management System \(AWS KMS\) key wrapping to encrypt ServiceNow data.
-   **[[ekms-create-encrypted-field-config|Create Encrypted Field Configurations]]**  
Configure specific fields to be encrypted using your External Key Management Service \(EKMS\) cryptographic module with external Amazon Web Services Key Management System \(AWS KMS\) key wrapping.
-   **[[ekms-set-up-maps|Set up Module Access Policies]]**  
Configure module access policies in External Key Management Service \(EKMS\) to control who can view encrypted data in clear text.
-   **[[ekms-test-external-key-definition|Test an external key definition]]**  
Test your external encryption key to use in External Key Management Service \(EKMS\).

**Parent Topic:**[[ekms-external-key-management|External Key Management Service]]

**Related topics**  


[External Key Management Service](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/platform-security/ekms-external-key-management.md)

[Activate External Key Management Service](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/platform-security/ekms-activate-external-key-management.md)

[Configure an external key definition](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/platform-security/ekms-configure-external-key-definition.md)

[Create a cryptographic module with external key wrapping](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/platform-security/ekms-create-crypto-module.md)

[Create Encrypted Field Configurations](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/platform-security/ekms-create-encrypted-field-config.md)

## Related

- [[ekms-activate-external-key-management|Activate External Key Management Service]]
- [[ekms-configure-external-key-definition|Configure an external key definition]]
- [[ekms-create-crypto-module|Create a cryptographic module with external key wrapping]]
- [[ekms-create-encrypted-field-config|Create Encrypted Field Configurations]]
- [[ekms-set-up-maps|Set up Module Access Policies]]
- [[ekms-test-external-key-definition|Test an external key definition]]
- [[ekms-external-key-management|External Key Management Service]]
- [[encryption-landing|Encryption]]
- [[ca-policies|Policies]]
- [[sc-access-control|Access control]]
- [[sc-configuration|Configuration]]
- [[c_requestAPI|request]]
- [[identity-landing|Identity]]
- [[access-management-landing|Access Management]]
- [[create-cryptographic-module|Create a cryptographic module]]
