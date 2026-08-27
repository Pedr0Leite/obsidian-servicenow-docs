---
aliases:
  - "What is “Presumed Interrupted” state"
area: "Flow Designer"
source: notion-export
tags:
  - flow-designer
  - sys-flow-context
  - troubleshooting
  - graceful-shutdown
  - automation
---

# What is “Presumed Interrupted” state?

### Use Cases

- Previously, when a flow
execution is unexpectedly interrupted the flow context state remained
"In Progress". This is misleading to the user.
- Examples of unexpected interruptions include the transaction being terminated or the node being restarted.
- A new sys_flow_context state "Presumed Interrupted" has been introduced
to aid in identifying these interrupted flow executions. This state
does not mean the flow is cancelled. It's possible that it's still
executing or could resume at a later point in time.
- Presumed
Interrupted state is intended to inform users that the flow is a long
running and appears stuck in some way. Possible causes include node
restart or infinite loop within the flow or in another BR or flow that
we triggered by the flow.
    - Starting in Utah, flows can be paused/resumed when a node is shutting down/restarting with the [Graceful Shutdown](https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB1523950) feature
- This feature does not cover flow executions that are interrupted while executing on the mid server
- This feature does not trigger flow error handling. It's intended that the flow should be able to resume if possible.

### How does it work?

- Two new columns have been added to sys_flow_context: transaction and claimed_by
- When the flow engine begins working on a flow context the
field sys_flow_context.claimed_by is set to the node id and the
field sys_flow_context.transaction is set to the sys_id of the current
transaction.
    - If the flow execution is sent to the mid, claimed_by will be set to "mid" and the transaction will be empty.
- Any flow context suspected to be interrupted will have its
state changed to "Presumed Interrupted". Also, an error message will
be logged. The error message starts with: "Flow state changed from
IN_PROGRESS to PRESUMED_INTERRUPTED due to inactivity…"
- At configured intervals, the sys_flow_context table will be checked for any flow executions that appears to be interrupted.
- There are two types of checks: "this node" (the happy path case) and "other
nodes" (for the case where a flow execution is interrupted when a node
is shutdown and that node is not restarted).
    - The "this node" check will
    run every 15 minutes and will look for any flow context that is claimed
    by the current node, has state IN_PROGRESS or CONTINUE_SYNC, was last
    updated more than 15 minutes ago, and has a transaction id that is no
    longer valid for the current node.
    - The "other node" check covers cases where the node that was running the flow execution is
    never restarted. This check will run every 1 hour and will look for any flow context that is claimed by a different node, has state IN_PROGRESS or CONTINUE_SYNC, and was last updated more than 8 hours ago. The
    transaction id can not be checked since valid transaction ids are only
    available for a running node.
        - If a flow has a step, such
        as a script, that runs for more than 8 hours it is possible that this
        feature will mistakenly update the state to PRESUMED_INTERRUPTED. If
        that does occur the state will be changed back to the expected value
        when the step finishes and the flow context quiesces.

### Remediation Steps

- Check if the transaction (sys_flow_context.transaction) is still active on the node (sys_flow_context.claimed_by)
    - If yes (usually this means it has been marked presumed
    interrupted by another node), the flow is likely in an infinite loop
    (bad script or bad looping condition) needs to be cancelled. Refactor
    the flow and re-execute it.
    - If no (usually this means the
    current node has been restarted or there was an unknown error that was
    not properly caught/handled), we need to either
        - manually complete the remainder of the flow from where the flow execution was interrupted or aborted
        - create a subflow based on the flow from the point where the flow execution was interrupted or aborted (example flow has 10 steps and it error'd on
        step 5 - resolve the error condition and execute subflow containing
        actions 5 to 10, for example)

To check if a Node shutdown or was restarted, grep the local host logs:

```markup
egrep “glide Loading platform|Initiating normal shutdown” localhost_log.2019-0*.txt
```

### Configurable System Properties

- Feature enabled (default true): com.glide.hub.flow.interrupted_flow_marker.enabled
- "This Node" check minimum time since last updated (default 900, 15
minutes): com.glide.hub.flow.interrupted_flow_marker.this_node.updated_sec_ago
- "Other Node" check minimum time since last updated (default 28800,
8 hours): com.glide.hub.flow.interrupted_flow_marker.other_nodes.updated_sec_ago

## Related

- [[Flow Designer]]
- [[How to nudge a flow]]
- [[sn_fd FlowAPI nudgeFlow does not work if completed]]
- [[Flow Designer Making the flow wait until a specifi]]
