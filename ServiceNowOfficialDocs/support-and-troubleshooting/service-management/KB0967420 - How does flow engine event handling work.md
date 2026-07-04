---
title: "How does flow engine event handling work?"
aliases:
  - KB0967420
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0967420
kb_number: KB0967420
last_modified: 2025-12-17
---

## Text

-   What are flow engine event handlers?  
    -   Flow Engine Event Handler (FEEH) jobs in sys\_trigger process asynchronous (flows triggered in the background) flow events
    -   By default there are (number of scheduled worker threads)/2 which is typically 4 per node (3 Flow Engine Event Handlers + 1 Flow Engine Interactive Event Handlers)
    -   There isn't a one size fits as to how many FEEH are needed as it depends on flow designer usage
-   Which nodes do FEEH run on?
    -   Starting in Utah, FEEH jobs are created on PRIMARY NODES.  PLEASE NOTE:
        -   PRIMARY NODES includes GENERIC, WORKER, and UI nodes, but not \*.Standby (or passive) nodes
        -   FEEH on UI nodes will process flows started on UI nodes.  UI nodes will not process any flow events from the general queue (that is a flow event that was triggered on a different node or a flow that wakes up from a Wait for Duration)
