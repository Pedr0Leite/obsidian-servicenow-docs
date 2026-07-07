---
title: "Get Logged in User Information"
aliases:
  - Get Logged in User Information
tags:
  - servicenow-dev-program
  - code-snippet
  - get-logged-in-user-information
  - client-scripts
---

# The Glide User (g_user) is a global object available within the client side. It provides information about the logged-in  user.

Property                   Description

g_user.userID              Sys ID of the currently logged-in user
g_user.name                User's Full name
g_user.firstName           User's First name
g_user.lastName            User's Last name

# It also has some methods available within the client side.

Method                     Description

g_user.hasRole()           Determine whether the logged-in user has a specific role
g_user.hasRoleExactly()    Do not consider the admin role while evaluating the method
g_user.hasRoles()          You can pass two or more roles in a single method

## Related Notes

- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Client-Side Components/Client Scripts/Abort action when description is empty/ReadMe|Abort action when description is empty]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Client-Side Components/Client Scripts/Abort direct incident closure without Resolve State/readme|Abort direct incident closure without Resolve State]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Client-Side Components/Client Scripts/Add Field Decoration/README|Add Field Decoration]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Client-Side Components/Client Scripts/Add Image to Field Based on Company/README|Add Image to Field Based on Company]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Client-Side Components/Client Scripts/Adding Placeholder on Resolution Notes/README|Adding Placeholder on Resolution Notes]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Client-Side Components/Client Scripts/Auto Update Priority based on Impact and Urgency/readme|Auto Update Priority based on Impact and Urgency]]
