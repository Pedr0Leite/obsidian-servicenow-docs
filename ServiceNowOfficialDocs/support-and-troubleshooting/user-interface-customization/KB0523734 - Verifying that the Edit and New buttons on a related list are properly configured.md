---
title: "Verifying that the Edit and New buttons on a related list are properly configured"
aliases:
  - KB0523734
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0523734
kb_number: KB0523734
last_modified: 2025-06-16
---

## Verifying that the Edit and New buttons on a related list are properly configured

  

### Issue

ServiceNow enables users with the personalize\_list role (including administrators) to hide controls and define access conditions by role to existing controls. For example, administrators can personalize a list of related tasks embedded in an incident record to comply with business needs.

For additional information, see [List configuration](https://docs.servicenow.com/csh?version=latest&topicname=c_ListConfiguration.html "List configuration") in the ServiceNow product documentation.

### Procedure

The following example personalizes a related list so the **New** and **Edit** buttons appear, enabling users to create new records from a form.

To display the **New** or **Edit** buttons on a related list:

1.  Navigate to the form that contains the related list you want to update.
2.  Right-click the header bar of the related list and select **Configure > List Control**.  
    The Related List Control form appears.
3.  Locate the following fields:  
    -   **Omit new button**: Select the check box to prevent the **New** button from displaying on this list. Clear the check box if you want the **New** button to appear on this list, or if you want to control the **New** button with roles (**New roles** field).
    -   **Omit edit button**: Select the check box to prevent the **Edit** button from displaying on this list. Clear the check box if you want the **Edit** button to appear on this list, or if you want to control the **Edit** button with roles (New roles field). Note that the **Edit** button does not apply to all lists.
    -   If the **Omit new button** and **Omit edit button** options are cleared, the **New** **roles** and **Edit** **roles** fields appear on the List Control form.  
        -   **New roles**: Specify the user roles required to have the **New** button appear on this list. Click the padlock icons to open the role selection lists.
        -   **Edit roles**: Specify the user roles required to have the **Edit** button appear in the list. Click the padlock icons to open the role selection lists.  
            These fields determine if specific roles are able to view the **New** or **Edit** buttons or if the buttons are excluded completely from the form.  
              
            ![Related list configuration](sys_attachment.do?sys_id=29793a47477d6e503542f24c736d4399 "Related list configuration")
4.  Clear the **Omit new button** and **Omit edit button** checkboxes to make the **Edit** and **New** buttons available on a form for all users.
5.  Click **Update**.
6.  Return to the parent form.
7.  Verify the **New** and **Edit** buttons appear in the related list.

### Release

All Releases

### Resolution

Configure appropriate permissions for a user on an extended table:

### 1\. Verify the Table Structure

-   Go to System Definition > Tables.
-   Identify the parent table and locate the extended (child) table.
-   Confirm the relationship by checking the _Extends table_ field.

### 2\. Check Table-Level ACLs

-   Navigate to System Security > Access Controls (ACLs).
-   Filter by:
    -   Type: _record_
    -   Operation: _read, write, create_
    -   Name: enter the name of the extended table

>  If no ACLs exist for the child table, it won’t inherit access from the parent.

### 3\. Check Inheritance and Conditions

-   Review ACLs on the parent table. Confirm if conditions (roles, scripts) would pass for the current user.
-   Ensure no script condition blocks access based on user roles or field values.

### 4\. Use the Access Control Debug Tools

-   Use ACL Debug by navigating to:  
    `https://<instance>.service-now.com/sys_security_acl.do?Sysparm_query=`
-   Enable Debug Security Rules from the gear icon or by adding **&sysparm\_debug=true** to the URL.
-   View logs that show which rules passed or failed.

### 5\. Verify Field-Level ACLs

-   Repeat the same process to check for field-level ACLs on both parent and child tables.
-   Fields inherited from the parent may still have separate ACLs.
