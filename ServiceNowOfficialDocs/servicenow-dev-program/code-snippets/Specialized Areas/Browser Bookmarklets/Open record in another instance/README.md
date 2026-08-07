---
title: "Open record in another instance"
aliases:
  - Open record in another instance
tags:
  - servicenow-dev-program
  - code-snippet
  - open-record-in-another-instance
  - browser-bookmarklets
---

# Open Same Record in Another Instance (Browser Bookmarklet)

## Description
This bookmarklet allows ServiceNow developers, admins, or QA testers to **quickly open the same record in another instance** (e.g., DEV → TEST → UAT → PROD) without manually searching for the record or typing the URL.  

It is especially useful for:
- Comparing records across environments
- Testing configuration changes
- Debugging workflows or UI policies across instances

Instead of typing the target instance every time, it provides **clickable buttons** for your predefined instances.

---

## Features
- Detects current instance automatically
- Opens the same record in a **new tab**
- Pop-up overlay with buttons for predefined target instances
- Toggleable: overlay disappears after selecting or closing
- Fully client-side — works on any ServiceNow record page

---

## How to use

1. Create a new bookmark in your browser.  
2. Name it: `Open in Another Instance`  
3. In the URL field, paste the bookmarklet code present in [Open Record in Another Instance](./Open%20record%20in%20another%20instance/Open%20record%20in%20another%20instance.js)
4. **Important** In the script, update the instance names with your instances.
   For example purpose ["dev12345","test12345","uat12345","prod12345"] are added in the code.
5. Now open any record in any ServiceNow instance and click on the bookmark and select the instance to open.

Note : Please be noted that this will work for all the ServiceNow instances with URL like https://xxxx.service-now.com
For custom URLs, you need to tweak the code slightly as required.

SCreenshots:
<img width="1900" height="534" alt="image" src="https://github.com/user-attachments/assets/03d0ae55-c2fb-48bc-bffc-a6061be79b16" />

## Related Notes

- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Specialized Areas/Browser Bookmarklets/Copy URL to ServiceNow Journal/README|Copy URL to ServiceNow Journal]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Specialized Areas/Browser Bookmarklets/Create new update set/README|Create new update set]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Specialized Areas/Browser Bookmarklets/Create story task/README|Create story task]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Specialized Areas/Browser Bookmarklets/Highlight Mandatory fields on form/README|Highlight Mandatory fields on form]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Specialized Areas/Browser Bookmarklets/Impersonation/README|Impersonation]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Specialized Areas/Browser Bookmarklets/Load List with Query/readme|Load List with Query]]
