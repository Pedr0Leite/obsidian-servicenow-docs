---
title: "Hide Search labels from tables (breadcrumbs)"
aliases:
  - KB0752438
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0752438
kb_number: KB0752438
last_modified: 2024-04-07
---

## Hide Search labels from tables (breadcrumbs)

  

### Issue

# Description

When adding a "Data Table from Instance Definition" widget, by default will display the breadcrumbs.![](/sys_attachment.do?sys_id=a0ba2ca6db42b450e515c223059619ac)

Here is how to go about removing or hiding breadcrumbs from "Data Table from Instance Definition" widget

# Procedure

To hide breadcrumbs from a existing **Single Table**:

1.  Navigate to the desired table
2.  Control-Click on the table headers -> Widget in Editor![](/sys_attachment.do?sys_id=a4ba2ca6db42b450e515c223059619b1)
    
    * * *
    
3.  Click Clone "Data table from Instance Definition"![](/sys_attachment.do?sys_id=68ba2ca6db42b450e515c223059619b6)
    
    * * *
    
4.  Make sure you are on the clone you just created to begin altering.![](/sys_attachment.do?sys_id=2cba2ca6db42b450e515c223059619bb)
    
    * * *
    
5.  In the Server Script, Scroll down to line 47![](/sys_attachment.do?sys_id=ecba2ca6db42b450e515c223059619c0)
    
    * * *
    
6.  Set the value to **false** to hide the breadcrumbs![](/sys_attachment.do?sys_id=a0ba2ca6db42b450e515c223059619c6)
    
    * * *
    
7.  Save it and go back to the widget on the page.
8.  Control-Click table header and Select "Instance Options"![](/sys_attachment.do?sys_id=64ba2ca6db42b450e515c223059619cb)
    
    * * *
    
9.  From the Context menu -> Click "Open in platform"![](/sys_attachment.do?sys_id=28ba2ca6db42b450e515c223059619d0)
    
    * * *
    
10.  Click on and change the "SP Instance Config view" to Default![](/sys_attachment.do?sys_id=f8ba2ca6db42b450e515c223059619d5)
     
     * * *
     
11.  Click on the Widget tab and change the Widget field to the copy previously created.![](/sys_attachment.do?sys_id=bcba2ca6db42b450e515c223059619da)![](/sys_attachment.do?sys_id=70ba2ca6db42b450e515c223059619e0)
12.  Click Update and go back to the page of the widget.
13.  Single table should only display breadcrumbs while filters still apply to table.![](/sys_attachment.do?sys_id=34ba2ca6db42b450e515c223059619e5)

To hide breadcrumbs from **Multiple tables:**

1.  Follow steps to make a Clone
2.  Apply the copy to each table (Refer to step 11)

To hide breadcrumbs from **ALL tables**:

1.  Skip steps 3, 4, 8-13 to affect the "Data table from Instance Definition" widget
2.  All current and future "Data table from Instance Definition" widget will no show breadcrumbs.
