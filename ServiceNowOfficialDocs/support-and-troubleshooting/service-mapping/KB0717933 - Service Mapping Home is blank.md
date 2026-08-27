---
title: "Service Mapping Home is blank"
aliases:
  - KB0717933
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0717933
kb_number: KB0717933
last_modified: 2024-04-07
---

## Service Mapping Home is blank

  

### Issue

# Symptoms

* * *

You have activated ServiceMapping plugin but the service mapping home page is blank. 

# Cause

* * *

You might still be using UI15 and not UI16 

The UI16 plugin is not active.

There is a dependency for Service Mapping home page with UI16. 

# Resolution

* * *

Activate plugin : "com.glide.ui.ui16"

If this is a non-production instance, with admin role you should be able to activate it yourself from the plugin list.

If this is production, you will have to put in a HI request to have that plugin activated. 

# Additional Information

* * *

Activating this plugin automatically forces all end-users with exception to admin users to use the new UI.

If you need to prevent this you will have to create a property and set it to 'public'. This will not prevent end-users from not getting the new UI, but it will give them the option to switch back to UI15. 

See here for more details on the property:

[https://docs.servicenow.com/csh?topicname=t\_SwitchBtwnUi16AndUi15.html&version=latest#t\_SwitchBtwnUi16AndUi15](https://docs.servicenow.com/csh?topicname=t_SwitchBtwnUi16AndUi15.html&version=latest#t_SwitchBtwnUi16AndUi15)
