---
title: "Conditional Form Section based on Role"
aliases:
  - Conditional Form Section based on Role
tags:
  - servicenow-dev-program
  - code-snippet
  - conditional-form-section-based-on-role
  - client-scripts
---

# Conditional Form Sections Based on User Role

## Overview
This client script dynamically shows or hides specific sections of a form based on the logged-in user’s role. It ensures that only authorized users, such as managers, can view and interact with sensitive sections (e.g., budget approvals).

## Use Case
- Managers: Can see the Budget Approval section.
- Other Users: The section remains hidden.

## How It Works
- The script runs onLoad of the form.
- It checks if the logged-in user has the specified role (manager in this example).
- If the user has the role, the Budget Approval section is shown. If not, it remains hidden.

## Related Notes

- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Client-Side Components/Client Scripts/Abort action when description is empty/ReadMe|Abort action when description is empty]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Client-Side Components/Client Scripts/Abort direct incident closure without Resolve State/readme|Abort direct incident closure without Resolve State]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Client-Side Components/Client Scripts/Add Field Decoration/README|Add Field Decoration]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Client-Side Components/Client Scripts/Add Image to Field Based on Company/README|Add Image to Field Based on Company]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Client-Side Components/Client Scripts/Adding Placeholder on Resolution Notes/README|Adding Placeholder on Resolution Notes]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Client-Side Components/Client Scripts/Auto Update Priority based on Impact and Urgency/readme|Auto Update Priority based on Impact and Urgency]]
