---
title: "Version Checker"
aliases:
  - Version Checker
tags:
  - servicenow-dev-program
  - code-snippet
  - version-checker
  - background-scripts
---

# Version Checker for Out of the box configuration analysis
# VersionUpdateChecker.js

# Why us it?
If an admin needs a list of all 'customized' files from certain applications

# How to use it?
Copy/Paste this as a background script ("Scripts - Background" module)  
Replace "< < names > >" with application names to check new versions that have been modified from OOTB  
Run script and then copy/paste the results into Excel, then do a split on columns, and select delimited and choose the pipe symbol  
Alternatively, save output as a .txt file and import into excel using the method linked below  
https://support.microsoft.com/en-us/office/import-or-export-text-txt-or-csv-files-5250ac4c-663c-47ce-937b-339e391393ba  
  
Initial author credit to gary.opela@servicenow.com

## Related Notes

- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Background Scripts/ACL Audit Utility/README|ACL Audit Utility]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Background Scripts/Access Analysis Utility/README|Access Analysis Utility]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Background Scripts/Add Bookmarks - ITIL Users/README|Add Bookmarks - ITIL Users]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Background Scripts/Add Comments/README|Add Comments]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Background Scripts/Add No Audit Attribute To Multiple Dictionary Entries/README|Add No Audit Attribute To Multiple Dictionary Entries]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Background Scripts/Add Standard Change Model/README|Add Standard Change Model]]
