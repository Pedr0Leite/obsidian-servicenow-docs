---
title: Access Observer configuration agentic workflow
description: Use the Access Observer configuration agentic workflow to view, create, deactivate, and delete Access Observer settings for a particular field.
locale: en-US
canonical_url: https://www.servicenow.com/docs/r/platform-security/now-assist-vault-access-observer-config.html
release: australia
topic_type: concept
last_updated: "2026-03-23"
reading_time_minutes: 1
keywords: [Now Assist, agentic AI]
breadcrumb: [Use agentic AI, ServiceNow Vault]
---

# Access Observer configuration agentic workflow

Use the Access Observer configuration agentic workflow to view, create, deactivate, and delete [[access-observer|Access Observer]] settings for a particular field.

## Access Observer configuration agentic workflow overview

Access Observer helps you monitor the people and processes that access data on your instance. Use the Access Observer configuration agentic workflow to modify Access Observer settings to track access across your enterprise.

When you [[configuring-now-assist-vault|install Now Assist for Vault]], this agentic workflow is turned on by default.

To modify the agentic workflow, [duplicate it](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/intelligent-experiences/clone-aia-usecase.md), and adjust the settings according to your requirements.

## Configure Access Observer

Configure Access Observer settings to track data access. The workflow requires that you have the following roles and elevate to them:

-   sn\_vault\_console.vault\_console\_admin
-   security\_admin

To access and configure the agentic workflow:

1.  Navigate to **All** &gt; **AI Agent Studio** &gt; **Create and manage**.
2.  Select **Access Observer [[sc-configuration|configuration]]**.

**Note:** The Access Observer configuration agentic workflow is triggered automatically when you secure custom applications using [[vault-dashboard|ServiceNow Vault console dashboard]]. You can also invoke the agentic workflow manually in the Now Assist panel.

## AI agents used in the Access Observer configuration agentic workflow

|Name|Description|
|----|-----------|
|Access Observer configuration manager agent|Uses various tools to view, create, deactivate, and delete Access Observer settings for a particular field.|

There might be AI agents installed with the Now Assist application that are not used in agentic workflows. To learn how to see all agents that are available to you, see [Find AI agents](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/intelligent-experiences/find-ai-agents.md).

**Parent Topic:**[[use-now-assist-vault-agentic-ai|Use agentic AI in Now Assist for Vault]]

## Related

- [[use-now-assist-vault-agentic-ai|Use agentic AI in Now Assist for Vault]]
- [[access-observer|Access observer]]
- [[configuring-now-assist-vault|Install Now Assist for Vault]]
- [[sc-configuration|Configuration]]
- [[vault-dashboard|ServiceNow Vault console dashboard]]
