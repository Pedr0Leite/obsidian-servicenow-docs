---
title: "Reconciliation Error: \"Cannot read property \"max_install_per_right\" from undefined\""
aliases:
  - KB1032467
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB1032467
kb_number: KB1032467
last_modified: 2025-01-04
---

## Issue

After running software reconciliation, it failed but shows 100%

Note: It is better to isolate the issue from a specific publisher.

## Resolution

Note:

If after checking the syslogs table and finding no related issues, please check the "samp\_recon\_progress\_summary" and use the "Reconciliation Results" number as "Reconciliation result".

1\. Check on the Software Entitlements related to the Software Publisher.

2\. Check for the License Metric "Per Application Instance".

3\. Change the license metric to something else in a Software Entitlement.

4\. Save.

5\. Then change it back to the correct license metric "Per Application Instance"

6\. Save.  
  
This should create a Metric Attribute in the Software Model record - related lists.
