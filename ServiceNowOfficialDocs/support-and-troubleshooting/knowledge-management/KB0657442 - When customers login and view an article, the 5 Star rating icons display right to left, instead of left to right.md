---
title: "When customers login and view an article, the 5 Star rating icons display right to left, instead of left to right"
aliases:
  - KB0657442
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0657442
kb_number: KB0657442
last_modified: 2024-04-07
---

## When customers login and view an article, the 5 Star rating icons display right to left, instead of left to right

  

### Issue

When viewing an article, the Stars rating icons display right to left instead of left to right. 

  

**Steps to Reproduce**  

* * *

**Note** – This occurs for all users, all browsers, only when they log in their instance. When SN TSEs access the instance, everything displays correctly, even when impersonating users.

1.  Navigate to **Self Service > Knowledge**.
    
2.  Select the Knowledge Base.
    
    Notice the Star rating next to article display left to right (as expected).
    
3.  Go into the article to view.
    
    When clients log in (unexpected): The rating stars for the article are displayed right to left.
    
    When we follow the same steps (even when replicating different users): The stars display as expected left to right.
    

### Cause

Customer has customized the Knowledge Common Styles style sheet: <instance-name>/nav\_to.do?uri=content\_css.do?sys\_id=b3ba3821d73221004792a1737e610382

  

  

### Resolution

Import OOB Knowledge Common Styles style sheet.
