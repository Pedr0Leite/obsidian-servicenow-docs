---
title: "The New or Edit button does not appear on a one-to-many related list "
aliases:
  - KB0522170
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0522170
kb_number: KB0522170
last_modified: 2025-06-02
---

## The New or Edit button does not appear on a one-to-many related list

  

### Issue

The New or Edit button does not appear on a related list for certain users or under specific conditions.

### Symptoms

-   The **New** button does not display on a related list
-   The **Edit** button does not display on a related list
-   A specific user or users in certain groups cannot see the Edit or New button on a related list

### Facts

-   One or more of the following may be preventing the buttons from appearing:
    -   List Control settings are configured to hide the New or Edit button.
    -   The user lacks create or write access to the child table or its reference field.
    -   The reference field on the child table is not configured as Reference Float.
    -   The first record in the related list fails ACL checks, hiding the button entirely.
    -   A UI Action condition is preventing the button from displaying.

### Release

All Releases

### Cause

-   List Control settings are restricting visibility to the Edit button
-   Users do not have create or write access to either the child table or the field in the child table that references the parent table
-   The field on the child table that references the parent table is not configured as Reference Floats
-   The first record in the related list does not have create or write access to the child table or the field in the child table that references the parent table
-   The UI Action is restricting visibility to the button

### Resolution

The New button is available on some related lists, enabling the user to create a new entry in the related list.

1.  Select New to open the Related List form.
2.  After filling in the form, click Submit to add the new entry directly to the related list and to the table the related list calls.

The Edit button on related lists is available when the relationship is either a one-to-many or many-to-many. The Edit button allows users to easily relate multiple records. The Edit button is NOT available on a scripted related list - sometimes called a "defined" or "custom" related list. Defined related lists can be accessed through the "Relationships" module.

The first step in troubleshooting any related list is to identify the type of related list. For more information, see [Determining a related list type](https://support.servicenow.com/kb_view.do?sysparm_article=KB0523665 "Determining a related list type").

To troubleshoot a one-to-many related list:

1\. Understand Related List Types

-   Determine if the related list is one-to-many, many-to-many, or a scripted/defined list.
-   The Edit button is only available on one-to-many and many-to-many relationships.
-   Defined (scripted) related lists do not support the Edit button.
-   See: [Determining a Related List Type](/kb_view.do?sysparm_article=KB0523665 "Determining a Related List Type")

2\. Check List Control Settings

-   Navigate to the form > Configure > Related Lists.
-   Open List Control and verify:
-   Show New Button is enabled.
-   Show Edit Button is enabled.
-   See: [Configuring List Controls](/kb_view.do?sysparm_article=KB0523734 "Verifying the Edit and New buttons on a related list are properly configured.")

3\. Verify User Permissions

-   Confirm the user has Create or Write ACLs on:
-   The child table.
-   The reference field that links to the parent table.
-   See: [Checking ACLs for Related Lists](/kb_view.do?sysparm_article=KB0523743 "Determining if a user has permissions to create, read, and write to an extended table")

4\. Enable Reference Float (for One-to-Many Lists)

-   Edit the dictionary entry for the reference field on the child table.
-   Enable the Reference Float option.
-   This allows the Edit button to appear in one-to-many relationships.
-   See: [Reference Float Functionality](/kb_view.do?sysparm_article=KB0523768 "Enabling the Reference float functionality on an extended table")

5\. Check the First Record’s ACLs

-   The system checks ACLs for the first record in the related list.
-   If that record fails the ACL check, the New and Edit buttons may be hidden—even if others pass.
-   [Sort or filter the related list](/kb_view.do?sysparm_article=KB0523778 "Verifying the order in the relate list does not prevent the Edit or New button from appearing") to test with a different first record.

6\. Review UI Action Conditions

-   Review any custom UI Action conditions for the New or Edit buttons.
-   Ensure the conditions do not inadvertently restrict visibility based on user roles or context.

### Related Links

[UI action controls](https://www.servicenow.com/docs/csh?topicname=c_UIActions.html&version=latest "UI action controls")
