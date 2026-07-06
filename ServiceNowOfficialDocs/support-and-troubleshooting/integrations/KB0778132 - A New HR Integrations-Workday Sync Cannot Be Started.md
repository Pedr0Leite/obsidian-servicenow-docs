---
title: "A New HR Integrations-Workday Sync Cannot Be Started"
aliases:
  - KB0778132
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0778132
kb_number: KB0778132
last_modified: 2025-09-03
---

## Issue

HR Integrations Job Trackers shows and old job that is still in State = Running. When trying to run a new synch it does not run.

## Resolution

If the running job is not actually running and is just "stuck" in State = Running delete the job from the HR Integrations Job Trackers (table = sn\_hr\_integrations\_job\_tracker) and then run a new synch.
