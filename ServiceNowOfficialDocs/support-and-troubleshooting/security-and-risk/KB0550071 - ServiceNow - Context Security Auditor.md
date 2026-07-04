---
title: "ServiceNow - Context Security Auditor"
aliases:
  - KB0550071
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0550071
kb_number: KB0550071
last_modified: 2025-01-03
---

## Issue

ServiceNow instance access control review  
  

# Overview

* * *

This article is a focused, actionable guide for auditing the access control rules for any and all users or roles in the ServiceNow platform and associated applications. This tool can be used in many ways. The potential uses include:

-   If a customer administrator wants to remediate the access control list (ACL) vulnerabilities based on the findings identified in penetration testing
-   If a development partner wants to understand access control posture on the application
-   Any project whereby you may want to get a big picture review (for example, audit) detailing what users have access to what tables  
      
      
    

# What is authentication / authorization / access control?

* * *

-   Authentication is the process for requesting access to the system.
-   Authorization defines what a user can access following authentication. Authorization is the process where requests to access a particular resource should be granted or denied.
-   Access control is the method or mechanism of authorization to enforce that requests to a system resource or functionality should be granted before the transaction is complete.  
      
      
    

# Role-based access control (RBAC)

* * *

ServiceNow enforces an access model whereby all user input and user transactions are to be validated and granted with explicit access to a resource, functionality, or workflow based on the user’s access role. A user’s role is defined in the users and groups setting, and evaluated by the application’s RBAC controls.

In role-based access control (RBAC), access decisions are based on the application user's roles and responsibilities within the boundaries of a specific application. The process of defining roles is based on analyzing the fundamental duties of a specific base system role and is linked to the ServiceNow Security policy.  
  
  

# How to validate the access controls on my application

* * *

ServiceNow provides administrators interactive access-control functionality in the application through the Contextual Security Auditor plugin. This plugin helps administrators understand and evaluate the access control settings configured in the ServiceNow application. As described in the product documentation [article](https://docs.servicenow.com/csh?topicname=c_SNCAccessControl.html&version=latest "article"), this plugin is not available by default and must be requested by the customer.  
  
  

# Procedure

* * *

Follow the steps below to configure, customize, and run the Contextual Security Auditor application once the plugin is installed on the instance:

1\. Log in to the instance using an **Administrator** role.

2\. In the navigation filter, enter **Audit.**

3\. Click **Audit Sets.**

4\. On the right-hand pane, click **New** to create a new audit set. 

![](/Audit_set.JPGx)

The record you create acts as a framework that contains the **Roles** versus **Targets/Assets** that are being audited for.

5\. Ensure that **field level security** checkbox is ticketed so that the audit can be performed against a particular system table, or the audit will be performed against all the application tables.

![](/field_security.JPGx)  
  

<table class="noteTable" align="left"><tbody><tr><td style="width: 50; vertical-align: middle; text-align: center;"><span style="font-family: arial,helvetica,sans-serif;"><img style="align: baseline;" title="Note" src="/Note_25x.pngx" alt="" align="bottom" border="" hspace="" vspace=""></span></td><td><strong>Note:</strong> ServiceNow recommends not to run the audit against all the tables at once due to memory exhaustion that might occur as a result.</td></tr></tbody></table>

  
  

6\. Pick the target table that needs to be audited against.

7\. Add the users/roles in the slushbucket on the right-hand side of the pane that need to be audited for.

8\. Click the **Check ESS** checkbox if non-users have to be audited for.

![](/Screen%20Shot%202015-06-18%20at%2011.24.38%20AM.JPGx)

9\. Submit the record.

10\. Click **Execute now** in the desired record.

11\. Once the operation is complete, the sections **Security Audit Lines** populate themselves to show the results of the audit operation.

![](/result_all.JPGx)

12\. As shown above in the result set, the 'C'R'W'D' operations are categorized per user role with the respective table/field to provide a comprehensive access control analysis on the system table(s).

<table class="noteTable" align="left"><tbody><tr><td style="width: 50; vertical-align: middle; text-align: center;"><span style="font-size: 12pt; font-family: arial,helvetica,sans-serif;"><img style="align: baseline;" title="Note" src="/Note_25x.pngx" alt="" align="bottom" border="" hspace="" vspace=""></span></td><td><strong>Note:</strong> A "Maybe" status in the result set indicates that a complicated access controls setup has been defined by either a business rule or script include.</td></tr></tbody></table>

# Auditing for system user role changes

* * *

Access control monitoring should be another important point to consider for any platform-based automation systems. ServiceNow provides a module to track for **Role** changes for any system table(s) on the application. The **Role Audit** module is available [here](https://docs.servicenow.com/csh?topicname=c_DelegateRoles.html&version=latest "here"). By default, the Role Audit table is not populated. As a prerequisite, enable auditing on the target table(s) as mentioned in the product documentation [article](https://docs.servicenow.com/csh?topicname=audited-tables-2.html&version=latest "article") needs to be tracked for user role changes.
