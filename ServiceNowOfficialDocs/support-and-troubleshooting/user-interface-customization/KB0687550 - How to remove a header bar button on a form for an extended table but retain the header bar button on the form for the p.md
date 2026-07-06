---
title: "How to remove a header bar button on a form for an extended table but retain the header bar button on the form for the parent table."
aliases:
  - KB0687550
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0687550
kb_number: KB0687550
last_modified: 2025-01-03
---

## How to remove a header bar button on a form for an extended table but retain the header bar button on the form for the parent table.

  

### Issue

How to remove a header bar button on a form for an extended table but retain the header bar button on the form for the parent table.

### Release

all

### Resolution

1\. Go to the UI action record corresponding to the button.  
  
2\. In the Condition field of the UI action record, append a condition after the current Condition value. Make sure there's a space character between the existing value and the additional condition if you're copying/pasting.   
  
&& current.getTableName() != 'extended\_table\_name'  
  
3\. Click the Update button.
