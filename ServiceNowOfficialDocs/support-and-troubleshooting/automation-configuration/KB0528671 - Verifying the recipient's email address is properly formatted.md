---
title: "Verifying the recipient's email address is properly formatted"
aliases:
  - KB0528671
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0528671
kb_number: KB0528671
last_modified: 2025-12-03
---

## Verifying the recipient's email address is properly formatted

  

### Issue

ServiceNow cannot send email if the email address is not properly formatted and valid. If a particular user or group does not receive an email notification, verify the user or group has a properly formatted and valid email address.

Email addresses generally follow this format:

[localname@domain](mailto:localname@domain)

The definition of a properly formatted email address is described in detail in [section 3.4 of RFC 2822](https://tools.ietf.org/html/rfc2822#section-3.4 "section 3.4 of RFC 2822").  The format is surprisingly complicated in what it allows, with various exceptional cases, making a succinct description difficult.

Simply having a properly formatted address is not enough.  The receiving mail server must recognize the email account. If your email address is properly formatted, but perhaps incorrectly spelled, the receiving mail server will reject the email address as not valid because it cannot find the email account.

Improperly formatted email address examples:

-   **john.smith**  - The 'domain' part is technically optional according to specification, so this is properly formatted.  However, ServiceNow email servers enforce email addresses with a full domain, in order to eliminate any ambiguity in the recipient.
-   **@example**  - missing the local part
-   **@ex amp le**  - unacceptable spaces

Properly formatted email address examples:

-   **[john.smith@example.com](mailto:john.smith@example.com)**
-   **[johnZZZ.smith@example.com](mailto:johnZZZ.smith@example.com)** \- This is properly formatted, but if the 'ZZZ' were typed in error, the receiving mail server will reject it as invalid because it cannot find this account.

### Release

All releases

### Resolution

#### **Email Investigation**

Check the **error\_string** field of the email record as well as the Email Log-related list.

1.  Open the email record you expected the recipient to receive
2.  Check the **error\_string** field. If a server rejected an email address as invalid, the error may appear here.  The text is server-dependent.
3.  In Eureka and later information is logged that may indicate why a particular user was included or excluded in an email notification.  Check the logs for the reason a recipient was excluded. An improperly formatted address is one reason a recipient might be excluded.   View the **'Email Log'** related list and look for the user in question.

#### **Notification Investigation**

The notification defines who receives an email in the "Who To Send" tab in the notification

1.  Log in to the instance.
2.  Navigate to **System Policy > Notifications**.
3.  Select the notification you expected the recipient to receive. For example, the incident commented notification.
4.  Identify the users and groups who would normally receive the notification. For example, the incident comment notification notifies the incident caller.
5.  Determine which specific users or groups did not potentially trigger the notification. For example, determine the user who is the incident caller.
6.  Navigate to **User Administration > Users**.
7.  Select the user record for the intended recipient.
8.  Verify the address in the **Email** field is properly formatted.
9.  If you change the user record, click **Update**.

### Related Links

Official RFC: [section 3.4 of RFC 2822](https://tools.ietf.org/html/rfc2822#section-3.4 "section 3.4 of RFC 2822")

Wikipedia article - [Email address](https://en.wikipedia.org/wiki/Email_address#Examples "Email address")
