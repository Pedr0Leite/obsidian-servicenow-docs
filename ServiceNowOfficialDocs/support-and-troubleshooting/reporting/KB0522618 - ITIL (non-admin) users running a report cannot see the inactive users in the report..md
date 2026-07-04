---
title: "ITIL (non-admin) users running a report cannot see the inactive users in the report."
aliases:
  - KB0522618
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0522618
kb_number: KB0522618
last_modified: 2024-04-30
---

## ITIL (non-admin) users running a report cannot see the inactive users in the report.

  

### Issue

## Problem

Run the report on the cmdb\_ci\_computer table, having selected the **Assigned to.User ID** column to display the results of the report. The inactive users are visible on the run report screen, but they are _not_ displayed in the exported Excel or .csv file.

## Solution

The _user query_ business rule (BR) is in place and prevents access to the inactive sys\_user object and its fields for non-admin users. The business rule is enabled by default, but can be turned off to allow non-admin users access to the inactive user fields.

The business rule does the following:

Disallows access to interactive sessions (UI) and user fields to inactive users and non-admin users.

The business rule does not make sense in scenarios like this when an ITIL user who manages assets and incidents does need to see all the associated data. The BR can be enabled or disabled as required.  
  
The business rule cannot be removed by default. The issue has come up on different occasions and the collective decision has been to advise the customer to disable the business rule if necessary.
