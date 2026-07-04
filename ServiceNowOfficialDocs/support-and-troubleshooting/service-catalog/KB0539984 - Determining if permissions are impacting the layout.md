---
title: "Determining if permissions are impacting the layout"
aliases:
  - KB0539984
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0539984
kb_number: KB0539984
last_modified: 2024-05-01
---

## Determining if permissions are impacting the layout

  

### Issue

Determining if permissions are impacting the layout

#   

# Symptoms

* * *

-   No variables appearing on the form.
-   Variable has incorrect layout.

#   

# Resolution

* * *

The variables may not appear correctly, even after

-   they have been ordered correctly
-   placed inside the correct containers
-   the layouts have been set up properly

If this occurs, read permissions may be blocking the variables from appearing correctly.

To view permissions for the variables, the easiest way is to add the **Read roles** column to the **Variables** related list on the relevant catalog item:

    ![](/sys_attachment.do?sys_id=d41be42adb42b450e515c22305961967)

# **Using Read Roles**

* * *

If a variable is set up with read roles, it does not appear to users without those roles.

For example, this item has the itil read role associated with the **Provide Date/Time** variable:

![](/sys_attachment.do?sys_id=dc1be42adb42b450e515c22305961975)

  

Users with the itil role see the **Provide Date/Time** variable:

  

![](/sys_attachment.do?sys_id=5c1be42adb42b450e515c22305961990)

  

Users without the itil role do not see the **Provide Date/Time** variable:

  

![](/sys_attachment.do?sys_id=a81be42adb42b450e515c223059619a3)

In this example, the variable layout also alters because the **Provide Date/Time** variable is not displayed and moves positions. The **Provide Date/Time** variable fails to appear and changes position because the variable before it is not available for the logged in user. Be aware that this can cause layouts to appear inconsistently. 

# Roles on Container Records

* * *

Setting roles on container records can have a confusing impact. If a container is set up for a role that the logged-in user does not have, all the variables within the container are hidden. For example:

![](/sys_attachment.do?sys_id=601be42adb42b450e515c223059619f1)

In this example, a user without itil does not see any variables:

  

![](/sys_attachment.do?sys_id=f41b282adb42b450e515c2230596196f)

Also see [KB0539982: Determining if you are using the correct container variable](/kb_view.do?sysparm_article=KB0539982 "KB0539982: Determining if you are using the correct container variable").

  

# Create Roles and Visibility

* * *

Create roles do not impact the visibility of the whole variable. If the variable you are restricted from writing to has a default value, you can see, but not edit, the value. If that variable has no default value, you can only see the variable name, not the inputs of the variable at all.

The following example shows all variables that are restricted by create roles to itil only:  
  

![](/screencapture-116.pngx)
