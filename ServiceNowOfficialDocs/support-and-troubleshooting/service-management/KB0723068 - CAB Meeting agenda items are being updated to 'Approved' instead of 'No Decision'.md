---
title: "CAB Meeting agenda items are being updated to 'Approved' instead of 'No Decision'"
aliases:
  - KB0723068
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0723068
kb_number: KB0723068
last_modified: 2024-04-07
---

## CAB Meeting agenda items are being updated to 'Approved' instead of 'No Decision'

  

### Issue

# Symptoms

* * *

When we move to the next agenda item, it will mark the item as Approved

# Release

* * *

London Patch 2

# Cause

* * *

This is the expected behavior when the Agenda Item is in the "New" state (when there are no approvals for the agenda item). 

# Resolution

* * *

Adding changes (agenda items) that do not have an approval record will do this. CAB is an extension of the approval mechanism for change, if there isn't an approval record, it will be approved.
