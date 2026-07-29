---
title: "Why SLAs are not posting e-mail notifications in the incident activity stream"
aliases:
  - KB0779115
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0779115
kb_number: KB0779115
last_modified: 2024-04-08
---

## Why SLAs are not posting e-mail notifications in the incident activity stream

  

### Issue

The user's P1 incidents are not posting e-mail updates to the activity stream on the related task record (e.g. Incident), even after one hour. 

### Resolution

To begin with, it is worth noting that this functionality does not exist naturally in an Out of Box (OOB) instance. Within an OOB instance, there is no native posting of this information to the parent task which the task\_sla is on. Rather, such activity stream updates are posted directly to the task\_sla, as that is where the workflow is running. The task\_sla form layout needs to be configured to show this, though. This is expected.

It was found that the user accomplished these updates via a custom workflow with a custom workflow activity within it and reported that they could see this process working fine in their Production instance, but not in their Development instance.

The reason that this is working in Production and not in Development is that the user is using the custom workflow on some SLA Definitions in their Production instance, but in Development, they are using the OOB "Default SLA Workflow", where this functionality does not exist.

When the user modified the workflow associated with their SLA Definitions in their Development instance to utilize their custom workflow, the behavior was corrected and their custom functionality worked once again.
