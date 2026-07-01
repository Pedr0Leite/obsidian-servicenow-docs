---
title: System logs
description: The System Logs module provides a variety of logs that you can use to troubleshoot and debug transactions and events that take place within the instance.
locale: en-US
canonical_url: https://www.servicenow.com/docs/r/platform-security/system-logs.html
release: australia
topic_type: concept
last_updated: "2026-03-12"
reading_time_minutes: 1
breadcrumb: [Logs, Platform Security]
---

# System logs

The System Logs module provides a variety of [[logs|logs]] that you can use to troubleshoot and debug transactions and events that take place within the instance.

Access the following logs from the System Logs module:

|Log|Description|
|---|-----------|
|[[r_TransactionLogs|Transactions]]|All application activity for an instance.|
|[[r_EmailLogs|Email]] and [[push-log|Push]]|All [[email|email]] notifications and Push messages sent from all instances within the system.|
|[Event Logs](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/platform-administration/event-logs-2.md)|All system events that occur within the system.|
|[[r_ImportLogs|Import]]|Data import activity within the platform.|
|Table Changes|Changes made to all tables in the system.|
|[Outbound web services logging](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/api-reference/web-services/outbound-request-logging.md)|All outbound web services requests such as REST and SOAP requests.|
|[[r_SystemLogs|System]]|Warnings and errors for instance processes, records, and non-critical events, such as memory usage on the server machine.|

Use the [[r_LogUtilities|Log File Browser]] to search and download logs. You can also search archived logs in the [[r_LogHistory|log history]].

## Other logs

Your instance offers other logs in addition to those in the System Logs module. For example, the [[c_SystemDiagnosticsApplication|System Diagnostics module]] provides upgrade history and slow query logs, which you can use to gain insight into how queries are affecting platform performance. The [[r_CustomerUpdatesTable|Customer Updates table]] records every change that is made in the system.

## Related

- [[r_TransactionLogs|Transaction logs]]
- [[r_EmailLogs|System email log and mailboxes]]
- [[push-log|Push logs]]
- [[r_ImportLogs|Import logs]]
- [[r_SystemLogs|System log]]
- [[r_LogUtilities|Use the log file browser]]
- [[r_LogHistory|Log history]]
- [[c_SystemDiagnosticsApplication|System Diagnostics module]]
- [[r_CustomerUpdatesTable|Customer Updates table]]
- [[logs|Logs]]
- [[email|Email]]
