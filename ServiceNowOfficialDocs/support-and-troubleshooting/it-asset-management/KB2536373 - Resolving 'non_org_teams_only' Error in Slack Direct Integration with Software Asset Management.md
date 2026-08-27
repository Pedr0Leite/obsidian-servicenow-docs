---
title: "Resolving 'non_org_teams_only' Error in Slack Direct Integration with Software Asset Management"
aliases:
  - KB2536373
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB2536373
kb_number: KB2536373
last_modified: 2025-11-06
---

## Text

When validating a direct integration profile for Slack Enterprise—or while retrieving integration subscriptions—you may encounter a 400 error in the outbound HTTP logs for the [`https://api.slack.com/scim/v1/Users`](https://api.slack.com/scim/v1/Users "https://api.slack.com/scim/v1/Users") endpoint, accompanied by the message `non_org_teams_only`.

This error indicates a configuration issue caused by the token being fetched at the wrong level within the Slack Enterprise organization.

To resolve this:

-   The person fetching the token must have the Organisation Owner role in Slack.
-   In ServiceNow, after clicking Get OAuth Token on the Credential record, a dialog box will appear. By default, it requests access at the workspace level.

![](/sys_attachment.do?sys_id=5899bd619301b618e7eef35d6cba10ed)

-   The customer should open the dropdown menu in the top-right corner of the dialog box to check if the Enterprise organization is listed.
    -   If listed, select the Enterprise org.

![](/sys_attachment.do?sys_id=c899bd619301b618e7eef35d6cba1044)

-   -   If not, choose Add another workspace and enter the Slack Enterprise URL.
        -   ![](/sys_attachment.do?sys_id=1099bd619301b618e7eef35d6cba10ea)
        -   ![](/sys_attachment.do?sys_id=5099bd619301b618e7eef35d6cba10f1)

Once the Enterprise organization is selected, the dialog box will request access at the Organization Level. This ensures the token is fetched correctly, allowing the connection to validate successfully.
