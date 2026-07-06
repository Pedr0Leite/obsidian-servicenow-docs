---
title: "GlideRecord query on a specific table is not working for non-role (end user) user"
aliases:
  - KB0749268
tags:
  - servicenow
  - support-kb
  - gliderecord
  - explicit-roles
  - script-include
  - snc_internal
  - snc_external
area: access-controls-authentication
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0749268
kb_number: KB0749268
last_modified: 2024-04-07
---

## GlideRecord query on a specific table is not working for non-role (end user) user

  

### Issue

# Symptoms

The Glide record query to a table is not working under the below scenario,

-   When an end user ( user without no role) is forcefully redirected to Service Portal via property "glide.entry.first.page.script"
-   When the snc\_internal and snc\_external roles exist on the instance, but "Explicit Roles" plugin was not active
-   Glide Record query is invoked from a Script Include

While the issue was occurring, we could observe below exception,

```
TypeError: Cannot convert null to an object. Param table: incident Param sys_id: xxxxxxxxxxxx Current user sys_id: xxxxxxxxxxxx : no thrown error
```

# Release

Any supported release. 

# Cause

The GlideRecord query was failing due to the reason that snc\_external and snc\_internal roles appear to be manually added/imported to the instance although the "Explicit Roles" plugin was inactive. 

# Resolution

Take a back up and delete the manually added/imported snc\_external & snc\_internal roles. If you don't have access to remove them, please open a HI case to clean them up.

Ideally, activating the "Explicit Roles" plugin would automatically create snc\_external & snc\_internal roles. 

# Additional Information

[Explicit Roles](https://docs.servicenow.com/csh?topicname=explicit-roles.html&version=latest "Explicit Roles")

[Activate the Explicit Roles plugin](https://docs.servicenow.com/csh?topicname=access-control-rules.html&version=latest "Activate the Explicit Roles plugin")

## Related

- [[KB0727017 - Best Practices for Installing 'Explicit Roles' and 'High Security Settings' Plugins]]
- [[c_GlideRecordAPI]] - official GlideRecord/GlideRecordSecure server-side API reference
- [[c_ScriptIncludes]] - official docs on Script Includes
