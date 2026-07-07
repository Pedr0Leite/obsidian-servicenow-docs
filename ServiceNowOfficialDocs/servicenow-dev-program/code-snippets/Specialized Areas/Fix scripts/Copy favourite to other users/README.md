---
title: "Copy favourite to other users"
aliases:
  - Copy favourite to other users
tags:
  - servicenow-dev-program
  - code-snippet
  - copy-favourite-to-other-users
  - fix-scripts
---

**Enhancement**
1. This code will create the sp favorites of the selected users along with the sys_ui_bookmarks.
2. The entry will be made in "sp_favorite" through new **createPortalFav** function.

You can use this script to take an existing favaourite from the sys_ui_bookmark table and create a copy of it for any number of users.
Can be useful when onboarding new staff, doing testing, etc.

You will need two things to get started:
* the sys_id of the original favourite you want to copy - take this from sys_ui_bookmark table
* an ecoded query string of a filtered list of users that you want to copy the favourite to

Run the script wherever you like, background script, Xplore, or as fix script.
Have fun!

## Related Notes

- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Specialized Areas/Fix scripts/Add Fields On All List Views/README|Add Fields On All List Views]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Specialized Areas/Fix scripts/Add Variable set to multiple catalog items/README|Add Variable set to multiple catalog items]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Specialized Areas/Fix scripts/Add bulk users to VTB/README|Add bulk users to VTB]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Specialized Areas/Fix scripts/Adjust Variable Order on Catalog Item/README|Adjust Variable Order on Catalog Item]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Specialized Areas/Fix scripts/Anonymise Data/README|Anonymise Data]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Specialized Areas/Fix scripts/Assign user list to a specific group/README|Assign user list to a specific group]]
