---
title: "Developer instance skipped upgrade"
aliases:
  - KB0533098
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0533098
kb_number: KB0533098
last_modified: 2024-04-30
---

## Issue

This article discusses how to bypass the **Developer instance – skipped upgrade** message and get the instance to upgrade.

  

## Resolution

-   If the property is not available yet, add the property:  
      
    1.  In the navigation filter, enter **sys\_properties.list**.
    2.  In the properties list, go to **All Properties**.
    3.  Click **New**.
    4.  In the **Name** field, enter **glide.installation.developer**.
    5.  In the **Type** field, select **true | false**.
    6.  In the **Value** field, enter **false**.  
          
        
-   Alternatively, apply the **sys\_properties\_glide.installation.developer-false.xml** attachment to import the property. Once this is applied, the scheduled job **Upgrade,** which runs on an hourly interval, is able to kick off the upgrade.  
      
    
-   Another way to kick off the upgrade is by running the following from the background scripts page:  
      
    gs.setProperty("glide.installation.developer","false");  
    new UpgradeClient().process();
