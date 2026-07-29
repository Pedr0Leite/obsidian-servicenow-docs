---
title: "Outlook Actionable Message 401 error on endpoint"
aliases:
  - KB0815869
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0815869
kb_number: KB0815869
last_modified: 2024-11-23
---

## Issue

Outlook Actionable Message 401 Error message at endpoint, while completing the survey/approval in the received email.

**Steps to Reproduce:**

-   Navigate to **System Notification** > **Email** > **Notifications**.
-   For the Survey User Invite notification, in the **What it will contain** tab, add the following script in the **Message** field in addition to the existing information:
    -   ${mail\_script:include\_survey\_actionable}
    -   This script includes the Outlook actionable message in the email notification sent to the user.
-   Navigate to **Survey** > **View Surveys**, and open a survey.
-   To send an email notification to the survey user, select the **Send notifications** check box in a survey.
-   Select the **Outlook Actionable Message** check box and save the survey

**Steps to trigger the survey user invite notification:**

1.  Navigate to the Customer Satisfaction Survey (example here) in asmt\_metric\_type table.
2.  Click on assign survey button and assign it to the user and click OK.
3.  Instance created successfully message will pop up.
4.  This will trigger the survey invite notification.
5.  An email notification with the embedded survey is sent to the user. The user can take the survey and submit it from the email client instead of opening the survey in a new browser tab.
6.  After completing the survey if the user clicks on the submit button, he will get an error "The remote Endpoint returned an error (HTTP 401). Please try again later.

## Resolution

Enter your instance name (https://<instance\_name>.service-now.com) in the client id of the outlook actionable message entry in  "oauth\_oidc\_entity" table. This will resolve the issue.

## Additional Information

Outlook Actionable Messages enables rich interactive emails for approvals and surveys in Microsoft Outlook. With Actionable Messages, it’s easier and faster to approve or complete a survey when you can take action right from the email message.
