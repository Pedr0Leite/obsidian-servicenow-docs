---
title: "Can we run a loop for 3 times in Flow Designer?"
aliases:
  - KB0817612
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0817612
kb_number: KB0817612
last_modified: 2024-04-08
---

## Can we run a loop for 3 times in Flow Designer?

  

### Issue

-   There's a flow designer where I want to run a loop for three times and for that I have used "Do the following until" flow logic and I have created a iteration flag before this loop, now I want when this flag count will be 3 then this loop will end, Now at node this flag is getting updated by one only once, In 2nd execution its not updating the updated flag value so this loop is not getting end. Is there any way I can achieve this or I can fetch the execution count? 

### Release

-   NY Patch 4 HF 1a

### Cause

-   This isn't currently possible in flow designer without doing a database operation.

### Resolution

-   We're working on a feature for flow variables (similar to the workflow scratchpad) which would allow you to do what you're trying to do.
