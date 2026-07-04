---
title: "Identifying the User and Details for Transactions with the Name of SystemTrigger<date/time>"
aliases:
  - KB0656730
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0656730
kb_number: KB0656730
last_modified: 2026-03-23
---

## Issue

Transactions seen in the format of SystemTrigger<date/time started> occur when a user manually executes a job when not executed by the scheduler. An example would be to open a scheduled job and click the Execute Now button. That action will execute the job but the transaction will be seen in the platform in the format of SystemTrigger<date/time started>.

## Resolution

To find the user that initiated this transaction as well as the transaction details, look for this job as follows:

1.  1.  Navigate to System Logs > Transactions (Background).
    2.  Use one of the following options: add a filter or go directly to a filtering URL.  
        -   Add the following filter:  
            **\[URL\] \[Contains\] \[SystemTrigger\]**  
            **AND**  
            **\[Created\] \[on\] \[month/date\_matching\_name\_of\_SystemTrigger\_job\]**
        -   Add the following link in the instance URL:  
            -   https://<your\_instance>.service-now.com/syslog\_transaction\_list.do?sysparm\_query=sys\_created\_onONThis%20week@javascript:gs.beginningOfThisWeek()@javascript:gs.endOfThisWeek()%5EurlLIKESystemTrigger&sysparm\_first\_row=1&sysparm\_view=
    3.  Make sure that the Created, Created\_by, and URL fields are displayed in the list columns.
    4.  For each record returned:  
        -   Created by: Shows the user ID for the user who executed this transaction manually
        -   URL: Shows the link to the transaction details, indicating table and parameters passed, such as a list view with a filter, or report details and the like.

**NOTE**: This content applies to transactions that have been completed, and is used post-mortem.  If the transaction is active, navigate to System Diagnostics > Active Transactions (All Nodes) or go to https://<your\_instance>.service-now.com/v\_cluster\_transaction\_list.do
