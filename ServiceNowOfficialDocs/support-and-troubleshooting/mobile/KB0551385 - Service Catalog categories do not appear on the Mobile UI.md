---
title: "Service Catalog categories do not appear on the Mobile UI"
aliases:
  - KB0551385
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0551385
kb_number: KB0551385
last_modified: 2024-04-07
---

## Service Catalog categories do not appear on the Mobile UI

  

### Issue

When configuring the Service Catalog on the Mobile UI, sometimes you may find that the Service Catalog categories are not shown when using the Mobile UI.  

In the Mobile UI, when you enter the Service Catalog through the Service Catalog favorite, or from the module in the navigation menu, you get an empty page with no categories icons, or with only part of the categories.

### Cause

The categories are missing because they do not meet all the conditions that they need in order to appear in the mobile UI.

### Resolution

The following are the conditions that need to be met in order for a catalog category to appear in the Mobile UI:  

  

**Setting Catalog Mobile Layout**

-   Go to **Service Catalog > Mobile Admin > Mobile Layout**

You will see the following list:

![](/sys_attachment.do?sys_id=0d7cac6edb42b450e515c223059619c5)

-   Go into the required catalog. You will have to do it by clicking on the information icon (pointed in the above screenshot) and not on the catalog name.
-   Edit the categories in the **Mobile Layout** related list, and set the required categories.

  

**Empty Categories will not appear**

-    Verify that the category that you want to appear has at least one active item in it. A category with only inactive items in it, will not appear in the Mobile UI.![](/sys_attachment.do?sys_id=117cac6edb42b450e515c223059619f4)

  

**Catalog items have to be available for the mobile UI**

-   Verify that the items in the category are available to the Mobile UI. On the catalog item form, you have a field called **Availability**. In order for the item to be available to the Mobile UI, the value in that field needs to be either **Mobile Only** or **Desktop and Mobile**.

![](/sys_attachment.do?sys_id=d57cec6edb42b450e515c22305961916)

-   If you can't find this field on the form, you might need to add it by configuring the form layout.

  

<table class="noteTable" align="left"><tbody><tr><td style="vertical-align: middle; text-align: center;"><img title="Note" src="/Note_25x.pngx" alt="" align="baseline" border="" hspace="" vspace=""></td><td style="vertical-align: middle; text-align: left;"><strong>Note</strong>:&nbsp;All the above conditions have to be met. If even only one of the conditions is not met, then the category will not appear in the Mobile UI.</td></tr></tbody></table>
