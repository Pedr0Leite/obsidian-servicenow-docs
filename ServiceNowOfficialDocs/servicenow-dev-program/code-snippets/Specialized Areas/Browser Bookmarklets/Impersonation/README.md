---
title: "Impersonation"
aliases:
  - Impersonation
tags:
  - servicenow-dev-program
  - code-snippet
  - impersonation
  - browser-bookmarklets
---

# User Impersonation
When a user impersonates another user, the page is redirected to the home page for the new user. This bookmarklet will open the impersonation page in a popup window so the user impersonation can be completed without redirecting the paging being viewed. After selecting the new user, the popup will close and the instance page will refresh with the new user context.

This was updated from a new tab to the popup based on the "Quick Login to current instance" bookmarklet by OrgovanGeza.

```js
javascript:let impWin=window.open("/impersonate_dialog.do", "Impersonation", "scrollbars=no,resizable=no,status=no,location=no,toolbar=no,menubar=no,width=300,height=300,left=100,top=100");setInterval(()=>{if(!impWin.location.pathname.includes("impersonate")){impWin.close();window.location.reload();};},500);
```

## Related Notes

- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Specialized Areas/Browser Bookmarklets/Copy URL to ServiceNow Journal/README|Copy URL to ServiceNow Journal]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Specialized Areas/Browser Bookmarklets/Create new update set/README|Create new update set]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Specialized Areas/Browser Bookmarklets/Create story task/README|Create story task]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Specialized Areas/Browser Bookmarklets/Highlight Mandatory fields on form/README|Highlight Mandatory fields on form]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Specialized Areas/Browser Bookmarklets/Load List with Query/readme|Load List with Query]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Specialized Areas/Browser Bookmarklets/Open copied record/README|Open copied record]]
