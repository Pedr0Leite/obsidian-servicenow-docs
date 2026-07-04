---
title: "Software Asset Management Professional Box Integration Download Subscriptions scheduled job fails with error \"The REST API call failed with status code: 403\""
aliases:
  - KB0824026
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0824026
kb_number: KB0824026
last_modified: 2024-12-21
---

## Issue

Software Asset Management Professional **Box Integration** Download Subscriptions scheduled job fails with the following error: 

"The REST API call failed with status code: 403"

## Resolution

Please assure that the user creating the '**Box Custom App**' on **Box Developer Console** has sufficient permissions to query **Box REST API** about the users/subscriptions then perform '**Get OAuth Token'** on **ServiceNow** end with the same user.
