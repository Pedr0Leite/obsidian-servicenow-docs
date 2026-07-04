---
title: "\"Show Workflow\" Related Link is missing on Requested Item (RITM)"
aliases:
  - KB0998274
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0998274
kb_number: KB0998274
last_modified: 2024-09-20
---

## "Show Workflow" Related Link is missing on Requested Item (RITM)

  

### Issue

The user noted that on their Requested Item (RITM) record, the "Show Workflow" Related Link was not present on the form. They wanted to know why.

### Cause

The parent Request (REQ) is not approved. Therefore, there is no context on the Requested Item (RITM). Due to this, the UI Action is failing it's condition.

### Resolution

As shared above, in the user's example record, the REQ's Approval field is set to "Requested".

Because this is "Requested", and has not been set to "Approved", the "Cascade Request Approval to Requested Item" Out of Box (OOB) Business Rule has not fired to pass the parent REQ's approval to the child RITM, thus kicking off the workflow and triggering the UI Action to show under the Related Links once a workflow context is created and attached.

Therefore, the "root" of this issue is the failure to approve the parent REQ.

OOB, this approval is typically handled by the "Service Catalog Request" workflow, which has an automatic approval if the item being requested is less than $1,000.00 in cost. This is a demo-data workflow that is shipped OOB.

The parent REQ's workflow in the user's example was not the OOB "Service Catalog Request", but rather a custom "Special Service Catalog Request" workflow which does not have any marking of Approval to "Approved" inside. This is the issue.

It was recommended to the customer to implement an approval to the REQ. This will mark the REQ as approved, trigger the OOB BR, and kick off the workflow on the child RITM and thus satisfy the UI Action's condition and show the "Show Workflow" Related link.
