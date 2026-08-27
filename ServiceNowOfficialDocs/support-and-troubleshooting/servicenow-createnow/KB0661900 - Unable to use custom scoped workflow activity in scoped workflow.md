---
title: "Unable to use custom scoped workflow activity in scoped workflow"
aliases:
  - KB0661900
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0661900
kb_number: KB0661900
last_modified: 2024-09-20
---

## Unable to use custom scoped workflow activity in scoped workflow

  

### Issue

Unable to use custom scoped workflow activity in scoped workflow 

Problem

* * *

Users have reported an issue where they are unable to use custom scoped workflow activities in scoped workflows, which are designed to run on scoped applications.  

Symptoms

* * *

-   User receives an error **Invalid Activity Definitions** when they hover over a Workflow activity that has executed on a running workflow
-   Custom activity is highlighted as red on the running Workflow with the result returned as error.

Cause

* * *

This issue occurs when users are creating custom workflow activities within a Scoped Application outside of the Activity Designer.

In this case, the user has manually created a Workflow Activity Definition directly via the wf\_activity\_definition table, under a Scoped Application.

As the core activities are looking within the Global Scope, the error **Invalid Activity Definitions** is displayed.

Resolution

* * *

It is recommended to use the Activity Designer to create custom activities, as it is able to handle the logic of creating custom activities inside scoped applications.

For more information on using the Activity Designer, please review the documentation below:

[https://docs.servicenow.com/csh?topicname=c\_WorkflowActivityDesigner.html&version=latest](https://docs.servicenow.com/csh?topicname=c_WorkflowActivityDesigner.html&version=latest)

Therefore to conclude, the behaviour that the users are experiencing is by design. Custom activity development is traditionally licensed under Orchestration. Orchestration provides support for application scoping for custom activities using the Activity Designer.

**WARNING**: Please note that the Activity Designer comes with the Orchestration plugin, which is a paid plugin that has separate subscription fees. Please ensure that you review the documentation above and consult your Account Manager or Territory Manager for more information.
