---
title: "Format JSON in String Fields"
aliases:
  - Format JSON in String Fields
tags:
  - servicenow-dev-program
  - code-snippet
  - format-json-in-string-fields
  - fix-scripts
---

**Details**
1. This script will format the JSON data in string fields on forms.
2. There is on OOB attribute "json_view" which can be added to field but it always reqires an extra click and has loading time issues.

**How to use**
1. Run this script as Fix Script.
2. Replace the table name and encoded query as per your requirement.
3. Replace the field to be formatted as per the table selected.

**Before Formatting**
<img width="956" height="371" alt="Before1" src="https://github.com/user-attachments/assets/1b35dfaf-d2ad-44c3-bbd2-d3198664073b" />

**After Formatting**
 <img width="950" height="382" alt="After" src="https://github.com/user-attachments/assets/c3a1c3c0-48bd-4d2f-9e27-fea0ed86004d" />

JSON.stringify() documentation : https://www.geeksforgeeks.org/javascript/javascript-json-stringify-method/

## Related Notes

- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Specialized Areas/Fix scripts/Add Fields On All List Views/README|Add Fields On All List Views]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Specialized Areas/Fix scripts/Add Variable set to multiple catalog items/README|Add Variable set to multiple catalog items]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Specialized Areas/Fix scripts/Add bulk users to VTB/README|Add bulk users to VTB]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Specialized Areas/Fix scripts/Adjust Variable Order on Catalog Item/README|Adjust Variable Order on Catalog Item]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Specialized Areas/Fix scripts/Anonymise Data/README|Anonymise Data]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Specialized Areas/Fix scripts/Assign user list to a specific group/README|Assign user list to a specific group]]
