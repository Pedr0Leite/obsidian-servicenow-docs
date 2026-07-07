---
title: "Remove extra spaces"
aliases:
  - Remove extra spaces
tags:
  - servicenow-dev-program
  - code-snippet
  - remove-extra-spaces
  - fix-scripts
---

## ServiceNow Fix Script: Remove Extra Spaces
A generic ServiceNow fix script to clean data by removing extra whitespace from any specified field on any table.

### Problem It Solves
This script resolves data integrity issues caused by inconsistent user input, such as:
- Leading or trailing spaces (e.g., " Hello World ").
- Multiple spaces between words (e.g., "Hello   World").
  
### How to use
1. Create and Configure the Fix Script
    - First, create a new Fix Script in your ServiceNow instance (**System Definition > Fix Scripts**) add past the code

2. Add your table name and field that you want to clean up
    - Before running, you must update the following variables inside the script to define your target:
      ```js
      var tableName = 'incident'; // <-- CHANGE THIS to your table name
      var fieldName = 'short_description'; // <-- CHANGE THIS to your field name
      ```

3. Change `processRecords` value and run
    - To see what changes will be made without actually updating records, ensure the `processRecords` variable in the script is set to `false`
      ```js
      var processRecords = false;
      ```
    - To actually do the update, change the `processRecords` variable to `true` and run the script
      ```js
      var processRecords = true;
      ```

4. Run the script

## Related Notes

- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Specialized Areas/Fix scripts/Add Fields On All List Views/README|Add Fields On All List Views]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Specialized Areas/Fix scripts/Add Variable set to multiple catalog items/README|Add Variable set to multiple catalog items]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Specialized Areas/Fix scripts/Add bulk users to VTB/README|Add bulk users to VTB]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Specialized Areas/Fix scripts/Adjust Variable Order on Catalog Item/README|Adjust Variable Order on Catalog Item]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Specialized Areas/Fix scripts/Anonymise Data/README|Anonymise Data]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Specialized Areas/Fix scripts/Assign user list to a specific group/README|Assign user list to a specific group]]
