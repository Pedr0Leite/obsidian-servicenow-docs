---
title: "How to manage Now Support users for Regulated Markets"
aliases:
  - KB0547279
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0547279
kb_number: KB0547279
last_modified: 2026-04-10
---

## Issue

This article describes how to manage Now Support users for Regulated Market customers. Use these procedures to:

-   View the list of users you manage
-   Create new users
-   Grant or revoke user roles
-   Edit user information

**Note:** This article is for Regulated Market customers only. For commercial customers, see [Creating and managing Now Support users, granting and removing access, editing user roles](https://support.servicenow.com/kb?id=kb_article_view&sys_kb_id=04466d8347697250c2488d01426d43a7).

### Before you begin

For access to Now Support, a user must have the customer role. As a customer administrator, you can grant and revoke the customer and customer\_admin roles to other users.

For a list of available roles with descriptions, see [Base System Roles](https://docs.servicenow.com/csh?topicname=r_BaseSystemRoles.html&version=latest "Base System Roles") in the product documentation.

### View Now Support users

To view the list of users associated with your organization:

1.  Go to [Now Support](https://support.servicenow.com/now "Now Support").
2.  Select **Manage Accounts > Users List**
3.  \[Optional\] Create a filter to find a specified user.

### Creating a user

Before creating a new user, filter the **Active** column in the user list for inactive users. If the user already exists as inactive, change their status to Active instead of creating a duplicate record. 

1.  Go to [Now Support.](https://support.servicenow.com/now "Now Support")
2.  Select **Manage Accounts > Users List.**
3.  Select **Add New User.**
4.  Complete the fields as appropriate. See the field descriptions in the following table. 
5.  Select **Submit**. The system sends an email with a password to the user. The user must reset the password at first sign in. 
6.  Select **Edit Roles**.
7.  Add and remove roles as necessary.
8.  Select **Submit**.

<table class="internalTable" style="width: 102.693%; height: 470.4px; border-collapse: collapse; border-width: 1px; border-style: solid;" border="1"><tbody><tr class="sphr" style="height: 22.4px;"><td style="height: 22.4px; width: 26.5992%; border-width: 1px; padding: 3px;"><strong>Field</strong></td><td style="width: 12.9752%; border-width: 1px; padding: 3px;"><strong>Required</strong></td><td style="height: 22.4px; width: 60.3348%; border-width: 1px; padding: 3px;"><strong>Description</strong></td></tr><tr class="sp" style="height: 44.8px;"><td style="height: 44.8px; width: 26.5992%; border-width: 1px; padding: 3px;"><p>Company</p></td><td style="width: 12.9752%; border-width: 1px; padding: 3px;"><p>No</p></td><td style="height: 44.8px; width: 60.3348%; border-width: 1px; padding: 3px;"><p>Company or organization to which the user is associated</p></td></tr><tr class="sp" style="height: 44.8px;"><td style="height: 44.8px; width: 26.5992%; border-width: 1px; padding: 3px;"><p>First Name&nbsp;</p></td><td style="width: 12.9752%; border-width: 1px; padding: 3px;"><p>Yes</p></td><td style="height: 44.8px; width: 60.3348%; border-width: 1px; padding: 3px;"><p>User first name</p></td></tr><tr class="sp" style="height: 44.8px;"><td style="height: 44.8px; width: 26.5992%; border-width: 1px; padding: 3px;"><p>Last Name&nbsp;</p></td><td style="width: 12.9752%; border-width: 1px; padding: 3px;"><p>Yes</p></td><td style="height: 44.8px; width: 60.3348%; border-width: 1px; padding: 3px;"><p>User last name</p></td></tr><tr class="sp" style="height: 22.4px;"><td style="height: 22.4px; width: 26.5992%; border-width: 1px; padding: 3px;"><p>Title</p></td><td style="width: 12.9752%; border-width: 1px; padding: 3px;"><p>No</p></td><td style="height: 22.4px; width: 60.3348%; border-width: 1px; padding: 3px;"><p>User title</p></td></tr><tr class="sp" style="height: 22.4px;"><td style="height: 22.4px; width: 26.5992%; border-width: 1px; padding: 3px;"><p>Email</p></td><td style="width: 12.9752%; border-width: 1px; padding: 3px;"><p>Yes</p></td><td style="height: 22.4px; width: 60.3348%; border-width: 1px; padding: 3px;"><p>User email address</p></td></tr><tr class="sp" style="height: 44.8px;"><td style="height: 44.8px; width: 26.5992%; border-width: 1px; padding: 3px;"><p>Business Phone</p></td><td style="width: 12.9752%; border-width: 1px; padding: 3px;"><p>Yes</p></td><td style="height: 44.8px; width: 60.3348%; border-width: 1px; padding: 3px;"><p>User business phone number</p></td></tr><tr class="sp" style="height: 22.4px;"><td style="height: 22.4px; width: 26.5992%; border-width: 1px; padding: 3px;"><p>Mobile phone</p></td><td style="width: 12.9752%; border-width: 1px; padding: 3px;"><p>No</p></td><td style="height: 22.4px; width: 60.3348%; border-width: 1px; padding: 3px;"><p>User mobile phone number</p></td></tr><tr class="sp" style="height: 22.4px;"><td style="height: 22.4px; width: 26.5992%; border-width: 1px; padding: 3px;"><p>Country</p></td><td style="width: 12.9752%; border-width: 1px; padding: 3px;"><p>Yes</p></td><td style="height: 22.4px; width: 60.3348%; border-width: 1px; padding: 3px;"><p>Country in which the user resides</p></td></tr><tr class="sp" style="height: 22.4px;"><td style="height: 22.4px; width: 26.5992%; border-width: 1px; padding: 3px;"><p>City</p></td><td style="width: 12.9752%; border-width: 1px; padding: 3px;"><p>No</p></td><td style="height: 22.4px; width: 60.3348%; border-width: 1px; padding: 3px;"><p>City in which the user resides</p></td></tr><tr class="sp" style="height: 22.4px;"><td style="height: 22.4px; width: 26.5992%; border-width: 1px; padding: 3px;"><p>State</p></td><td style="width: 12.9752%; border-width: 1px; padding: 3px;"><p>No</p></td><td style="height: 22.4px; width: 60.3348%; border-width: 1px; padding: 3px;"><p>State in which the user resides</p></td></tr><tr class="sp" style="height: 134.4px;"><td style="height: 134.4px; width: 26.5992%; border-width: 1px; padding: 3px;"><p>Time zone&nbsp;</p></td><td style="width: 12.9752%; border-width: 1px; padding: 3px;"><p>Yes</p></td><td style="height: 134.4px; width: 60.3348%; border-width: 1px; padding: 3px;"><p>Time zone in which the user resides.</p><p>When you file a case with ServiceNow, the time zone on the user record is the default time used. You can specify a different time zone for individual incidents. For more information, see&nbsp;<a title="Technical Support" href="/kb_view.do?sysparm_article=KB0547260" target="_blank" rel="noopener noreferrer">Technical Support</a>.</p></td></tr></tbody></table>

### Grant or revoke access

To update a user's roles:

1.  Go to [Now Support.](https://support.servicenow.com/now "Now Support")
2.  Select **Manage Accounts > Users List.**
3.  In the Action menu for the user, select update **Update role(s).**  
      
    ![Manage accounts to Grant and revoke access](/sys_attachment.do?sys_id=d4efa0ef870cc71057288519dabb3571)  
      
    
4.  In the popup, add or remove roles as needed, and then select **Submit**.   
      
    ![Updating roles on now support](/sys_attachment.do?sys_id=5cefa0ef870cc71057288519dabb3576)

**Alternative method:** You can also open the user's profile and select **Update or add responsibility** to access the same popup.

![Open the user's profile and select Update or add responsibility to access the same popup](/sys_attachment.do?sys_id=18ef64ef870cc71057288519dabb35b0)

### Update user information

To edit an existing user:

1.  Go to [Now Support](https://support.servicenow.com/now "Now Support").
2.  Select **Manage Accounts > Users List**
3.  Select the user's name.
4.  Edit the fields as appropriate.  For field descriptions, see the table in the **Create a user** section. 
5.  Select **Save**.

**Note:** The **ID** field is set automatically from the user email address to create a unique key for each user. Only a Now Support admin can edit a User ID number. You cannot create a user account with an email address that is already in use. 

**Missing field notifications**

When the **Business phone**, **Mobile phone**, **Email**, or **Time zone** field is empty on a user profile, a notification appears on the profile page and the empty fields are highlighted. After you add the missing information and select **Submit**, the notification and highlighting no longer appear.   

## Resolution

For all Commercial Customers:

[Introducing Now Support User Management](https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB1279988)

[Creating and managing Now Support users, granting and removing access, editing user roles](https://support.servicenow.com/kb_view.do?sysparm_article=KB1284666 "Creating and managing Now Support users, granting and removing access, editing user roles")
