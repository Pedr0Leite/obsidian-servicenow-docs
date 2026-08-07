---
title: "Configurer Approve Reject Buttons Using Email Scripts"
aliases:
  - Configurer Approve Reject Buttons Using Email Scripts
tags:
  - servicenow-dev-program
  - code-snippet
  - configurer-approve-reject-buttons-using-email-scripts
  - mail-scripts
---

Use Case: Set up Approve and Reject buttons using Email script to Approve/Reject through Email (Use thisv email script on the sysapproval_approver Table Notifications)

1)Upload below images to DB tables in ServiceNow (System UI> Images)and use them in email scripts

Approve Button Image : ![image](https://github.com/user-attachments/assets/a7113ce8-7acf-4c78-af29-dde41a816332)

Reject Button Image: ![image](https://github.com/user-attachments/assets/9b01e1c8-b8f2-4a14-8274-a7d4d4fdbf73)


2)Go to Email Scripts > Click new
3)Add Scripts (Refer Email script file)
4)Call this in email in your Notification by using below syntax below
${mail_script:"name of the email script"}
5)Preview the email verify results

Output: ![image](https://github.com/user-attachments/assets/6c65a977-de11-4abd-918f-a4edeab4b2ce)

## Related Notes

- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Integration/Mail Scripts/Add Checklist/README|Add Checklist]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Integration/Mail Scripts/Add HTML Table for Requested Item Variables/README|Add HTML Table for Requested Item Variables]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Integration/Mail Scripts/Add Users in Watchlist to CC/README|Add Users in Watchlist to CC]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Integration/Mail Scripts/Add a link which opens ticket in Service Portal/README|Add a link which opens ticket in Service Portal]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Integration/Mail Scripts/Call Script Include in Notification Mail Script/README|Call Script Include in Notification Mail Script]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Integration/Mail Scripts/Call UI Message or System Property in Notification Mail Script/README|Call UI Message or System Property in Notification Mail Script]]
