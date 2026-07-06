---
title: "How to synchronize a discovery pattern with MID server after pattern modifications."
aliases:
  - KB0745146
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0745146
kb_number: KB0745146
last_modified: 2024-04-07
---

## How to synchronize a discovery pattern with MID server after pattern modifications.

  

### Issue

# Description

After making modifications to the patterns, that should be synchronized to the mid server.

# Procedure

Click the UI action **'Synchronize with MID Servers'**.  
  
This UI action can be viewed by users with pd\_admin or evt\_mgmt\_admin roles.To edit this go to the below link and edit the condition.

```
https://<instance-name>.service-now.com/nav_to.do?uri=sys_ui_action.do?sys_id=8ada83e1ff020200ab8fffffffffffa8
```

![](sys_attachment.do?sys_id=064c246edb42b450e515c223059619bc)

Method 1:

-   Go to sa\_pattern or sn\_discovery\_patterns table.
-   Select the pattern that should be synchronized with the mid server.
-   Under 'Actions on selected rows' click 'Synchronize with MID Servers'

![](sys_attachment.do?sys_id=d64c246edb42b450e515c223059619c1)

  
Method 2:  
  

-   Go to sa\_pattern table.
-   Open the respective pattern.
-   Under Related Links click 'Synchronize with MID Servers' UI action.

![](sys_attachment.do?sys_id=9e4c246edb42b450e515c223059619eb)

# Applicable Versions

All
