---
title: "Error while converting Manual to Application Service."
aliases:
  - KB0754414
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0754414
kb_number: KB0754414
last_modified: 2024-04-07
---

## Error while converting Manual to Application Service.

  

### Issue

# Symptoms

The error "Error on server request getServiceTimeline. No historical data exists for this Business Service" appears while trying to convert a **Manual Business Service** to an **Application Service**, though the convert attempt finishes successfully resulting in an application service, the map would not be seen and instead of which the below would be seen.

![](sys_attachment.do?sys_id=f70aa4e2db42b450e515c223059619db)

-   The conversion of **Manual Business Service** to an **Application Service** is performed using the UI action **'Convert to Application Service'** and this feature is available from **London** release**.** 

# Release

-   London \*

# Cause

When converting a Manual Business service to an Application service

-   An attempt would be made to create a service model (container, environment and layers) which would be a source for the Application service map.
-   In this scenario, because of a Manual business service's **'discovery source'** value is set to **'Unknown'**, the conversion process doesn't reach a point where a **Service Model** creation happens.
-   Since the converted services do not have a model to support them, the UI Map displays the error.

# Resolution

-   Navigate to **Manual Business Services** list view or open up a single map record that is being targeted to be converted as **Application service**.
-   If the column **'Discovery Source'** is not present on the list view or as a field on the form view, please add it.
-   If its the list view, you may see the list as below, after you apply the filter.

![](/sys_attachment.do?sys_id=c81aa4e2db42b450e515c223059619e0)

-   Update the **'discovery source'** field from **'Unknown'** to **'None'**
-   Once the above update is performed, perform the UI action 'Convert to Application Service' and you would see that the conversion process would be successful and a visible application service map.

Note: Please make sure to perform the above steps prior to converting the manual business service into application service. If in case an attempt has been made prior to applying the above resolution, there will be a target application service already present. You may have to delete the faulty **Application Service** which has been created.

# Additional Information

-   If in case the problem persists even after implementing the above workaround or if you already see the business service in a state other than 'Unknown', please raise a case to ServiceNow's technical support team through 'HI' for further investigation.
