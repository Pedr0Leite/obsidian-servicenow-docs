---
title: "Custom action with input variable of type JSON is not accepting my data pills"
aliases:
  - KB0829979
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0829979
kb_number: KB0829979
last_modified: 2024-04-08
---

## Custom action with input variable of type JSON is not accepting my data pills

  

### Issue

-   the action's input variable of type "JSON" is very picky about what data pills can be put inputted
-   In this example, we will get getting the sys\_id of the requested item trigger record, so a flow with a "service catalog" trigger

### Resolution

-   create a custom action, with one input of type reference.sc\_req\_item
-   the input of this flow will be the Requested Item trigger record back in the main flow
-   add a script step, get the sys id of the reference record and add it to your output variable of type string
-   Then use the output of the custom action in your other action's input to build your JSON object
