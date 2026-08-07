---
title: Chat surveys
description: Display conversational questionnaires to your end users to gather important information from them, before and after they chat with a live or virtual agent.
locale: en-US
canonical_url: https://www.servicenow.com/docs/r/conversational-interfaces/agent-chat/ci-conversational-chat-surveys.html
release: australia
product: Agent Chat
classification: agent-chat
topic_type: concept
last_updated: "2026-03-12"
reading_time_minutes: 3
breadcrumb: [Explore, Agent Chat, Conversational Interfaces]
tags:
  - conversational-interfaces
  - agent-chat
  - live-chat
  - messaging
  - support
  - type-concept
---

# Chat surveys

Display conversational questionnaires to your end users to gather important information from them, before and after they chat with a live or [[virtual-agent-landing-page|virtual agent]].

## How chat surveys work

Instead of using forms to collect information from your requesters, you can create different questionnaires that run in the chat client to capture preliminary user information or post-chat feedback. The questions in the following pre-chat survey example ask users to identify their service issue and to provide additional details.

\[Omitted image "pre-chat-survey-example.png"\] Alt text: Web chat client with pre-chat surveys highlighted.

Survey administrators and administrators use [Survey Designer](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/servicenow-platform/c_SurveyDesigner.md) to:

-   Build survey content: Survey Designer provides various controls for defining survey questions. The example above shows the choice list control, which displays a list of items that your users can choose from. Each survey question has corresponding properties that you can set to manage survey behavior. For instance, you can make a survey response mandatory. If you make a survey response optional, users can skip the question in the survey. You can also configure your survey so that an introductory note starts the survey and an end note displays after users finish the survey.
-   \(Optional\) Save certain survey responses as chat context: When defining your survey, you can map a particular survey question to a chat context variable so that survey responses are stored in the context variable. You can then use these variables to route chats to live agents in certain queues, by specifying the chat context variables in routing conditions or to the virtual agent.

After creating the surveys, administrators configure the surveys to run as conversations in the chat client. The chat client renders the chat survey as a live chat conversation.

## Activating and deactivating pre-chat surveys in Now Assist

By default, you can manage pre-chat surveys by navigating to **All** &gt; **[[convint-landing-page|Conversational interfaces]]** &gt; **Settings** and and opening **Pre-chat surveys** in the **General** tab. Now Assist honors these settings in both Virtual Agent and Self-service.

You can also turn pre-chat surveys on and off specifically for Now Assist Self Service. Navigate to **All** &gt; **sys\_properties.list**, and under **com.glide.cs.nass.prechat.enabled** set the value to `True` or `False`.

## What to do next

Setting up chat surveys involves these main steps:

\[Omitted image "survey-implementation-steps.png"\] Alt text: Infographic describing steps for setting up pre-chat and post-chat conversational surveys.

-   **[[ac-configure-context-variables|1. \(Optional\) Define chat context.]]**

    Configure the chat context variables for storing survey responses using **Context Variables** in Chat Settings.

-   **[[create-chat-surveys|2. Create chat surveys]]**

    In Survey Designer, build your conversational questionnaires for gathering pre-chat information and post-chat feedback from your requesters. If you defined chat context variables to store certain survey responses, you can map the appropriate survey question to the corresponding chat context variable.

-   **[[ac-configure-pre-chat-surveys|3. Define pre-chat survey configurations.]]**

    Determine the pre-chat questionnaire to be presented to your requesters based on conditions that you apply.

-   **[[define-post-chat-survey-config|4. Define post-chat survey configurations.]]**

    Control the post-chat questionnaire displayed to your requesters to gather feedback on their experience with live agents.

-   **[[ac-configure-context-topic-intent|5. If using Virtual Agent, define context topic intent configurations.]]**

    Use pre-chat survey information to determine the appropriate Virtual Agent conversation topic automatically displayed to your requesters, rather than prompting them to choose from a list of conversation topics.


The Interaction Related Records list stores the post-survey chat results and creates a related record that links the assessment to the live agent \(fulfiller\).

## Related

- [[ac-configure-context-variables|Configure context variables for storing chat-related information]]
- [[create-chat-surveys|Create chat surveys]]
- [[ac-configure-pre-chat-surveys|Define pre-chat survey configurations]]
- [[define-post-chat-survey-config|Define post-chat survey configurations]]
- [[ac-configure-context-topic-intent|Define topic context intent configurations]]
- [[virtual-agent-landing-page|Virtual Agent]]
- [[convint-landing-page|Conversational Interfaces]]
