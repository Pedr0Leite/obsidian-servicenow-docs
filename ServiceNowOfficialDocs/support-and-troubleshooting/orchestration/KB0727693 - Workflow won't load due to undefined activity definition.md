---
title: "Workflow won't load due to undefined activity definition"
aliases:
  - KB0727693
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0727693
kb_number: KB0727693
last_modified: 2024-04-07
---

## Workflow won't load due to undefined activity definition

  

### Issue

# Symptoms

* * *

Workflow won't load due to undefined activity definition. When attempting to load the workflow the following is displayed:

![](/sys_attachment.do?sys_id=c19ae0a6db42b450e515c22305961910)

# Release

* * *

All releases 

# Cause

* * *

The activity definition may be missing and if this is the case the workflow canvas won't load.

# Resolution

* * *

The activity definition may be missing. To confirm this, in the filter navigator type wf\_activity.list and filter by the affected workflow version and empty activity definition. For example:

![](/sys_attachment.do?sys_id=c99ae0a6db42b450e515c22305961921)

Look up for the activity definition in wf\_element\_activity, for example:

![](/sys_attachment.do?sys_id=c99ae0a6db42b450e515c22305961926)

Take the sys\_id of the above record and go back to the wf\_activity.list to assign the appropriate activity definition there (use filters to match the sys\_id found in the previous step):

![](/sys_attachment.do?sys_id=819ae0a6db42b450e515c22305961938)

Go back to the workflow and it should now load properly.
