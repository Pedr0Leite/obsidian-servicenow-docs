---
title: "Cancel a Long-Running Transaction"
aliases:
  - KB0656014
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0656014
kb_number: KB0656014
last_modified: 2026-03-31
---

## Cancel a Long-Running Transaction

  

### Issue

Cancel a transaction that does not complete and is blocking other transactions on your instance. The ServiceNow platform includes a built-in method that allows you to cancel your own active transaction.

### Release

All supported releases

### Resolution

To cancel a long-running transaction, paste the following URL into any browser tab and press **Enter**:

[https://<INSTANCE>.service-now.com/cancel\_my\_transaction.do](https://\<INSTANCENAME\>.service-now.com/cancel_my_transaction.do "https://<INSTANCENAME>.service-now.com/cancel_my_transaction.do") 

Replace <instance\_name> with your instance name. In most cases, this cancels the active transaction.

If this does not resolve the issue, contact your ServiceNow admin team. An admin can cancel the transaction on the active node.

### Related Links

[View and kill active transactions](https://docs.servicenow.com/csh?topicname=t_ViewAndKillAnActiveTransaction.html&version=latest "Doc: View and kill active transaction")

[Transaction Quotas](https://docs.servicenow.com/csh?topicname=c_TransactionQuotas.html&version=latest "Transaction Quotas")
