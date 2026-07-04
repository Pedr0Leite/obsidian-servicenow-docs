---
title: "How to deactivate the Connect plugin"
aliases:
  - KB0656241
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0656241
kb_number: KB0656241
last_modified: 2025-01-03
---

## How to deactivate the Connect plugin

  

### Issue

# Description

* * *

Like other plugins, completely deactivating the Connect plugin once it is activated is not possible. However, you can try to turn it off to a certain extent.

# Procedure

* * *

To disable Connect, set the following properties as indicated: 

-   **glide.connect.enabled**: false
-   **collaboration.frameset**: false

If the **Follow** button is still available on the form, set the property **connect.roles** to the value **nobody**.

# Applicable Versions

* * *

All

# Additional Information

* * *

See the following Kingston product documentation topics:

-   [Properties installed with Connect Support](https://docs.servicenow.com/csh?topicname=t_ActivateConnectSupport.html&version=latest#ariaid-title2 "Properties installed with Connect Support") 
-   [Properties for Connect](https://docs.servicenow.com/csh?topicname=r_PropertiesForConnect.html&version=latest "Properties for Connect")
