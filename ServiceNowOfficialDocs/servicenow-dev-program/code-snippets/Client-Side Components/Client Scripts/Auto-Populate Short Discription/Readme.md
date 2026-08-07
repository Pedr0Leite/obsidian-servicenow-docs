---
title: "Auto-Populate Short Discription"
aliases:
  - Auto-Populate Short Discription
tags:
  - servicenow-dev-program
  - code-snippet
  - auto-populate-short-discription
  - client-scripts
---

# Auto-Populate Short Description (Client Script)
## Overview

This client script automatically updates the Short Description field in ServiceNow whenever a user selects a category on the form. It improves data consistency, saves time, and ensures that short descriptions remain meaningful and standardized.

## How It Works

When a user selects a category such as Hardware, Software, or Network, the script automatically prefixes the existing short description with a corresponding label (for example, “Hardware Issue –”).
This makes incident records easier to identify and improves the quality of data entry.

## Configuration Steps

1. Log in to your ServiceNow instance with admin or developer access.
2. Navigate to System Definition → Client Scripts.
3. Create a new Client Script with the following details:

```
Table: Incident
Type: onChange
Field name: category
Copy and paste the provided script into the Script field.
Save the record and make sure the script is active.
```

## Testing

1. Open any existing or new Incident record.
2. Select a category such as Hardware or Software.
3. The Short Description field will automatically update with the corresponding prefix.

## Benefits

Speeds up data entry for users.
Maintains consistency in short descriptions.
Reduces manual effort and human errors.
Enhances clarity in incident listings and reports.

## Related Notes

- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Client-Side Components/Client Scripts/Abort action when description is empty/ReadMe|Abort action when description is empty]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Client-Side Components/Client Scripts/Abort direct incident closure without Resolve State/readme|Abort direct incident closure without Resolve State]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Client-Side Components/Client Scripts/Add Field Decoration/README|Add Field Decoration]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Client-Side Components/Client Scripts/Add Image to Field Based on Company/README|Add Image to Field Based on Company]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Client-Side Components/Client Scripts/Adding Placeholder on Resolution Notes/README|Adding Placeholder on Resolution Notes]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Client-Side Components/Client Scripts/Auto Update Priority based on Impact and Urgency/readme|Auto Update Priority based on Impact and Urgency]]
