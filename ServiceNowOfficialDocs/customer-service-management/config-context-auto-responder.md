---
title: Configuring the search context for Auto-Responder
description: You can configure the predefined search context for customer service cases to include relevant search resources in Auto-Responder email notifications.
locale: en-US
canonical_url: https://www.servicenow.com/docs/r/customer-service-management/config-context-auto-responder.html
release: australia
topic_type: concept
last_updated: "2026-03-12"
reading_time_minutes: 1
breadcrumb: [Configure Auto-Responder notifications, Machine learning solutions, Implement Intelligence, Configure, Customer Service Management]
tags:
  - customer-service-management
  - type-concept
---

# Configuring the search context for Auto-Responder

You can configure the predefined search context for customer service cases to include relevant search resources in Auto-Responder email notifications.

The Predictive [[intelligence-csm|Intelligence]] for [[c_CustomerServiceManagement|Customer Service Management]] plugin \(com.snc.csm\_ml\) includes the predefined **Case Email Autoresponder KB search** search context for customer service cases configured for use in the Auto-Responder feature. This search context uses the predeﬁned Search Knowledge Articles searcher that provides knowledge articles as search results.

By default, the **Case Email Autoresponder KB search** search context includes [[osp-contextual-search|contextual search]] results based on Predictive Intelligence. You can edit this search context to include any additional resources. For more information, see [Define a search context](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/platform-administration/t_DefineSearchContext.md).

**Note:** To provide other relevant recommendations to resolve a customer service case when Predictive Intelligence results are insufficient or unavailable, you can also enable the text search recommendations in the Auto-Responder email notification. For more information, see [[enable-text-based-auto-responder|Enable text search recommendations in Auto-Responder notifications]].

## Related

- [[enable-text-based-auto-responder|Enable text search recommendations in Auto-Responder notifications]]
- [[intelligence-csm|Intelligence]]
- [[c_CustomerServiceManagement|Customer Service Management]]
- [[osp-contextual-search|Contextual search]]
