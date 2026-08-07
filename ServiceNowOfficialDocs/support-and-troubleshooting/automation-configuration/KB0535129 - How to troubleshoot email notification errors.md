---
title: "How to troubleshoot email notification errors"
aliases:
  - KB0535129
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0535129
kb_number: KB0535129
last_modified: 2026-01-26
---

## How to troubleshoot email notification errors

  

### Issue

Troubleshoot common email notification errors and their solutions, including users not receiving notifications, missing recipients, and event creator settings.

### Email Notification Troubleshooting

<table border="1" width="100%"><colgroup><col style="width: 36.7427%;" width="75"><col style="width: 63.2248%;" width="25"></colgroup><tbody><tr><th>Error or Symptom</th><th>Solution</th></tr><tr><td><p>A specific user is not receiving email notifications.</p></td><td><p>The user's notification preferences may be disabled.</p><p>To verify notification preferences:</p><ol><li>Go to <strong>Self Service</strong> &gt; <strong>My Profile</strong>.</li><li>Verify that the <strong>Notification&nbsp;</strong>field is set to <strong>Enable</strong>.</li></ol><p>&nbsp;</p></td></tr><tr><td><p>Closing a new incident does not generate an Incident Opened notification.&nbsp;</p></td><td><p>This is expected behavior. The Incident Opened email notification has a condition of [active] [is] [true], so it only sends when the incident is active. When a user selects <strong>Close Incident</strong> to submit a new incident, the incident is inactive and the notification does not send.</p><p>To send notifications for closed incidents, create a custom email notification for this use case.</p></td></tr><tr><td><p>Notification fails with the error: "SMTPSender: no recipients, email send ignored"&nbsp;</p></td><td><p>This error occurs when an email notification generates but has no valid recipients based on its notification definition. For example, an email configured to send to the assigned_to user cannot send if the incident is unassigned.</p><p>Review the email notification configuration and verify it contains at least one valid recipient.</p></td></tr><tr><td><p>Some users receive email notifications but other users do not.</p></td><td><p>There are two possible reasons why users may not receive email notifications:</p><p><strong>User notifications are disabled</strong></p><p>The user record contains a notification setting that may be disabled.</p><p>To check the user's notification setting:</p><ol style="list-style-position: inside;"><li>Go to <strong>User Administration</strong> &gt; <strong>Users</strong>.</li><li>Open the record for the user who is not receiving email.</li><li>If the <strong>Notification&nbsp;</strong>field is set to Disable, change it to <strong>Enable</strong>.</li></ol><p><strong>Note</strong>: Do not modify the choice list values for the Notification field. Changing these values can cause all notifications to fail.</p><p><strong>User is the event creator</strong></p><p>By default, ServiceNow does not send email notifications to the person who triggered the email action. For example, if you assign an incident to yourself, the system does not notify you of the assignment.</p><p>To enable notifications for event creators:</p><ol><li>Go to <strong>System Policy</strong> &gt; <strong>Email&nbsp;</strong>&gt; <strong>Email Notifications</strong>.</li><li>Open the notification record.</li><li>Select the <strong>Send to event creator</strong> check box.</li><li>Add yourself to the list of notified users to verify notifications are working.</li></ol><p>&nbsp;</p></td></tr></tbody></table>

### Release

  All supported releases

### Resolution
