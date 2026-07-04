---
title: "After sharing a Performance Analytics dashboard with a user, that user can still not access the dashboard"
aliases:
  - KB0656248
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0656248
kb_number: KB0656248
last_modified: 2025-10-16
---

## After sharing a Performance Analytics dashboard with a user, that user can still not access the dashboard

  

### Issue

After sharing a Performance Analytics dashboard with a user, that user can still not access the dashboard

Symptoms

* * *

As per the [documentation](https://docs.servicenow.com/csh?topicname=t_ControlAccessToADashboard.html&version=latest), PA dashboards can be shared with Portal users, not requiring any roles. But when sharing an existing dashboard with a user, the user cannot see the dashboard using the direct link to the dashboard from the email that gets sent as a result of the sharing.  
  
Instead, the webpage shows this message:  
  
"Sorry! The outages and Availability dashboard dashboard hasn't been shared with you."  

Cause

* * *

Though the dashboard has been shared with the user, it can also be restricted to specific roles in the dashboard properties.  
  
If the user does not have the roles the dashboard is restricted to, he/she will not be able to access the dashboard even when it has been shared with that user.  

Resolution

* * *

To check the restrict to roles permissions on the dashboard:

1.  Open the dashboard as the owner or user that can also share it, for example, a pa\_admin user
2.  Click on the **More Actions** button, also known as the hamburger icon, on the left of the dashboard name dropdown
3.  Select **Dashboard properties**
4.  Click the edit icon for the **restrict to roles** field to add/remove roles. If the dashboard should be accessible to users without roles, ensure there are no roles in this list. If there should be a role based restriction, ensure that anyone who is supposed to have access to the dashboard, also has that role.

Note that this is also mentioned in the [documentation](https://docs.servicenow.com/csh?topicname=t_ControlAccessToADashboard.html&version=latest), **Dashboard permissions may also be impacted by the Restrict to role field on the dashboard properties form**.
