---
title: "Using the output of \"Look Up Records\" action inside an custom action"
aliases:
  - KB0831437
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0831437
kb_number: KB0831437
last_modified: 2025-01-03
---

## Using the output of "Look Up Records" action inside an custom action

  

### Summary

-   how to use the output of "Look Up Records" action in a custom action
-   the custom action has an input of type "records" with the reference table of the "Look Up Records"
-   So now that it's in the action, now what?

### Instructions

-   to obtain for example the sys\_id's of all the records brought into the action into an array name "list," do the following:
-   add a script step
-   attach the action's input to the script step's inputs
-   from the script do the following:
-   input.<lookRecords\_output>.query()  
    while (input.<lookRecords\_output>.next() {  
        list.push(input.<lookRecords\_output>.sys\_id);  
    }
-   We use the query() and next() because the object we're passing into the custom object is GlideRecord
