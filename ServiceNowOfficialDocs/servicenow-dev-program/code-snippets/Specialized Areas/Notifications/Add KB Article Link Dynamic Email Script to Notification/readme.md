---
title: "Add KB Article Link Dynamic Email Script to Notification"
aliases:
  - Add KB Article Link Dynamic Email Script to Notification
tags:
  - servicenow-dev-program
  - code-snippet
  - add-kb-article-link-dynamic-email-script-to-notification
  - notifications
---

📘 README — KB Article Link Email Script for Notification
✅ Overview

This script is used in a ServiceNow notification triggered from the kb_knowledge table.
It dynamically retrieves the instance URL and constructs a clickable Knowledge Article link in the email body.

🧩 Script Functionality
✔ What It Does

Builds a direct URL pointing to the KB article
Displays the KB Number as a clickable hyperlink
Opens the article in a new browser tab
Improves Knowledge Manager review workflow

🔧 Script Used
// This script assumes it is used in a notification triggered by the kb_knowledge table. 
//use this line to get KB Number ${mail_script:get_kbarticle_link}
(function executeEmailScript(current, template) {
    // Construct the URL to the KB article

    var instanceURL = gs.getProperty('glide.servlet.uri'); // Get the instance URL
    var kbLink = instanceURL + "kb_view.do?sysparm_article=" + current.number; // Adjust based on your URL structure

    // Output the link in HTML format
    template.print('<a href="' + kbLink + '" target="_blank">' + current.number + '</a>');
})(current, template);

📝 Notification Configuration
Setting	Details
Table	Knowledge [kb_knowledge]
Condition	Example: State changes to Pending Approval
Email Script Used	${mail_script:get_kbarticle_link}
Audience	Knowledge Managers / Approvers
📥 Input
Input Source	Description
current.number	KB Article Number (e.g. KB0012345)
System Property	glide.servlet.uri — full instance URL
Notification Payload	Uses script reference in message body

Example Input Values:

Instance URL: https://company.service-now.com/
KB Number: KB1029384

⚙️ Process Flow

1️⃣ Notification triggered on kb_knowledge
2️⃣ Script collects instance URL
3️⃣ Script forms hyperlink using KB Number
4️⃣ Link injected into template via template.print
5️⃣ Email delivered to recipients

✅ Output / Result

📌 Email will show a clickable KB Number link:
➡ Example Link Generated:
https://company.service-now.com/kb_view.do?sysparm_article=KB1029384


📌 In Email (HTML):
KB1029384 → Click → Opens article in new browser tab

📬 Final Email Result Includes:
KB Article Number (hyperlinked)
Article details (added in notification body)
Approve & Reject action buttons (if included)
Cleaner and faster approval workflow

🖼️ Visual Result (Explained from Shared Image)

<img width="733" height="446" alt="image" src="https://github.com/user-attachments/assets/675b3d9b-f121-4c79-8253-bcb964ae05b3" />


The screenshot you shared displays:
✅ KB Article Number hyperlink
✅ Metadata such as short description & requested by
✅ Buttons for Article Approval / Rejection
✅ HTML formatted clean layout for readability

## Related Notes

- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Modern Development/Service Portal Widgets/serviceportal-widget-library/serviceportal-widget-library-master/notifications/pe-bootstrap-notify/README|pe-bootstrap-notify]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Specialized Areas/Notifications/Conditional Trigger/README|Conditional Trigger]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Specialized Areas/Notifications/Modern Email Layout Designs/Readme|Modern Email Layout Designs]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Specialized Areas/Notifications/Notify Users on Specific Date/README|Notify Users on Specific Date]]
- [[ServiceNowOfficialDocs/support-and-troubleshooting/access-controls-authentication/KB0715790 - Users see an error message Record doesn't exist or ACL restricts the record retrieval when making changes to their Notif|Users see an error message \"Record doesn't exist or ACL restricts the record retrieval\" when making changes to their Notifications settings]]
- [[ServiceNowOfficialDocs/support-and-troubleshooting/access-controls-authentication/KB0717149 - Error message Record doesn't exist or ACL restricts the record retrieval appearing when ITIL users try to disallow notif|Error message \"Record doesn't exist or ACL restricts the record retrieval\" appearing when ITIL users try to disallow notifications]]
