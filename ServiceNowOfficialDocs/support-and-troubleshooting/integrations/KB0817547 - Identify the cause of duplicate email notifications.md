---
title: "Identify the cause of duplicate email notifications "
aliases:
  - KB0817547
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0817547
kb_number: KB0817547
last_modified: 2025-12-12
---

## Issue

Identify and resolve possible causes of duplicate email notifications. 

## Resolution

To resolve this: 

-   Disable the duplicate business rule
-   Correct the business rule logic 

Using the previous example, update the script as shown to eliminate the duplicate notifications. 

  
if ((current.state.changesTo(-11')))   
{  
gs.eventQueue("event\_name", current, current.comments, current.comments);  
}

  
**Note:** Test the script on a sub-production instance before implementing on a production instance.

## Related

- [[KB0724449 - Duplicate email notification were sent from the instance when it was not intended]] - the OOB "Ignore duplicates" business rule this article extends
