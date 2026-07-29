---
title: "Generate Attachment and add it to the email"
aliases:
  - Generate Attachment and add it to the email
tags:
  - servicenow-dev-program
  - code-snippet
  - generate-attachment-and-add-it-to-the-email
  - server-side
---

ServiceNow Incident CSV Export Email Script

This ServiceNow email script automatically generates and attaches a CSV file containing incident data to email notifications. The script extracts active incidents from your ServiceNow instance, formats them into a structured CSV file, and attaches the file to outbound email notifications, providing recipients with a comprehensive incident report in a portable format.

What This Script Does:
The email script performs the following operations:
Data Extraction: Queries all active incidents from the ServiceNow incident table
CSV Generation: Formats incident data into a structured CSV file with predefined headers
File Attachment: Automatically attaches the generated CSV file to email notifications
Dynamic Content: Creates fresh data exports each time the notification is triggered
Portable Format: Provides incident data in a universally readable CSV format

## Related Notes

- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Server Side/CallScriptIncludeWithParameters/README|CallScriptIncludeWithParameters]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Server Side/CheckTableExtension/README|CheckTableExtension]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Server Side/Create Admin Users/README|Create Admin Users]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Server Side/Create Tiny Url with API's/README|Create Tiny Url with API's]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Server Side/CreateUpdateCIThroughIRE/README|CreateUpdateCIThroughIRE]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Server Side/Custom Relationship/README|Custom Relationship]]
