---
aliases:
  - "sn_fd FlowAPI nudgeFlow does not work if completed"
area: "Flow Designer"
source: notion-export
tags:
  - flow-designer
  - flow-api
  - nudge-flow
  - subflows
  - bug-workaround
  - sys-flow-context
---

# sn_fd.FlowAPI.nudgeFlow does not work if completed subflow context watching record is deleted causing parent flow error

## Description

Nudging
 a subflow/child context causes the parent flow to fail because of the 
flow context retention policy. The flow error is due to the completed 
subflow context being cleaned up.

## Steps to Reproduce

1. Create a subflow with 5 min timer.

2. Create another subflow consuming the above subflow.

3. Start subflow #2 and note the context_Id.

4. Open the sys_flow_rw_action table and delete the watching record. Make sure to note these values.

5. Wait the child subflow context to complete. This will not continue the parent flow, as RW was deleted.

6. Delete the child subflow context from the sys_flow_context table.

7. Use sn_fd.FlowAPI.nudgeFlow to nudge the parent context_Id. This fails to nudge the parent flow, which does not continue.

## Workaround

This problem is fixed in an upcoming release. If you are able to upgrade, review the **Fixed In** section to determine the latest version with a permanent fix your instance can be upgraded to.

A possible workaround would be to change the retention period.

[Ref.: Flow execution details retention](https://docs.servicenow.com/bundle/rome-servicenow-platform/page/administer/flow-designer/concept/flow-reporting.html)

## Related

- [[Flow Designer]]
- [[How to nudge a flow]]
- [[What is “Presumed Interrupted” state]]
