---
title: "Get Instance Info"
aliases:
  - Get Instance Info
tags:
  - servicenow-dev-program
  - code-snippet
  - get-instance-info
  - background-scripts
---

A background script that retrieves and displays essential ServiceNow instance information including IP address, node ID, and instance name.

## Usage

1. Navigate to **System Definition → Scripts - Background**
2. Copy and paste the script content from `getInstanceInfo.js`
3. Click "Run script"
4. Check the system logs and info messages for the instance details

## What It Does

The script:
1. Retrieves the remote IP address of the current transaction using `GlideTransaction.get().getRemoteAddr()`
2. Gets the system/node ID using `GlideServlet.getSystemID()`
3. Fetches the instance name from system properties using `gs.getProperty("instance_name")`
4. Displays IP address and Node ID as info messages in the UI
5. Logs the instance name to the system logs


## Sample Output

**Info Messages:**
```
IP Address: 192.168.1.100
Node ID: node1abc123def456
```

**System Log:**
```
*** Script: mycompany-dev
```

## Related Notes

- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Background Scripts/ACL Audit Utility/README|ACL Audit Utility]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Background Scripts/Access Analysis Utility/README|Access Analysis Utility]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Background Scripts/Add Bookmarks - ITIL Users/README|Add Bookmarks - ITIL Users]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Background Scripts/Add Comments/README|Add Comments]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Background Scripts/Add No Audit Attribute To Multiple Dictionary Entries/README|Add No Audit Attribute To Multiple Dictionary Entries]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Background Scripts/Add Standard Change Model/README|Add Standard Change Model]]
