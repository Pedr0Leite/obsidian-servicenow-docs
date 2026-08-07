---
title: Logging, auditing, and errors \(instance security hardening\)
description: Apply a logging and auditing strategy so that you can identify and act on suspicious activity in a timely manner.
locale: en-US
canonical_url: https://www.servicenow.com/docs/r/platform-security/logging-auditing-errors-instance-security-hardening.html
release: australia
topic_type: reference
last_updated: "2026-03-12"
reading_time_minutes: 1
breadcrumb: [Logs, Platform Security]
tags:
  - platform-security
  - type-reference
---

# Logging, auditing, and errors \(instance security hardening\)

Apply a logging and [[c_AuditedTables|auditing]] strategy so that you can identify and act on suspicious activity in a timely manner.

To learn more about what can be logged in the instance, see [[system-logs|System logs]]. Ensure that there is a schedule for monitoring system events such as logins and failed logins by using **System Logs** &gt; **Events**.

-   **[[disabling-sql-error-messages|Disabling SQL error messages \(instance security hardening\)]]**  
Use the **glide.db.loguser** property to [[sc-disabling-sql-error-messages|disable SQL error messages]] from rendering in a browser.

**Parent Topic:**[[logs|Logs]]

## Related

- [[system-logs|System logs]]
- [[disabling-sql-error-messages|Disabling SQL error messages \(instance security hardening\)]]
- [[logs|Logs]]
- [[c_AuditedTables|Auditing]]
- [[sc-disabling-sql-error-messages|Disable SQL error messages]]
