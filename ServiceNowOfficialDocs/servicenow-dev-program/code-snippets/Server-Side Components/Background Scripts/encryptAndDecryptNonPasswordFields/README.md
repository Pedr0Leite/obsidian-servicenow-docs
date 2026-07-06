---
title: "encryptAndDecryptNonPasswordFields"
aliases:
  - encryptAndDecryptNonPasswordFields
tags:
  - servicenow-dev-program
  - code-snippet
  - encryptanddecryptnonpasswordfields
  - background-scripts
---

Dear ServiceNow Community,


The GlideEncrypter API uses 3DES encryption standard with NIST 800-131 A Rev2 has recommended against using to encrypt data after 2023. ServiceNow offers alternative cryptographic solutions to the GlideEncrypter API. 

Glide Element API to encrypt/decrypt password2 values through GlideRecord.

Below are the sample scripts I ran in my PDI: For Password fields. 

Note: 'u_pass' is Password (2 Way Encrypted) field.

## Related Notes

- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Background Scripts/ACL Audit Utility/README|ACL Audit Utility]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Background Scripts/Access Analysis Utility/README|Access Analysis Utility]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Background Scripts/Add Bookmarks - ITIL Users/README|Add Bookmarks - ITIL Users]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Background Scripts/Add Comments/README|Add Comments]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Background Scripts/Add No Audit Attribute To Multiple Dictionary Entries/README|Add No Audit Attribute To Multiple Dictionary Entries]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Background Scripts/Add Standard Change Model/README|Add Standard Change Model]]
