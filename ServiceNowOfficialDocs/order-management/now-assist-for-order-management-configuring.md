---
title: Configuring Now Assist for Order Management
description: If you have the admin role, you can configure the Now Assist for Order Management application so that your agents can use the generative AI skills in the CSM/FSM Configurable Workspace and Business Portal.
locale: en-US
canonical_url: https://www.servicenow.com/docs/r/order-management/now-assist-for-order-management-configuring.html
release: australia
topic_type: concept
last_updated: "2026-01-13"
reading_time_minutes: 3
keywords: [Now Assist, AI Agents, generative AI, agentic AI]
breadcrumb: [Now Assist for Order Management, Sales Customer Relationship Management]
---

# Configuring Now Assist for Order Management

If you have the admin role, you can configure the [[now-assist-order-management|Now Assist for Order Management]] application so that your agents can use the generative AI skills in the CSM/FSM Configurable Workspace and Business Portal.

Installing the Now Assist for Order Management application installs the following AI applications and skills on your ServiceNow instance:

-   Manage [[order-operations-landing|Order Operations]] \(com.sn\_ord\_ops\_aias\)
-   Manage Invoice Operations \(com.sn\_inv\_ops\_aias\)
-   Summarization for [[explore-order-management|Order Management]]

Request the Now Assist for Order Management application from the [ServiceNow Store](https://store.servicenow.com/sn_appstore_store.do#!/store/application/b75a55a63f71b6108428dd8d001f8bca) and install it using the Application Manager. For more information, see [Install a ServiceNow Store application](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/platform-administration/t_InstallApplications.md).

## Configuring order summarization skill

The Now Assist skills for Sales CRM:

-   Order summarization for order capture
-   Order summarization for [[reviewing-orchestration-plans-order-fulfillment|order fulfillment]]

For information on customizing the order summarization skill, see [[customize-order-summarization-skill-now-assist-order-management|Customize an order summarization skill in Now Assist for Order Management]].

**Note:** Microsoft Azure, Amazon bedrock, Now LLM, Now LLM LTS, and Google Cloud vertex AI are currently the providers for this Now Assist application's skills.

## Configuring the Manage Order Operations application

Business-to-business \(B2B\) customers can submit order cases using Now Assist Virtual Assistant from the Business Portal. Interaction channels include chat and voice options. Before you can use the AI agents for managing order operations from the Business Portal:

-   [[enable-manage-order-operations-ai-agent|Enable the manage order operations agent on the Business Portal]]
-   [[create-atp-api-call|Configure scripted extension points for the manage order operations agent]]
-   [[order-case-email-notifications|Email notifications for order cases]]

Enable AI voice agent support on your phone channels by installing the Now Assist Voice \[sn\_voice\_aia\] plugin. For more information, see [Deploy AI voice agents](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/intelligent-experiences/deploy-ai-agents-for-voice.md).

Configure Chat Summarization to enable the AI summarization and recommendation features in Active Chat. For more information, see [Configure chat summarization](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/customer-service-management/configure-chat-summarization-in-now-assist_0.md).

## Configuring the Manage Invoice Operations application

Business-to-business \(B2B\) customers can submit invoice cases using Now Assist Virtual Assistant from the Business Portal. Interaction channels include chat and voice options. Billing specialists and agents can use the invoice dispute assist agentic workflow from the CSM/FSM Configurable Workspace to resolve invoice cases. Before you can use the AI agents for managing order operations agent in the Business Portal:

-   [[enable-manage-invoice-operations-ai-agent|Configure AI-assisted invoice dispute intake on the Business Portal]]
-   [[configure-invoice-quantity-check-ep|Configure the invoice quantity validation extension point]]
-   [[configure-invoice-case-resolution-ep|Configure the invoice dispute resolution extension point]]
-   [[enable-invoice-dispute-assist-agentic-workflow|Make the invoice dispute assist workflow available in the Now Assist panel]]

Enable AI voice agent support on your phone channels by installing the Now Assist Voice \[sn\_voice\_aia\] plugin. For more information, see [Deploy AI voice agents](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/intelligent-experiences/deploy-ai-agents-for-voice.md).

Configure Chat Summarization to enable the AI summarization and recommendation features in Active Chat. For more information, see [Configure chat summarization](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/customer-service-management/configure-chat-summarization-in-now-assist_0.md).

**Related topics**  


[Overview tab in Now Assist Admin](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/intelligent-experiences/configuring-now-assist.md)

[Configuring Now Assist Admin features](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/intelligent-experiences/configuring-na-landing.md)

[[now-assist-order-management-using|Using Now Assist for Order Management]]

## Related

- [[customize-order-summarization-skill-now-assist-order-management|Customize an order summarization skill in Now Assist for Order Management]]
- [[enable-manage-order-operations-ai-agent|Enable the manage order operations agent on the Business Portal]]
- [[create-atp-api-call|Configure scripted extension points for the manage order operations agent]]
- [[order-case-email-notifications|Email notifications for order cases]]
- [[enable-manage-invoice-operations-ai-agent|Configure AI-assisted invoice dispute intake on the Business Portal]]
- [[configure-invoice-quantity-check-ep|Configure the invoice quantity validation extension point]]
- [[configure-invoice-case-resolution-ep|Configure the invoice dispute resolution extension point]]
- [[enable-invoice-dispute-assist-agentic-workflow|Make the invoice dispute assist workflow available in the Now Assist panel]]
- [[now-assist-order-management-using|Using Now Assist for Order Management]]
- [[now-assist-order-management|Now Assist for Order Management]]
- [[order-operations-landing|Order operations]]
- [[explore-order-management|Order management]]
- [[reviewing-orchestration-plans-order-fulfillment|Order fulfillment]]
