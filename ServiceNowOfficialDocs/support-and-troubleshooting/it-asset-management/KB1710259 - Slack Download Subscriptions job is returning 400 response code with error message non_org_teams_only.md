---
title: "Slack Download Subscriptions job is returning 400 response code with error message : \"non_org_teams_only\"
aliases:
  - KB1710259
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB1710259
kb_number: KB1710259
last_modified: 2025-02-14
---

## Issue

Following the docs : [Integrating with Slack](https://www.servicenow.com/docs/bundle/xanadu-it-asset-management/page/product/software-asset-management2/concept/integrate-with-slack.html) to create and publish the Slack integration profile.

The profile was published successfully but the Scheduled Job 'SAM - Refresh Slack Direct Integration Profile Subscriptions' was failed to download subscriptions.

The corresponding Outbound HTTP Log was returning below error message from the slack endpoint. Error code '400' is generally meaning the target has denied connection request.

{"Errors":{"description":"non\_org\_teams\_only","code":400}}

Checking the logs of flow 'Slack Download Subscriptions' via 'sys\_flow\_context' table, may see errors similar like below :

java.lang.RuntimeException: com.glide.transform.transformer.exceptions.InvalidPathException: Could not find path in stream: $.Resources

com.snc.process\_flow.exception.OpException: Failed to iterate on data stream: com.glide.transform.transformer.exceptions.InvalidPathException: Could not find path in stream: $.Resources 

## Resolution

As the error 'non\_org\_teams\_only' is throwing from the slack side, the customer can seek help from Slack support to confirm the Slack Enterprise Grid application has been created on the Grid organization level other than a workspace within the organization.

Can also use the Postman to test the API call with the same bearer token and make sure it's returning response code 200.
