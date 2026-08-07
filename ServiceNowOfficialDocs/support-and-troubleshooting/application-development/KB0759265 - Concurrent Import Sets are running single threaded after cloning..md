---
title: "Concurrent Import Sets are running single threaded after cloning."
aliases:
  - KB0759265
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0759265
kb_number: KB0759265
last_modified: 2024-04-07
---

## Concurrent Import Sets are running single threaded after cloning.

  

### Issue

Trying to use Concurrent Import Sets for data loads, but the system only created a single import set, and it's not using concurrent processing.

List the sys\_concurrent\_import\_set\_job table, and there are no CISETs for the concurrent job.

Display the sys\_trigger using this condition: Name is  Import Set Transformer AND Parent is empty.  The System ID column is empty.

### Release

Madrid and above.

### Cause

The clone does not copy the \[sys\_trigger.parent\] values correctly to the target instance.

### Resolution

List sys\_trigger using this condition: Name is  Import Set Transformer AND Parent is empty. 

Set System ID to ACTIVE NODES on the rows where Parent is empty.

Run the concurrent import again to make sure it's fixed.
