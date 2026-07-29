---
title: "Calculate attachment hash code"
aliases:
  - Calculate attachment hash code
tags:
  - servicenow-dev-program
  - code-snippet
  - calculate-attachment-hash-code
  - attachments
---

This is example of recalculate the hash code using the glide digest getSHA256HexFromInputStream method.

GlideDigest() -
    This class provides methods for creating a message digest from strings or input streams using MD5, SHA1, or SHA256 hash algorithms.

Docs link: https://developer.servicenow.com/dev.do#!/reference/api/tokyo/server/no-namespace/c_GlideDigestScopedAPI#r_SGDigest-GlideDigest

getSHA256HexFromInputStream - function takes GlideScriptableInputStream input stream as parameter.

## Related Notes

- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Integration/Attachments/Attachment to Base64/README|Attachment to Base64]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Integration/Attachments/Attachment to base64 in scope/README|Attachment to base64 in scope]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Integration/Attachments/Base 64 to Attachment/README|Base 64 to Attachment]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Integration/Attachments/CSVParser/README|CSVParser]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Integration/Attachments/Convert KnowledgePage to PDF/README|Convert KnowledgePage to PDF]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Integration/Attachments/Create Attachments/README|Create Attachments]]
