---
title: "attachments"
aliases:
  - attachments
tags:
  - servicenow-dev-program
  - code-snippet
  - attachments
  - script-includes
---

Little utility for attachment types

## Example Script
var att = new Attachment(current);
if(att.hasImage())
    var attID = att.getImageID();

## Related Notes

- [[ServiceNowOfficialDocs/support-and-troubleshooting/application-development/KB0750563 - Simultaneous update alert is shown when saving a form after adding an attachment|Simultaneous update alert is shown when saving a form after adding an attachment]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Client-Side Components/UI Actions/Open Record in Alternate Instance/Script Includes/README|Script Includes]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Client-Side Components/UI Actions/Open Record in Alternate Instance/Script Includes/sys_script_include_config|sys_script_include_config]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Integration/Attachments/Attachment to Base64/README|Attachment to Base64]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Integration/Attachments/Attachment to base64 in scope/README|Attachment to base64 in scope]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Integration/Attachments/Base 64 to Attachment/README|Base 64 to Attachment]]
