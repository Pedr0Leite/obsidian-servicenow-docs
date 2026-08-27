---
title: "Lifecycle Events Logging - Zurich Release"
aliases:
  - KB2588126
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB2588126
kb_number: KB2588126
last_modified: 2026-03-19
---

## Lifecycle Events Logging - Zurich Release

  

### Summary

### Overview

The Zurich release introduces enhanced Lifecycle Events (LE) logging capabilities designed to improve root cause analysis, reduce support dependency, and empower administrators with deeper visibility into LE Cases execution and failures. This feature is part of the HRSD Lifecycle Events module and is available to users with the _sn\_hr\_le.admin_ role.

* * *

### Key Capabilities

#### **1\. Execution Logging**

Admins can now view execution logs directly within LE Cases by selecting **Show execution logs** from the Related Links section. This applies to both Workflows and Flow Designer executions.

#### ![](/sys_attachment.do?sys_id=7438161493337214f538fb2d6cba10fa "UI action.png")

#### **2\. Log Levels**

Logging supports four cascading levels:

-   None – No logs captured.
-   Error – Only error logs.
-   Info _(default)_ – Captures both informational and error logs.
-   Debug – Full trace logs for deep diagnostics.

The logging level is driven by System Property **sn\_hr\_le.log\_level** (/sys\_properties.do?sys\_id=9b46aa07ff03121007edfffffffffff8)

#### **3\. Log Content**

Each log entry includes:

-   Message
-   Source identifiers
-   Activity sets contexts and Activities
-   Timestamps

![](/sys_attachment.do?sys_id=2038161493337214f538fb2d6cba10f4 "LE Logs.png")

* * *

### Use Cases

-   Troubleshooting Failures: Identify exactly where and why an LE Case failed, including cases where workflows exceed execution limits, or Activities/Activity Sets haven't triggered due to Audience criteria not being met.
-   Self-Service Enablement: Customers (LE Admins) can now diagnose issues independently, reducing the need to contact ServiceNow Support.
-   Audit and Compliance: Logs provide a traceable history of LE execution, supporting governance and audit requirements.

* * *

### Activation, Access & Retention

-   Availability: Lifecycle Events logging has been introduced in the Zurich release
-   Access Control: Only users with the **_sn\_hr\_le.admin_** role can view execution logs.
-   Logs location: Logs are stored in the HR Lifecycle Events Case Logs table \[**sn\_hr\_le\_case\_log**\] and can be accessed via the LE Case form (from the **Show execution logs** Related Link).
-   Retention: Logs for any specific LE Case are deleted when the case is inactive and hasn't been updated in 30 days. The Table Cleaner "sn\_hr\_le\_case\_log" (sys\_auto\_flush.do?sys\_id=7a017ae2ff93121007edfffffffffffa) is responsible for this.

For more details, refer to the [Lifecycle Events logging](https://www.servicenow.com/docs/csh?topicname=le-logging.html&version=latest "Lifecycle Events logging") product documentation page.

### Related Links

[Lifecycle Events logging](https://www.servicenow.com/docs/csh?topicname=le-logging.html&version=latest "Lifecycle Events logging")
