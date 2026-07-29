---
title: "Create story task"
aliases:
  - Create story task
tags:
  - servicenow-dev-program
  - code-snippet
  - create-story-task
  - browser-bookmarklets
---

# Create a new story task

When viewing a record in the rm_story table, this bookmarklet will create a new child task and enable you to pre-populate values. The example below will create a task of type `Testing` and set the short description to `Test STRY12345 - Short Description` where the story number and short description values are taken from the story record.

```js
javascript:
var w=window.frames["gsft_main"]!==undefined?window.frames["gsft_main"]:window;
var q="parent="+w.g_form.getUniqueValue()+
"^type=4"+
"^short_description=Test "+w.g_form.getValue("number")+" - "+w.g_form.getValue("short_description")+
"^EQ";
top.open("rm_scrum_task.do?sys_id=-1&sysparm_query="+q);
```

## Related Notes

- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Specialized Areas/Browser Bookmarklets/Copy URL to ServiceNow Journal/README|Copy URL to ServiceNow Journal]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Specialized Areas/Browser Bookmarklets/Create new update set/README|Create new update set]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Specialized Areas/Browser Bookmarklets/Highlight Mandatory fields on form/README|Highlight Mandatory fields on form]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Specialized Areas/Browser Bookmarklets/Impersonation/README|Impersonation]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Specialized Areas/Browser Bookmarklets/Load List with Query/readme|Load List with Query]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Specialized Areas/Browser Bookmarklets/Open copied record/README|Open copied record]]
