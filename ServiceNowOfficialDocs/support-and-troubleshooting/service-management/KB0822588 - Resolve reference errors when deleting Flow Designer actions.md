---
title: "Resolve reference errors when deleting Flow Designer actions"
aliases:
  - KB0822588
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0822588
kb_number: KB0822588
last_modified: 2025-08-26
---

## Resolve reference errors when deleting Flow Designer actions

  

### Issue

When you try to delete a Flow Designer action, you may see the error message: "Delete of "XXX" not allowed because of a reference in record within the Action Instance file."

This occurs even when the action is no longer part of any flow or subflow because an instance of the action still exists. 

### Release

New York Patch 7

### Cause

Action instances should only exist as part of a flow or subflow. The cascade delete reference rule manages the process of automatically deleting action instances (sys\_hub\_action\_instance table) when you delete the flow or subflow that references them. An action can sometimes remain associated with a snapshot of a flow or subflow, preventing deletion.

### Resolution

You can safely delete a snapshot if it is neither the main snapshot nor the base definition and not part of a flow execution (sys\_flow\_context table). 

To check the references:

1.  Go to sys\_hub\_action\_instance.list and identify instances associated with your action. 
2.  Verify that the associated flow is not:
    -   The main or latest snapshot
    -   The base definition (sys\_hub\_flow table)
    -   Related to a flow execution (where sys\_flow\_context.flow matches sys\_hub\_action\_instance.flow)
3.  Remove the action instances that relate to the action.
