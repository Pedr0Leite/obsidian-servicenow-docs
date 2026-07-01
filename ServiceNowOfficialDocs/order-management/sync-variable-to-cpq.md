---
title: Sync context variables to CPQ
description: Sync context variables to CPQ to be associated with blueprints.
locale: en-US
canonical_url: https://www.servicenow.com/docs/r/order-management/sync-variable-to-cpq.html
release: australia
topic_type: task
last_updated: "2026-05-28"
reading_time_minutes: 1
breadcrumb: [Product pricing, Configure, price, quote apps, Configure, Sales Customer Relationship Management]
---

# Sync context variables to CPQ

Sync context variables to CPQ to be associated with [[blueprints|blueprints]].

## Before you begin

Role required: admin

## About this task

Context variables provide the business data that pricing and configuration [[rules_101|rules]] need to evaluate a transaction, such as the shipping country, currency, or customer tier. Before this data can be used in rules, the context variable definition must be available in the rules engine. Syncing a context variable to CPQ publishes its definition, including its type, mapping, and whether it applies at the transaction header or line level to the rules engine, where you can reference it directly in blueprint rules without writing [[scripts|scripts]].

Administrators can sync context variables to CPQ, if not already. Context variables are synced automatically when newly created or updated. Existing context variables that are not synced can be synced manually.

## Procedure

1.  In the CSM Configurable Workspace, select the **List** \[Omitted image "list-outline-24.svg"\] Alt text: view.

2.  Navigate to **Context Rule Management** &gt; **Context Variables**.

3.  In the Context Variables list, select the context variables that you want to sync to CPQ.

    **Note:** You can sync only the context variables that are not synced. The **Synced to CPQ** field in the Context Variables list is set to true if the context variable is synced.

4.  Select **Sync To CPQ**.

    If you don't see the **Sync To CPQ** field, personalize the form and add this field.


## Result

The **Synced to CPQ** field in the Context Variables list is set to true after the sync is successful and the context variable is can be associated with blueprints and rules.

Navigate to **All** &gt; **CPQ Administration** &gt; **ALL [[fields|FIELDS]]** to verify and use the synced context variables.

**Related topics**  


[[som-create-context-variable|Create a custom context variable]]

## Related

- [[som-create-context-variable|Create a custom context variable]]
- [[blueprints|Blueprints]]
- [[rules_101|Rules]]
- [[scripts|Scripts]]
- [[fields|Fields]]
