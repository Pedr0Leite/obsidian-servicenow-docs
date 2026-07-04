---
title: "SAM - Refresh CB Workday HRIT profile Subscriptions job is failing"
aliases:
  - KB2466570
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB2466570
kb_number: KB2466570
last_modified: 2025-08-26
---

## Issue

SAM - Refresh CB Workday HRIT profile Subscriptions job is failing due to **\[ERROR CODE: -1\] The host did not accept the connection within timeout of 10000**  
  

## Resolution

Customers need to coordinate with Workday Admins to confirm the below:  
  
1\. If Workday was under maintenance at the reported time.

2\. Request Workday SLA/uptime details if this recurs.

If the error repeats frequently (more than once in a week), and if all jobs consistently fail (persistent connectivity issue), or if retries and increased timeout do not resolve.

Escalate to ServiceNow Support with `sys_outbound_http_log` and Workday tenant logs.
