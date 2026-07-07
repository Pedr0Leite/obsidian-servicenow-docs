---
title: "Inbound Email Action to Create User and Assign Groups"
aliases:
  - Inbound Email Action to Create User and Assign Groups
tags:
  - servicenow-dev-program
  - code-snippet
  - inbound-email-action-to-create-user-and-assign-groups
  - inbound-actions
---

Inbound Email Action to Create User and Assign Groups

If an admin sends an email with specific user details, the script automatically:
Creates a new user (if not existing).
Assigns them to multiple groups.

Create new Inbound Action:
Target table: sys_user
Type: New / Reply (depending on how you want it triggered)

Example Email Format

Subject: Create New User
Name: Abc Xyz
Email: abc.xyz@example.com
UserID: abc_xyz
Department: IT
Groups: Network Team, Application Support, Database Admins

Working:

Script reads each line from email body.
Extracts values for each field (Name, Email, etc.) using regex.
Checks if the user exists → if not, creates it.
Adds the user to the given list of groups.

## Related Notes

- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Inbound Actions/Advanced Scripts/README|Advanced Scripts]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Inbound Actions/Auto Incident Creation from Case Email/README|Auto Incident Creation from Case Email]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Inbound Actions/Auto Reply Email/README|Auto Reply Email]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Inbound Actions/Automate creation of incidents through inbound actions/README|Automate creation of incidents through inbound actions]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Inbound Actions/Duplicate Incident Detection and Creation/README|Duplicate Incident Detection and Creation]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Inbound Actions/Email Text as Attachment/README|Email Text as Attachment]]
