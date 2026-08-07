---
title: "Create new update set"
aliases:
  - Create new update set
tags:
  - servicenow-dev-program
  - code-snippet
  - create-new-update-set
  - browser-bookmarklets
---

# Create udpate set

When viewing a record in the rm_story table, this bookmarklet will create a update set in a DIFFERENT instance and enable you to pre-populate values. The example below will create an update set in the ficticious "MYDEV" instance and set the Name (`STRY1234 - Short Description`) and Description fields based on values taken from the story record. To use this bookmarklet, udpate the instance name and query string as needed.

```js
javascript:
var w=window.frames["gsft_main"]!==undefined?window.frames["gsft_main"]:window;
var q="name="+w.g_form.getValue("number")+" - "+w.g_form.getValue("short_description")+
    "^description=Description:  @"+w.g_form.getValue("description");
top.open("https://MYDEV.service-now.com/sys_update_set.do?sys_id=-1&sysparm_query="+q);

```

## Related Notes

- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Specialized Areas/Browser Bookmarklets/Copy URL to ServiceNow Journal/README|Copy URL to ServiceNow Journal]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Specialized Areas/Browser Bookmarklets/Create story task/README|Create story task]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Specialized Areas/Browser Bookmarklets/Highlight Mandatory fields on form/README|Highlight Mandatory fields on form]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Specialized Areas/Browser Bookmarklets/Impersonation/README|Impersonation]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Specialized Areas/Browser Bookmarklets/Load List with Query/readme|Load List with Query]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Specialized Areas/Browser Bookmarklets/Open copied record/README|Open copied record]]
