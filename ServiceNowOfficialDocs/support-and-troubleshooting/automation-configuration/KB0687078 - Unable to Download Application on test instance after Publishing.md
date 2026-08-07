---
title: "Unable to Download Application on test instance after Publishing"
aliases:
  - KB0687078
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0687078
kb_number: KB0687078
last_modified: 2023-11-10
---

## Unable to Download Application on test instance after Publishing

  

### Issue

# Symptoms

* * *

Unable to download application on test instance after publishing.

# Release

* * *

All

# Cause

* * *

It is likely that this application was installed previously on the test instance via update set. Once it is installed, it cannot be downloaded again from the repo. If you check your other instances, you will see that it is available for download.

# Resolution

* * *

To enable downloading of the application to test via the app repo, completely uninstall the application on that instance. The best way to do this is to clone down from production.

#
