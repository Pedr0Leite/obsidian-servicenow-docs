---
title: "Email Text as Attachment"
aliases:
  - Email Text as Attachment
tags:
  - servicenow-dev-program
  - code-snippet
  - email-text-as-attachment
  - inbound-actions
---

# Save Email Text as Attachment

### Steps:

Navigate to System Definition \ Script Includes and click New.
Set the following values:<br />
**Name:** emailAsAttachmentUtil<br />
**Accessible from:** All application Scopes = this will allow it to be called by all applications<br />
**Active:** checked<br />
**Description:** You may want to set the description to something like the following to document what this script includes does and how to call it<br />

* [Click here for Script include script](script.js)

**Example of calling a script include from the Inbound action**
```js
//This utility script will take contents from an inbound email and create an attachment on the created record from the inbound email action.  To utilize this script, add the following lines at the end of the inbound email action script:
var emailAsAttachment = new global.emailAsAttachmentUtil();
emailAsAttachment.createAttachment(email, current);
```

## Related Notes

- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Inbound Actions/Advanced Scripts/README|Advanced Scripts]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Inbound Actions/Auto Incident Creation from Case Email/README|Auto Incident Creation from Case Email]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Inbound Actions/Auto Reply Email/README|Auto Reply Email]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Inbound Actions/Automate creation of incidents through inbound actions/README|Automate creation of incidents through inbound actions]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Inbound Actions/Duplicate Incident Detection and Creation/README|Duplicate Incident Detection and Creation]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Inbound Actions/Inbound Email Action to Create User and Assign Groups/Readme|Inbound Email Action to Create User and Assign Groups]]
