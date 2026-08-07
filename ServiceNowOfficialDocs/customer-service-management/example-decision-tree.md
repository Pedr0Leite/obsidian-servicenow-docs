---
title: Example configuration of a decision tree
description: This example demonstrates an end-to-end configuration of a decision tree to help you get started with Guided Decisions. After you configure the decision tree, you can either embed it in a playbook or use it as a recommendation in Recommended Actions.
locale: en-US
canonical_url: https://www.servicenow.com/docs/r/customer-service-management/example-decision-tree.html
release: australia
topic_type: concept
last_updated: "2026-03-12"
reading_time_minutes: 1
breadcrumb: [Guided Decisions configuration, Agent tools, Organize agent workspaces, Configure, Customer Service Management]
tags:
  - customer-service-management
  - type-concept
---

# Example configuration of a decision tree

This example demonstrates an end-to-end configuration of a decision tree to help you get started with Guided Decisions. After you configure the decision tree, you can either embed it in a playbook or use it as a recommendation in [[configure-nba|Recommended Actions]].

For more information about decision trees, see [[decision-trees-in-guided-decisions|Decision trees in Guided decision]] and [[configuring-guided-decisions|Configuring guidances and decision trees]].

## Troubleshooting a failed credit card transaction

Paul, who holds an account with the StellarVest bank is trying to purchase a smart watch using their credit card. But the transaction failed at the time of payment. Paul created a case in the StellarVest bank portal seeking assistance. Agents from the StellarVest bank work on the cases created by customers to resolve their issues.

In this scenario, the agent assigned to the Paul’s case uses a decision tree to troubleshoot the failed credit card transaction. The decision tree collects user, credit card, and transaction details. If money was debited, transaction tracking is initiated. However, if no money was debited, the agent provides a failure code which determines what guidance is provided. Examples of potential guidances include: reassigning the case, creating a work order, or assigning the case to an IT technician.

\[Omitted image "example-complete-decision-tree.png"\] Alt text: A completed decision tree for troubleshooting a failed credit card transaction in Decision Tree Builder. The tree includes start node, question nodes, and guidance nodes.

## Creating the decision tree to troubleshoot the failed transaction

Learn how process analysts or business owners create a decision tree, and configure various [[guided-decision-tree-node-types|decision tree nodes]] in the [[preparation-for-creating-a-decision-tree|next pages]].

## Related

- [[decision-trees-in-guided-decisions|Decision trees in Guided decision]]
- [[configuring-guided-decisions|Configuring guidances and decision trees]]
- [[preparation-for-creating-a-decision-tree|Preparation for creating a decision tree]]
- [[configure-nba|Recommended Actions]]
- [[guided-decision-tree-node-types|Decision tree nodes]]
