---
title: Configuring decision trees in Decision Tree Builder
description: Configure decision trees using the no-code visual Decision Tree Builder, which provides a canvas for a diagrammatic representation of nodes and their paths in a troubleshooting process.
locale: en-US
canonical_url: https://www.servicenow.com/docs/r/customer-service-management/decision-trees-in-gdb.html
release: australia
topic_type: concept
last_updated: "2026-03-12"
reading_time_minutes: 4
breadcrumb: [Configuring guidances and decision trees, Guided Decisions configuration, Agent tools, Organize agent workspaces, Configure, Customer Service Management]
tags:
  - customer-service-management
  - type-concept
---

# Configuring decision trees in Decision Tree Builder

Configure decision trees using the no-code visual Decision Tree Builder, which provides a canvas for a diagrammatic representation of nodes and their paths in a troubleshooting process.

As a process owner or business analyst, you can configure [decision tree](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/glossary/now-platform-glossary.md) by adding nodes, defining paths, and attaching guidances through Decision Tree Builder. For more information, see [[guided-decision-tree-node-types|Decision tree nodes]].

You can validate and activate a decision tree with a single action. For more information, see [[activate-guided-decision-tree|Activate a decision tree]].

## Decision Tree Builder canvas

\[Omitted image "diagram-canvas-gd-builder.png"\] Alt text: Decision Tree Builder with a flow chart and a side panel that has node configuration properties.

## Accessing Decision Tree Builder

You can access the Decision Tree Builder by selecting the **Open in Builder** button on the decision tree record.

## Configuring question and guidance nodes

You can configure a new node as a question node or a guidance node. When there are multiple questions in a start node or a question node, you can delete a question or change the order of the questions. For more information, see [[configure-start-node-gdb|Add questions or instructions to a decision tree]].

Guidance nodes provide actions to agents to resolve or escalate a customer issue. You can either select a guidance from the list of available guidances or create a guidance in Core UI. You can then configure guidance inputs by entering static values or reuse inputs from prior nodes. For more information, see [[configure-guidance-in-gdb|Provide actions to agents in a decision tree]].

## Linking node

You can configure a new node as a linking node to link a child decision tree to the current decision tree. This linking connects the execution of the primary decision tree to another decision tree when a specific condition is met. For more information, see [[configure-linking-node-dtb|Link an activated decision tree to this decision tree]].

## Creating paths for the next nodes

A path in a decision tree connects one node to another. You can configure a condition to define when the path must be taken. Selecting certain answers can be a condition for the path. The priority order for a path sets the precedence of one path over another.

For more information, see [[configure-path-in-gdb|Determine the next node displayed in a decision tree]].

## Editing a node or a path

When you edit the inputs of nodes and their paths, make sure to update the following nodes as well because they might be reusing data from these inputs.

## Deleting a node or a path

Note the following information about deleting a node or path:

-   You can delete a leaf node if it isn’t connected to any path or a node.
-   Deleting a leaf node removes the node from the decision tree but the configuration of the path before the deleted node remains intact.
-   You can't delete an intermediate node or path.
-   When you delete the question node after a guidance node, both the question node and the path are deleted.

## Linking inputs

You can link inputs from one node to another to reuse input values from prior nodes. You can use linked inputs to create path conditions. For more information about input mapping in the question node or guidance node, see [[guided-decision-tree-input-mapping|Linking inputs in decision tree nodes]].

For more information, see [[map-inputs-in-decision-guidance-node|Reuse answers at decision points]].

**Related topics**  


[[validation-errors-builder|Validation error notifications in Decision Tree Builder]]

[Activate a decision tree](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/customer-service-management/activate-guided-decision-tree.md)

[[discard-latest-changes|Revert to the previous activated decision tree version]]

## Related

- [[guided-decision-tree-node-types|Decision tree nodes]]
- [[activate-guided-decision-tree|Activate a decision tree]]
- [[configure-start-node-gdb|Add questions or instructions to a decision tree]]
- [[configure-guidance-in-gdb|Provide actions to agents in a decision tree]]
- [[configure-linking-node-dtb|Link an activated decision tree to this decision tree]]
- [[configure-path-in-gdb|Determine the next node displayed in a decision tree]]
- [[guided-decision-tree-input-mapping|Linking inputs in decision tree nodes]]
- [[map-inputs-in-decision-guidance-node|Reuse answers at decision points]]
- [[validation-errors-builder|Validation error notifications in Decision Tree Builder]]
- [[discard-latest-changes|Revert to the previous activated decision tree version]]
