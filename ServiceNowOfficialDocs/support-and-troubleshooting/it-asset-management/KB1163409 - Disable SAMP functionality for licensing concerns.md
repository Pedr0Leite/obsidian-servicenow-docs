---
title: "Disable SAMP functionality for licensing concerns"
aliases:
  - KB1163409
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB1163409
kb_number: KB1163409
last_modified: 2025-03-26
---

## Issue

There is currently no process in place to remove SAMP functionality if a customer is worried about licensing installs/subscriptions that no longer apply.

SAMP charges by the devices in the installs table and users in the subscriptions table, so appropriate actions need to be taken regarding these.

## Resolution

The recommendation is for the customer to:

1) Exclude software assets on CIs for all devices to prevent charging in the installs table. Follow directions here

[https://www.servicenow.com/docs/bundle/yokohama-it-asset-management/page/product/software-asset-management2/task/exclude-software-assets-cis.html](https://www.servicenow.com/docs/bundle/yokohama-it-asset-management/page/product/software-asset-management2/task/exclude-software-assets-cis.html)

2) Set a business rule to exclude futures assets (Ensure custom column from step #1 has true values), or make the default value 'true' on the column

3) Delete all SaaS integrations to delete the corresponding subscriptions and prevent charging in the subscriptions table (samp\_sw\_subscription)

4) Disable scheduled jobs starting with "SAM - ", including the content jobs.
