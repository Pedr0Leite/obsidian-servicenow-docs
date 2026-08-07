---
title: "Auto-Deactivate Users Not Logged In for X Days"
aliases:
  - Auto-Deactivate Users Not Logged In for X Days
tags:
  - servicenow-dev-program
  - code-snippet
  - auto-deactivate-users-not-logged-in-for-x-days
  - background-scripts
---

# 🧹 ServiceNow Dormant User Cleanup

**ServiceNow Background Script** to automatically **deactivate users** who haven't logged in for a specified number of days.

## 🚀 Usage
1. Navigate to **System Definition → Scripts - Background**.  
2. Paste the script and execute:
   ```javascript
   deactivateDormantUsers(90);

## Related Notes

- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Background Scripts/ACL Audit Utility/README|ACL Audit Utility]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Background Scripts/Access Analysis Utility/README|Access Analysis Utility]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Background Scripts/Add Bookmarks - ITIL Users/README|Add Bookmarks - ITIL Users]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Background Scripts/Add Comments/README|Add Comments]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Background Scripts/Add No Audit Attribute To Multiple Dictionary Entries/README|Add No Audit Attribute To Multiple Dictionary Entries]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Background Scripts/Add Standard Change Model/README|Add Standard Change Model]]
