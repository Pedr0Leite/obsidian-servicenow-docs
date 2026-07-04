---
title: "Resolve local login failures when the Okta plugin is active"
aliases:
  - KB0596969
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0596969
kb_number: KB0596969
last_modified: 2026-05-12
---

## Resolve local login failures when the Okta plugin is active

  

### Issue

Resolve an issue where users cannot log in to a ServiceNow instance using the local login prompt when the Okta plugin is active. Users receive a "Login Failed" error when attempting local authentication, even though their credentials are valid.

This issue occurs when all of the following conditions are true:

-   The Okta plugin is installed and active on the instance.
-   Okta is configured to provision users and synchronize their passwords in ServiceNow.
-   User records are synchronized with their Active Directory passwords.
-   Users are authenticating through the local instance login prompt rather than through Okta.

### Symptoms

-   Users can log in successfully through Okta — either directly from the Okta tenant or using the Okta login link on the instance login page.
-   If users attempt to set the Okta External Login to inactive and then reactivate it, they receive the error: "Okta authentication configuration failed. Invalid token provided."

### Release

All supported releases

### Cause

The Okta API token expires 30 days after creation if it is not used. Okta renews the token automatically each time the application uses it, but if the token expires before it is renewed, ServiceNow loses the ability to validate the Okta connection. This causes local login to fail and prevents the Okta External Login configuration from being reactivated.

Resetting the token forces the instance to revalidate the connection and resolves the issue.

### Resolution

Create a new Okta API token and update the token in ServiceNow to restore the connection.

#### Part 1: Create a new API token in Okta

1.  Log in to your Okta tenant as an Okta admin user.
2.  If you are on the Applications home page, select the **Admin** link in the upper right corner of the page.
3.  In the main navigation bar, go to **Security > API**.
4.  Select **Create Token**.
5.  Enter a name for the token and select **Create Token**.
6.  Copy the token value and save it — this value is only shown once.

#### Part 2: Update the token in ServiceNow

7.  Log in to your ServiceNow instance as an admin user.
8.  Go to **User Administration > SSO** provided by Okta, Inc.
9.  Paste the copied token into the **Okta API token** field.
10.  Select **Yes** for **Enable Okta external authentication**.
11.  Select **Save**.
12.  Verify that the following confirmation message appears: "Okta authentication configured successfully."

After completing these steps, ask users to test local login to confirm the issue is resolved.

### Related Links

-   [PRB704082](/now?id=form&sys_id=c3c03c4fdb01a6087fc27c541f9619c5&table=problem&view= "PRB704082") related problem record
