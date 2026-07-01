---
title: Privileged Users
description: View the trend line for the privileged users \(active and inactive\) and their activity on the ServiceNow AI Platform.
locale: en-US
canonical_url: https://www.servicenow.com/docs/r/platform-security/security-center/privileged-users.html
release: australia
product: Security Center
classification: security-center
topic_type: concept
last_updated: "2026-03-12"
reading_time_minutes: 1
breadcrumb: [Security metrics, Security monitoring console, Security Center, Platform Security]
tags:
  - platform-security
  - security-center
  - posture
  - compliance
  - risks
  - type-concept
---

# Privileged Users

View the trend line for the privileged users \(active and inactive\) and their activity on the ServiceNow AI Platform.

The Privileged users overview section displays the trend line for the privileged users \(active and inactive\) and their activity on the ServiceNow AI Platform. Privileged users are [[users|users]] who have been assigned additional roles by admins to access the features like [[c_HighSecuritySettings|High Security Settings]], Import, and Portal users.

Below is an explanation of the privileged users:

-   Total users: Total count of users on your instance.
-   Active users: Total number of users who initiated sessions on your instance.
-   Inactive users: Users who have not recently logged into your instance.
-   Inactive users who are not locked out: Users who have not recently logged in but still have access to their account.
-   Locked out users: Users who are not permitted to authenticate into their account.
-   New users: Users who have recently been added to your instance.
-   Successful logins: Users that have successfully logged in.
-   Failed logins: Unsuccessful login attempts.
-   Local logins not protected by MFA: Users that logged in without MFA.
-   Users never logged in: Users that have never logged into your instance.
-   Users not logged in since last month: Users that have not logged in the last 30 days.
-   Users not logged in since the last 6 months: Users that have not logged in the last 6 months.
-   Users not logged in since the last 1 year: Users that have not logged in the past year.
-   Need to reset password: Users that need to reset their password.
-   [[c_SelfServicePasswordReset|Password reset]] failures of the users: Number of password failures per user.

Select the cards to view the individual [[ca-metrics|metrics]] page with additional details.

Select the **+Create task** button to create a Security Task related to a metric. For details on [[security-task-manager|Security Tasks]], see [Security Tasks](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/platform-security/security-center/security-task-manager.md).

**Parent Topic:**[Security metrics](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/platform-security/security-center/sc-metrics.md)

## Related

- [[users|Users]]
- [[c_HighSecuritySettings|High Security Settings]]
- [[c_SelfServicePasswordReset|Password Reset]]
- [[ca-metrics|Metrics]]
- [[security-task-manager|Security Tasks]]
