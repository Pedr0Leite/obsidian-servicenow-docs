---
title: "Incident 'Business duration' and 'Business resolve time' do not account for holidays"
aliases:
  - KB0870044
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0870044
kb_number: KB0870044
last_modified: 2023-12-09
---

## Incident 'Business duration' and 'Business resolve time' do not account for holidays

  

### Issue

A user noted that in several examples within their instance, incident fields Business duration and Business resolve time were not accounting for calendar holidays. They wanted to know why this was.

### Cause

It was found that the method which should accomplish this, the "calcDateDiff" method, has been deprecated, and is [no longer supported](https://developer.servicenow.com/dev.do#!/reference/api/paris/server_legacy/c_GlideSystemAPI#r_GS-calDateDiff_S_S_B "no longer supported").

### Resolution

As shared above, the previously used method is now deprecated and is no longer supported.

However, there is [documentation](https://docs.servicenow.com/bundle/paris-application-development/page/script/useful-scripts/concept/c_UsefulSchedulingScripts.html "documentation") on how to ensure that incident Business timings consider and honor Schedules and their related holiday entries.

This information can be found in the documentation under the "**Calculate duration given a schedule**" header.
