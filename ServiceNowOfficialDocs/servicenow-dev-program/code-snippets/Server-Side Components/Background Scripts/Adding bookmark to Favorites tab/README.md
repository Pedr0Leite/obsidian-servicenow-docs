---
title: "Adding bookmark to Favorites tab"
aliases:
  - Adding bookmark to Favorites tab
tags:
  - servicenow-dev-program
  - code-snippet
  - adding-bookmark-to-favorites-tab
  - background-scripts
---

The script bookmarks the list of incidents assigned to the user's groups in ServiceNow's favorite tab. It works by :
  
--> Constructing a filter for incidents assigned to logged-in user's groups using the OOTB dynamic filter functionality.  
--> Checking if the list is already bookmarked.  
--> If not, it creates a new bookmark with the title : "Incidents assigned to my groups", adds the list url.  

This allows the user to quickly access the list of relevant incidents from the favorites tab.	 

## Related Notes

- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Background Scripts/ACL Audit Utility/README|ACL Audit Utility]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Background Scripts/Access Analysis Utility/README|Access Analysis Utility]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Background Scripts/Add Bookmarks - ITIL Users/README|Add Bookmarks - ITIL Users]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Background Scripts/Add Comments/README|Add Comments]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Background Scripts/Add No Audit Attribute To Multiple Dictionary Entries/README|Add No Audit Attribute To Multiple Dictionary Entries]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Background Scripts/Add Standard Change Model/README|Add Standard Change Model]]
