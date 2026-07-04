---
title: "Workflow Stage Rendering | RITM Stage Icons"
aliases:
  - KB0551102
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0551102
kb_number: KB0551102
last_modified: 2024-04-07
---

## Workflow Stage Rendering | RITM Stage Icons

  

### Issue

Workflow Stage Rendering | RITM Stage Icons

  
  

# Introduction

* * *

The purpose of this article is to document the behavior change for Workflow Stages within the Service Catalog when users migrate to the new Workflow Stage Rendering.

Starting from Dublin, ServiceNow has introduced a new workflow stage engine that allows users to control the value of the **stage** field, based on the behavior of their workflow. This allows users to have a perception of what stage that their Incidents, Problems, Changes, and Requests are at before they are completed/fulfilled. By default, the Stage rendering set for the base system workflows will be **Legacy**. This would produce the behavior of how the Workflow Stages used to behave in the pre-Dublin release. However, changing the Workflow Stage rendering to the new Stage renderers causes a behavior change with Service Catalog workflows on the RITM level when users reject the parent REQ level.

For more information, see [Workflow Stage Renderers](https://docs.servicenow.com/csh?topicname=r_WorkflowStageRenderers.html&version=latest "Workflow Stage Renderers").

# Pre-Dublin/Legacy stage rendering behavior

* * *

When the REQ has the Approval field set to **rejected**, the first stage field on the RITM will always show as **Rejected**, and the workflows on the RITM that use the **Legacy** stage rendering will show all of the stages for the RITM as **Rejected**.

![](/Screen%20Shot%202015-08-24%20at%2009.25.33.JPGx)

# Post-Dublin/New stage rendering

* * *

If the workflow on the RITM level is using the new stage rendering, only the first stage value of the RITM will show as **Rejected**, while the next stages would show as **Pending - has not started**. This behavior only occurs when the new stage rendering is used for the workflows on the RITM level.

![](/Screen%20Shot%202015-08-24%20at%2009.35.08.JPGx)
