---
title: "Connect Plugin Activation and How to Disable Connect"
aliases:
  - KB0647741
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0647741
kb_number: KB0647741
last_modified: 2024-04-07
---

## Connect Plugin Activation and How to Disable Connect

  

### Issue

# Overview

* * *

This article addresses the following two questions.

-   How did the Connect plugin get enabled on my instance?
-   How to disable Connect globally for that instance?

# How Connect is enabled on an Instance

* * *

Connect is enabled is by default on all new instances on Geneva and later product releases. If the instance is pre-Geneva, Connect is activated through plugin activation either manually or as a requirement of another plugin.

To validate how a plugin was activated if it was not there by default:

1.  Navigate to **System Diagnostics > Upgrade History**.
    
2.  Search the To column for "com.glide.connect".
    
    If no records match that name exactly, the plugin was enabled by default or was brought over from a clone. Take the same steps in the instance from which it was cloned.
    
    If the record is found, note the timestamp when it was activated.
    
3.  Remove the search and filter the list by "Upgrade Started" so you can see other plugins activated at that time.
    
4.  Look for the plugin that was upgraded last during the same time as Connect. That plugin likely had the Connect plugin as a requirement.
    
5.  Search the Transactions (All User) module for "URL contains v\_plugin" around the time the plugin was activated to determine who activated the plugin.
    

# How to Disable Connect

* * *

Use the _**glide.connect.chat.disabled**_ system property to disable connect. For more information, see the product documentation topic [Disable Connect Chat](https://docs.servicenow.com/).

You also need to deactivate the modules that link to Connect pages. Navigate to **System Definition > Modules** to find them.

# Additional Information

* * *

Please do check the following if you like all users to not have access to Connect Chat:

\- Check any active queues available under **Collaboration > Support Administration > Queues.**

-   If it does, please check whether the **Assignment Group** field in the queue is mapped to any user group.
-   if yes, then clear that field's value mapping (reason being that users in that user group will still have access to the module).
