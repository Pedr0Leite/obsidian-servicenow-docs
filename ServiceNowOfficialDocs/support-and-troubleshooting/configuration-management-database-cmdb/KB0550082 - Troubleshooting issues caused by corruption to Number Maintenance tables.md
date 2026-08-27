---
title: "Troubleshooting issues caused by corruption to Number Maintenance tables"
aliases:
  - KB0550082
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0550082
kb_number: KB0550082
last_modified: 2026-02-24
---

## Issue

There are two primary flavours of symptoms for this issue. The reason the symptoms will look different is that some customers have made a unique index at the Database level on the number column for the target table (for example, task.number). If a unique index is created on the target table then the result is a failed operation. The standard system does not have a unique index on the number field and in that case the symptom will be duplicate numbers. There may be other cases if a custom business rule has been created to avoid duplicate numbers (see the Workaround in [KB0522835](/kb_view.do?sys_kb_id=5c7faf627b0d01c0d4b5c5ee4a4d4d89 "KB0522835")).

**Note**: Creating a unique index on the task.number field is not a base system setting, but many customers have done this and it is described in the ServiceNow documentation to enforce unique numbering at the database level.

For more information, see [Enforcing Unique Numbering.](https://docs.servicenow.com/search?q=enforce+unique+number&labels=2 "Enforcing Unique Numbering.").

The most easily recognisable symptoms are either one of the following:

-   **Duplicate record numbers** start to appear in the Incident table (or another commonly used task table like change\_request)  
    OR
-   **Updating or creating records will fail** and a Database error similar to the following appears:  
      
    Unique Key violation detected by database (Duplicate entry 'INCxxxxx' for key 'task\_xx')

Although the most recognisable symptoms affect the task tables, Number Maintenance controls the unique identifiers for many tables in the system including, Email Watermarks, Warranties, Metic Definitions, Update Set Collision Maps, and more. Because so many tables have dependencies on Number Maintenance, this can cause many different symptoms.

You may not be able to identify and address all the collateral damage that is introduced when this table becomes corrupt. We recommend fixing the underlying corruption to the sys\_number\_counter table first and then looking for obvious collateral damage. After that, manage user issues as they occur. You can, of course, engage ServiceNow [Customer Support](http://www.servicenow.com/support/contact-support.html "Customer Support") for assistance with clean up issues or to ask questions. Here are examples of other symptoms:

-   Many of the workflows that are active during the affected time can break. When a workflow activity tries to create tasks, it fails catastrophically on the insert due to duplicate violation on the database. There is nothing that fixes these workflows automatically. Admins need to "push" them through.
-   Approval made via email does not process. This can be due to duplicate outbound email watermark values.
-   Updates to incidents made using email are not made on the corresponding incident, but the updates are placed into a different incident. (This is also due to outbound email watermark confusion.)

The extent of your symptoms is confined to the extent of the corruption that was introduced. If the only thing that was changed was the value of a single sys\_number\_counter record (for example, the numbers for one table) then no clean up may be necessary. Consider the following questions when addressing cleanup:

-   How often are new records created in this table?
-   If your number table is not enforced on the database, how long were duplicates being created?
-   If your number table is enforced on the database, how long were duplicate key violations being seen?
-   Are there automations that create records in this table? (for example, emails, workflows, scheduled import sets, web services)
-   Does the creation of duplicates or failure to insert records into this table cause logical problems with other tables and features?

## Resolution

#### To set the sys\_number/sys\_number\_counter table back to what it should be

Set the values in the Number Maintenance table to n+1 of the maximum number in affected tables.

For example, for the error "Unique Key violation detected by database (Duplicate entry 'INC123456' for key 'task\_xx')"

1.  Get the maximum INC number in the Incident table. Suppose it is INC1 23456.
2.  Locate the record for the Incident table in [https://<instancename>.service-now.com/sys\_number\_counter\_list.do](https://\<instancename\>.service-now.com/sys_number_counter_list.do).
3.  If the number is set to 123456 or a lower number, you may change to 123457, since INC123457 is greater than the current maximum INC number, INC123456.

#### To re-number duplicate record numbers

For an example of how to address this operation see the KB article, ["Renumbering auto-incremented custom tables" - KB0538764.](/kb_view.do?sysparm_article=KB0538764 "\"Renumbering auto-incremented custom tables\" - KB0538764.") Do not assume that any article will address your particular needs without thorough testing and verification on a sub-production instance.

#### To address fallout (i.e. secondary symptoms)

As stated above there are many types of secondary symptoms that may occur when the sys\_number\_counter table is set to the wrong value (e.g. misdirected emails, broken workflows, missed approvals). It is not possible to address all the failure modes in this one article.
