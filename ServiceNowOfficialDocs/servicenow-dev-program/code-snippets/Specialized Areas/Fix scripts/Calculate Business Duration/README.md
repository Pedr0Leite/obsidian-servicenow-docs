---
title: "Calculate Business Duration"
aliases:
  - Calculate Business Duration
tags:
  - servicenow-dev-program
  - code-snippet
  - calculate-business-duration
  - fix-scripts
---

# Calculate Business Duration

Use this script to update the business duration field for records.

## Description

Updates the business duration field for tables such as incident and sc_req_item. The business duration can be determined by using a schedule if required.

## Getting Started

### Dependencies

* This script will only work in the Global scope.

### Execution

* Copy the script from calculate-business-duration.js to either a background script or a fix script.
* If using a schedule, add the sys_id of the required schedule to the selectedSchedule variable.
* Set the table using the table variable.
* Set the encoded query to obtain the records you would like to update. The preconfigured query includes records from January 1, 2022 where the state is either closed or cancelled.
* Run the script.

## Author

Brad Warman

https://www.servicenow.com/community/user/viewprofilepage/user-id/80167

## Version History

* 0.1
    * Initial Release

## Related Notes

- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Specialized Areas/Fix scripts/Add Fields On All List Views/README|Add Fields On All List Views]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Specialized Areas/Fix scripts/Add Variable set to multiple catalog items/README|Add Variable set to multiple catalog items]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Specialized Areas/Fix scripts/Add bulk users to VTB/README|Add bulk users to VTB]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Specialized Areas/Fix scripts/Adjust Variable Order on Catalog Item/README|Adjust Variable Order on Catalog Item]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Specialized Areas/Fix scripts/Anonymise Data/README|Anonymise Data]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Specialized Areas/Fix scripts/Assign user list to a specific group/README|Assign user list to a specific group]]
