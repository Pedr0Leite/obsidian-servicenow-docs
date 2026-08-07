---
title: "Profile user pictures and avatars that are part of the User Presence feature do not work in UI16"
aliases:
  - KB0647818
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0647818
kb_number: KB0647818
last_modified: 2024-04-07
---

## Profile user pictures and avatars that are part of the User Presence feature do not work in UI16

  

### Issue

Profile user pictures and avatars from the user presence feature do not work in UI16

  
  

# Description

* * *

User presence is a UI16 feature that enables you to see who is online when you are logged in and working in an instance. This feature is controlled by the system property _**glide.ui16.live\_forms.enabled**_.

# Issue

* * *

When you are viewing a record in a form, such as an incident, you can see whether other users are viewing the same record. User presence does not show who is viewing the record if only two people are viewing the same record even if live\_forms is enabled in the instance.

In some scenarios, the browser JavaScript console shows errors like:

Failed to load resource: the server responded with a status of 400 (Bad Request) https://<instance name>.service-now.com/api/now/live/profiles/sys\_user.<sys\_id>

# Cause

* * *

The profile service is part of the Connect plugin; therefore, it does not work if this plugin is not enabled on the instance.

# Proposed Solution

* * *

Check whether the following plugins are activated in the instance:

-   Connect: com.glide.connect
-   Live Feed: com.glide.ui.$live

For more information, see the documentation topic [Activate a plugin](https://docs.servicenow.com/csh?topicname=t_ActivateAPlugin.html&version=latest "Activate a plugin").

**Note** – If you do not need Connect, you can still activate the Connect plugin and then turn Connect off. To turn off Connect:

1.  Go to /sys\_properties\_list.do and search for glide.connect.chat.disabled.
2.  Set the value to true.

For more information, see the documentation topic [Disable Connect Chat](https://docs.servicenow.com/ "Disable Connect Chat").
