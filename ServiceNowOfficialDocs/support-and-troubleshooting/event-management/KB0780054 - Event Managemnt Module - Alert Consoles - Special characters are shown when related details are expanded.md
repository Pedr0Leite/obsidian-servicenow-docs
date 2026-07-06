---
title: "Event Managemnt Module - Alert Consoles - Special characters are shown when related details are expanded"
aliases:
  - KB0780054
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0780054
kb_number: KB0780054
last_modified: 2025-01-03
---

## Issue

In Event Management Alert Consoles, when related details are expanded either to show Secondary Alerts or Events, special characters are visible like (&nbsp;).

  

## Resolution

Set the system property: glide.ui.escape\_text, to true and this should resolve the issue. Sometimes you might need to logout and log back in to see the changes as there might be a cache issue.
