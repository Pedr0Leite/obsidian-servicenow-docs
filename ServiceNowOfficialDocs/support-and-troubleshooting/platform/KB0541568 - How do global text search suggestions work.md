---
title: "How do global text search suggestions work?"
aliases:
  - KB0541568
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0541568
kb_number: KB0541568
last_modified: 2025-01-26
---

## Issue

When ServiceNow customers do global text searches they often see suggested search terms based on the characters they have entered into the field. This article describes exactly how these suggested values are determined.

### Procedure

Every text search users do is captured in a table called text\_search. The "TS Search Stats" scheduled job then calls our java code to populate the ts\_search\_stats table.

It begins by looking at all the record that fall into the stat search window which is controlled by the glide.ts.search\_stat\_window system property. If there is no property in the instance, it defaults to 365 days.

The job does an aggregate query within the date range and orders the results by search term and then adds records to the ts\_search\_stats table. Please be aware that records in the ts\_search\_stats table are restricted by access controls such that you will not be able to read them. If you want to see the records in that table then you will need to enable the admin overrides on the read ACL for that table.

When you type into the text search box, it runs a search against the ts\_search\_stats table as follows:

-   The search\_term column starts with the characters entered  
      
    
-   The mean\_hits column value is greater than zero

The results are then ordered by search\_count, mean\_hits, and search\_term. Search results are limited to whatever the maximum # of choices is set to in the glide.xmlhttp.max\_choices system property. Be very cautious about increasing this property as making it too large can result in performance degradation. This is because we do an asynchronous round trip to the server and more results means a larger data set being returned which can increase the time it takes to display.

## Additional Information

Please note that global text search suggestions do not work in UI16 as of the Geneva release. This was an intentional design change due to performance concerns and is documented in PRB669534. The feature may return in a later release if it can be done with a minimal performance impact.
