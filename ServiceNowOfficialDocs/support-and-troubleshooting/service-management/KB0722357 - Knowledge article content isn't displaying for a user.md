---
title: "Knowledge article content isn't displaying for a user"
aliases:
  - KB0722357
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0722357
kb_number: KB0722357
last_modified: 2024-04-07
---

## Knowledge article content isn't displaying for a user

  

### Issue

Some Knowledge articles' content is not visible for a user

### Release

ALL

### Cause

After a thorough investigation, this behavior is a result of the users' customization of a OOB (Out of Box) UI Page plus an additional custom UI Macro.

### Resolution

it was found that the behavior seen stems from fields referenced in two customizations:  
  

-   kb\_view\_customer UI Page   
    -   /nav\_to.do?uri=sys\_ui\_page.do?sys\_id=1f5e464b0a0a0b3200dbbe75f65063e4
-   kb\_view\_custom UI Macro  
    -   /nav\_to.do?uri=sys\_ui\_macro.do?sys\_id=7edf96502d2030405736db840fdcb970

  
Support Engineers are experts in OOB functionality and specialize in OOB break-fix behaviors. The debugging and implementing of custom code are not in the Engineer's area of expertise, unfortunately.  
  
Therefore, it was recommended that the user kindly review these customizations with the team who developed them as that team has a firm understanding of what the customizations are trying to accomplish as well as a more intimate knowledge of the users' environment.
