---
title: Search for knowledge articles in CSM Configurable Workspace
description: Search for knowledge articles in Agent Assist, including similar knowledge articles.
locale: en-US
canonical_url: https://www.servicenow.com/docs/r/customer-service-management/csm-workspace-search-knowledge.html
release: australia
topic_type: task
last_updated: "2026-03-12"
reading_time_minutes: 1
breadcrumb: [Using CSM Configurable Workspace in Customer Service Management, Manage cases, Use, Customer Service Management]
---

# Search for knowledge articles in CSM Configurable Workspace

Search for knowledge articles in [[migration-agent-assist|Agent Assist]], including similar knowledge articles.

## Before you begin

Role required: sn\_customerservice\_agent, sn\_customerservice.consumer\_agent, workspace\_admin, admin

## About this task

Agent Assist displays [[osp-contextual-search|contextual search]] results based on text entered in the **Short description** field on the [[r_CustomerServiceCaseForm|Case form]]. These search results include knowledge articles and other types of information, such as open or resolved cases and community content. You can narrow the list of results by selecting a specific type of information to view.

**Note:** With the Predictive [[intelligence-csm|Intelligence]] for [[c_CustomerServiceManagement|Customer Service Management]] plugin \(com.snc.csm\_ml\), you can also view Similar Knowledge Articles.

## Procedure

1.  [[csm-workspaces-open|Open CSM Configurable Workspace]].

2.  Open a customer service case.

3.  Perform one of the following.

    -   In the Agent Assist panel, click the search resource icon \(\[Omitted image "agent-assist-select-search-resource-icon.png"\] Alt text: Search resource icon.\) and select a search source.
        -   `Knowledge Articles`
        -   `Similar Knowledge Articles`
    -   In the [[configure-nba|Recommended Actions]] - Search tab, search with a keyword and select the **Search source** as `Knowledge` to filter the knowledge articles.

        For more information on how to enable Recommended Actions - AI Search and disable Agent Assist, see [[migrate-ra-agent-assist|Enable AI search in Recommended Actions]].

4.  Select a knowledge article.

5.  Click **Attach**.

    Depending on your configuration, you can add a link or embed an article directly into the Additional comments \(customer visible\) portion of the [[csm-config-ws-activity-stream|activity stream]].

## Related

- [[migrate-ra-agent-assist|Enable AI search in Recommended Actions]]
- [[migration-agent-assist|Agent assist]]
- [[osp-contextual-search|Contextual search]]
- [[r_CustomerServiceCaseForm|Case form]]
- [[intelligence-csm|Intelligence]]
- [[c_CustomerServiceManagement|Customer Service Management]]
- [[csm-workspaces-open|Open CSM Configurable Workspace]]
- [[configure-nba|Recommended Actions]]
- [[csm-config-ws-activity-stream|Activity stream]]
