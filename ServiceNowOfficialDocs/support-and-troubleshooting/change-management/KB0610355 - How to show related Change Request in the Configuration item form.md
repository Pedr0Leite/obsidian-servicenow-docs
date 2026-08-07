---
title: "How to show related Change Request in the Configuration item form"
aliases:
  - KB0610355
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0610355
kb_number: KB0610355
last_modified: 2025-01-03
---

## How to show related Change Request in the Configuration item form

  

### Issue

How to display related Change Requests in the Configuration item form

  
  

# Overview

* * *

There are two ways to associate related Configuration Items on a Change Request form:

-   Use the Configuration Item field, which will fill in the data of a specific record.
    
    ![](sys_attachment.do?sys_id=892a6ce2db42b450e515c223059619c7)
    
-   Use the Affected CIs related list, where you can add several Configuration Items. The record that was entered in the Configuration Item field will display in this related list by default.
    
    ![](sys_attachment.do?sys_id=d92aace2db42b450e515c2230596190e)
    

To display the related Change Requests in the Configuration Item form, add the Affected By Task related list.

# Process

* * *

1.  Navigate to **Change > Create New** and select **Normal: Changes without predefined plans that require approval and CAB authorization.create a Normal Change Request**.
    
2.  Insert a configuration item (for example, \*BOW-IBM from the demo data) in the **Configuration Item** field and click **Submit**.
    
3.  Add some more Configuration Item records in the **Affected CIs** related list (for example, \*ANNIE-IBM and \*BETH-IBM).
    
4.  In the **Affected CIs** related list, select any of the Affected CI records.
    
    Note that there is no information about the related Change Request.
    
5.  Right-click in the Configuration Item form header and choose **Configure** > **Form Layout**.
    
6.  Use the slushbucket to add Affected by Task to the form and click **Save**.
    
    The related Change Request is listed in the Affected by Task field.
    
    ![](sys_attachment.do?sys_id=a52aace2db42b450e515c22305961942)
    
    **Note** – If you select Change Request->Configuration Item, the related Change Request will display only in the form of the record added in the Configuration Item field of the Change Request (in this example, \*BOW-IBM). The forms of the other Affected CIs (\*ANNIE-IBM and \*BETH-IBM) will not display the Change Request.
