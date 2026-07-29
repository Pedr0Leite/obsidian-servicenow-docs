---
title: Add Guided Decisions to Recommended Actions
description: Add decision trees created using the Guided Decisions Experience application to Recommended Actions, so customer service agents can work through it to resolve cases more efficiently.
locale: en-US
canonical_url: https://www.servicenow.com/docs/r/customer-service-management/add-guided-decisions-to-recommended-actions.html
release: australia
topic_type: task
last_updated: "2026-03-12"
reading_time_minutes: 1
breadcrumb: [Configuring guidances and decision trees, Guided Decisions configuration, Agent tools, Organize agent workspaces, Configure, Customer Service Management]
tags:
  - customer-service-management
  - type-task
---

# Add Guided Decisions to Recommended Actions

Add decision trees created using the Guided Decisions Experience application to [[configure-nba|Recommended Actions]], so customer service agents can work through it to resolve cases more efficiently.

## Before you begin

Ensure that you have Recommended Actions application \(sn\_nb\_action\) installed.

Role required: sn\_nb\_action.next\_best\_action\_author, admin

## Procedure

1.  Navigate to **All** &gt; **Recommended Actions** &gt; **Contexts**.

2.  [[ra-csm-contexts-create|Create a context for a table.]]

    A context enables agents to see recommended actions for a record in that table.

3.  [[ra-csm-rules-create|Create a rule for the context.]]

    A rule is a set of conditions that applies to a context and determines when a recommended action appears for records in the context table.

4.  [[ra-csm-recommendations-create|Create a recommendation of type decision tree.]]

    A recommendation is a way to suggest an action to an agent.


**Related topics**  


[[setting-up-guided-decisions|Configuring Guided Decisions]]

[[configuring-guided-decisions|Configuring guidances and decision trees]]

## Related

- [[ra-csm-contexts-create|Create a context in Recommended Actions]]
- [[ra-csm-rules-create|Create a rule in Recommended Actions]]
- [[ra-csm-recommendations-create|Create a recommendation in Recommended Actions]]
- [[setting-up-guided-decisions|Configuring Guided Decisions]]
- [[configuring-guided-decisions|Configuring guidances and decision trees]]
- [[configure-nba|Recommended Actions]]
