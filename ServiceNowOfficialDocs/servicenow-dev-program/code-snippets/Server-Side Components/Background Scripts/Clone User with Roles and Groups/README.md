---
title: "Clone User with Roles and Groups"
aliases:
  - Clone User with Roles and Groups
tags:
  - servicenow-dev-program
  - code-snippet
  - clone-user-with-roles-and-groups
  - background-scripts
---

# Clone User with Roles and Groups

A background script that clones an existing user's profile including all their roles and group memberships to a new user account.

## Usage

1. Navigate to **System Definition → Scripts - Background**
2. Copy and paste the script content
3. Update the function call at the bottom with the source and target user IDs:
   ```javascript
   cloneUser('source.username', 'new.username');
   ```
4. Click "Run script"

## What It Does

The script:
1. Creates a new user record with the specified username
2. Copies all field values from the source user to the new user (except fields already set)
3. Clones all directly assigned roles (excludes inherited roles)
4. Clones all group memberships
5. Returns the sys_id of the newly created user

## Use Cases

- Onboarding new team members with similar access needs
- Creating test users with specific role/group combinations
- Setting up backup user accounts with identical permissions
- Standardizing user setup based on role templates

## Related Notes

- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Background Scripts/ACL Audit Utility/README|ACL Audit Utility]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Background Scripts/Access Analysis Utility/README|Access Analysis Utility]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Background Scripts/Add Bookmarks - ITIL Users/README|Add Bookmarks - ITIL Users]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Background Scripts/Add Comments/README|Add Comments]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Background Scripts/Add No Audit Attribute To Multiple Dictionary Entries/README|Add No Audit Attribute To Multiple Dictionary Entries]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Background Scripts/Add Standard Change Model/README|Add Standard Change Model]]
