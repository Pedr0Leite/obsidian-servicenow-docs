---
title: "RITM request has been approved without clicking on \"Approve\" button"
aliases:
  - KB0781553
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0781553
kb_number: KB0781553
last_modified: 2024-12-13
---

## RITM request has been approved without clicking on "Approve" button

  

### Issue

RITM request has been approved just by replying and not clicking the "Approve" button.

### Cause

The Email Inbound Action: "Update Approval Request" has processed the Approval request which has been customized.

### Resolution

Fix this Email Inbound Action: "Update Approval Request" by adding conditions or by making necessary changes in the script to resolve the issue.  
OR  
Revert the Email Inbound Action to the OOB Version.
