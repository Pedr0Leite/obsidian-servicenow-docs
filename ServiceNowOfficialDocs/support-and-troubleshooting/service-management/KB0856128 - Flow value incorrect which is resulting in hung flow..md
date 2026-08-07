---
title: "Flow value incorrect which is resulting in hung flow."
aliases:
  - KB0856128
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0856128
kb_number: KB0856128
last_modified: 2024-04-08
---

## Issue

-   The approval record generated from the flow was "Approved"
-   Once the approval is done, The flow updates the requested item Approval
-   Then the flow checks if the item is approved. In this scenario, the flow logic was evaluated to "false". It should have been evaluated to "true" since the approval was approved.

## Resolution

Add Wait for Duration on the flow before checking for the Approval field in the RITM.
