---
title: "Group Membership API"
aliases:
  - Group Membership API
tags:
  - servicenow-dev-program
  - code-snippet
  - group-membership-api
  - scripted-rest-api
---

# Group Membership API- Scripted REST API
## Overview
This API provides a simple, secure way to reterive all members of a specified user group in ServiceNow. It allows integrations, Service Portal widgets, or external systems to query group membership without giving direct access to user tables

### API Details
- **API Name**: Group Membership API
- **API ID**: group_membership_api
- **ResourceName**: Members
- **Relative Path**: /members
- **HTTP Method**: GET
- **Query Parameter**: groupName (required)

## Request Format

### Example Request
GET https://<instance>.service-now.com/api/1819147/group_membership_api/members?groupName=Hardware

### Example Response
```json
{
   {
  "result": {
    "groupName": "Hardware",
    "totalMembers": 7,
    "member": [
      {
        "userName": "beth.anglin",
        "displayName": "Beth Anglin",
        "email": "beth.anglin@example.com",
        "active": "true"
      },
      {
        "userName": "itil",
        "displayName": "ITIL User",
        "email": "itil@example.com",
        "active": "true"
      },
      {
        "userName": "bow.ruggeri",
        "displayName": "Bow Ruggeri",
        "email": "bow.ruggeri@example.com",
        "active": "true"
      },
      {
        "userName": "david.dan",
        "displayName": "David Dan",
        "email": "david.dan@example.com",
        "active": "true"
      },
      {
        "userName": "david.loo",
        "displayName": "David Loo",
        "email": "david.loo@example.com",
        "active": "true"
      },
      {
        "userName": "don.goodliffe",
        "displayName": "Don Goodliffe",
        "email": "don.goodliffe@example.com",
        "active": "true"
      },
      {
        "userName": "fred.luddy",
        "displayName": "Fred Luddy",
        "email": "fred.luddy@example.com",
        "active": "true"
      }
    ]
  }
}

}

## Related Notes

- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Client-Side Components/UI Actions/Open Record in Alternate Instance/Scripted REST API/sys_ws_definition_config|sys_ws_definition_config]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Client-Side Components/UI Actions/Open Record in Alternate Instance/Scripted REST API/sys_ws_operation/sys_ws_operation_config|sys_ws_operation_config]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Integration/Scripted REST Api/Approval APIs/README|Approval APIs]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Integration/Scripted REST Api/Approval on Behalf/README|Approval on Behalf]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Integration/Scripted REST Api/CMDB API/README|CMDB API]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Integration/Scripted REST Api/CURL Script to create incident via tableAPI/README|CURL Script to create incident via tableAPI]]
