---
title: "Encode and Decode URI"
aliases:
  - Encode and Decode URI
tags:
  - servicenow-dev-program
  - code-snippet
  - encode-and-decode-uri
  - background-scripts
---

EncodeURI refers to the process of converting a string into that is safe for use in URI(Uniform Resource identifier). 
It is done by replacing characters that have special meanings in a URI with their percentage encoded equivalents.

The common use case in ServiceNow is in the Rest Message Endpoint.
This endpoint in Rest Message doesn't accept the special characters such as { so by using encodeURI we can encode it and 
then use it in the Rest message endpoint to get/post responses.

DecodeURI which just do the reverse by decoding the EncodedURI.

## Related Notes

- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Background Scripts/ACL Audit Utility/README|ACL Audit Utility]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Background Scripts/Access Analysis Utility/README|Access Analysis Utility]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Background Scripts/Add Bookmarks - ITIL Users/README|Add Bookmarks - ITIL Users]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Background Scripts/Add Comments/README|Add Comments]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Background Scripts/Add No Audit Attribute To Multiple Dictionary Entries/README|Add No Audit Attribute To Multiple Dictionary Entries]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Background Scripts/Add Standard Change Model/README|Add Standard Change Model]]
