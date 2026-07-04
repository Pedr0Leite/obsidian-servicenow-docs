---
title: "Cannot send out surveys via Send Invitations UI action"
aliases:
  - KB0688900
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0688900
kb_number: KB0688900
last_modified: 2024-04-07
---

## Cannot send out surveys via Send Invitations UI action

  

### Issue

# Symptoms

* * *

When assigning surveys via the Send Invitations UI action, a message is displaying that no new invitations were sent.

# Release

* * *

Jakarta Patch 6

# Cause

* * *

There were existing surveys in the ready state from the previous 'Send Invitations' although the due date had already past.

# Resolution

* * *

Modify the 'Cancel Expired Assessments' scheduled job to run more frequently so that the previous surveys can be canceled.
