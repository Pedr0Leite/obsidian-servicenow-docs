---
title: "Unable to change background color of reference field using g_form.getControl in client script"
aliases:
  - KB0726412
tags:
  - servicenow
  - support-kb
  - client-scripts
  - g_form
  - reference-fields
  - ui-customization
area: application-development
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0726412
kb_number: KB0726412
last_modified: 2024-04-07
---

## Unable to change background color of reference field using g\_form.getControl in client script

  

### Issue

# Symptoms

* * *

When trying to change the background color of a reference field, the following does not work:

g\_form.getControl('reference\_field').style.backgroundColor = 'red'

The above will work for other field types, except not for reference fields.

# Release

* * *

All

# Cause

* * *

The getControl() method is not appropriate for reference fields.

# Resolution

* * *

The right method for reference fields is getDisplayBox(), like so:

g\_form.getDisplayBox('reference\_field').style.backgroundColor = 'green'

## Related

- [[KB0725201 - Function URLSearchParams is not supported by IE]] - other client-script/browser API quirk
- [[KB0745114 - Catalog client script is not hiding the container and the variables within the container]] - g_form API usage pitfalls

## Related Notes

- [[ServiceNowOfficialDocs/support-and-troubleshooting/application-development/KB0686723 - The Field MessageNotification will be cleared if we use Client Script to set value for the field on a form|The Field Message/Notification will be cleared if we use Client Script to set value for the field on a form]]
- [[ServiceNowOfficialDocs/support-and-troubleshooting/application-development/KB0696583 - Setting 'setSectionDisplay' function to 'false' does not hide the form section.|Setting 'setSectionDisplay' function to 'false' does not hide the form section.]]
- [[ServiceNowOfficialDocs/support-and-troubleshooting/application-development/KB0697413 - In Client scripts, setvisible() or setDisplay() is not honored when used along with setmandatory()|In Client scripts, setvisible() or setDisplay() is not honored when used along with setmandatory()]]
- [[ServiceNowOfficialDocs/support-and-troubleshooting/application-development/KB0721276 - How to adjust VIP icon near to the field label|How to adjust VIP icon near to the field label]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Client-Side Components/Client Scripts/Abort action when description is empty/ReadMe|Abort action when description is empty]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Client-Side Components/Client Scripts/Abort direct incident closure without Resolve State/readme|Abort direct incident closure without Resolve State]]
