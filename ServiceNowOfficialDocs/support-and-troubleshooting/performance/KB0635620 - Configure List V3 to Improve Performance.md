---
title: "Configure List V3 to Improve Performance"
aliases:
  - KB0635620
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0635620
kb_number: KB0635620
last_modified: 2026-05-06
---

## Issue

 

Configure List V3 to Improve Performance

## Resolution

**Enable List V3 only for specific users**

Sometimes there is a list V3 need for some specific users but not for the all the users. This is set up by creating following two user preferences.

**NOTE:** Only users with the **admin role** can make this change.

After enabling list V3 in the instance, create a user preference with following details:  
  
Description : -Blank-  
Name : use.list\_v3  
System : True  
Type : True/False  
Value : False  
User : -Blank-  
  
After that, create a similar user preference with a few changes:  
  
Description : -Blank-  
Name : use.list\_v3  
System : False  
Type : True/False  
Valuse : True  
User : -Name of the user, who wants to use list V3-  
  
After that, the List V3 is disabled for all users except the one mentioned in the second user preference.

#### Enable list V3 only for specific lists

Some lists are having too much data with too many columns visible. In that case list V3 may be expensive to load, turn off list v3 for the specific lists.

-   Navigate to the list for which you want to disable List v3.
-   Click the list title menu icon (![enu icon](/sys_attachment.do?sys_id=4d67c7bb83ec43d4cdbbc430feaad3bc)).
-   Select Configure > List Control.
-   The List Control form appears.
-   Select the Disable list v3 check box.
-   Click Update

**  
NOTE**: Only users with the **personalize\_control** role can make this change.

#### Disable Live functionalities for better performance

The List V3 plugin is generally activated together with the Live Forms and Live Lists new UI16 plugins. These enable real time updates on forms and lists, as part of the activity stream, without the need of manual refresh. When this live functionality is enabled, the system continues to feed transactions, possibly affecting the instance performance. To prevent the issue on list views or related lists, the live functionality can be switched off by disabling the following two properties:

1.  Name: glide.ui16.live\_lists.enabled

Type: true | false

Default value: true

Location: System Properties > List v3

2.  Name: glide.ui.list\_v3.enable\_live\_related\_lists

Type: true | false

Default value: true

Location: System property \[sys\_properties\] table
