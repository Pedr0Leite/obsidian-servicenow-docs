---
title: "Customer setup Flow Designer Integration and all the messages on Microsoft Team (MS Team) channel post are being posted by same User ID"
aliases:
  - KB0815282
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0815282
kb_number: KB0815282
last_modified: 2024-04-08
---

## Issue

Customer reported that they have successfully integrated their ServiceNow instance with Microsoft Team (MS Team) using Flow Designer. Whenever a P1 incident is created in their ServiceNow instance, Flow Designer integration triggers and post a message on MS Team channel. But the problem is, all such messages are being posted by the same User ID.

Expectation is that message in MS Team should be posted by the user who creates the P1 incident.

## Resolution

As noticed, there is no automation added/used in this Flow Designer Integration for pulling the **OAuth Access Token** before running the REST Integration call. Therefore, using below approach can help improving this situation:

a) Follow-up with **MS Team** admin asking for an API for retrieving **OAuth Access token** and configure an **Outbound REST Message** accordingly.

b) Call this **REST Message** in Flow Designer before existing **REST Message** which **POST** P1 incident info on MS Team channel.

c) This REST call will pull an OAuth token as a user who creates the **P1 Incident** and the same user will display on **MS Team** channel post.

## Additional Information
