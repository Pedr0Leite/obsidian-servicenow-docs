---
title: "How to add custom TAG for reference on Blueprint"
aliases:
  - KB0716344
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0716344
kb_number: KB0716344
last_modified: 2025-01-07
---

## How to add custom TAG for reference on Blueprint

  

### Issue

# Description

* * *

Adding a custom TAG for reference on Blueprint

# Procedure

* * *

-   Login to the Instance.
-   Navigate to Cloud Management >>  **Admin Portal.**
-   Click on **Analyze** (Left side). 
-   Click on **Tag Management** tab. 
-   Click on **New** button.
-   Enter following details on the new record form
    1.  Label
    2.  Name
    3.  Variable Name
    4.  Check the **Active** and **Visible** checkboxes.
-   Click on **Submit** button.

![](sys_attachment.do?sys_id=081de062db82b450e515c223059619c0)

-   Navigate to Cloud Management >>  **Admin Portal.**
-   Click on **Design** (Left side) 
-   Click on **Blueprints**.
-   Click on **New** button.
-   Provide all the necessary resources for the Blueprint as per the requirement.
-   Click on **Operations** (Bottom)
-   Click on **Provision** for Blueprint container resource.
-   Check TLR resource block newly added tag should show up as the attribute (Right Side).

![](sys_attachment.do?sys_id=881de062db82b450e515c223059619de)

-   Click on **Publish To Catalog** (Top) (Make sure all other information on the Blueprint are satisfactory) 

-   Navigate to Cloud Management >>  **User Portal.**
-   Click on **Launch a Stack.**
-   Choose the **Catalog** that we just published to catalog as above.
-   It will launch the OrderGuide with **General Info** and **Provision** Tabs.
-   In the **General Info** tab, we can now see the  TAG named "TestRD" appears >> Provide any tag name in the field.

![](sys_attachment.do?sys_id=4c1de062db82b450e515c223059619e3)

-   Submit the catalog to Provision the Stack
-   Once after successful provision of the Stack > Review the Stack details > We can now see the newly added TAG in the details. 

![](sys_attachment.do?sys_id=001de062db82b450e515c223059619e9)

# Applicable Versions

* * *

**Kingston P\*** and **London P\***

# Additional Information

* * *

Information in above procedure can be performed on any Cloud providers which are capable to create a blueprint, and we may also perform the same for existing Blueprints.
