---
title: "Modern Email Layout Designs"
aliases:
  - Modern Email Layout Designs
tags:
  - servicenow-dev-program
  - code-snippet
  - modern-email-layout-designs
  - notifications
---

### Overview

Added a **modern, fully responsive Email Layout** for ServiceNow notifications.  
This layout provides a professional and dynamic look for system emails such as approvals, alerts, and workflow updates.

---

### 🔑 Features

- Clean, responsive HTML with inline CSS (Outlook-safe)
- Dynamic placeholders for subject, body, recipient, and links
- Supports unsubscribe and preference management variables
- Compatible with all standard ServiceNow notification types
- Easily customizable header colors, logo, and footer content

---

### 📁 Files Included

| File          | Description                          |
| ------------- | ------------------------------------ |
| `Script.html` | Email Layout definition (HTML + CSS) |
| `README.md`   | Setup guide and usage instructions   |

---

### ⚙️ Installation

1. Navigate to **System Policy → Email → Email Layout** → New
2. Paste the HTML layout above into the content field
3. Save and name it **"Modern Notification Layout"**
4. Assign this layout to your email notifications (under "Layout" field)

---

### 💡 Example Use Case

Used for travel approvals, expense updates, password resets, or ticket notifications:

```html
${mail_script:travel_notification}
```

## Related Notes

- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Modern Development/Service Portal Widgets/serviceportal-widget-library/serviceportal-widget-library-master/notifications/pe-bootstrap-notify/README|pe-bootstrap-notify]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Specialized Areas/Notifications/Add KB Article Link Dynamic Email Script to Notification/readme|Add KB Article Link Dynamic Email Script to Notification]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Specialized Areas/Notifications/Conditional Trigger/README|Conditional Trigger]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Specialized Areas/Notifications/Notify Users on Specific Date/README|Notify Users on Specific Date]]
- [[ServiceNowOfficialDocs/support-and-troubleshooting/access-controls-authentication/KB0715790 - Users see an error message Record doesn't exist or ACL restricts the record retrieval when making changes to their Notif|Users see an error message \"Record doesn't exist or ACL restricts the record retrieval\" when making changes to their Notifications settings]]
- [[ServiceNowOfficialDocs/support-and-troubleshooting/access-controls-authentication/KB0717149 - Error message Record doesn't exist or ACL restricts the record retrieval appearing when ITIL users try to disallow notif|Error message \"Record doesn't exist or ACL restricts the record retrieval\" appearing when ITIL users try to disallow notifications]]
