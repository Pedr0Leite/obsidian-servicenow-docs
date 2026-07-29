---
title: "Simultaneous update alert is shown when saving a form after adding an attachment"
aliases:
  - KB0750563
  - Simultaneous update alert is shown when saving a form after adding an attachment
tags:
  - servicenow
  - support-kb
  - attachments
  - script-includes
  - form-behavior
area: application-development
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0750563
kb_number: KB0750563
last_modified: 2024-04-07
---

## Simultaneous update alert is shown when saving a form after adding an attachment

  

### Issue

# Symptoms

When using the crossfuze simultaneous update alert package, after adding an attachment to a form, the user receives a simultaneous update alert popup when saving, even if no other updates were made.

# Release

All

# Cause

The crossfuze script include SimultaneousUpdateAlert checks to see if the record was last updated by the current user. When adding an attachment, the update is made under the user: 'system'. As system is not the current user, the script include will show the simultaneous update alert popup.

# Resolution

To resolve this, you can add an additional check for the system user to the SimultaneousUpdateAlert script include.

1) Navigate to System Definition > Script Includes

2) Find the SimultaneousUpdateAlert script include entry

3) In the script text area, change line 8 as shown below:

```
if(rec.sys_updated_by != this.getParameter('sysparm_user') && rec.sys_updated_by != 'system'){
```

4) Save the record

## Related

- [[KB0749222 - Scripted fields not filling in for non-admin Users for the scoped applications]]
- [[KB0748577 - How to avoid live form feature triggering th onchange client script on another user screen]]

## Related Notes

- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Script Includes/attachments/README|attachments]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Client-Side Components/UI Actions/Open Record in Alternate Instance/Script Includes/README|Script Includes]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Client-Side Components/UI Actions/Open Record in Alternate Instance/Script Includes/sys_script_include_config|sys_script_include_config]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Integration/Attachments/Attachment to Base64/README|Attachment to Base64]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Integration/Attachments/Attachment to base64 in scope/README|Attachment to base64 in scope]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Integration/Attachments/Base 64 to Attachment/README|Base 64 to Attachment]]
