---
title: "How to Cancel a Long Running Transaction | All Nodes"
aliases:
  - KB0635968
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0635968
kb_number: KB0635968
last_modified: 2026-04-23
---

## How to Cancel a Long Running Transaction | All Nodes

  

### Issue

Sometimes we start transactions that we may want to cancel. The transaction may end up running longer than expected, potentially causing performance issues or unexpected behavior. This article provides information on how to cancel a long-running transaction.

### Release

All releases

### Resolution

### Canceling transactions on any Node

This ability was added in the Istanbul release to be able to cancel any transaction from the node the user is logged into. This is available in the module **System Diagnostics > Active Transactions (All Nodes)**. Follow these steps to kill transactions:

-   Select the transaction in the list
-   Open the menu at the bottom of the list and select **Kill**

![Active Transactions module](sys_attachment.do?sys_id=4fb0bd3593706e10e7eef35d6cba102c "Active Transactions module")

 **Note**: Transactions are grouped by the application node that is currently running them.

### Related Links

### On releases before Istanbul (Node Specific)

Before the Istanbul release, canceling transactions was only available for the node you were currently logged into under **User Administration > All Active Transactions**

![All Active Transactions](/sys_attachment.do?sys_id=cbb0bd3593706e10e7eef35d6cba102a "All Active Transactions")

Clicking on **All Active Transactions** brings up a list of the actively running transactions from the node the user is logged into. To cancel a transaction:

-   Select the transaction in the list
-   Open the menu at the bottom of the list and select **Kill**

![Kill the transaction](sys_attachment.do?sys_id=5fb0bd3593706e10e7eef35d6cba102e "Kill the transaction")

**Note**: It may take a few seconds for the transaction to die in the background. Refresh the list several times to confirm the transaction is properly killed.
