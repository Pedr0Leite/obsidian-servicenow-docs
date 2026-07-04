---
title: "SLAs are not being generated for one customer"
aliases:
  - KB0778512
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0778512
kb_number: KB0778512
last_modified: 2024-04-08
---

## SLAs are not being generated for one customer

  

### Issue

The user is having some issues with SLAs for one customer. Start conditions on the SLA Definitions are matching and true, but the expected task\_slas are not attaching.

### Cause

The user has deeply customized two main SLA-related Script Includes.

### Resolution

As mentioned above, through research of the affected instance and the issue at hand, it was found that two major customizations were made to the OOB SLA process:

-   Script Includes:
    -   **SLAConditionBase**: Out of Box (OOB) has 175 lines. The current version in the user's Production instance has 97 lines. That is nearly half the code missing ( ref: /nav\_to.do?uri=sys\_script\_include.do?sys\_id=6cbf4dca7f000001763341f65c6ff1cd ).
    -   **TaskSLAController**: OOB has 923 lines. The user's current version in their Production instance has 460 lines. That is near 500 lines of code missing ( ref: /nav\_to.do?uri=sys\_script\_include.do?sys\_id=24a759e30a0a2c3960e024ad3b60d9e8 ).

The investigation cannot move forward until or unless the customizations made to these two core SLA Script Includes are reverted back to Out of Box (OOB).  
  
Support engineers are experts in OOB behavior and specialize in resolving OOB break-fix behaviors. Unfortunately, the debugging and implementing of customizations like this is not in the engineer's area of expertise. This is no longer an OOB SLA environment.

Until an OOB environment/SLA process is in place, customizations cannot be ruled out as the root of the issue.
