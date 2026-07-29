---
title: "Application Menu Module - Setting 'Override application menu roles' field to true not having expected results"
aliases:
  - KB0714261
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0714261
kb_number: KB0714261
last_modified: 2024-04-07
---

## Issue

# Symptoms

* * *

The 'Create a Module' documentation, [https://docs.servicenow.com/csh?topicname=t\_CreateAModule.html&version=latest](https://docs.servicenow.com/csh?topicname=t_CreateAModule.html&version=latest), states the following for the 'Override application menu roles' field:

"Allows users to access this module even if they do not have permission to view the containing application menu. Users must still meet the role requirements for this module."

This wording is causing confusion with developers, who then expect only the Modules against which this field has been set to 'true' to then be visible. This is not the case.

The comment against the underlying code states the following,

"Determine if the provided application contains at least one module that is set to 'Override application menu roles'"

That is, if there is even just one Module defined against an Application menu that has 'Override application menu roles' it will mean that all Modules defined against the Application menu that meet the Role requirements of the user will then be visible, not just the one against which this parameter is set to true.

# Cause

* * *

Documentation needs clarifying to explain expected behaviour in respects to the setting of the 'Override application menu roles' field.

# Resolution

* * *

If you wish for an Application menu to not display for specific users, ensure that you do not have the 'Override application menu roles' field set to true against any Modules for which the Roles defined against it meet those the user possesses.

# Additional Information

* * *

A request has been put in with our Docs team, asking that they re-word this document to clarify the actual expected behaviour.
