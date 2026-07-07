---
title: "After cloning the instance loses all the active workflow conetxt showing error \"There are no workflow contexts for this document\"
aliases:
  - KB0711954
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0711954
kb_number: KB0711954
last_modified: 2025-07-16
---

## Issue

The error "There are no workflow contexts for this document" is due to the _**wf\_context**_ table not being part of the excluded tables while cloning.

## Resolution

On an out of box instance, there is a list of tables that are excluded from being cloned. Remove the WF\_Context table from the list of the excluded tables before cloning.

## Additional Information

[https://community.servicenow.com/community?id=community\_question&sys\_id=0fefcc49dbdf9b4023f4a345ca961949](https://community.servicenow.com/community?id=community_question&sys_id=0fefcc49dbdf9b4023f4a345ca961949)
