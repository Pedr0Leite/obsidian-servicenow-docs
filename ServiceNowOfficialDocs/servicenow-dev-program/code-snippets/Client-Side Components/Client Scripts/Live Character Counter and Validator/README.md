---
title: "Live Character Counter and Validator"
aliases:
  - Live Character Counter and Validator
tags:
  - servicenow-dev-program
  - code-snippet
  - live-character-counter-and-validator
  - client-scripts
---

This solution dynamically provides users with real-time feedback on the length of a text input field (like short_description or a single-line text variable).
It immediately displays a character count beneath the field and uses visual cues to indicate when a pre-defined character limit has been reached or exceeded.

This is a vital User Experience (UX) enhancement that helps agents and users write concise, actionable information, leading to improved data quality and better integration reliability.

Name	Live_Character_Counter_ShortDesc_OnLoad	
Table	: Custom Table or Incident
Type	onChange 
Field : Description 
UI Type	All	
Isolate Script	false

## Related Notes

- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Client-Side Components/Client Scripts/Abort action when description is empty/ReadMe|Abort action when description is empty]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Client-Side Components/Client Scripts/Abort direct incident closure without Resolve State/readme|Abort direct incident closure without Resolve State]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Client-Side Components/Client Scripts/Add Field Decoration/README|Add Field Decoration]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Client-Side Components/Client Scripts/Add Image to Field Based on Company/README|Add Image to Field Based on Company]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Client-Side Components/Client Scripts/Adding Placeholder on Resolution Notes/README|Adding Placeholder on Resolution Notes]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Client-Side Components/Client Scripts/Auto Update Priority based on Impact and Urgency/readme|Auto Update Priority based on Impact and Urgency]]
