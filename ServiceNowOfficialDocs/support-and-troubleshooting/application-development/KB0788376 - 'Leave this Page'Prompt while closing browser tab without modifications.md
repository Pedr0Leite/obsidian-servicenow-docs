---
title: "'Leave this Page'Prompt while closing browser tab without modifications"
aliases:
  - KB0788376
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0788376
kb_number: KB0788376
last_modified: 2024-04-20
---

## 'Leave this Page'Prompt while closing browser tab without modifications

  

### Issue

A message appears that you are leaving the page without saving the record prompts even if you just open the page and leave without making any interaction to it or just reloading the page.

### Cause

'Leave this Page' prompt appears when a setValue() is passed on on-load via client scripts or UI policies OR a 'Clear a field Value' is check on UI policy action

### Resolution

Check for onLoad Client scripts and UI policies Run scripts to see any setValue() is passed on load and comment setValue() and check for prompt appears or not on loading the record.

Similarly, check for UI policies executing on the affected record and open the UI policy actions under it. If 'Clear the field Value' is checked, every time the record loads whether value defined or not on the field, this check allows to clear the field value and this modification forces prompt to appear 'Changes you made may not be saved.'. Uncheck the 'Clear the field Value' field, this will fix the issue
