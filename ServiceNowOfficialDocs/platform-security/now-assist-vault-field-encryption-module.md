---
title: Field encryption with Vault module agentic workflow
description: Use the field encryption with Vault module agentic workflow to encrypt specific fields and configure secure access to users with designated roles.
locale: en-US
canonical_url: https://www.servicenow.com/docs/r/platform-security/now-assist-vault-field-encryption-module.html
release: australia
topic_type: concept
last_updated: "2026-03-23"
reading_time_minutes: 1
keywords: [Now Assist, agentic AI]
breadcrumb: [Use agentic AI, ServiceNow Vault]
tags:
  - platform-security
  - type-concept
---

# Field encryption with Vault module agentic workflow

Use the field encryption with Vault module agentic workflow to encrypt specific fields and configure secure access to [[users|users]] with designated roles.

## Field encryption with Vault module agentic workflow overview

Add [[field-encryption|field encryption]] protection and improve your security posture with the field encryption with Vault module agentic workflow.

When you [[configuring-now-assist-vault|install Now Assist for Vault]], this agentic workflow is turned on by default.

To modify the agentic workflow, [duplicate it](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/intelligent-experiences/clone-aia-usecase.md), and adjust the settings according to your requirements.

## Use the field encryption with Vault module

Encrypt specific fields and configure user access. The workflow requires that you have the following roles and elevate to them:

-   sn\_vault\_console.vault\_console\_admin
-   security\_admin
-   sn\_kmf.admin
-   sn\_kmf.cryptographic\_manager

To access and configure the agentic workflow:

1.  Navigate to **All** &gt; **AI Agent Studio** &gt; **Create and manage**.
2.  Select **Field Encryption with Vault module**.

**Note:** The field encryption with Vault module agentic workflow is triggered automatically when you secure custom applications using [[vault-dashboard|ServiceNow Vault console dashboard]]. You can also invoke the agentic workflow manually in the Now Assist panel.

## AI agents used in the field encryption with Vault module agentic workflow

|Name|Description|
|----|-----------|
|Vault crypto module manager agent|Uses various tools to encrypt fields and ensures that only those users with particular roles have access to those fields.|

There might be AI agents installed with the Now Assist application that are not used in agentic workflows. To learn how to see all agents that are available to you, see [Find AI agents](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/intelligent-experiences/find-ai-agents.md).

**Parent Topic:**[[use-now-assist-vault-agentic-ai|Use agentic AI in Now Assist for Vault]]

## Related

- [[use-now-assist-vault-agentic-ai|Use agentic AI in Now Assist for Vault]]
- [[users|Users]]
- [[field-encryption|Field Encryption]]
- [[configuring-now-assist-vault|Install Now Assist for Vault]]
- [[vault-dashboard|ServiceNow Vault console dashboard]]
