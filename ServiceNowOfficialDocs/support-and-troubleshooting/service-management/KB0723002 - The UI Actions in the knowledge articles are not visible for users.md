---
title: "The UI Actions in the knowledge articles are not visible for users"
aliases:
  - KB0723002
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0723002
kb_number: KB0723002
last_modified: 2024-04-07
---

## The UI Actions in the knowledge articles are not visible for users

  

### Issue

# Symptoms

* * *

The checkout, publish, Retire UI actions are not visible

# Release

* * *

Kingston Patch 11 

# Cause

* * *

The issue is caused due to the v3 knowledge base UI action conditions being evaluated to the v2 knowledge base

# Resolution

* * *

The issue is caused due to the v3 knowledge base UI action conditions being evaluated to the v2 knowledge base. The issue occurs when the instance has both v2 and v3 knowledge bases enabled.

It is recommended that all the knowledge bases are migrated to v3.

For temporary relief, please follow the steps below:

In the Review UI action (for instance)

1\. The UI action condition is failing at this function call " new KBKnowledge().canRetire(current)"

2\. In the KBKnowledgeSNC (base class which is extended in the child KBKnowledge) script include, the function "canRetire" is, in turn, calling another function named "canRetire" in the script include, KBVersioning

3\. The function is defined in the base class (base script include KBVersioningSNC) 

4\. Therefore that function can be overridden by defining our own custom function (that skips the canContribute condition check for v2 knowledge bases but still checks the condition for v3 knowledge bases) in the Child script include "KBVersioning".

5\. To do this copy the entire "canRetire" function from the base class and paste in the child class. Have an if condition that checks if the knowledge base is v2, then add your own condition that determines who should see the UI action.

The same steps can be followed for Publish and Checkout UI actions.
