---
title: "Optimize widget rendering time on responsive dashboards"
aliases:
  - KB0635324
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0635324
kb_number: KB0635324
last_modified: 2026-04-20
---

## Optimize widget rendering time on responsive dashboards

  

### Issue

### Overview of types of dashboards

Two types of dashboards exist: [Responsive](https://docs.servicenow.com/csh?topicname=c_ResponsiveDashboards.html&version=latest "Responsive") and [Non-responsive](https://docs.servicenow.com/csh?topicname=non-responsive-dashboards.html&version=latest "Non-responsive"). To determine which type you are using, click **Edit** on a dashboard.

-   Responsive dashboards have the context menu ("hamburger") button on the top left side. Users with editing rights will see the **Add Widget** (![Add Widget button](sys_attachment.do?sys_id=90ef59f4db0d741022e0fb24399619ec)) and **Quick Layout** (![Quick Layout button](sys_attachment.do?sys_id=dcef59f4db0d741022e0fb24399619ed)) buttons appear.  
      
    ![](/sys_attachment.do?sys_id=bdfca822db82b450e515c223059619c6)  
      
    
-   On non-responsive dashboards, the **Change layout** button appears for users with edit permissions. All users will have a **link** icon, a **favorite** icon, and **refresh** icon.  
      
    ![](sys_attachment.do?sys_id=31fca822db82b450e515c223059619cc)

  

### Advantages of responsive dashboards

Responsive dashboards improve the creation and management of dashboard content. They are not enabled by default (prior to Istanbul), and must be enabled by an admin. Set the _**glide.cms.enable.responsive\_grid\_layout**_ system property to true. If this property does not exist, you can create it.

![](/sys_attachment.do?sys_id=71fca822db82b450e515c223059619d1) 

Responsive dashboards are active and enabled by default for new customers since Istanbul. Customers who upgraded from previous versions to Istanbul or later need to enable responsive dashboards manually by setting the system property to true.

Some of the many advantages of using responsive layouts are:

-   The ability to drag to move and resize widgets.
    
-   Create and edit reports, Performance Analytics, and other widgets directly from the dashboard by clicking the pencil icon on the widget that displays the editor page for that widget.
    
-   Use the Add Widget pane to quickly find and preview widgets to add to the dashboard.
    
-   Use quick layouts to snap widgets into a predefined layout, then adjust the layout as desired.
    
-   The permission system applies to all dashboards and all users, and you need to explicitly share your dashboard for others to be able to view or edit it.
    
-   Lazy loading: Only visible widgets load. More widgets load as the user scrolls down in order to reduce load on the system and speed up the loading of initial widgets.
    

  

### How to optimize how widgets load

To improve the overall performance of your dashboards, you can use the _**glide.canvas.grid.widget\_render\_concurrent\_max**_ system property to optimize how widgets load. 

<table class="noteTable" style="border: 1px solid #e0e0e0; width: 100%; border-spacing: 5px; background-color: #f5f5f5;"><tbody><tr><td style="text-align: center; padding: 5px;" width="25"><img title="Note" src="https://support.servicenow.com/Note_25x.pngx" alt="Note icon" align="bottom"></td><td style="text-align: left; padding: 5px;" width="100%"><strong>Note:</strong> This system property applies to responsive dashboards only.</td></tr></tbody></table>

**Type:** Integer

**Default value:** 3 if the property is not manually set. The minimum value is 2 if the property is manually set.

**Location:** Add to the System Property \[sys\_properties\] table.

**Behavior:**

-   Defines the maximum number of widgets that render simultaneously on a dashboard. With smaller values, individual sets of widgets load more quickly. With larger values, fewer requests to the server are made.
    
-   Widgets that are outside of the screen do not load at all until you scroll past them.
    
-   If the value is set to a low number, a slow widget blocks fewer widgets from loading. The widgets visible on the dashboard take slightly longer to load because more requests are sent to the server. Setting a value of less than 2 causes all widgets that are visible above the page “fold” to be loaded at once.
    
    For example: If a very large monitor allows you to see 10 widgets at once, then 10 will be loaded in a single request. If the monitor is small, or you shrunk your browser window, and you can only see 4 at once, only 4 will be loaded in a single request. If you can see 10 widgets at once and you’ve set the value of the property to 4, it will load all 10 widgets using 3 requests: 4 widgets + 4 + 2. Additional widgets will be loaded in the same fashion when you scroll the page. If you scroll very fast to the bottom of the page you cause the loading of all widgets.
    
-   If the value is set to a higher number, one slow-loading widget blocks a larger number of widgets from loading. The widgets visible on the dashboard load a little more quickly because fewer requests are sent to the server.
    

### Best practices

-   Set the value of this property to half of the number of widgets that are visible when your most-used dashboard loads. For example, if six widgets are visible on that dashboard, set the value of this property to three.
    
-   The values to use for these properties depend on the performance of your instance and the contents of its dashboards.
    

The overall performance of a dashboard depends on the combined performance of all its widgets. Optimizing the performance of the data requests each widget is making goes a long way to improve the dashboard’s performance.
