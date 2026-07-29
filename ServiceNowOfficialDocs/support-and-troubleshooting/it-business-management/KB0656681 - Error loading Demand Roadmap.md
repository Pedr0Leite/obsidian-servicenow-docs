---
title: "Error loading Demand Roadmap"
aliases:
  - KB0656681
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0656681
kb_number: KB0656681
last_modified: 2024-04-07
---

## Error loading Demand Roadmap

  

### Issue

Error loading Demand Roadmap.

### Cause

Changes made to Timeline Visualization record.  

  

### Resolution

The behaviour seen is due to the changes made to the Timeline Visualization record 'Demand Backlog' seen here:

  

[/nav\_to.do?uri=roadmap\_page.do?sys\_id=72625ff94f68c200b014a50f0310c77d](https://instance_name.service-now.com/nav_to.do?uri=roadmap_page.do?sys_id=72625ff94f68c200b014a50f0310c77d)

  

Notice how the Lane condition is currently blank. In an OOB instance the default condition for this field is:

  

Portfolio.Task type - is - Portfolio

  

This is not necessarily the condition that will need to be used, this is just an example of why this roadmap is not loading properly. Please update the lane condition to test the solution. Here is further documentation on creating Timeline Visualizations:

  

[https://docs.servicenow.com/csh?topicname=t\_CreateATimelineVisualization.html&version=latest](https://docs.servicenow.com/csh?topicname=t_CreateATimelineVisualization.html&version=latest "https://docs.servicenow.com/csh?topicname=t_CreateATimelineVisualization.html&version=latest")
