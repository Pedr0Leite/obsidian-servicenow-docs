---
title: "Software Asset workspace overview Dashboard we are not able to see the data in domain but we can see under global domain."
aliases:
  - KB2701828
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB2701828
kb_number: KB2701828
last_modified: 2026-01-01
---

## Issue

In a domain-separated environment, when users switch the domain context from Global to a non-Global domain in Software Asset Workspace → Software asset overview, multiple widgets (for example, compliance-related widgets) display “No data available”, even though data is expected.

## Resolution

1.  Navigate to Performance Analytics → Jobs (PA jobs list / sysauto\_pa).
2.  Locate the job “**SAM - Data collection**” and set it to Active.
3.  Execute the job (Run/Execute Now) and confirm it completes successfully in PA Job Logs (job run history).
4.  Go back to Software Asset Workspace → Software asset overview, switch to the required non-Global domain, and refresh the page — the widgets should now populate with data.
