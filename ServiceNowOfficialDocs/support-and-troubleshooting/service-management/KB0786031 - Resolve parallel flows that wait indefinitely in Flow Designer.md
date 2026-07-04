---
title: "Resolve parallel flows that wait indefinitely in Flow Designer"
aliases:
  - KB0786031
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0786031
kb_number: KB0786031
last_modified: 2025-08-26
---

## Resolve parallel flows that wait indefinitely in Flow Designer

  

### Issue

Parallel flows in Flow Designer continue waiting indefinitely even after one branch completes the run. 

### Release

Any supported release

### Cause

Missing End actions cause parallel branches to continue waiting for other branches to complete, even when their own logic has finished.

### Resolution

To resolve indefinite waiting in parallel flows:

1.  Go to Flow Designer and open the affected flow.
2.  Verify that each branch in the parallel flow has an End action defined.
3.  Add End actions to any branches that are missing them.

  
  

### Related Links

For more information, see the product documentation, [Workflow Studio flow logic](https://www.servicenow.com/docs/bundle/zurich-build-workflows/page/administer/flow-designer/concept/flow-logic.html)
