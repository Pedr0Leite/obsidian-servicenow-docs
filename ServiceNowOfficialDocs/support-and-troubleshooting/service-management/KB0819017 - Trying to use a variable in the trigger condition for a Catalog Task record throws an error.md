---
title: "Trying to use a variable in the trigger condition for a Catalog Task record throws an error"
aliases:
  - KB0819017
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0819017
kb_number: KB0819017
last_modified: 2024-04-08
---

## Trying to use a variable in the trigger condition for a Catalog Task record throws an error

  

### Issue

If you try to use a variable in the trigger condition for a Catalog Task record (sc\_task) then the condition will not save and the console will show the error:

angular\_includes\_1.4.jsx?v=03-02-2020\_2243:109 ReferenceError: $j is not defined  
at Comparison.toQueryString (js\_includes\_filter\_widget.jsx?v=03-02-2020\_2243&lp=Tue\_Jan\_07\_19\_14\_40\_PST\_2020&c=5\_55:3539)  
at js\_includes\_filter\_widget.jsx?v=03-02-2020\_2243&lp=Tue\_Jan\_07\_19\_14\_40\_PST\_2020&c=5\_55:967  
at Array.filter (<anonymous>)  
at js\_includes\_filter\_widget.jsx?v=03-02-2020\_2243&lp=Tue\_Jan\_07\_19\_14\_40\_PST\_2020&c=5\_55:966  
at Array.forEach (<anonymous>)  
at js\_includes\_filter\_widget.jsx?v=03-02-2020\_2243&lp=Tue\_Jan\_07\_19\_14\_40\_PST\_2020&c=5\_55:965  
at Array.forEach (<anonymous>)  
at js\_includes\_filter\_widget.jsx?v=03-02-2020\_2243&lp=Tue\_Jan\_07\_19\_14\_40\_PST\_2020&c=5\_55:964  
at Array.forEach (<anonymous>)  
at Object.filterEmptyComparisonsFromGlideQuery (js\_includes\_filter\_widget.jsx?v=03-02-2020\_2243&lp=Tue\_Jan\_07\_19\_14\_40\_PST\_2020&c=5\_55:963)

### Cause

Currently using variables from a Catalog Task (sc\_task) is not supported.

### Related Links

There are enhancement requests on the idea portal that can be voted on to increase the change this will get implemented.
