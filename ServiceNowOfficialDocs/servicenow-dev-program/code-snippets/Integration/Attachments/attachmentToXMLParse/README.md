---
title: "attachmentToXMLParse"
aliases:
  - attachmentToXMLParse
tags:
  - servicenow-dev-program
  - code-snippet
  - attachmenttoxmlparse
  - attachments
---

How to use this script:

1. Create new Script Include named as "getXMLContent"
2. Add the script provided in the code.js script

How to Test this script:

1. Create Data source XML Type
2. Attach a xml attachment to it
3. Use the script include in below format
4. Pass the Data source table name and sysid of the data source in the function

This script block will extract the XML content from the ServiceNow XML attachment. Below is an example:

```var xmlContent = new getXMLContent();```

```gs.print(xmlContent.getXMLContentFromAttachment('sys_data_source',<sys_id of the record where attachment attached>));```

## Related Notes

- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Integration/Attachments/Attachment to Base64/README|Attachment to Base64]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Integration/Attachments/Attachment to base64 in scope/README|Attachment to base64 in scope]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Integration/Attachments/Base 64 to Attachment/README|Base 64 to Attachment]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Integration/Attachments/CSVParser/README|CSVParser]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Integration/Attachments/Calculate attachment hash code/README|Calculate attachment hash code]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Integration/Attachments/Convert KnowledgePage to PDF/README|Convert KnowledgePage to PDF]]
