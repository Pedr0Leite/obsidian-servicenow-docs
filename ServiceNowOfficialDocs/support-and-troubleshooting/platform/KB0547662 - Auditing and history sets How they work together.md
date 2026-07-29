---
title: "Auditing and history sets | How they work together"
aliases:
  - KB0547662
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0547662
kb_number: KB0547662
last_modified: 2026-04-23
---

## Auditing and history sets | How they work together

  

### Issue

This article discusses the \[sys\_audit\], \[sys\_history\_set\], and \[sys\_history\_line\] tables and how are they related.

### Sys\_audit and sys\_history\_line tables

These tables are queried whenever a form on a table (like _incident_) has a section that needs to check all historical changes (like _Activity_).

The \[sys\_history\_set\] and \[sys\_history\_line\] tables come from the History Sets plugin (com.glide.history\_set). Their purpose is to view a record's audit, email, and relationship data in a table format (see: [History Sets](https://docs.servicenow.com/csh?topicname=c_HistorySets.html&version=latest "History Sets") for more information).

A History Set is a record in the \[sys\_history\_set\] table. It contains a list of \[sys\_history\_line\] records that are built from the \[sys\_audit\] records. History Set records are generated when a record is opened that contains an Activity Formatter. This shows the history of the record. There is typically only one History Set record generated per record (although multiple can be seen for different time zones). This history set generates \[sys\_history\_line\] records for all of the corresponding \[sys\_audit\] records.

The Audit \[sys\_audit\] and History Sets capture the same data, but data is managed differently. The major difference between them is persistence:

-   The **Audit table** \[sys\_audit\] records persist forever.
-   The **History Set** \[sys\_history\_set\] records are generated on use and are removed by the table cleaner 30 days after their most recent use.
-   The **History Set Line** \[sys\_history\_line\] records are on four tables that are managed using Table Rotation, which is customizable. From the base system, the tables are rotated on a seven-day basis, meaning that the records are dropped 28 days after generation unless they are requested again.

Based on the above, when you observe that loading some records (case, incident, etc.) is slow but other records in the same table are fast, you may need to check the history from sys\_audit (for example, when an incident has not been viewed for over a month). Looking in the system logs, you can see slow queries to sys\_audit with a UNION ALL statement, or from history sets (when the incident has been viewed _last_ in less than a month). It also depends on how old the incident is and how much data is in the history. More data causes a slower load. This example does not take into account other factors that can contribute to slowness (client scripts, business rules, UI policies, etc.). The focus is solely on historical changes.

### Workflow

Open a record form (Incident, Change, etc.):

-   Does this record have an existing history set?  
    -   **Yes**: Has anything changed to the history of the record since this history set was built?  
        -   **Yes**: The system will query the records from \[sys\_history\_line\] corresponding to the history set record as well as all \[sys\_audit\] information between the day the record was opened and the current time.
        -   **No**: Query only the \[sys\_history\_line\] data for that history set.
    -   **No**: Build the history set by querying all of \[sys\_audit\] for records between the open date and the current date
