---
title: "Not able to view the the UX Page Properties lists."
aliases:
  - KB0999365
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0999365
kb_number: KB0999365
last_modified: 2024-10-12
---

## Not able to view the the UX Page Properties lists.

  

### Issue

The four UX Page properties listed in the "Display the form ribbon and form header secondary values in the contextual side panel" documentation are not appearing in the list.

Properties:

-   ribbonLocation
-   record\_secondary\_values\_location
-   ribbonLocation\_interaction
-   interaction\_secondary\_values\_location

Please refer to the following Doc for additional info.

https://docs.servicenow.com/bundle/rome-customer-service-management/page/product/customer-service-management/task/config-csm-display-header-in-sidebar.html

### Cause

If you have upgraded your instance to Rome, the four-page properties are not automatically installed with the update. Only zbooted instances starting in Rome would contain these four-page properties.

### Resolution

As a solution, you can manually create these four-page properties to change the ribbon and secondary value views to the sidebar.

This can be done by navigating to Now Experience Framework > Experiences > CSM/FSM Configurable Workspace and then creating the four properties listed in our document in the UX Page Properties list and set the values to sidebar.
