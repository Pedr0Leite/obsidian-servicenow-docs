---
title: "How should I design my Knowledge Base user criteria?"
aliases:
  - KB0689656
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0689656
kb_number: KB0689656
last_modified: 2024-04-07
---

## How should I design my Knowledge Base user criteria?

  

### Issue

# Overview

* * *

Several questions regarding Knowledge Management user criteria.

1) Is it working as designed where the identified User Criteria at the Knowledge base level overrides the article level?

2) How should Knowledge be set-up (i.e., multiple knowledge bases vs. single knowledge base) when there are varying levels of access required?

# Subject

* * *

Knowledge Base user criteria

# Response

* * *

1) Correct it is working as designed per Per [https://docs.servicenow.com/csh?topicname=t\_SelectUCArticle.html&version=latest,](https://docs.servicenow.com/csh?topicname=t_SelectUCArticle.html&version=latest,) "Knowledge base user criteria restrictions override article-level user criteria." docs.servicenow.com 

Select user criteria for an article. You can specify user criteria for an article to control which users can read the article. About this task If an article has no user criteria selected, the article is available to all users who have access to that knowledge 

So that's a yes, that's expected. 

2) How your knowledge base is set up is based on your business needs If you want a knowledge base that only TSEs use, for example, and another that only Managers use, then make two separate Bases and set the criteria they need on the knowledge bases respectively.

# Additional Information

* * *

[https://docs.servicenow.com/csh?topicname=t\_SelectUCArticle.html&version=latest,](https://docs.servicenow.com/csh?topicname=t_SelectUCArticle.html&version=latest,) "Knowledge base user criteria restrictions override article-level user criteria."
