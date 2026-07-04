---
title: "Missing \"New\" UI Button for the Software Contracts List in Software Asset Workspace's License Operations View"
aliases:
  - KB2472753
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB2472753
kb_number: KB2472753
last_modified: 2026-05-12
---

## Missing "New" UI Button for the Software Contracts List in Software Asset Workspace's License Operations View

  

### Issue

In Software Asset Workspace's License Operations view under Default Lists, the Software Contracts list is missing the New UI button for creating new contract records.

### Symptoms

-   The New button is visible on the Contract \[ast\_contract\] table in Classic UI.
-   The New button is still missing when creating a new list for the Contract \[ast\_contract\] table under 'My Lists' in License Operations view.
-   No ACLs are found to be blocking the New button.
-   Contract Workspace is installed on the instance.

### Release

All Releases

### Cause

• Software Asset Workspace uses the Global table declarative Action Assignment New from the UX List Configurations plugin for the New button on the Software Contracts list.

[/sys\_declarative\_action\_assignment\_list.do?sysparm\_query=sys\_id%3D17c13e7273131010a0a79329faf6a794](https://empdgoodman0.service-now.com/sys_declarative_action_assignment_list.do?sysparm_query=sys_id%3D17c13e7273131010a0a79329faf6a794&sysparm_view=)

• The Software Contracts list is just a display name in the Workspace for the Contracts \[ast\_contract\] table.

• When the Contract Workspace plugin is installed an Action Assignment for New on the Contract \[ast\_contract\] table is created.

• This New Action Assignment is meant to hide the New button on Contract \[ast\_contract\] lists in the Contract Workspace.

• However the Experience Restricted field is not set to true to contain it's use within Contract Workspace.

• Because Experience Restricted is false, it's also being unintentionally used by Software Asset Workspace and 'hiding' the New button.

### Resolution

1\. Change your current scope to **Contract Workspace application scope**.

2\. Go to the **Action Assignments** \[sys\_declarative\_action\_assignment\] table.

3\. **Query** for the record WHERE Action Label IS New, Table IS Contract \[ast\_contract\], Action Model IS List, and Package IS Contract Workspace.

/sys\_declarative\_action\_assignment.do?sys\_id=2c56f6bf77040210f9a4ef860d5a992e

4\. **Open** the record.

5\. Find the **Experience Restricted** field and set it to **true** by checking the box.

6\. **Save** the record.

Go back to Software Asset Workspace > License Operations > Default Lists > **Software Contracts** and confirm the **New** button is no longer hidden.
