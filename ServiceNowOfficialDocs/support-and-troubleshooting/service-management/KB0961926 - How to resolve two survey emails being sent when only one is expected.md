---
title: "How to resolve two survey emails being sent when only one is expected"
aliases:
  - KB0961926
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0961926
kb_number: KB0961926
last_modified: 2026-06-25
---

## How to resolve two survey emails being sent when only one is expected

  

### Issue

Resolve two survey emails being sent to a user when only one survey is expected to trigger based on the configured conditions.

When an incident is resolved, two survey emails are generated even though only one survey's trigger conditions are met. A second survey triggers because a separate notification also evaluates to true under the same conditions.

### Release

All supported releases

### Cause

Two notifications on the instance both evaluate to true when the incident is resolved, causing both survey emails to be sent.

The survey trigger for the intended survey fires correctly. However, a second notification — Survey User Invite — also evaluates to true under the same conditions and generates a second survey email. In the email logs, both emails are sent at the same time when the incident is resolved:

-   The unintended survey email is triggered by the Survey User Invite notification.
-   The intended survey email is triggered by the Incident Closure Survey notification.

The trigger for the unintended survey is not the survey trigger itself — it is the Survey User Invite notification condition evaluating to true.

### Resolution

Update the Survey User Invite notification to add a condition that prevents it from triggering for incidents that should only send the intended survey.

1.  Go to the Survey User Invite notification.
2.  Add a condition to restrict when the notification triggers. For example, add a condition such as Metric type is not \[intended survey name\] or Metric type is \[unintended survey name\] based on your requirements.
3.  Test the updated condition on a non-production instance before applying it to production.
