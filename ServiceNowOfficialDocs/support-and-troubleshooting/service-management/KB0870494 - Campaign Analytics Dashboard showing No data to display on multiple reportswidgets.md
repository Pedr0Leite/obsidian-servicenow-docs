---
title: "Campaign Analytics Dashboard showing \"No data to display\" on multiple reports/widgets"
aliases:
  - KB0870494
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0870494
kb_number: KB0870494
last_modified: 2023-12-15
---

## Campaign Analytics Dashboard showing "No data to display" on multiple reports/widgets

  

### Issue

Many reports/widgets on the user's Campaign Analytics Dashboard were showing "No data to display". They wanted to know why.

### Cause

In the past, the user had customized some records related to the cdAnalytics angular provider. Unfortunately, as the records were marked as modified by the system when the user installed the Content Analytics plugin, these didn't get updated.

### Resolution

The user was able to remove the two sys\_update\_xml records which showed customizations to the cdAnalytics angular provider, and then they repaired the Content Delivery plugin. 

After doing this, all current files were brought onto the user's system, and the Scheduled Jobs which check against Campaigns and report against them successfully pulled back and populated Campaign data to the Campaign Analytics Dashboard.
