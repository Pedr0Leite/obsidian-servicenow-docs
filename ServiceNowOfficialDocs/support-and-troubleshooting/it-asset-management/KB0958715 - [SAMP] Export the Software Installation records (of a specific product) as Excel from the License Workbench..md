---
title: "[SAMP] Export the Software Installation records (of a specific product) as Excel from the License Workbench."
aliases:
  - KB0958715
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0958715
kb_number: KB0958715
last_modified: 2024-03-06
---

## \[SAMP\] Export the Software Installation records (of a specific product) as Excel from the License Workbench.

  

### Issue

When we are on License Workbench, once we reviewed you might wanted to export the related data to different documents (like Excel/pdf/XML).

This article will guide you how can you export the data from License Workbench to different formats.

### Release

Jakarta ++

### Cause

1.  Goto the license workbench. (Application Navigator >> Software Asset >> License Workbench)
2.  Open the intended Publisher and related Product.
3.  On the right side panel you will see Unlicensed Installs (if exists)
4.  If you try exporting the Excel using the Right Click on Header it will not work.

### Resolution

Please take the steps as below:  
1\. Goto the license workbench. (Application Navigator >> Software Asset >> License Workbench)  
2\. Open the intended Publisher and related Product.  
3\. On the right side panel you will see Unlicensed Installs (if exists)  
4\. If you try exporting the Excel using the Right Click on Header it will not work.

![](https://support.servicenow.com/sys_attachment.do?sys_id=d459e4eedb02b450e515c223059619f0)

  
5\. So, click on gear button on the list header select the Product Result column and add it.

![](https://support.servicenow.com/sys_attachment.do?sys_id=5c59e4eedb02b450e515c223059619f3)

  
6\. Now do show matching on the Product Result. Now right click on the query and open in new Window.

![](https://support.servicenow.com/sys_attachment.do?sys_id=d059e4eedb02b450e515c223059619f7)

  
On the list view in new window you can try exporting the Excel (or other format) as needed.
