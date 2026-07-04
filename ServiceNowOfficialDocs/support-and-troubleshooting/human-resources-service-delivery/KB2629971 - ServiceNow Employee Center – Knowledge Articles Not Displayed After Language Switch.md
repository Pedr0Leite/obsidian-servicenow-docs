---
title: "ServiceNow Employee Center – Knowledge Articles Not Displayed After Language Switch"
aliases:
  - KB2629971
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB2629971
kb_number: KB2629971
last_modified: 2026-01-01
---

## ServiceNow Employee Center – Knowledge Articles Not Displayed After Language Switch

  

### Issue

When a user switches their preferred language in the Employee Center portal from a non-English language to English, knowledge base articles do not display according to the updated preference until the user logs out and logs back in.  
The issue occurs only when switching from a non-English language to English; switching from English to another language does not cause the problem.  
  

### Release

Any Release

### Cause

The system property enable\_topic\_content\_lang\_fallback being set to false prevents immediate fallback to English content when the language is changed.

### Resolution

-   Enable the system property **enable\_topic\_content\_lang\_fallback** to allow content fallback when switching languages.
-   If the property must remain false due to business requirements, apply a customization or update set to handle language preference changes dynamically.
-   After implementing the update set or enabling the property, test by switching languages and verify that knowledge articles display correctly without requiring logout or cache clear.
