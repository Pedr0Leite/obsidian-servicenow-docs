---
title: "Optimize flow performance when working with large flows"
aliases:
  - KB0856136
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0856136
kb_number: KB0856136
last_modified: 2025-08-28
---

## Optimize flow performance when working with large flows

  

### Issue

Large flows with many elements can cause UI performance issues when scrolling, editing, or relocating steps. This article provides guidance on improving performance for flows with numerous activities.

### Release

All releases

### Resolution

There is no fixed limit on flow size (actions, logic, and other elements). For optimal performance:

-   Create flows in an application scope instead of the Global scope.
-   Consider breaking large flows into smaller, linked flows.
-   Minimize the number of elements in a single flow when possible.

Scope selection significantly impacts flow performance.

### Related Links

Community article: [Why Flow Designer is slow](https://www.servicenow.com/community/servicenow-ai-platform-forum/why-flow-designer-is-slow/m-p/1161076)
