---
title: "How to resolve Copy Attachment action errors in Flow Designer"
aliases:
  - KB0813220
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0813220
kb_number: KB0813220
last_modified: 2025-08-11
---

## How to resolve Copy Attachment action errors in Flow Designer

  

### Issue

When you configure Flow Designer to copy attachments from one record to another using the Copy Attachment action, you may see the following error and the attachments don't appear on the target record.

Error message: "The Record type sc\_req\_item does not match with Attachment table type."

### Release

Any supported release

### Cause

When you configure the Lookup Attachment action with only the triggered record sys\_id, the Copy Attachment action cannot determine the attachment sys\_id in the source record. This happens because the location or table where the attachment is stored isn't defined.

Using the Lookup Record action retrieves the attachment record to pass into the Copy Attachment action.

### Resolution

To copy attachments from one record to another:

1.  Look up the attachments from the triggered record ID.
2.  Look up the record with the lookup attachment sys\_id from the sys\_attachment table.
3.  Configure the Copy Attachment action with the source record set as the attachment record from the Lookup Record action.
4.  Save and activate the flow.
5.  Test the flow with an existing record or by submitting a new request with an attachment.
