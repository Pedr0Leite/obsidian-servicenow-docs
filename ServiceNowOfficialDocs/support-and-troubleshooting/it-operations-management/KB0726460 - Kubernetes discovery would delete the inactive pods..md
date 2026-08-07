---
title: "Kubernetes discovery would delete the inactive pods."
aliases:
  - KB0726460
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0726460
kb_number: KB0726460
last_modified: 2024-04-07
---

## Issue

# Description

* * *

Kubernetes discovery would delete **kubernetes pods(cmdb\_ci\_kubernetes\_pod)** that have been removed instead of marking them as stale.

Instead of deleting the pods we can mark them as stale with the below steps.

# Procedure

* * *

-   Go to: sa\_pattern.list.
-   Filter by name kubernetes.
-   Change the Deletion strategy of CI type: cmdb\_ci\_kubernetes\_pod from "Delete" to "Mark as Absent".
-   Save and update the kubernetes pattern.
-   Open the updated pattern from sa\_pattern.LIST and under the related links click 'Synchronize with MID servers'.
-   Re-run discovery and the POD's are marked as absent and not being deleted![]("sys_attachment.do?sys_id=9d5696fedbab67c0f\</li).

![](sys_attachment.do?sys_id=dabeb4a2db0ab450e515c2230596198f)

# Applicable Versions

* * *

Starting from Jakarta Patch 9
