---
title: Use agentic AI in Now Assist for Vault
description: Use the Now Assist for Vault agentic workflows to complete tasks autonomously.
locale: en-US
canonical_url: https://www.servicenow.com/docs/r/platform-security/use-now-assist-vault-agentic-ai.html
release: australia
topic_type: concept
last_updated: "2026-03-23"
reading_time_minutes: 2
keywords: [AI Agents, Agentic AI]
breadcrumb: [ServiceNow Vault]
tags:
  - platform-security
  - type-concept
---

# Use agentic AI in Now Assist for Vault

Use the [[now-assist-vault-landing|Now Assist for Vault]] agentic workflows to complete tasks autonomously.

**Note:** Depending on your license, you will have access to certain application features, generative AI skills, agentic workflows, and AI agents. For more information, see [ServiceNow product tiers](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/intelligent-experiences/ai-native-sku-overview.md).

|Agentic workflow name|Description|Available AI agents|
|---------------------|-----------|-------------------|
|Securing custom apps with Vault agents|Proposes data classifications and available protections for a custom application.|Custom app recommendations|
|Access observer configuration|Views, creates, deactivates, and deletes [[access-observer|Access Observer]] settings for a particular field.|Access observer [[sc-configuration|configuration]] manager|
|Summarize access observer logs|Reviews and summarizes access [[logs|logs]] for a specific field, identifying access sources, [[users|users]], and their roles.|Access observer log analyzer|
|Field [[encryption-landing|encryption]] with Vault module|Encrypts specific fields and configure secure access to users with designated roles.|Vault crypto module manager|

**Important:** Some Now Assist skills, agents, and agentic workflows are turned on by default. For more information, see [Now Assist skills, agents, and agentic workflows on by default](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/intelligent-experiences/now-assist-skills-on-by-default.md).

## AI model providers

You can use Now LLM Service, Now LLM Long Term Stable models \(LTS\), Azure OpenAI, Google Gemini or Anthropic Claude on AWS as the AI model provider for all Now Assist skills and AI agents. Use the Configuration Controls in [AI Control Tower](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/intelligent-experiences/ai-model-providers.md) to define which options are available, then set the skill-level preferences in the [Now Assist Admin console](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/intelligent-experiences/manage-large-language-models.md). For more information, see [Large language models on the ServiceNow AI Platform®](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/intelligent-experiences/exploring-large-language-models.md).

## Security

Enable security settings to run AI agents and agentic workflows using [[sc-access-control|access control]] lists \(ACLs\) and user identities. You can configure and manage the ACLs in AI Agent Studio. See [Implement access control in Now Assist AI agents](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/intelligent-experiences/aia-security-implementation.md) for more information.

## Installed agents

There might be AI agents installed with the Now Assist application that are not used in agentic workflows. To learn how to see all agents that are available to you, see [Find AI agents](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/intelligent-experiences/find-ai-agents.md).

-   **[[now-assist-vault-securing-custom-apps-agents|Securing custom apps with the Vault agents agentic workflow]]**  
Use the securing custom apps with Vault agents agentic workflow to get recommended data classifications and available protections for a custom application.
-   **[[now-assist-vault-access-observer-config|Access Observer configuration agentic workflow]]**  
Use the Access Observer configuration agentic workflow to view, create, deactivate, and delete Access Observer settings for a particular field.
-   **[[now-assist-vault-access-observer-logs|Summarize Access Observer logs agentic workflow]]**  
Use the summarize Access Observer logs agentic workflow to review and summarize access logs for a specific field, identifying access sources, users, and their roles.
-   **[[now-assist-vault-field-encryption-module|Field encryption with Vault module agentic workflow]]**  
Use the field encryption with Vault module agentic workflow to encrypt specific fields and configure secure access to users with designated roles.

**Parent Topic:**[[servicenow-vault-landing|ServiceNow Vault]]

## Related

- [[now-assist-vault-securing-custom-apps-agents|Securing custom apps with the Vault agents agentic workflow]]
- [[now-assist-vault-access-observer-config|Access Observer configuration agentic workflow]]
- [[now-assist-vault-access-observer-logs|Summarize Access Observer logs agentic workflow]]
- [[now-assist-vault-field-encryption-module|Field encryption with Vault module agentic workflow]]
- [[servicenow-vault-landing|ServiceNow Vault]]
- [[now-assist-vault-landing|Now Assist for Vault]]
- [[access-observer|Access observer]]
- [[sc-configuration|Configuration]]
- [[logs|Logs]]
- [[users|Users]]
- [[encryption-landing|Encryption]]
- [[sc-access-control|Access control]]
