---
title: "FAQ - Plugin migration from Company Separation to Domain Separation"
aliases:
  - KB0584446
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0584446
kb_number: KB0584446
last_modified: 2025-01-17
---

## Issue

Mandatory migration of Company Separation to Domain Separation | Customer FAQ 

  
  
Table of Contents  

* * *

<table class="tocTable"><tbody><tr><td><a style="text-decoration: none;" href="#overview"><span style="color: #d1232b;">Overview&nbsp;&nbsp;</span></a></td></tr><tr><td><a style="text-decoration: none;" href="#1"><span style="color: #646464;"><span style="color: #d1232b;">1.</span>&nbsp;What was Company Separation?</span></a></td></tr><tr><td><a style="text-decoration: none;" href="#2"><span style="color: #646464;"><span style="color: #d1232b;">2.</span>&nbsp;What is Domain Separation?</span></a></td></tr><tr><td><a style="text-decoration: none;" href="#3"><span style="color: #646464;"><span style="color: #d1232b;">3.</span>&nbsp;Why does my instance have to be migrated from Company Separation to Domain Separation or have Company Separation disabled if I am no longer using it?</span></a></td></tr><tr><td><a style="text-decoration: none;" href="#4"><span style="color: #646464;"><span style="color: #d1232b;">4.</span>&nbsp;Is there any downtime during the migration or while disabling the plugin?</span></a></td></tr><tr><td><a style="text-decoration: none;" href="#5"><span style="color: #646464;"><span style="color: #d1232b;">5.</span>&nbsp;How do I disable company separation if I am no longer using the plugin?</span></a></td></tr><tr><td><a style="text-decoration: none;" href="#6"><span style="color: #646464;"><span style="color: #d1232b;">6.</span>&nbsp;Are customers currently using Company Separation charged for Domain Separation?</span></a></td></tr></tbody></table>

  
  
Overview

* * *

The Company Separation plugin will no longer be supported once Helsinki is released and will need to be migrated to Data Only Domain Separation.  We are requiring all customers with the Company Separation plugin activated on their instances to work with ServiceNow to migrate to Data Only Domain Separation.  There will be no additional charges for the usage of Data Only Domain Separation for customers that are migrated from Company Separation with Data Only usage. Domain separation provides additional fee based features that are not part of this migration. Please contact your sales rep before enabling additional domain features.

If you are no longer using company separation, the plugin must be disabled.

To disable company separation:

1.  1.  Navigate to **System Properties > All Properties**.
        
    2.  Search for and select properties **glide.db.separation.field and glide.db.separation.exception.field**.
        
    3.  Clear out the values (i.e., set them to empty value) of both the properties to disable company separation.(Do not delete the properties)
        

<table class="noteTable" style="border: 1px solid #e0e0e0;" align="left"><tbody><tr><td style="width: 50; vertical-align: middle; text-align: center;"><img style="align: baseline;" title="Note" src="/Note_25x.pngx" alt="" align="bottom" border="" hspace="" vspace=""></td><td style="vertical-align: middle; text-align: left;"><strong>Note</strong>: Testing this procedure in a test/dev environment before moving into production is highly recommended.</td></tr></tbody></table>

1\. What was Company Separation?

* * *

When Company Separation is activated on a ServiceNow instance, users with a Company value in their user record can only see data for their company and any child companies. Company Separation applies to any table that has a **company** or **u\_company** field. For example, the task table has a **company** field. So a user in Company A can see only tasks (cases, change requests, problems, etc.) that are assigned to Company A or Company A's hierarchical children.

For more information, see [Domain Separation](https://docs.servicenow.com/csh?topicname=t_ActivateDomainSeparation.html&version=latest "Domain Separation") in the product documentation. 

2\. What is Domain Separation?

* * *

Domain separation is a way to separate data into (and optionally to separate administration by) logically defined domains. Domain separation is best for customers who need to do the following:

-   Enforce absolute data segregation between business entities (data separation)
-   Customize business process definitions and user interfaces for each domain (delegated administration)
-   Maintain some global process and global reporting in a single instance of ServiceNow

For more information, see [Domain Separation](https://docs.servicenow.com/ "Domain Separation") in the product documentation.

 

3\. Why does my instance have to be migrated from Company Separation to Domain Separation, or have Company Separation disabled, if I am no longer using Company Separation?

* * *

ServiceNow is no longer supporting the Company Separation Plugin. The plugin must be migrated to Domain Separation if you are currently using it or shut off on your instance if you are no longer using it. In some cases your company may have been testing the functionality and it was never used. Turning off the plugin or migrating to Domain Separation ensures that your instance is free of the plugin and any potential issues that remain with Company Separation.

  
  
4\. Is there any downtime during the migration or while disabling the plugin?

* * *

No, there is no downtime. 

  
  
5\. How do I disable company separation if I am no longer using the plugin?

* * *

1.  Navigate to **System Properties > All Properties**.
2.  Search for and select the properties _**glide.db.separation.field**_ and _**glide.db.separation.exception.field**_.
3.  Clear out the values (i.e., set them to empty value) of both the properties to disable company separation.(Do not delete the properties)

**Note:** Testing this procedure in a test/dev environment before moving into production is highly recommended.

  
  
6\. Are customers currently using Company Separation charged for Domain Separation?

* * *

There will be no additional charges for the usage of Data Only Domain Separation for customers that are migrated from Company Separation with Data Only usage. Domain separation provides additional fee based features that are not part of this migration. Please contact your sales rep before enabling additional domain features.

Save
