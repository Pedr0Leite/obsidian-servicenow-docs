---
title: "There is a time difference between the time reported in the list view and the flow execution details"
aliases:
  - KB0855275
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0855275
kb_number: KB0855275
last_modified: 2025-01-02
---

## There is a time difference between the time reported in the list view and the flow execution details

  

### Summary

There is a time difference between the time reported in the list view and the flow execution details. It's a timezone difference, the list view looks at the user's timezone settings (System Settings -> General -> Timezone) whereas the Execution Details screen uses UTC. It's the expected behaviour. You can match the user's timezone to UTC temporarily if this causes confusion.
