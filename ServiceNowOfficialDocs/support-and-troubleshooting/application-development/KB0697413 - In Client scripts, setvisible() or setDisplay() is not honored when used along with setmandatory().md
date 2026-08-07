---
title: "In Client scripts, setvisible() or setDisplay() is not honored when used along with setmandatory()"
aliases:
  - KB0697413
tags:
  - servicenow
  - support-kb
  - client-scripts
  - ui-policy
  - GlideForm
  - g_form
area: application-development
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0697413
kb_number: KB0697413
last_modified: 2024-01-28
---

## In Client scripts, setvisible() or setDisplay() is not honored when used along with setmandatory()

  

### Issue

# Symptoms

* * *

setVisible() and setDisplay() are working as expected but when these APIs used with setMandatory(), setVisible/setDisplay is not honored. 

# Release

Istanbul, Jakarta, Kingston, London 

# Cause

* * *

From Istanbul onwards, we specifically and intentionally block setVisible or setDisplay calls on Mandatory fields to prevent scenarios where a field is mandatory, but not visible to be populated. This is designed functionality that is behaving as expected.

# Resolution

* * *

In order to display and make fields mandatory at the same time:

\-- Use UI Policies instead of client script. Its also recommended using UI Policies over client script due some of the benefits check this doc: [Use UI policy instead of a client script](https://docs.servicenow.com/csh?topicname=client-script-best-practices.html&version=latest#ariaid-title5 "Use UI policy instead of a client script")

\-- If UI Policy is not helping you to achieve your functionality use setMandatory and setVisible in two separate client scripts.

## Related

- [[KB0696583 - Setting 'setSectionDisplay' function to 'false' does not hide the form section.]]
- [[KB0711972 - oldValue returns empty value instead of the previous value for onChange client scripts]]
- [[KB0720671 - Generic error on form Submit canceled due to a script error - please contact your System Administrator]]

## Related Notes

- [[ServiceNowOfficialDocs/support-and-troubleshooting/application-development/KB0696583 - Setting 'setSectionDisplay' function to 'false' does not hide the form section.|Setting 'setSectionDisplay' function to 'false' does not hide the form section.]]
- [[ServiceNowOfficialDocs/support-and-troubleshooting/application-development/KB0686723 - The Field MessageNotification will be cleared if we use Client Script to set value for the field on a form|The Field Message/Notification will be cleared if we use Client Script to set value for the field on a form]]
- [[ServiceNowOfficialDocs/support-and-troubleshooting/application-development/KB0711972 - oldValue returns empty value instead of the previous value for onChange client scripts|oldValue returns empty value instead of the previous value for onChange client scripts]]
- [[ServiceNowOfficialDocs/support-and-troubleshooting/application-development/KB0717382 - An empty or blank box appears inside List collector in Service Portal|An empty or blank box appears inside List collector in Service Portal]]
- [[ServiceNowOfficialDocs/support-and-troubleshooting/application-development/KB0726412 - Unable to change background color of reference field using g_form.getControl in client script|Unable to change background color of reference field using g_form.getControl in client script]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Client-Side Components/Client Scripts/Abort action when description is empty/ReadMe|Abort action when description is empty]]
