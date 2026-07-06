---
title: "How to query the alert management rules by conditions in \"Alert filter\" field within \"Alert management rules\" table list view"
aliases:
  - KB0748277
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0748277
kb_number: KB0748277
last_modified: 2025-01-03
---

## How to query the alert management rules by conditions in "Alert filter" field within "Alert management rules" table list view

  

### Issue

# Description

Most of the time customers have a large number of Alert Management rules in the instance. They wanted to be able to filter their rules, using the 'Alert Filter'.

'Alert Filter' allows you to create compound conditions.  This field has type of 'Conditions' in dictionary, which extends the type string. 

There may be a requirement to create a query in "Alert management rules" table list view, to filter results based on this field.  This article describes the procedure for this.

To demonstrate this we will assume that we have a alert rule with 'Alert Filter' set to use node, keywords, description and short description as displayed in the below screenshot

![](sys_attachment.do?sys_id=7bdca022db82b450e515c223059619c4)

The requirement is to search for 'Alert Management Rules', where 'Alert Filter' has:

1.  node=dev1234\*
2.  node=dev1234\* AND short\_description contains nagios,openview,scom  
      
      
    

# Procedure

-   Do not try to put a compound conditions in the one field for Alert Filter e.g. condition1^condition2^condition3, even though it seems intuitive.
-   Create a series of 'Alert Filter' queries which are AND'd together.
-   We can't use wildcards e.g. \* but you use substrings along with 'contains'/'does not contain' operations, to get closer to what you want.

E.g.

![](sys_attachment.do?sys_id=3fdca022db82b450e515c223059619c9)

This procedure is handy in the scenario where there are many alert management rules with very similar (but still distinct) alert filters.

# Applicable Versions

All (prior to London - alert filter is in Alert Action Rules)
