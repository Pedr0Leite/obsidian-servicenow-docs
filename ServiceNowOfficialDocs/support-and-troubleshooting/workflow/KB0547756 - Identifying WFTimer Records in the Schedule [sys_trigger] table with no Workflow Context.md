---
title: "Identifying WFTimer Records in the Schedule [sys_trigger] table with no Workflow Context"
aliases:
  - KB0547756
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0547756
kb_number: KB0547756
last_modified: 2024-09-20
---

## Identifying WFTimer Records in the Schedule \[sys\_trigger\] table with no Workflow Context

  

### Issue

-   In customer support, we have encountered scenarios where a customer has reported a large number of WFTimer records within the Schedule \[sys\_trigger\] table.

### Release

In customer support, we have encountered scenarios where a customer has reported a large number of WFTimer records within the Schedule \[sys\_trigger\] table.

### Cause

Potential Cause

* * *

There are two potential scenarios where this issue can occur. 

<table class="noteTable" align="left"><tbody><tr><td style="vertical-align: middle; text-align: center;"><img title="Note" src="/Note_25x.pngx" alt="" align="bottom" border="" hspace="" vspace=""></td><td style="vertical-align: middle; text-align: left;"><strong>Note</strong>: The number of scenarios can vary due to the nature of the customer’s implementation on the instance and the build that their instance is reported on. Do not assume that the root causes below are the actual root cause for a customer issue. A full investigation is required before determining the root cause. The guidelines below are available to assist customer support.</td></tr></tbody></table>

  

**  
  
Potential Root Cause 1:** A user may have created a script within their workflow to delete the Workflow Context \[wf\_context\] record only, leaving orphaned WFTimer records in the Schedule \[sys\_trigger\] table.

**Potential Root Cause 2:** A user may have removed the **Context** reference field value from a Workflow Executing Activities \[wf\_executing\] table. This can be done via the list view or the form itself if a user has the **admin** or **workflow\_admin** role.

  

Assistance identifying orphaned WFTimer jobs without a workflow context

### Resolution

In the Schedule \[sys\_trigger\] table, there is a field called document\_key. The document\_key field contains a sys\_id, which is linked to a record in any table where the Schedule \[sys\_trigger\] is being triggered.

In this scenario, the expected analysis would be that the document\_key within the WFTimer records on the Schedule \[sys\_trigger\] table would contain a sys\_id of the Workflow Executing Activities \[wf\_executing\] table. This can be found by following the steps below:

1.  Log into any instance as an **admin** or **maint** user.
2.  Navigate to **System Scheduler > Scheduled Jobs**.
3.  Open any WFTimer records within this table.  
    A WFTimer record appears if there was a running workflow containing the activity definition **Timer** or **SLA Percentage Timer**.
4.  Copy the document\_key field value from a WFTimer record within the Schedule \[sys\_trigger\] table.
5.  On the Application, navigate to **Workflow > Live Workflows > Executing Activities** (this leads to the wf\_executing table).
6.  On the search navigation bar, select **sys\_id** on the right of the **Go To** bar and paste the document\_key within the field.
7.  Press Enter on your keyboard and only one result should appear within the Workflow Executing Activities \[wf\_executing\] table.
8.  Open the record.  
    You should see a field called **Context**, that is a reference field to the Workflow Context \[wf\_context\] table where the triggered workflows are stored.

  

Example 1 - workflow executing activity \[wf\_executing\] record

* * *

![](/sys_attachment.do?sys_id=d37ae866db42b450e515c223059619e7)

Actual behavior:

In some customer scenarios, we have seen that although there is an Executing Activity that matches the document\_key from the Schedule \[sys\_trigger\] table, the Context reference field is empty.

This is an issue because if there are workflow activities that are in **running** state with no reference to a context, then the activity continues to run because there is no workflow to continue the flow to the next activity.

  

Example 2 - workflow executing list records with no workflow

* * *

 ![](/sys_attachment.do?sys_id=577ae866db42b450e515c223059619f3)

  

  

* * *

In order to identify the orphaned WFTimer Jobs without a Workflow Context associated, run the query below.

**CAUTION:** Due to the nature of the query, perform the query on a sub-production instance first. Due to the amount of tables being referenced, it is expected to become a long running query depending on the data within those tables. Therefore, before running the query, take into account the number of records within the following tables:

-   Workflow Context \[wf\_context\]
-   Workflow Executing Activities \[wf\_executing\]
-   Schedule \[sys\_trigger\]

If there is a huge amount of data contained within the tables, do not use the query. The query has been tested on a demonstration instance only and therefore it is not guaranteed to work as expected on customer instances with a huge amount of data stored within the tables listed above. Use the query at your **OWN** risk:

**Query:** SELECT e.sys\_id from wf\_executing e left join wf\_context c on e.context = c.sys\_id inner join sys\_trigger t on e.sys\_id = t.document\_key where c.sys\_id is null;
