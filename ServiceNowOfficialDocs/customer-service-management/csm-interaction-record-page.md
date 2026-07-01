---
title: CSM Interaction record page
description: The CSM Interaction record page provides CSM interaction management features and functionality and enables agents to accept and respond to live chats, calls, email and SMS messages.
locale: en-US
canonical_url: https://www.servicenow.com/docs/r/customer-service-management/csm-interaction-record-page.html
release: australia
topic_type: concept
last_updated: "2026-03-12"
reading_time_minutes: 4
breadcrumb: [Record pages, Record pages and page templates, CSM Configurable Workspace, Organize agent workspaces, Configure, Customer Service Management]
tags:
  - customer-service-management
  - type-concept
---

# CSM Interaction record page

The CSM Interaction record page provides CSM interaction management features and functionality and enables agents to accept and respond to live chats, calls, email and SMS messages.

The CSM Interaction record page provides the basic structure for an interaction record, including interaction information and related search results.

\[Omitted image "csm-Interaction-record-template.png"\] Alt text: The CSM Interaction record page provides agents with the active chat panel, interaction details, and the ability to [[lookup-verify-contact-consumer|look up and verify a contact or consumer]].

The CSM Interaction record page is included with the CSM/FSM Configurable Workspace experience.

## Record presence feature

The [[csm-default-record-page|CSM default record page]] and the CSM Interaction record page include the record presence feature. This feature allows agents to see other users who are viewing the same record and enables easy collaboration.

The user presence component displays an icon in the form header that shows the user who is currently viewing the record. For three or more users, the component displays two icons plus a number that represents additional users.

-   Hover over an icon to see more information about a user.
-   Click the number icon to see more information about the additional users.

For more information about this feature, see [User presence](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/platform-user-interface/c_UserPresence.md).

## Thin compose modeless dialogs

[[csm-front-line-case-page-modeless-dialogs|Thin compose modeless dialogs]] enable agents to initiate a work note or email from the [[csm-config-ws-activity-stream|activity stream]] in a modeless dialog.

**Note:** For the CSM Interaction record page, the thin compose modeless dialogs feature is hidden by default and can be enabled by the admin.

## Recommended Actions feature

The Recommended Actions tab is now available as the first tab in the contextual side panel and is enabled for Pro customers. It includes a set of base system recommendations, such as similar incidents and similar open incidents.

The Recommended Actions tab includes [[ra-csm-ai-search|AI search]] functionality and Suggested Actions for the chat, video, email, and walk-up channels on the CSM Interaction record page.

-   AI search tab: Agents can use AI search to find relevant resources or resolutions for customer issues. The search feature displays an initial set of search results based on the text in the interaction short description. This initial set of results includes knowledge articles. Agents can also enter different search keywords and repeat the search. From the list of search results, agents can select a source to see search results of that type.

    For the Knowledge source type, agents can do the following:

    -   Share an article link in chat and email.
    -   Copy a link to an article.
    -   Read an article.
    -   Flag an article.
    -   Mark an article as helpful.
    For all the other source types, default guidance is supported. The default guidance for search results is a guidance that can be used for any search sources that don't have mapped guidances. For more information on default guidance, see [[ra-csm-guidances-default-guidance-search|Default guidance for search results]].

    For more information on how to avail the AI search feature in Recommended Actions, see [[migrate-ra-agent-assist|Enable AI search in Recommended Actions]].

    For more information, see [[nba-use-ai-search|Use AI search in Recommended Actions to resolve cases]].

    **Note:** Using Recommended Actions in the contextual side panel requires the [[nba|Recommended Actions]] application \(sn\_cs\_nb\_action\) which is included with the [[csm-workspaces-configure|CSM Configurable Workspace]] application.

-   Suggested Actions tab: This tab displays relevant actions to agents based on a context of a record or recommend a value for a field. For more information on how to configure contexts so that relevant actions are displayed for the agents, see [[configure-nba|Recommended Actions]].

## Editable record header field

Agents can edit the short description of a record directly from the record header field. For more information, see [[csm-workspace-agent-actions|Editable record headers]].

## Collaborate component

The Collaborate component enables agents to communicate with stakeholders and other users and gather information for case resolution. This component is available on the CSM default record page n the contextual side panel. For more information, see [[csm-config-ws-collaborate-component|Collaborate component]].

**Related topics**  


[[csm-native-voice-record-page|CSM voice interaction record page]]

## Related

- [[csm-front-line-case-page-modeless-dialogs|Modeless dialogs]]
- [[ra-csm-ai-search|AI search in Recommended Actions]]
- [[ra-csm-guidances-default-guidance-search|Default guidance for search results]]
- [[migrate-ra-agent-assist|Enable AI search in Recommended Actions]]
- [[nba-use-ai-search|Use AI search in Recommended Actions to resolve cases]]
- [[nba|Configuring Recommended Actions]]
- [[configure-nba|Recommended Actions]]
- [[csm-workspace-agent-actions|CSM Configurable Workspace form features]]
- [[csm-config-ws-collaborate-component|Collaborate component]]
- [[csm-native-voice-record-page|CSM voice interaction record page]]
- [[lookup-verify-contact-consumer|Look up and verify a contact or consumer]]
- [[csm-default-record-page|CSM default record page]]
- [[csm-config-ws-activity-stream|Activity stream]]
- [[csm-workspaces-configure|CSM Configurable Workspace]]
