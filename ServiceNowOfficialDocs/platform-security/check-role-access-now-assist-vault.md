---
title: Check role access for an encrypted column with Now Assist for Vault
description: Use the check role access for encrypted column skill to identify user roles that have access to encryption and decryption keys in your instance.
locale: en-US
canonical_url: https://www.servicenow.com/docs/r/platform-security/check-role-access-now-assist-vault.html
release: australia
topic_type: task
last_updated: "2026-03-12"
reading_time_minutes: 1
breadcrumb: [Use generative AI skills, ServiceNow Vault]
tags:
  - platform-security
  - type-task
---

# Check role access for an encrypted column with Now Assist for Vault

Use the check role access for encrypted column skill to identify user roles that have access to [[encryption-landing|encryption]] and decryption keys in your instance.

## Before you begin

-   [[install-vault|Install ServiceNow Vault]]. For more information, see [[configuring-servicenow-vault|Configuring ServiceNow Vault]].
-   Ensure that the check role access for encrypted column skill is active. For more information, see [Activate a Now Assist skill](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/intelligent-experiences/configure-a-now-assist-skill.md).

Role required: sn\_vault\_console.vault\_console\_admin

## Procedure

1.  Navigate to **All** &gt; **Vault** &gt; **Vault console**.

2.  In the Ask Now Assist panel, select **Check role access for encrypted column** and specify the details.

    Example prompt: `Which roles have decryption key access to an encrypted column? Access includes read access.`


**Parent Topic:**[[using-now-assist-vault|Use generative AI skills in Now Assist for Vault]]

## Related

- [[configuring-servicenow-vault|Configuring ServiceNow Vault]]
- [[using-now-assist-vault|Use generative AI skills in Now Assist for Vault]]
- [[encryption-landing|Encryption]]
- [[install-vault|Install ServiceNow Vault]]
