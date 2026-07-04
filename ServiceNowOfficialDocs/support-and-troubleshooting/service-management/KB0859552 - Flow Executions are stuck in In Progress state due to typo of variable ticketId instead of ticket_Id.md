---
title: "Flow Executions are stuck in \"In Progress\" state due to typo of variable ticketId instead of ticket_Id"
aliases:
  - KB0859552
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0859552
kb_number: KB0859552
last_modified: 2025-10-31
---

## Issue

We are developing flow and sometimes due to some script error our flow is returning an error and is stuck in an **"In progress"** state. We have a problem here, we are unable to cancel this **"In Progress"** transaction from UI. As this transaction is stuck, we cannot run the flow again even after correcting the script issue.

AutoCompletion could be a PRB or a configuration Issue as it is showing the wrong variable

## Resolution

-   Take a look at the inline script step. The first line **"ticketId"** is wrong. It should be **"fd\_data.trigger.current.ticket\_id".**
-   The inline script autocomplete seems to suggest ticketId rather than ticket\_id and it is not correct, That could be an internal Issue but for reference, and as far as this particular error goes, that should solve the Flow Error Issue if it gets stuck.
