---
title: "Why \"Uncaught Error: chart.js library needs to be included\"occurs?"
aliases:
  - KB0712275
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0712275
kb_number: KB0712275
last_modified: 2024-04-07
---

## Why "Uncaught Error: chart.js library needs to be included"occurs?

  

### Issue

# Symptoms

* * *

While loading any form on the platform like incident.do, rm\_release.do, etc, observed below java script error on browser,

Uncaught Error: chart.js library needs to be included

-   Eventually this script error can cause issue with other UI script / UI policy /Client script execution on the form.
-   Also, it can cause failure with Automated Test Framework ( ATF) steps.

Complete error is shown in below screenshot,

![](sys_attachment.do?sys_id=076ce86edb42b450e515c2230596194c)

# Release

* * *

Any supported release. 

# Cause

* * *

Following third party libraries are added into a Global UI Scripts, probably needed for implementing custom chart functionalities in service portal.

-   **chart.js x.x.x**
-   **angular-chart.js x.x.x**

Since they are defined as global script, they get executed on load of all the forms in platform and causing the error in browser console.

# Resolution

* * *

Review the custom custom chart global UI scripts, if they are not required, de-activate them.

OR

If they are required, do not make them as "Global", instead try to utilize them only on the portal page where it is needed.

# Additional Information

* * *

[UI Scripts](https://docs.servicenow.com/csh?topicname=c_UIScripts.html&version=latest "UI Scripts")

[GlideUIScripts](https://docs.servicenow.com/csh?topicname=GUIScriptsAPI.html&version=latest#ariaid-title2 "GlideUIScripts")

[Community article](https://community.servicenow.com/community?id=community_question&sys_id=f4e843a1db5cdbc01dcaf3231f96192b "Community article")
