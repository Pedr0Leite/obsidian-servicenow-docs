---
title: "Post-clone Set Instance Banner"
aliases:
  - Post-clone Set Instance Banner
tags:
  - servicenow-dev-program
  - code-snippet
  - post-clone-set-instance-banner
  - fix-scripts
---

# Set a unique banner to your non-production instance to help users realise where they are :)
 ## Can be used as clean-up script on a clone profile, or run as fix script, background script etc. manually on the target instance after cloning.


 ### Prerequisites:
 * 1) You need to have the target instance's banner image attached to a record on the source system, e.g. have a knowledge article in production with the banner attached to it.
 * 2) Make sure the table above mentioned table and record and included in your clone!
 * 3) Set the source table name and the source record's sys_id as values for srcTbl and srcRec variables in the below section!

## Related Notes

- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Specialized Areas/Fix scripts/Add Fields On All List Views/README|Add Fields On All List Views]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Specialized Areas/Fix scripts/Add Variable set to multiple catalog items/README|Add Variable set to multiple catalog items]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Specialized Areas/Fix scripts/Add bulk users to VTB/README|Add bulk users to VTB]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Specialized Areas/Fix scripts/Adjust Variable Order on Catalog Item/README|Adjust Variable Order on Catalog Item]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Specialized Areas/Fix scripts/Anonymise Data/README|Anonymise Data]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Specialized Areas/Fix scripts/Assign user list to a specific group/README|Assign user list to a specific group]]
