---
title: "Discovery error: Multiple paths leading to the same destination"
aliases:
  - KB0694749
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0694749
kb_number: KB0694749
last_modified: 2026-06-27
---

## Issue

When running patterns with Service Mapping or Discovery you come across an error like the following:

-   "Multiple paths leading to the same destination: \[class:cmdb\_ci\_\[SOME\_CLASS\], sys\_id:\[SOME SYS\_ID\]\] -> \[class:cmdb\_ci\_\[SOME\_CLASS\]\], sys\_id:\[SOME SYS\_ID\]\]"

## Resolution

\*\*\*This resolution will use the following example error message\*\*\*

Multiple paths leading to the same destination: \[class:cmdb\_ci\_appl\_peoplesoft, sys\_id:33418429db239f008ef67d9bbf961924\] -> \[class:cmdb\_ci\_linux\_server, sys\_id:2722c581db956644c9e9fd39bf96195b\]

1.  Go to the cmdb\_rel\_ci table by typing in cmdb\_rel\_ci.list into the filter navigator of the instance. 
2.   Copy both sys\_ids:   
    -   Parent sys\_id: 33418429db239f008ef67d9bbf961924   
        Child sys\_id: 2722c581db956644c9e9fd39bf96195b 
3.  Using the table's filter, set the following:   
    -   Parent.sys\_id = 33418429db239f008ef67d9bbf961924   
        AND   
        Child.sys\_id = 2722c581db956644c9e9fd39bf96195b 
4.  In the result of the search you should see more than one record (could be 2 or more) where they have the same parent, child, and type. 
5.   If you sort that list by created date, go ahead and delete all of the duplicates except for one. (recommend deleting all the oldest ones and keeping the newest created one). 
6.  After that you can run the discovery or service map again.
