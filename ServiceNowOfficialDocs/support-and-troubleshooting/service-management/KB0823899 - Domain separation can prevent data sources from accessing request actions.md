---
title: "Domain separation can prevent data sources from accessing request actions"
aliases:
  - KB0823899
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0823899
kb_number: KB0823899
last_modified: 2024-04-08
---

## Domain separation can prevent data sources from accessing request actions

  

### Issue

When configuring a Data Source of Type _REST (IntegrationHub)_ you need to configure a _Request action._ If the Flow Designer Action that you configure is in a different Domain (for example _TOP_) to the Data Source (which is by default in the _Global_ Domain) then the Data Source will be unable to use that Action as its _Request action_.

The error message will be something like:

_com.glide.db.impex.datasource.stream.StreamDataSourceException: com.glide.plan.runners.FlowObjectAPIException: The action named: your\_action\_name does not exist within application scope: global_

### Release

Orlando

### Resolution

The Flow Designer Action needs to be in the same Domain as the Data Source, usually _Global_
