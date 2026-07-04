---
title: "The flow does not run"
aliases:
  - KB0824489
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0824489
kb_number: KB0824489
last_modified: 2024-04-08
---

## The flow does not run

  

### Issue

-   -   After submitting the catalog item the flow does not appear to have ran
    -   The flow is not triggering
    -   \[sys\_flow\_context\] has a state of error

### Cause

We see the following errors in the node logs:

```
2020-05-12 10:16:54 (848) worker.6 worker.6 txid=8c01476cdbf4 SEVERE *** ERROR *** Flow Designer: Operation(28a89e9c1bb0105033ab0d47dc4bcb9a.bca8de9c1bb0105033ab0d47dc4bcb1b.eab2f71f1b541010d576fd13cd4bcb0f) failed with error: java.security.AccessControlException: Access denied to create new email
```

```
2020-05-12 10:16:54 (853) worker.6 worker.6 txid=8c01476cdbf4 SEVERE *** ERROR *** Flow Designer: Operation(DSIF Data Request.ForEach$1.item$1) failed with error: com.snc.process_flow.exception.OpException: called block 'DSIF Data Request.ForEach$1.item$1' failed. Check the context log for exception details.
```

-   we were able to reproduce the issue on UAT instance, with a user that did not have admin role
-   flow execution is more strict than workflow, it will run the flow more secured so if the user does not have permission it will error out

### Resolution

To avoid this the flow can be run as system from the flow's properties
