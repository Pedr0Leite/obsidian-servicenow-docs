---
title: "Adding Placeholder on Resolution Notes"
aliases:
  - Adding Placeholder on Resolution Notes
tags:
  - servicenow-dev-program
  - code-snippet
  - adding-placeholder-on-resolution-notes
  - client-scripts
---

# Adding Placeholder Text in Resolution Notes

To maintain consistency and ensure specific information is captured in resolution notes, process owners may require fulfillers to follow a predefined format when resolving tickets.

By adding **placeholder** text in the resolution notes, fulfillers are reminded of the required information(e.g., Root cause, Steps taken, Resolution provided), reducing the risk of missing important details. The placeholder disappears as soon as the fulfiller begins entering their notes, ensuring it doesn't interfere with their input.

## How It Works

### When?
- The placeholder text is automatically added when the state of the ticket changes to Resolved (6).

### What Happens?
- A placeholder text appears in the resolution notes field to guide the fulfiller.
- As soon as the fulfiller starts typing, the placeholder disappears.
- This ensures consistency and alignment with the process requirements.

## Related Notes

- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Client-Side Components/Client Scripts/Abort action when description is empty/ReadMe|Abort action when description is empty]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Client-Side Components/Client Scripts/Abort direct incident closure without Resolve State/readme|Abort direct incident closure without Resolve State]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Client-Side Components/Client Scripts/Add Field Decoration/README|Add Field Decoration]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Client-Side Components/Client Scripts/Add Image to Field Based on Company/README|Add Image to Field Based on Company]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Client-Side Components/Client Scripts/Auto Update Priority based on Impact and Urgency/readme|Auto Update Priority based on Impact and Urgency]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Client-Side Components/Client Scripts/Auto-Populate Planned End Date/README|Auto-Populate Planned End Date]]
