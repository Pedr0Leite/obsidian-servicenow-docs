---
title: "Live feed comments not showing up on knowledge articles"
aliases:
  - KB0656542
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0656542
kb_number: KB0656542
last_modified: 2024-04-07
---

## Live feed comments not showing up on knowledge articles

  

### Issue

Issue Summary  

* * *

Unable to view feedback comments on knowledge article when the article is loaded. Started facing this issue after upgrading the instance to Jakarta patch 5. 

Most Probable Cause  

* * *

To retain the legacy comment functionality with knowledge articles for all users, set the Use Live Feed for Knowledge feedback property (_**glide.knowman.use\_live\_feed**_) to false. This knowledge property is true by default. 

Solution Proposed  

The knowledge property (_**glide.knowman.use\_live\_feed**_) holds the comments on knowledge articles. This property has to be set to false to view the live feed. Please check the property and verify the live feed.

Related references:

[https://docs.servicenow.com/csh?topicname=r\_KnowledgeFeedback.html&version=latest](https://docs.servicenow.com/csh?topicname=r_KnowledgeFeedback.html&version=latest)
