---
title: "How to review and remediate script sandboxing configuration in ServiceNow"
aliases:
  - KB0550837
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0550837
kb_number: KB0550837
last_modified: 2026-06-23
---

## Issue

Learn how to review and remediate script sandboxing configuration on ServiceNow instances. This article explains what script sandboxing is, why it is required, and how to identify scripts that may be affected when the glide.script.use.sandbox property is enabled.

This article is intended for system administrators, consultants, and partners with experience in ServiceNow system security.

## What is script sandboxing?

Script sandboxing is a security mechanism that evaluates JavaScript submitted by end users — through a UI page or a request URL — in a restricted environment. In this environment, only a limited subset of ServiceNow scripting APIs is available, and certain JavaScript features are not available at all, including:

-   Function declarations
-   The eval function
-   Looping constructs such as for and while

There are two common scenarios where a client submits JavaScript to the server for evaluation:

-   **Filters and queries:** A filter can send JavaScript to the server — for example: assigned\_to=javascript:getMyGroups()
-   **System API (AJAXEvaluate):** This API allows the client to run arbitrary scripts on the server and receive a response.

Both scenarios are potential security risks because a malicious user could alter the JavaScript before it is submitted. Script sandboxing reduces this risk by evaluating all client-submitted JavaScript in a restricted environment before the query runs.

**Note:** Script sandboxing applies only to client-submitted JavaScript — not to script artifacts such as script includes marked as client-callable. All client-submitted JavaScript is prefixed with "javascript:" followed by a JavaScript expression.

## Resolution

## How script sandboxing is implemented

Script sandboxing uses the Rhino server-side JavaScript engine and is controlled by the system property glide.script.use.sandbox. Set this property to true to enable script sandboxing.

**Note:** For instances on a release prior to Geneva, setting the property to true is permanent — the value cannot be changed by an upgrade. For instances on Geneva or later, the property value cannot be modified once it is set to true.

When glide.script.use.sandbox is set to true, the following restrictions apply to all client-side JavaScript queries:

-   Only business rules marked as Client callable are available in the sandbox and can be called by client scripts.
-   Only script includes marked as Client callable are available in the sandbox and can be called by client scripts.
-   In AJAX and filter calls, data cannot be modified from within the sandbox. Calls such as current.update() are ignored.
-   Certain back-end API calls that provide direct database access are not permitted in the sandbox.
-   The eval function is not permitted.
-   Package calls are not permitted.
-   Looping constructs (for, while, and similar) are not permitted.
-   Only a subset of GlideSystem (gs.function) API calls is available.
-   Only a small subset of GlideScriptable API calls is available.
-   Sandbox versions of scriptable objects such as GlideRecord are used. These may refuse certain operations with a SecurityException or silently do nothing.
-   Function declarations are not permitted.

## Reviewing and testing script functionality

Follow the steps in this section only if your instance has conflicting items as described in the previous section. Base system business rules and script includes are not affected by this property change — only custom business rules and script includes need to be reviewed.

Set items to **Client callable** only when there is a legitimate business reason for doing so and when no sensitive information is exposed as a result. Test all changes on a non-production instance before applying them to production.

Below are critical components to query and test before applying the final remediation:

### Identify client scripts accessing business rules or script includes

1.  Log in as a user with the admin role.
2.  Go to **System Definition > Client Scripts**.
3.  Select the **Show/Hide filter** icon to add a filter condition.
4.  Add filter conditions to identify client scripts that reference business rules or script includes.
5.  Select **Run**.
6.  Review the results. For any client scripts that call business rules or script includes, verify that those business rules or script includes are set to **Client callable**.

![Filter of Client Scripts table list](/sys_attachment.do?sys_id=e203b6d34725c750f93138ce536d43dd "Filter of Client Scripts table list")

### Identify non-client callable business rules

1.  Log in as a user with the admin role.
2.  Go to S**ystem Definition > Business Rules**.
3.  Select the **Show/Hide filter** icon and filter by **\[Client callable\] \[is\] \[false\]**.
4.  Select **Run**.
5.  Review the results. These business rules are not available within the sandbox and cannot be called by client scripts.

![Client callable business rule record](/Screen%20Shot%202015-07-29%20at%2011.00.36%20AM.JPGx "Client callable business rule record")

### Make a business rule client callable

If a business rule in the results list must be called by a client script, open the business rule record and select the Client callable checkbox.

