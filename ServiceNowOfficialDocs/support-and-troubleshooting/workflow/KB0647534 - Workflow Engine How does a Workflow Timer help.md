---
title: "Workflow Engine | How does a Workflow Timer help?"
aliases:
  - KB0647534
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0647534
kb_number: KB0647534
last_modified: 2026-03-05
---

## Workflow Engine | How does a Workflow Timer help?

  

### Issue

# Workflow Engine | How does a Workflow Timer help

### Release

### Cause

# Scenario

* * *

On a ServiceNow instance a user can trigger the creation of a record, which in turn triggers a running Workflow and can also cause Business Rules and Script-Includes to execute. 

Occasionally, unexpected behavior occurs due to either long running Business Rules or Workflow Script execution.

One of the solutions available to implement is to place a one second timer. However, the question remains: How does a Workflow Timer help, and why is it used as a solution?

### Resolution

# What does a Workflow Timer do?

* * *

When a Workflow Timer runs for the first time a Scheduled Job is created. All Scheduled Jobs are stored in a table called **sys\_trigger**.

A triggered Workflow Timer is stored on a table called **wf\_executing**.

When the Scheduled Job is created, the timer activity is referenced in the document\_key field of the sys\_trigger record.

The Scheduled Job remains in the sys\_trigger table until the timer duration is completed. The duration of the timer activity depends on the duration set on the timer itself, based on user configuration.

Once the duration is completed, the Scheduled Job runs and sends an event back to the Workflow to notify it, and the Workflow continues to run the next activity in line.

# Impact of the Workflow Timer

* * *

The Scheduled Job for the timer is run by a system user, and as all Scheduled Jobs, they are run in the background. 

This means that every script execution _after_ implementing a workflow timer is run by system user and is also run in the background on the system scheduler. This allows Business Rules, Script-Includes and Workflow Scripts to run asynchronously, which allows for better system performance.

Also, having a timer activity in the workflow allows the system to stop and commit changes to the database after the last activity. By design, the Workflow Engine only commits changes in the database for the current object held in memory.
