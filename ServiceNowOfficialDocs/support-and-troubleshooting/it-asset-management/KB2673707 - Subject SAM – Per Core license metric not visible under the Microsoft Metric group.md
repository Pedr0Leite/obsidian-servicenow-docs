---
title: "Subject: SAM – \"Per Core\" license metric not visible under the Microsoft Metric group "
aliases:
  - KB2673707
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB2673707
kb_number: KB2673707
last_modified: 2025-12-10
---

## Issue

"Per Core license metric not visible under the Microsoft Metric group 

## Resolution

OOTB, the Metric group must be present for the Per core license metric to be available. If it is missing, you’ll need to import the OOB XML file to restore the choice:

`samp_sw_license_metric_ef64c370534323005d74ddeeff7b1238.xml`

Steps to fix:

Navigate to the samp\_sw\_license\_metric table.

Import XML from OOB or working instance and upload the attached XML file.

After the import completes, the issue will be resolved and the missing Per core choice will be restored.
