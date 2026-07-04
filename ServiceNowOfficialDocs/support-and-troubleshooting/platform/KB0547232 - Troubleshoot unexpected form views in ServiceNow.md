---
title: "Troubleshoot unexpected form views in ServiceNow"
aliases:
  - KB0547232
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0547232
kb_number: KB0547232
last_modified: 2026-03-24
---

## Troubleshoot unexpected form views in ServiceNow

  

### Issue

Troubleshoot why a user does not see the expected view for a form. This article covers the most common causes and how to identify which view is being applied.

### Release

  All releases

### Cause

Several conditions can cause a user to see an unexpected form view:

-   A view rule is forcing a different view.
-   A business rule is forcing a different view.
-   A user preference is set to a different view.

### Resolution

To quickly check whether a different view is active, right-select the record, go to **View**, and verify which view is selected. If you do not have access to that option, use the following steps to identify the view from the record URL.

1.  Display a list of records from the table you want to check (for example, Incident).
2.  Open one of the records in a new browser tab. You can do this by holding the Windows key and selecting the record ID in the list, or by right-selecting the record and choosing **Open in new window**.
3.  In the browser tab, locate the full URL. For example: https://\[myinstance\].service-now.com/incident.do?sys\_id=3ed3e2172b8631006c59ae6219da1585&sysparm\_record\_target=incident&sysparm\_record\_row=1&sysparm\_record\_rows=63&sysparm\_record\_list=active%3Dtrue%5EORDERBYDESCnumber
4.  In the URL, look for **sysparm\_view**. If no view is specified, the default view is used. If a different view appears in the URL, that view may be causing the unexpected display.
5.  If a different view is active, check the following to identify the source:
    -   Go to **System UI > View Rules** and check for any view rules that apply to your table.
    -   Search business rules for any that could affect the view. Look for the text <tablename>GetViewName in the **Script field**, replacing <tablename> with the actual table name. For example, for the Incident table, search for incidentGetViewName.
    -   Check whether the affected users have a system preference set to a different view. User preferences for views follow the naming pattern **<tablename>.view** — for example, incident.view.

### Related Links

[Create a view rule](https://www.servicenow.com/docs/r/platform-user-interface/t_CreateAViewRule.html "Create a view rule")

[Control when the system displays a view](https://www.servicenow.com/docs/r/platform-user-interface/control-views.html "Control when the system displays a view")
