---
title: "Resolve issue with latest scoped application version not displaying on target instance"
aliases:
  - KB0780739
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0780739
kb_number: KB0780739
last_modified: 2025-12-16
---

## Resolve issue with latest scoped application version not displaying on target instance

  

### Issue

You cannot see the most recent version of your custom application on the target instance after migration. This prevents you from updating the application.

### Release

All supported releases

### Cause

The application version number is not incremented correctly. The platform treats version 1.0.8 as higher than 1.0.28, so the latest version does not appear.

### Resolution

Publish the application with a version number higher than the current highest version on the target instance.

For example, if the current version is 1.0.8, use 1.0.9 or 1.0.81 for the next version.

-   See the documentation for publishing to the [Update set](https://docs.servicenow.com/csh?topicname=t_PublishApplicationsToAnUpdateSet.html&version=latest "Update set") and [ServiceNow Store](https://docs.servicenow.com/csh?topicname=t_PublishAppsToTheServiceNowStore.html&version=latest "ServiceNow Store")
-   Refer to [Publish to Application Repository](https://docs.servicenow.com/csh?topicname=t_PublishAppsToTheAppRepository.html&version=latest "Publish to Application Repository") on publishing to repository
