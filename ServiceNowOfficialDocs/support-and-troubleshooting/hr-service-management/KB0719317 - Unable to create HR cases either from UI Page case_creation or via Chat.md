---
title: "Unable to create HR cases either from UI Page \"case_creation\" or via Chat"
aliases:
  - KB0719317
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0719317
kb_number: KB0719317
last_modified: 2024-04-07
---

## Unable to create HR cases either from UI Page "case\_creation" or via Chat

  

### Issue

# Symptoms

* * *

We have an OOB UI page called "**case\_creation**" that assists in creating HR cases.

This can be either explicitly loaded via "**sn\_hr\_core\_case\_creation.do**" or via Collaboration chat.

You may face occurrence of this issue where the page loads nothing (blank white) with the following browser console error:

```
angular_includes_1.4.jsx?v=03-02-2018_1305:8 Uncaught Error: [$injector:modulerr] http://errors.angularjs.org/1.4.8/$injector/modulerr?p0=caseCreation&p1=Error%3A%20%5B%24injector%3Amodulerr%5D%20http%3A%2F%2Ferrors.angularjs.org%2F1.4.8%2F%24injector%2F......
```

# Release

* * *

Jakarta, Kingston, London.

# Environment

* * *

UI15.

# Cause

* * *

\- The **UI16** plugin was not activated.

# Resolution

* * *

-   Installation of **UI16** plugin is required for the UI page to work. It is not necessary to use the **UI16** theme/ui, but the plugin is necessary to load angular on the case\_creation ui page.
-   It's not actually necessary to use **UI16** features and you can completely disable it by following the below steps:
    -   On filter navigator, go to "**User Administration**" > "**User Preferences**".
    -   Look for the record with name "**use.concourse**".
    -   Notice it's value is "**true**". Set this to "**false**" => logout and log back in.
    -   You will see that your UI will be in **UI15** mode.
