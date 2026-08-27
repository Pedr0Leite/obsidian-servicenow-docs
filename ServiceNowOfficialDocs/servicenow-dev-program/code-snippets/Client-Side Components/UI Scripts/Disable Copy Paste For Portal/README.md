---
title: "Disable Copy Paste For Portal"
aliases:
  - Disable Copy Paste For Portal
tags:
  - servicenow-dev-program
  - code-snippet
  - disable-copy-paste-for-portal
  - ui-scripts
---

**Steps to Activate**
1. Open the portals you want to disable copy/paste operation in "sp_portal" table.
2. Open the theme attached to the portal.
In the theme under "JS Includes" relatd list, create new JS include and select the UI script you created. Go to your portal and try to copy/paste in any catalog item field or any text field on portal.The operation will be prevented with the alert message.

**Use Case**
1. Many high security organizations like banks do not want the users to copy paste account number or passwords to ensure safety.
2. Many input form want the users to re-enter the password or username without copying from other fields.

This UI script is applied through portal theme , so it will be specific to portals using that theme. It will not have instance wide affect.

## Related Notes

- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Client-Side Components/UI Scripts/Custom Change Schedule/README|Custom Change Schedule]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Client-Side Components/UI Scripts/Display number of created records/README|Display number of created records]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Client-Side Components/UI Scripts/Make OOB Attachment Mandatory/README|Make OOB Attachment Mandatory]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Client-Side Components/UI Scripts/Observe MRVS Events/README|Observe MRVS Events]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Client-Side Components/UI Scripts/PersistentAnnouncementBanner/README|PersistentAnnouncementBanner]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Client-Side Components/UI Scripts/Prevent right click on portals/README|Prevent right click on portals]]
