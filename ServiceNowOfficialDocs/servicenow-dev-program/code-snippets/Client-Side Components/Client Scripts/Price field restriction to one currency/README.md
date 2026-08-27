---
title: "Price field restriction to one currency"
aliases:
  - Price field restriction to one currency
tags:
  - servicenow-dev-program
  - code-snippet
  - price-field-restriction-to-one-currency
  - client-scripts
---

# Client Script - Set Price type field to only one currency

In a multi currecny enabled servicenow environment, if you have a requirement to enable only one currency choice for a particular table and field of type Price.

## Usage

- Create a new client script
- Set the type to OnLoad.
- Copy the script to your client script.
- Update the <price_field> in the client script to 'Your field name'
- Add your currency code and symbol in place of USD & $
- Save

## Related Notes

- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Client-Side Components/Client Scripts/Abort action when description is empty/ReadMe|Abort action when description is empty]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Client-Side Components/Client Scripts/Abort direct incident closure without Resolve State/readme|Abort direct incident closure without Resolve State]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Client-Side Components/Client Scripts/Add Field Decoration/README|Add Field Decoration]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Client-Side Components/Client Scripts/Add Image to Field Based on Company/README|Add Image to Field Based on Company]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Client-Side Components/Client Scripts/Adding Placeholder on Resolution Notes/README|Adding Placeholder on Resolution Notes]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Client-Side Components/Client Scripts/Auto Update Priority based on Impact and Urgency/readme|Auto Update Priority based on Impact and Urgency]]
