---
title: Preparation for creating a decision tree
description: Before configuring a decision tree, process analysts should document the flow of the decision tree using a flow chart including the questions, answers, associated paths, and guidance.
locale: en-US
canonical_url: https://www.servicenow.com/docs/r/customer-service-management/preparation-for-creating-a-decision-tree.html
release: australia
topic_type: concept
last_updated: "2026-03-12"
reading_time_minutes: 2
breadcrumb: [Example configuration of a decision tree, Guided Decisions configuration, Agent tools, Organize agent workspaces, Configure, Customer Service Management]
tags:
  - customer-service-management
  - type-concept
---

# Preparation for creating a decision tree

Before configuring a decision tree, process analysts should document the flow of the decision tree using a flow chart including the questions, answers, associated paths, and guidance.

Anita, who is a process analyst at the StellarVest bank wants to create a decision tree that enables agents to troubleshoot a failed credit card transaction.

Anita first creates a flowchart to document the flow of a decision tree to determine the questions, answers, and possible guidance to configure.

\[Omitted image "ex-decision-tree-flow-chart.png"\] Alt text: A flow chart depicting the flow of the decision tree that the admin wants to configure.

|No.|Element|Name|Description|
|---|-------|----|-----------|
|1|Start node|[[ask-card-holder-and-transaction-details|Card holder and transaction details]]|Start node that collects customer, credit card, and transaction details.|
|2|Path|[[configuring-paths-for-next-nodes|Amount is debited]]|Path with condition: Amount is debited.|
|3|Guidance node|[[configure-guidance-node-initiate-transaction-tracking|Initiate transaction tracking]]|Guidance to initiate transaction tracking when amount is debited.|
|4|Question node|[[configure-a-question-node-for-further-assistance|Further assistance needed]]|Ask whether the customer needs further assistance.|
|5|Guidance node|Provide more options|Guidance to provide more options such as talk to an agent or request a new card.|
|6|Path|[Amount is not debited](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/customer-service-management/configuring-paths-for-next-nodes.md)|Path with condition: amount isn’t debited.|
|7|Question node|[[configure-question-node-to-ask-failure-codes|Failure codes]]|Collect transaction failure codes when amount isn’t debited.|
|8|Path|[[configure-path-for-200-failure-code|Error 200]]|Error code received is 200.|
|9|Guidance node|[[associate-guidances-for-different-failure-codes|Reassign case]]|Guidance to reassign the case to someone else.|
|10|Path|[Error 300](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/customer-service-management/configure-path-for-200-failure-code.md)|Error code received is 300.|
|11|Guidance node|[Create work order](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/customer-service-management/associate-guidances-for-different-failure-codes.md)|Guidance to [[create-work-orders|create a work order]] for dispatching a new credit card.|
|12|Path|[Error 500](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/customer-service-management/configure-path-for-200-failure-code.md)|Error code received is 500.|
|13|Guidance node|[Assign IT technician](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/customer-service-management/associate-guidances-for-different-failure-codes.md)|Guidance to assign an IT technician to resolve the issue.|

## Related

- [[ask-card-holder-and-transaction-details|Configure the start node for cardholder and transaction details]]
- [[configuring-paths-for-next-nodes|Configuring paths with conditions whether the amount is debited or not]]
- [[configure-guidance-node-initiate-transaction-tracking|Configure a guidance node to initiate the transaction tracking]]
- [[configure-a-question-node-for-further-assistance|Configure a question node for further assistance]]
- [[configure-question-node-to-ask-failure-codes|Configure a question node to ask failure codes]]
- [[configure-path-for-200-failure-code|Configure paths for different failure code conditions]]
- [[associate-guidances-for-different-failure-codes|Associate guidances for different failure codes]]
- [[create-work-orders|Create a work order]]
