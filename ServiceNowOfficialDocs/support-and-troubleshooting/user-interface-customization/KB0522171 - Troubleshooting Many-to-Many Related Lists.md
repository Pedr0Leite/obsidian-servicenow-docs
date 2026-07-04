---
title: "Troubleshooting Many-to-Many Related Lists"
aliases:
  - KB0522171
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0522171
kb_number: KB0522171
last_modified: 2024-04-30
---

## Issue

The number of records that appear in the left pane of the slush bucket is unexpected.

## Resolution

Use access control list (ACL) rules to grant the user write permissions to the child table. This operation allows the user to update records using API protocols such as web services.

For information on granting or denying access, refer to [Access control list rules](https://docs.servicenow.com/csh?topicname=access-control-rules.html&version=latest "Access control list rules") and [Contextual Security](https://docs.servicenow.com/csh?topicname=r_ContextualSecurity.html&version=latest "Contextual Security") in the ServiceNow documentation pages.
