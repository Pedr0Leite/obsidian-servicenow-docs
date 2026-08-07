---
title: Flow action
description: Workflow Studio predefined actions help you preserve mapped variable integrity and maintain flow compatibility across configuration revisions.
locale: en-US
canonical_url: https://www.servicenow.com/docs/r/service-exchange/service-bridge-v2-flow-action.html
release: australia
product: Service Exchange
classification: service-exchange
topic_type: concept
last_updated: "2026-05-13"
reading_time_minutes: 1
keywords: [flow action, Flow Designer, remote task variables, provider task variables, remote record producer]
breadcrumb: [Explore, Service Exchange]
tags:
  - service-exchange
  - marketplace
  - spokes
  - apps
  - type-concept
---

# Flow action

Workflow Studio predefined actions help you preserve mapped variable integrity and maintain flow compatibility across configuration revisions.

[[tmt-service-bridge-both-landing-page|Service Exchange]] provides a set of predefined Workflow Studio actions that you can use in your flows or subflows to retrieve variable values from [[service-bridge-v2-remote-task-overview|remote tasks]] and [[service-bridge-v2-provider-tasks|provider tasks]]. For details on flows, see [Getting started with flows](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/build-workflows/getting-started-flow.md).

Service Exchange provides the following actions in Workflow Studio:

**Note:** To avoid upgrade issues, use these predefined actions in your flows and subflows.

<table id="table_x1x_ch2_zfc"><thead><tr><th>

Action

</th><th>

Description

</th><th>

Input

</th><th>

Purpose

</th><th>

Output

</th></tr></thead><tbody><tr><td>

Get Provider Task Variables for RRP

</td><td>

Retrieve variable values from a Provider task based on a selected remote record producer \(RRP\) as data pills for use in other actions.Must be in the `sn_sb` base scope.

</td><td>

provider task, RRP.

</td><td>

Use variables in automation flows, such as updating a parent task or ordering a local catalog item.

</td><td>

Returns named data pills based on the variables within the RRP.

</td></tr><tr><td>

Get Remote Task Variables from Consumer

</td><td>

Retrieves variable answers from a remote task based on a selected remote task definition \(RTD\) identity, exposing them as data pills for use in other actions.Must be in the provider scope.

</td><td>

remote task, RTD identity.

</td><td>

Use variables in automation flows, such as updating a parent task.

</td><td>

Returns named data pills based on the variables within the latest published RTD.

</td></tr><tr><td>

Get Remote Task Variables from Provider

</td><td>

Retrieve variable values from a remote task based on selected remote task definitions.Must be in the consumer scope.

</td><td>

remote task,RTD identity.

</td><td>

Use variables in automation flows, such as updating a parent task.

</td><td>

Returns named data pills based on the variables within the latest published RTD.

</td></tr><tr><td>

Order Remote Record Producer

</td><td>

Automate ordering a RRP.Must be in the consumer scope.

</td><td>

RRP.

</td><td>

Streamline processes such as hardware asset management \(HAM\) by scripting RRP ordering.

</td><td>

Returns the newly created provider task GlideRecord.

</td></tr></tbody>
</table>

## Related

- [[tmt-service-bridge-both-landing-page|Service Exchange]]
- [[service-bridge-v2-remote-task-overview|Remote tasks]]
- [[service-bridge-v2-provider-tasks|Provider tasks]]
