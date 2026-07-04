---
title: "Knowledge articles are not obeying alphabetical sorting"
aliases:
  - KB0853134
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0853134
kb_number: KB0853134
last_modified: 2024-04-08
---

## Knowledge articles are not obeying alphabetical sorting

  

### Issue

The user reported that a single Knowledge Article (KA) was not obeying alphabetical ordering, and they wanted to know why this was.

### Resolution

After an in-depth investigation into the SQL statements associated with the KA (checking what ORDERBY clause was used), the source code of the KA to see if any erroneous formatting was found (such as special characters), and the XML of the KA, there was no sign of any issue.  
  
Finally, a query was run from the back-end and it was found that there was a space preceding the title of the article. Unfortunately, this space did not appear on the front-end UI.  
  
Here is what the user saw: "General Knowledge Article"

Here is what displayed per the back-end: " General Knowledge Article"  
  
As a result of the space, and as per ASCII sorting, anything with a space in front of letters comes last alphabetically. Therefore, this (mis)sorting is by design as per the back-end values, albeit completely unexpected based on front-end values.  
  
There are two paths to correct this issue:

1.  Create a case for the _CS - Platform Technologies_ group of Subject Matter Experts to run a quick change in the back-end to remove the space preceding the article title, or  
    
2.  Recreate the article. This will cause the user to lose the history of the article (say, if versioning is enabled and the article has some amount of history on it), but it should resolve the issue as this is an extremely rare occurrence
