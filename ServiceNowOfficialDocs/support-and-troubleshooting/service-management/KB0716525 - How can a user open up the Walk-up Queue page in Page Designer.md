---
title: "How can a user open up the \"Walk-up Queue\" page in Page Designer?"
aliases:
  - KB0716525
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0716525
kb_number: KB0716525
last_modified: 2024-04-07
---

## How can a user open up the "Walk-up Queue" page in Page Designer?

  

### Issue

# Symptoms

* * *

-   Unable to open "Walk-up Queue" page in Page Designer, met with message which says, "Sorry, you are not authorized to access the walk-up pages. Please login using the correct user account."

# Release

* * *

London Patch 1 and London Patch 2

# Resolution

* * *

After reviewing OOB (Out of Box) behavior, the message seen is expected per design.  
  
This is corroborated in documentation: [Configure the Walk-up Experience portal](https://docs.servicenow.com/csh?topicname=configure-walkup-portal.html&version=latest#configure-walkup-portal "Configure the Walk-up Experience portal")

There are some security measures that were put in place when the Walk-up Experience was designed - namely, that it is meant to be an external user experience, hence the role restrictions for accessibility. With that in mind, the Walk-up Experience service portal can be configured by an admin user utilizing the following two methods:  
  
First, per the documentation, if the user wishes to configure the portal with their unique company branding, title, logo, theme colors, layout, properties, widgets, etc - they can do so through utilizing the Page Editor.  
  
Second, the user can configure the Walk-up service portal using the Service Portal Walk-up form via Form Designer. To do this:  
  
1\. Navigate to Walk-up Experience > Administration > Portal Configurations. Then, click "Walk-up".  
2\. When that loads, in the contextual menu (the triple, stacked lines), click Configure > Form Design.   
3\. In the form designer header drop-down list (in the top left of the screen - should default to "Service Portal \[sp\_portal\]"), select or search for any of the configurable walk-up forms to customize the portal appearance (in this case, the Walk-up Queue On Site page).  
  
Alternatively, to "work around" this restriction and authorization message, feel free to do the following:   
  
1\. Within a typical Chrome browser window, have the user log into their admin account and make their changes to the Portal.   
2\. Simultaneously, open up an incognito Chrome browser window, logged in as the walk-up user who is viewing the specific page the admin user is editing.   
3\. As the admin user makes changes to the portal from their end, refresh the incognito Chrome window (walk-up user) to see the changes.   
  
In this way, the admin user can see their changes in a somewhat live format.
