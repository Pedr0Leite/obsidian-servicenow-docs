---
title: "How to Modify the Number of Items Visible in the Collection Slushbucket on a Related List"
aliases:
  - KB0523809
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0523809
kb_number: KB0523809
last_modified: 2026-04-02
---

## How to Modify the Number of Items Visible in the Collection Slushbucket on a Related List

  

### Issue

Slushbuckets allow users to select multiple items from a list of available items. They are used in many operations, such as personalizing lists, adding items to related lists, and service catalog list collector variables. Some slushbuckets provide filter and search controls for available items, such as adding items to related lists. 

Users often need to increase the number of records that appear in the Collection slushbucket. The maximum number of entries shown in the Collection slushbucket is set by a global property called **glide.xmlhttp.excessive**. This property sets the number of items visible in the Available half of a many-to-many or one-to-many slushbucket.

The **glide.xmlhttp.excessive** property defaults to 100, including instances where the property does not exist. The value can be modified, if necessary. If the value is set too high, it can cause performance degradation because all items need to be loaded every time the list collection form window is opened.

### Resolution

The **glide.xmlhttp.excessive** property only impacts the Collection (left) slushbucket. The List (right) slushbucket contains as many items as selected, regardless of the property value. 

<table style="width: 1256px;" align="left"><tbody><tr><td style="vertical-align: middle; text-align: center;"><img title="Note" src="/Note_25x.pngx" alt="" align="baseline" border="" hspace="" vspace=""></td><td style="vertical-align: middle; text-align: left;"><strong>Note</strong>: In some cases, the property does not exist in a base instance, but can be added&nbsp;if you need to change the value.</td></tr></tbody></table>

  

To change the maximum number of records that display in a slushbucket:

1.  1.  In the **Navigation** filter, type **sys\_properties.list**.
    2.  Search for the property name **glide.xmlhttp.excessive**.
    3.  The **Value** field sets the desired value for property. Update the property value to the number of records you want to appear in the Collection slushbucket.
    4.  Navigate to a related list and click the **Edit** button. Verify that the number of records in the slushbucket reflects the property value. 

![](sys_attachment.do?sys_id=a0d8646edb02b450e515c2230596196c)
