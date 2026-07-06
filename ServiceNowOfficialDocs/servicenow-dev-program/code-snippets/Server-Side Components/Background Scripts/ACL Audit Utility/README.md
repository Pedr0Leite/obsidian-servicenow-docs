---
title: "ACL Audit Utility"
aliases:
  - ACL Audit Utility
tags:
  - servicenow-dev-program
  - code-snippet
  - acl-audit-utility
  - background-scripts
---

# ACL Audit Utility for ServiceNow

## Overview

This script audits Access Control Lists (ACLs) in your ServiceNow instance to identify potential security misconfigurations. It helps ensure that ACLs are properly configured and do not unintentionally expose sensitive data.

## Features

- Detects **inactive ACLs**
- Flags ACLs with **no condition or script**
- Warns about **public read access** (ACLs with no roles assigned)
- Logs findings using `gs.info()` and `gs.warning()` for visibility

## Usage

1. Navigate to **System Definition >Scripts - Background** in your ServiceNow instance.
2. Create a new Script Include named `ACL_Audit_Utility`.
3. Paste the contents of `code.js` into the script field.


## Notes

- This script does not make any changes to ACLs; it only audits and logs findings.
- You can extend the script to send email notifications or create audit records in a custom table.

## Related Notes

- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Background Scripts/Access Analysis Utility/README|Access Analysis Utility]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Background Scripts/Add Bookmarks - ITIL Users/README|Add Bookmarks - ITIL Users]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Background Scripts/Add Comments/README|Add Comments]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Background Scripts/Add No Audit Attribute To Multiple Dictionary Entries/README|Add No Audit Attribute To Multiple Dictionary Entries]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Background Scripts/Add Standard Change Model/README|Add Standard Change Model]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Background Scripts/Adding bookmark to Favorites tab/README|Adding bookmark to Favorites tab]]
