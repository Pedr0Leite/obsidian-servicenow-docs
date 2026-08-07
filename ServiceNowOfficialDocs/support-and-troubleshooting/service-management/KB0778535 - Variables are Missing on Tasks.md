---
title: "Variables are Missing on Tasks"
aliases:
  - KB0778535
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0778535
kb_number: KB0778535
last_modified: 2024-04-08
---

## Variables are Missing on Tasks

  

### Issue

The user has two variables which are missing on their SCTASK record even though they have specified that they should be carried over in their Catalog Task workflow activity via the slush bucket.

### Cause

A custom Catalog UI Policy is the culprit, and why the user is seeing the behavior.

### Resolution

As mentioned above, the custom Catalog UI Policy is causing the issue.

The user can easily test this by navigating to the policy and setting it to active = false.

Then, when they reload the affected SCTASK record, both of the previously hidden variables display properly, per the user's expectation.