**Note:** The option to mark a business rule as client callable may not be available in newer platform versions. If this option is not available, create a client-callable script include to achieve the same functionality.

1.  Click the desired record in the result set:  
      
    ![Business rules record](/sys_attachment.do?sys_id=3203f6d34725c750f93138ce536d431f "Business rules record")  
      
    
2.  In the record form, enable the **Client callable** checkbox:  
      
    ![Client callable checkbox](/sys_attachment.do?sys_id=3603f6d34725c750f93138ce536d4318 "Client callable checkbox")

### Identify non-client callable script includes

1.  Log in as a user with the admin role.
2.  Go to **System Definition > Script Includes**.
3.  Select the **Show/Hide filter** icon and filter by **\[Client callable\] \[is\] \[false\]**.
4.  Select **Run**.
5.  Review the results. These script includes are not available within the sandbox and cannot be called by client scripts.

![Client callable value](/Screen%20Shot%202015-07-29%20at%2011.08.14%20AM.JPGx "Client callable value")

### Make a script include client callable

If a script include in the results list must be called by a client script, open the script include record and select the **Client Callable** checkbox.

1.  From the result set, click the desired record:  
    ![Screenshot of Script Includes record](https://support.servicenow.com/sys_attachment.do?sys_id=3e03f6d34725c750f93138ce536d432b "Screenshot of Script Includes record")

2.  In the record's form view, select the **Client Callable** checkbox.  
    ![Checkbox of Client callable](/sys_attachment.do?sys_id=fe03f6d34725c750f93138ce536d4325 "Checkbox of Client callable")

### Identify scripted filters, processors, and modules

JavaScript filters and queries can also reside in the following locations. Review each area for client-side JavaScript calls.

#### Filters

1.  Log in as a user with the admin role.
2.  Go to **System Definition > Filters**.
3.  Select the **Show/Hide filter** icon to add a filter condition to find records containing client-side JavaScript calls.
4.  Select **Run**.
5.  Review the results — for example, the "Assigned to me" filter uses the value javascript:gs.user\_id().

![Filters table filter of list](/Screen%20Shot%202015-07-29%20at%2011.49.17%20AM.JPGx "Filters table filter of list")

#### Processors

1.  1.  Log in as a user with the admin role.
    2.  Go to **System Definition > Processors**.
    3.  Select the **Show/Hide filter** icon to add a filter condition.
    4.  Select **Run**.
    5.  Review the results for client-side JavaScript calls.

![Processors table filter](/Screen%20Shot%202015-07-29%20at%2012.04.26%20PM.JPGx "Processors table filter")

#### Modules

1.  Log in as a user with the admin role.
2.  Go to **System Definition > Modules**.
3.  Select the **Show/Hide filter** icon to add a filter condition.
4.  Select **Run**.
5.  Review the results for client-side JavaScript calls.

![Modules table filtering keywords](/Screen%20Shot%202015-07-30%20at%203.15.51%20PM.JPGx "Modules table filtering keywords")

After reviewing all three areas, verify that records that have been modified are tested on a non-production instance with glide.script.use.sandbox set to true before applying changes to production.

### Testing JavaScript calls in other areas

Given the variety of JavaScript call entry points in ServiceNow, test all relevant areas on a non-production instance with glide.script.use.sandbox set to **true** before making any changes to production.

Before testing, clone production data and configuration to the non-production instance to verify functionality against a representative data set.

## Additional Information

[Add a system property](https://docs.servicenow.com/csh?topicname=t_AddAPropertyUsingSysPropsList.html&version=latest "Add a system property")

[The script sandbox property](https://docs.servicenow.com/csh?topicname=r_ScriptSandboxing.html&version=latest "The script sandbox property")

[Scripts](https://docs.servicenow.com/csh?topicname=c_Script.html&version=latest "Scripts")

[Business rules](https://docs.servicenow.com/csh?topicname=c_BusinessRules.html&version=latest "Business rules")

[Script includes](https://docs.servicenow.com/csh?topicname=c_ScriptIncludes.html&version=latest "Script includes")

[Filters and breadcrumbs](https://docs.servicenow.com/csh?topicname=c_UsingFiltersAndBreadcrumbs.html&version=latest "Filters and breadcrumbs")

[Get a user object](https://docs.servicenow.com/csh?topicname=t_GetAUserObject.html&version=latest "Get a user object")
