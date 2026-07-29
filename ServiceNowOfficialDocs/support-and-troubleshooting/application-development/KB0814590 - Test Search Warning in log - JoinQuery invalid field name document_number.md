---
title: "Test Search: Warning in log - JoinQuery invalid field name: document_number"
aliases:
  - KB0814590
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0814590
kb_number: KB0814590
last_modified: 2024-04-08
---

## Issue

Unexpected messages are seen in logs when the user executes a text search (or global search):  
  
WARNING \*\*\* JoinQuery invalid field name: document\_number  
WARNING \*\*\* JoinQuery invalid field name: position  
  
  
Steps to reproduce:

1\. Navigate to incident\_list.do  
2\. Perform a keywords search \[Use the \`for text\` Search\]

## Resolution

This is not considered a bug eg. there is no fix for this. Just ignore these messages in the logs.

## Additional Information

Development has confirmed that this is not considered a problem.

Enhancement request has been raised:  
PRB1386584 Remove warning in log - JoinQuery invalid field name: document\_number
