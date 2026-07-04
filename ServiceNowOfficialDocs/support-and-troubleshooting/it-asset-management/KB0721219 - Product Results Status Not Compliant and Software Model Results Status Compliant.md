---
title: "Product Results Status \"Not Compliant\" and Software Model Results Status \"Compliant\""
aliases:
  - KB0721219
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0721219
kb_number: KB0721219
last_modified: 2024-04-07
---

## Issue

# Overview

* * *

This KB article is to determine why the Product Results status is "Not Compliant" while its related Software Model Results shows "Compliant" and there's no "Unlicensed Installs" listed.

# Product Results Status "Not Compliant" and Software Model Results Status "Compliant"

* * *

After Reconciliation runs, a Reconciliation Result will be created where a related Product Results is also created.

If the status of the "Product Results" is displayed as "Not Compliant", usually this is due to:

1.  Software Model Results status is "Not Compliant", or
2.  There are "Unlicensed Installs" found in the related list of the Product Result

If the Software Model Results status is "Compliant" and the "Unlicensed Installs" is empty, check the "Latest" checkbox of the "Product Result" record.

1.  If the "Latest" checkbox is "unchecked", that means it is NOT the latest Product Results that runs and this is the reason why the "Unlicensed Installs" is empty.
2.  Next, is to navigate to the "Software Asset > Reconciliation > Product Results" and filter with Publisher <PUBLISHER> and Product <PRODUCT>.
3.  This is to check the latest Product Result for the said Publisher and Product.
4.  Open the latest Product Result record, noticed that the "Latest" checkbox is checked.
5.  Check the "Software Model Results" status, if (Compliant or Not Compliant).
6.  Check the "Unlicensed Installs" related list, if it is not empty, the Product Result status is "Not Compliant".
