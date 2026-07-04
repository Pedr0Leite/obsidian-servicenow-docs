---
title: "'sys_flow_context' table is not selectable in Flow Designer trigger Table list"
aliases:
  - KB0860684
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0860684
kb_number: KB0860684
last_modified: 2024-04-08
---

## 'sys\_flow\_context' table is not selectable in Flow Designer trigger Table list

  

### Issue

"sys\_flow\_context" is not by default selectable in Flow Designer trigger Table list.

### Cause

"sys\_flow\_context" is by default not included in the flow trigger table list, because it can cause loops easily if the trigger condition is not carefully designed.

For example, trigger on "sys\_flow\_context" record created/updated with no conditions will immediately cause infinite loops and creating huge amount of the flow contexts in the system when triggered. Which will cause high impact outage to the instance.

### Resolution

Add "sys\_flow\_context" to "sn\_flow\_designer.allowed\_system\_tables" system property.

But to trigger flow on flow contexts is not recommended, include the logic in your flow design as subflow should meet the requirements in most cases.
