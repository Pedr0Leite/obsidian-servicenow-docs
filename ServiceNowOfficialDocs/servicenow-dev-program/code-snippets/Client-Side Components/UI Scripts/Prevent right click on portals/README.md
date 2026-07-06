---
title: "Prevent right click on portals"
aliases:
  - Prevent right click on portals
tags:
  - servicenow-dev-program
  - code-snippet
  - prevent-right-click-on-portals
  - ui-scripts
---

**Steps to Activate**
1. Open the portals you want to disable right-click in "sp_portal" table.
2. Open the theme attached to the portal.
3. In the theme under "JS Includes" relatd list, create new JS include and select the UI script you created.
Go to your portal and try to roght click, it will prevent and show the alert message.

**Use Case**
1. Many high security organizations like banks do not want their images or links to be copied through "inspect" so right-click need to be disabled.
2. Many organizations want their source code to be hidden so they prevent right-click.


 **Note**
  1. This UI script is applied through portal theme , so it will be specific to portals using that theme. It will not have instance wide affect.

## Related Notes

- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Client-Side Components/UI Scripts/Custom Change Schedule/README|Custom Change Schedule]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Client-Side Components/UI Scripts/Disable Copy Paste For Portal/README|Disable Copy Paste For Portal]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Client-Side Components/UI Scripts/Display number of created records/README|Display number of created records]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Client-Side Components/UI Scripts/Make OOB Attachment Mandatory/README|Make OOB Attachment Mandatory]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Client-Side Components/UI Scripts/Observe MRVS Events/README|Observe MRVS Events]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Client-Side Components/UI Scripts/PersistentAnnouncementBanner/README|PersistentAnnouncementBanner]]
