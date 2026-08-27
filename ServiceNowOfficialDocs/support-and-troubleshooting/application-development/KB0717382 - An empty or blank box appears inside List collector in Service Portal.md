---
title: "An empty or blank box appears inside List collector in Service Portal"
aliases:
  - KB0717382
tags:
  - servicenow
  - support-kb
  - client-scripts
  - list-collector
  - service-portal
  - ui-policy
area: application-development
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0717382
kb_number: KB0717382
last_modified: 2025-06-23
---

## An empty or blank box appears inside List collector in Service Portal

  

### Issue

If the list collector field shows an empty box, this means any empty character is passed in the field via client script or UI policies via setValue().

### Cause

As shown in the following screenshot, when an empty box shows in the list collector field it means your client script is using a space character to set the value.

![](sys_attachment.do?sys_id=33762ab5839ea2d4cdbbc430feaad371)

### Resolution

Identify the client scripts used to set the value for the list collector variable

This example shows the extra space in the g\_form.setValue() 

g\_form.setValue('affected\_varibale\_name',' ');

To fix the issue, remove the empty space used in the setValue() 

g\_form.setValue('affected\_varibale\_name','');

## Related

- [[KB0724429 - glide_list reference field created through a REST API call stores the actual value instead of reference of the field]]
- [[KB0711972 - oldValue returns empty value instead of the previous value for onChange client scripts]]

## Related Notes

- [[ServiceNowOfficialDocs/support-and-troubleshooting/application-development/KB0696583 - Setting 'setSectionDisplay' function to 'false' does not hide the form section.|Setting 'setSectionDisplay' function to 'false' does not hide the form section.]]
- [[ServiceNowOfficialDocs/support-and-troubleshooting/application-development/KB0697413 - In Client scripts, setvisible() or setDisplay() is not honored when used along with setmandatory()|In Client scripts, setvisible() or setDisplay() is not honored when used along with setmandatory()]]
- [[ServiceNowOfficialDocs/support-and-troubleshooting/application-development/KB0749991 - [Service Portal] Injection argument not found (newValue) error|[Service Portal]: Injection argument not found (newValue) error]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Client-Side Components/Client Scripts/Abort action when description is empty/ReadMe|Abort action when description is empty]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Client-Side Components/Client Scripts/Abort direct incident closure without Resolve State/readme|Abort direct incident closure without Resolve State]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Client-Side Components/Client Scripts/Add Field Decoration/README|Add Field Decoration]]
