---
title: "Slowness On a transaction because of slow db_context_menu loading"
aliases:
  - KB0789962
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0789962
kb_number: KB0789962
last_modified: 2024-02-28
---

## Issue

The form to add CIs to a change request takes excessively long to load

Steps to reproduce:

1.  Navigate to the Change Request form
2.  View existing change
3.  Navigate to the bottom of the form, and select 'Add' under the 'Affected CIs' tab
4.  Wait for the form to load

## Resolution

Delete a big amount of the high volume of labels in order to make the 'Add New CI' form faster.
