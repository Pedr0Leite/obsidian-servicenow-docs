---
title: "Awaiting Acceptance state is getting skipped and HR cases goes straight through Close Complete "
aliases:
  - KB3018681
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB3018681
kb_number: KB3018681
last_modified: 2026-05-14
---

## Issue

When clicking the UI Action 'Close Complete' in HR Agent Workspace on a Case, instead of going to 'Awaiting Acceptance' status, it goes straight to 'Close Complete'.

when using the native UI and closing a case there, the state goes to 'Awaiting Acceptance'. The HR Service configuration shows no Case option to skip the Awaiting acceptance status.  
  

## Resolution

1\. Activate the Business Rule 'Add User Acceptance State' which controls the transition to the Awaiting Acceptance state.

The BR is currently inactive 725330019f22120047a2d126c42e70fa.

2\. Revert the Business Rule to the latest Out-of-the-Box (OOB) version if necessary.

3\. Verify if the issue is resolved after activating and reverting the Business Rule.
