---
title: "How to resolve data policy exceptions in Flow Designer"
aliases:
  - KB0820823
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0820823
kb_number: KB0820823
last_modified: 2025-08-06
---

## How to resolve data policy exceptions in Flow Designer

  

### Issue

When you create a flow with an Insert Record action that targets a table with data policy requirements, the flow may fail if those requirements aren't met.

For example, if the Change Request table has a data policy making the Assigned to field mandatory, but your flow doesn't set a value for this field, the flow will fail with a data policy exception. 

![Data policy rule UI with assigned\_to field settings](sys_attachment.do?sys_id=2e450d88471f2e9048cb2920326d43f1)

### Release

Any supported release

### Cause

The flow fails because the Insert Record action attempts to create a record without satisfying the data policy requirements on the target table. In this example, the data policy requires a value for the Assigned to field in the Change Request table.

### Resolution

When this error occurs, you'll see a message similar to:

"Flow Designer: Operation failed with error: com.snc.process\_flow.exception.OpException: Error occurred while inserting record: Data Policy Exception: The following fields are mandatory: Assigned To"

To resolve this issue:

-   Add the required field value in the Insert Record action. For the previous example, set a value for the Assigned to field in the Change Request table.
-   Alternatively, modify the data policy to make the field optional if appropriate for your business requirements.

### Related Links

For the latest information, see [Create record action](https://docs.servicenow.com/csh?topicname=create-record-flow-designer.html&version=latest).
