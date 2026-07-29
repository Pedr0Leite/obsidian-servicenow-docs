---
title: "Automatic Group Membership Updates via API"
aliases:
  - Automatic Group Membership Updates via API
tags:
  - servicenow-dev-program
  - code-snippet
  - automatic-group-membership-updates-via-api
  - business-rules
---

# Overview
This code snippet helps ServiceNow developers manage group memberships automatically by integrating with an external API. It retrieves group membership data from a specified API endpoint and updates user-group relationships in ServiceNow accordingly. 

This is useful for organizations where user groups are managed dynamically in external systems, and developer want a seamless and up-to-date integration with ServiceNow.

# How It Works
The script:
- Fetches API Data: It connects to an external API (specified by the `apiEndpoint` variable) to retrieve the current group membership details.
- Parses API Response: The response is parsed to extract user information (based on email) and group identifiers.
- Updates Group Memberships:
    - For each member in the response, the script queries the `sys_user` table to locate the user in ServiceNow based on their email address.
    - Once a user is found, the script creates a new record in the `sys_user_grmember` table, associating the user with the appropriate group.

# Implementation
- Define the `apiEndpoint` URL, replacing `https://your-group-api.com/members` with the actual endpoint from which group membership data will be fetched.
- Ensure that any necessary authentication for the API is configured, such as API keys or tokens.
- This script uses email as a unique identifier for users. Adjust `userGR.addQuery('email', member.email)`; if another identifier is needed.
- Deploy the script as a Business Rule in ServiceNow, setting the appropriate table and conditions under which it should execute. For example, it could run on a schedule or be triggered by a specific update.

## Related Notes

- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Business Rules/ATF Duplicate Execution Order/README|ATF Duplicate Execution Order]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Business Rules/Abort Parent Incident Closure When Child is Open/README|Abort Parent Incident Closure When Child is Open]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Business Rules/Add HR task for HR case/README|Add HR task for HR case]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Business Rules/Add itil role to ootb user query to also see inactive users/README|Add itil role to ootb user query to also see inactive users]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Business Rules/Add notes on tag addition or removal/README|Add notes on tag addition or removal]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Business Rules/Add or remove a tag from the ticket whenever the comments are updated/README|Add or remove a tag from the ticket whenever the comments are updated]]
