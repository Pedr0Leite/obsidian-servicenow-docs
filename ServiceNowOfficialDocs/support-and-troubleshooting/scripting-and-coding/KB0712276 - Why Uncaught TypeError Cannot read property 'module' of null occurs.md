---
title: "Why \"Uncaught TypeError: Cannot read property 'module' of null\" occurs?"
aliases:
  - KB0712276
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0712276
kb_number: KB0712276
last_modified: 2024-04-07
---

## Why "Uncaught TypeError: Cannot read property 'module' of null" occurs?

  

### Issue

# Symptoms

* * *

While loading any form on the platform like incident.do , rm\_release.do etc, observed below java script error in browser console,

Uncaught TypeError: Cannot read property 'module' of null

-   Eventually this script error can cause issue with other UI script / UI policy /Client script execution on the form.
-   Also, it can cause failure with Automated Test Framework ( ATF) steps.

Complete error is shown in below screenshot,

![](sys_attachment.do?sys_id=380dac22db82b450e515c223059619c6)

# Release

* * *

Any supported release. 

# Cause

* * *

Following third party library was added into a Global UI Scripts, probably needed for implementing custom functionalities in service portal.

-   **ngTable.js** 

Since it is defined as global script, it get executed on load of all the forms in platform and causing the error in browser console.

# Resolution

* * *

Review the custom custom global UI script, if it is not required, de-activate it.

OR

If it is required, do not make it as "Global", instead try to utilize it only on the portal page where it is needed.

# Additional Information

* * *

[UI Scripts](https://docs.servicenow.com/csh?topicname=c_UIScripts.html&version=latest)

[GlideUIScripts](https://docs.servicenow.com/csh?topicname=GUIScriptsAPI.html&version=latest#ariaid-title2)
