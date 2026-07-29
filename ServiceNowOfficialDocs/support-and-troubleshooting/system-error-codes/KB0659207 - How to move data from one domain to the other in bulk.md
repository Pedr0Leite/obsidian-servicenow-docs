---
title: "How to move data from one domain to the other in bulk"
aliases:
  - KB0659207
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0659207
kb_number: KB0659207
last_modified: 2024-04-07
---

## Issue

How to move data from one domain to the other in bulk  

  
  

# Introduction

* * *

When domain separation is enabled in your instance, each of your domain-separated tables has a field called "Domain \[sys\_domain\]" that determines the domain to which a particular record belongs. However, in certain situations, you might have to move large amount of records from one domain to the other.

This article provides guidelines and recommendations on how to perform this type of move.

**Note:** This document describes only how to move data from one domain to another. It does not cover how to move customizations such as business rules, client scripts, UI actions, or UI policies.

# Recommendations

* * *

-   Using import sets or transform maps is not recommended when moving data from one domain to the other.
    
-   The recommended approach is to use Background Scripts / Fix Scripts; however, keep in mind that there might be business rules that can overwrite the value of sys\_domain field you set through Background Scripts / Fix Scripts.
    
-   Fix Script might be a more viable solution in cases where you want to keep the script for future use.
    
-   When running the script, make sure you are in the "global" domain so that you have full visibility throughout your domain map.
    

# Guidelines

* * *

In a domain-separated instance, the domain of the data in OOB tables are connected in the following pattern:

-   Companies (independent)
-   Groups (dependent on company)
-   Users (dependent on company)
-   Group Membership (dependent on users)
-   Tasks (dependent on users)
-   Task SLAs (dependent on Tasks)

As this pattern suggests, when moving records from one domain to the other, use the following sequence: Companies > Groups > Users > Tasks.

## Moving Company Records

Use GlideRecord to query the Company records and update its sys\_domain field.

Moving Companies will automatically trigger the following:

1.  It will trigger the change in all Users and Group associated with this company.
2.  Due to the change of domain in the Users record, the **sys\_user\_grmember** and **sys\_user\_has\_role** records are also updated.

## Moving Tasks (e.g., Incident/Change/Problem/Catalog Tasks/RITMs etc.)

Once the domain of the User, Groups and Company records are set, you need to manually change the domain of the Tasks. The following business rule sets the domain of any existing task -

Domain - Set Domain - Task: Sets the Task’s domain same as the task’s Company’s domain

However, this business rule does not fire when the domain of the Company changes. You have to trigger it manually by running a Background / Fix script.

**Note:** When writing a Background / Fix Script to bulk update the domain of certain records, keep in mind that all the business rules (OOTB and Custom) will trigger when running your script. The behavior of your script will depend on those business rules.

# Current Limitations

* * *

-   As mentioned previously, these guidelines are not applicable for customizations, which fall under Delegated Administration.
    
-   Methods for moving the data of custom tables is not in scope of this document. To move this data, you have to be aware of any scripts you have written to derive the sys\_domain field’s value in your custom table. If your custom table is extended from Task / Task based tables, the OOB business rules for tasks will also apply.
