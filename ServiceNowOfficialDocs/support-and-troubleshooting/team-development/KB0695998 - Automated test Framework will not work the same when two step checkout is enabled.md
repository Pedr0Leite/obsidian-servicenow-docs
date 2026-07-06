---
title: "Automated test Framework will not work the same when two step checkout is enabled"
aliases:
  - KB0695998
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0695998
kb_number: KB0695998
last_modified: 2024-04-07
---

## Automated test Framework will not work the same when two step checkout is enabled

  

### Issue

# Symptoms

* * *

Automated test framework is will not be enable to query requested item based on request that got created. Results in no request found.

Query - ![](sys_attachment.do?sys_id=900c602edb42b450e515c2230596195c)

# Release

* * *

All versions

# Cause

* * *

Due to two step checkout process enabled.

# Resolution

* * *

The step "order catalog item" doesn't consider the two step, if two step is enabled.

Make sure to disable to the two step checkout when planning to use "oder catalog item".

# Additional Information

* * *

[https://docs.servicenow.com/csh?topicname=atf-tut-build-first.html&version=latest](https://docs.servicenow.com/csh?topicname=atf-tut-build-first.html&version=latest)
