---
title: "Software models are not being created automatically"
aliases:
  - KB0756686
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0756686
kb_number: KB0756686
last_modified: 2024-04-07
---

## Issue

Software models are not being created automatically even after "Automatically create software models for all 'licensable' products" is enabled.

More on this here: [https://docs.servicenow.com/csh?topicname=sam-properties.html&version=latest](https://docs.servicenow.com/csh?topicname=sam-properties.html&version=latest)

## Resolution

Software models are automatically created for any unlicensed installs, subscriptions, or options in the Product Results list that do not have an entitlement.

There are two properties that we can enable to make this work:

Software Asset -> Administration -> Properties.

\> Automatically create software models for all 'licensable' products (system property: com.snc.samp.automaticsmrcreation)

Note: This is enabled by default.

\> Automatically create software models for all 'not licensable' products (system property: com.snc.samp.automaticsmcreation)

Note: Note enabled by default.

![](sys_attachment.do?sys_id=6bba4c70db8cf0d022e0fb2439961939)

One of the reasons for failure to create the Software model is due to failure of Reconciliation job. A separate investigation is needed to make sure Reconciliation is successful and the Software product results are created which would create Software Models when this property "Automatically create software models for all 'licensable' products" is enabled.
