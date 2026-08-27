---
title: "User acknowledgement Using UI script and user preferences"
aliases:
  - User acknowledgement Using UI script and user preferences
tags:
  - servicenow-dev-program
  - code-snippet
  - user-acknowledgement-using-ui-script-and-user-preferences
  - ui-scripts
---

**Create a user preference as follows:**
<img width="1675" height="420" alt="image" src="https://github.com/user-attachments/assets/efcd19dd-f1ad-440a-ae59-10cc63832cad" />
**Create a UI script:**
<img width="1646" height="808" alt="image" src="https://github.com/user-attachments/assets/207f9dfa-4c6c-4686-84ac-3ff5294a0771" />
This script runs during login and checks the user preference. 
If the preference is set to false, it displays the acknowledgement popup by calling UI page

**UI Page details:**
<img width="1511" height="897" alt="image" src="https://github.com/user-attachments/assets/74d4be0f-9401-4733-81df-fca8f52b644e" />
Set the user preference to true so that the popup will not appear for every login.

**Output**:
**On user login:**
<img width="1896" height="748" alt="image" src="https://github.com/user-attachments/assets/1af1b7ec-4647-4bb4-a786-8070817b21f8" />

## Related Notes

- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Client-Side Components/UI Scripts/Custom Change Schedule/README|Custom Change Schedule]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Client-Side Components/UI Scripts/Disable Copy Paste For Portal/README|Disable Copy Paste For Portal]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Client-Side Components/UI Scripts/Display number of created records/README|Display number of created records]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Client-Side Components/UI Scripts/Make OOB Attachment Mandatory/README|Make OOB Attachment Mandatory]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Client-Side Components/UI Scripts/Observe MRVS Events/README|Observe MRVS Events]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Client-Side Components/UI Scripts/PersistentAnnouncementBanner/README|PersistentAnnouncementBanner]]
