---
title: Record numbering
description: In the base system, several tables are numbered, including Incident, Problem, Change Request, and Knowledge. You can also use these numbers anywhere that script is present, for example to generate watermarks for emails. Records in tables can be numbered automatically.
locale: en-US
canonical_url: https://www.servicenow.com/docs/r/platform-administration/c\_ManagingRecordNumbering.html
release: australia
topic_type: concept
last_updated: "2026-03-12"
reading_time_minutes: 1
breadcrumb: [Customize, Field administration, Forms, fields, and lists, Configure core features, Administer the ServiceNow AI Platform]
---

# Record numbering

In the base system, several tables are numbered, including Incident, Problem, Change Request, and Knowledge. You can also use these numbers anywhere that script is present, for example to generate watermarks for emails. Records in tables can be numbered automatically.

Administrators can manage record numbering by navigating to **System Definition** &gt; **Number Maintenance**. The current number format for a table, including the prefix \(such as **INC** for incidents or **CHG** for changes\), is stored in a record on the Number \[sys\_number\] table.

\[Omitted image "Number1.png"\] Alt text: A sample of number records, organized alphabetically by prefix.

You can renumber auto-incremented tables that extend the task table or manage numbering with a database field named **Number this field**.

**Note:** If you reset numbering in Number Maintenance, it only renumbers new records. It leaves the numbering as-is for existing records in system tables.

-   **[[t_AutoNumberingRecordsInATable|Add auto-numbering records in a table]]**  
You can define one number format per table in the system.
-   **[[t_PrepToLeftPadNumFldsInCustmTbls|Prepare to left-pad number fields in custom tables]]**  
Before you configure left padding of number fields on a custom table or a table that does not extend the task table, you must prepare business rules and script includes.
-   **[[t_PreventNumberingGaps|Prevent numbering gaps]]**  
By default, numbers are generated every time a new record is created.
-   **[[c_EnforcingUniqueNumbering|Enforcing unique numbering]]**  
Although duplicate numbers are rare, numbering does not enforce uniqueness, by default.

**Parent Topic:**[[customize-fields-now-platform-landing|Customizing fields on the ServiceNow AI Platform]]

## Related

- [[t_AutoNumberingRecordsInATable|Add auto-numbering records in a table]]
- [[t_PrepToLeftPadNumFldsInCustmTbls|Prepare to left-pad number fields in custom tables]]
- [[t_PreventNumberingGaps|Prevent numbering gaps]]
- [[c_EnforcingUniqueNumbering|Enforcing unique numbering]]
- [[customize-fields-now-platform-landing|Customizing fields on the ServiceNow AI Platform]]
