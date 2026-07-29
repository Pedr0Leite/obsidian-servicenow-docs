---
title: "Add bulk users to VTB"
aliases:
  - Add bulk users to VTB
tags:
  - servicenow-dev-program
  - code-snippet
  - add-bulk-users-to-vtb
  - fix-scripts
---

For the teams who are using large number of VTBs on a daily basis based on multiple categories, for them adding multiple users to a Visual Task Board (VTB) manually is a tedious task.
To solve this, we can use a Fix Script to automate the process. 
Visual Task Boards are stored in the vtb_board table, and board members are linked through the vtb_board_member table. 
This script will allow us to add multiple users to a specific board by querying and inserting them as board members.

Explanation
- Set the boardSysId variable to the sys_id of the Visual Task Board to which you want to add users.
- Add the sys_id values of the users you want to add to the board in the userSysIds array.
- The script checks if the board with the specified boardSysId exists in the vtb_board table. If it doesn’t, it will display an error message.
- After adding all users, the script displays a message with the total number of users added to the board.

## Related Notes

- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Specialized Areas/Fix scripts/Add Fields On All List Views/README|Add Fields On All List Views]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Specialized Areas/Fix scripts/Add Variable set to multiple catalog items/README|Add Variable set to multiple catalog items]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Specialized Areas/Fix scripts/Adjust Variable Order on Catalog Item/README|Adjust Variable Order on Catalog Item]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Specialized Areas/Fix scripts/Anonymise Data/README|Anonymise Data]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Specialized Areas/Fix scripts/Assign user list to a specific group/README|Assign user list to a specific group]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Specialized Areas/Fix scripts/Authenticate using ScriptedRESTAPI/README|Authenticate using ScriptedRESTAPI]]
