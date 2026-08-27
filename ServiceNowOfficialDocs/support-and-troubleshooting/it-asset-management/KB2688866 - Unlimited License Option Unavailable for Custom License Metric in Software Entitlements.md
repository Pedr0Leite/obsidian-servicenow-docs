---
title: "Unlimited License Option Unavailable for Custom License Metric in Software Entitlements"
aliases:
  - KB2688866
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB2688866
kb_number: KB2688866
last_modified: 2026-05-15
---

## Unlimited License Option Unavailable for Custom License Metric in Software Entitlements

  

### Issue

The Unlimited License option is not available when using a custom license metric in the Software Entitlements table. Attempting to create an entitlement with a custom license metric results in an error message, even after modifying the UI policy.  
  

### Release

All supported releases

### Cause

The platform's reconciliation engine supports unlimited license functionality only for specific, default license metrics. Custom license metrics do not currently have the capability to handle unlimited licenses. Modifying the UI policy does not resolve this limitation, as the underlying platform functionality does not support this configuration for custom metrics.  
  

### Resolution

To work around this limitation, set the Purchased Rights field to a sufficiently high number on the entitlement record:

1.  Navigate to Software Asset > Entitlements and open the relevant entitlement record.
2.  In the Purchased Rights field, enter a high value that exceeds the expected license consumption in your environment.
3.  Select Update to save the record.

This allows the reconciliation engine to process the entitlement without triggering a compliance violation.

Note: This is a workaround, not a permanent resolution. The platform does not currently support unlimited license functionality for custom license metrics.

* * *

Enhancement Request

To request support for custom license metrics with unlimited license functionality in a future release, submit an Enhancement Request via the [ServiceNow Idea Portal](https://community.servicenow.com/community?id=ideas_list&sysparm_module_id=enhancement_requests).
