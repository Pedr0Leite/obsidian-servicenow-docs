---
title: "Receive Slack Error when trying to Create a Slack Enterprise Connection required by the Software Asset Management and Slack integration"
aliases:
  - KB1968975
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB1968975
kb_number: KB1968975
last_modified: 2025-03-10
---

## Issue

The Slack Integration requires to [Create a Slack Enterprise connection](https://www.servicenow.com/docs/bundle/xanadu-it-asset-management/page/product/software-asset-management2/concept/integrate-with-slack.html#title_create-slack-enterprise-connection) from the instance side.

You have followed the steps but received an error (no\_bot\_scope\_requested) thrown from the Slack side when trying to get the OAuth Token.

![](/sys_attachment.do?sys_id=d98f94488318aa50cdbbc430feaad305 "SlackIntegrationError.png")

## Resolution

If the 'org-readiness' setting is enabled, there is no way to disable this setting.

You need to create a new Slack app and make sure NOT to enable this setting. Then, reconfigure the connections by using the new app in the ServiceNow instance.
