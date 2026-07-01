---
title: Feature configuration for Engagement Messenger
description: Configure the features of Engagement Messenger so that you can change the default settings to suit your customer needs.
locale: en-US
canonical_url: https://www.servicenow.com/docs/r/customer-service-management/customer-self-service-and-omnichannel-engagement/configure-features-of-engagement-messenger.html
release: australia
product: Customer Self-service and Omnichannel Engagement
classification: customer-self-service-and-omnichannel-engagement
topic_type: task
last_updated: "2026-03-12"
reading_time_minutes: 3
breadcrumb: [Engagement Messenger, Set up self-service, Configure, Customer Service Management]
tags:
  - customer-service-management
  - self-service
  - omnichannel
  - portal
  - engagement
  - type-task
---

# Feature configuration for Engagement Messenger

Configure the [[features-of-engagement-messenger|features of Engagement Messenger]] so that you can change the default settings to suit your customer needs.

## Before you begin

Role required: sn\_csm\_ec.ec\_admin

You must [[create-engagement-messenger-module|configure Engagement Messenger]] before configuring its features. For more information, see [Configure Engagement Messenger](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/customer-service-management/customer-self-service-and-omnichannel-engagement/create-engagement-messenger-module.md).

## About this task

Configure how the features of Engagement Messenger appear to your customers, their display arrangement, and their behavior.

Use the Features section of the guided configuration to customize the messenger configuration. View a live preview of how the Engagement Messenger would look like in your third-party website. You can also watch the [academy video](https://www.youtube.com/watch?v=uViv-3bcg3k&list=PLkGSnjw5y2U79gjQuQW-2GBqzEccwFkWH&index=20) to understand the overall functionality of Engagement Messenger.

## Procedure

1.  Navigate to **All** &gt; **Engagement Messenger** &gt; **Modules**.

2.  In the Edit module column of the messenger module that you want to configure, select **Edit**.

    The guided configuration view is displayed.

3.  From the Features section of the guided configuration, enable or disable a feature by using the toggle \(\[Omitted image "toggle-icon.png"\] Alt text: Toggle icon.\) on the feature card.

4.  Open one of the following features and modify the values:

    -   Greeting: See [[greeting-feature-configuration-fields|Greeting feature configuration]].
    -   Knowledge: See [[knowledge-feature-configuration-fields|Knowledge feature configuration]].
    -   Search: See [[search-feature-configuration-fields|Search feature configuration]].
    -   Case: See [[case-management-feature-configuration-fields|Case management feature configuration]].
    -   Catalog: See [[catalog-feature-configuration|Catalog feature configuration]].
    -   Field service: See [[field-service-feature-configuration|Field service feature configuration]].
    -   Walk-up: See [[walk-up-feature-configuration|Walk-up feature configuration]].
    -   Chat with an agent: See [[agent-chat-feature-configuration-fields|Chat feature configuration form fields]].

        **Note:**

        -   The knowledge article, catalog item, and case links sent by an agent can be opened within Engagement Messenger. You can configure how links should be open in a messenger. For more information, see [Create a smart link preference](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/conversational-interfaces/create-smart-link-preference.md).
        -   You can also enable the Now Assist in Virtual Agent in Engagement Messenger by [Configuring assistants overview](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/conversational-interfaces/configure-now-assist-va.md) and then [Display your assistant](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/conversational-interfaces/display-assistant-portal-channel.md) in Engagement Messenger.
    -   Configurable Cards: See [[configurable-card|Configurable Cards feature configuration]].
    -   Callback: See [[em-callback|Callback feature configuration form]].
5.  You can also add a feature in the **Features** section using Configurable Cards.

    1.  Select **Add custom feature**.

    2.  Enter the feature name and select the feature type.

    3.  Select **Add**.

    For more information, see [Configurable Cards feature configuration](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/customer-service-management/configurable-card.md).

6.  Select **Update**.

7.  Change the display order of the features by reordering the feature cards.

    You can see the modified home page layout of your Engagement Messenger in the live preview of the module.

    \[Omitted image "em-config-feature.gif"\] Alt text: View of the Configure Engagement Messenger form with a list of features like Greeting, Search, Knowledge and so on that can be used for configuration.

    **Note:** Engagement Messenger extends service portal capabilities that don't support domain separation. For more information, see \([Domain separation and Service Portal](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/platform-user-interface/domain-separation-service-portal.md)\). However, other tables that are used in Engagement Messenger may support domain separation according to the configurations with which they're created.


## What to do next

[Create an identity provider \(IdP\) for Engagement Messenger](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/customer-service-management/customer-self-service-and-omnichannel-engagement/create-identity-providers-for-engagement-messenger.md)

## Related

- [[greeting-feature-configuration-fields|Greeting feature configuration]]
- [[knowledge-feature-configuration-fields|Knowledge feature configuration]]
- [[search-feature-configuration-fields|Search feature configuration]]
- [[case-management-feature-configuration-fields|Case management feature configuration]]
- [[catalog-feature-configuration|Catalog feature configuration]]
- [[field-service-feature-configuration|Field service feature configuration]]
- [[walk-up-feature-configuration|Walk-up feature configuration]]
- [[agent-chat-feature-configuration-fields|Chat feature configuration form fields]]
- [[configurable-card|Configurable Cards feature configuration]]
- [[em-callback|Callback feature configuration form]]
- [[features-of-engagement-messenger|Features of Engagement Messenger]]
- [[create-engagement-messenger-module|Configure Engagement Messenger]]
