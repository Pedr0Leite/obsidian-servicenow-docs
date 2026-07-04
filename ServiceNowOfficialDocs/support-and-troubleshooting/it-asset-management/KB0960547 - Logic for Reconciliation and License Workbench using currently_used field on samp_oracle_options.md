---
title: "Logic for Reconciliation and License Workbench using currently_used field on samp_oracle_options"
aliases:
  - KB0960547
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0960547
kb_number: KB0960547
last_modified: 2025-03-19
---

## Logic for Reconciliation and License Workbench using currently\_used field on samp\_oracle\_options

  

### Summary

When reconciliation runs, samp\_oracle\_options is counted only when the below conditions match:

1.  currently\_used field must be in either in use, or empty (when empty, it's considered as in use).
2.  Software model is not empty.
3.  Licensable true.
4.  samp\_oracle\_options must be for an Oracle instance that runs on a physical server (Is Virtual: false)

or on a virtual server (Is Virtual: true), and the virtual server has a Virtualized by relation to a physical server.

If the virtual server doesn't have such relation, then that samp\_oracle\_options is not counted.

\---

The entitlement created should have Metric Group: Oracle and a valid License metric with Database option.

On License Workbench, it will show as License metric +  Database option, e.g. "Per Processor Label Security"

\---

On License Workbench, the Rights Consumed logic is below:

-   find samp\_oracle\_options that should be counted (explained above)
-   find related physical servers, Rights Consumed for each physical server = CPU core count \* CPU count \* (Process name.Core factor mapping.Oracle core factor)
-   sum up above

### Related Links

Refer to below doc for more information:

[**Software license usage**](https://docs.servicenow.com/bundle/quebec-it-asset-management/page/product/software-asset-management2/concept/sam-license-workbench.html "Software license usage")
