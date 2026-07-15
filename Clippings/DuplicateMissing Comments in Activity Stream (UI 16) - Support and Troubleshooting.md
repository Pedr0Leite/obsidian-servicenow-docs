---
title: "Duplicate/Missing Comments in Activity Stream (UI 16) - Support and Troubleshooting"
source: "https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB2122007"
author:
published:
created: 2026-07-14
description: "This knowledge article explains how customers can be affected by various kinds of issues with comments on the activity stream in UI 16. How Do Comments Appear in the Activity Stream? Whenever a comment"
tags:
  - "clippings"
---
### Issue

This knowledge article explains how customers can be affected by various kinds of issues with comments on the activity stream in UI 16.

**How Do Comments Appear in the Activity Stream?**  
  
Whenever a comment or work note is added to a record (e.g., an incident), and the corresponding table is configured for auditing (such as the Incident table), the update is logged in the `sys_audit` table. This results in the creation of a record for the relevant field (e.g., `comments`). Similarly, a record is also created in the `sys_journal_field` table.

However, the activity stream does not interact directly with the `sys_audit` or `sys_journal_field` tables. Instead, it renders data from the associated `sys_history_set` record.

The `sys_history_set` is generated or updated on demand when a change is made to the parent record (such as an incident). It references the parent record and acts as a container for the historical changes. All the associated history entries are created in the `sys_history_line` table, which holds a reference to its corresponding `sys_history_set`.

The `sys_history_line` records are created whenever the `sys_history_set` is triggered by the activity stream. These are generated in real-time by retrieving data from:

- `sys_audit`
- `sys_journal_field`
- `sys_email`

### When Is a Customer Not Affected by the Duplicate Comments Issue?

There are situations where the same comment appears twice in the activity stream, but with different update times. In such cases, the duplication is intentional or expected, as there are multiple records for the same comment in both the `sys_audit` and `sys_journal_field` tables.

This can happen due to:

- A user accidentally posts the same comment twice.
- Scripts, business rules, or background processes unintentionally duplicate comments.

**  
Common Cause: Business Rule-Induced Duplicates**

A frequent root cause of such unintentional duplicates is business rules (BRs), particularly when GlideRecord update calls are used. These can create looping or recursive behaviours that result in the same comment being posted multiple times.

Example: Recursive BR Loop Between `sc_task` and `sc_req_item`

1. A comment is added to a `sc_task` record.
2. An "After" Business Rule (`sc_task_br1`) on the `sc_task` table copies the latest comment to the related `sc_req_item`.
3. Another Business Rule on the `sc_req_item` table performs a GlideRecord update on the related `sc_task`.
4. This update re-triggers `sc_task_br1`, resulting in the same comment being copied twice to the `sc_req_item`.

This is one of the reasons why Business rules shouldn't have update calls in them, best practices to use business rules are mentioned here: [https://support.servicenow.com/kb?id=kb\_article\_view&sysparm\_article=KB0715782](https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0715782)  

### When Does the Duplicate Comments Issue Occur?

The duplicate comments issue arises when only a single journal entry (such as a comment or work note) exists in both the `sys_audit` and `sys_journal_field` tables, but the same comment appears twice in the activity stream. This typically happens when the same comment is loaded twice into the corresponding `sys_history_set` record.

One key indicator of this issue is the timestamp of the duplicated comments. If both entries in the activity stream have identical update times, it suggests that the system might be affected by this duplication issue.  
  
Additional use cases and troubleshooting steps are outlined later in the KB article, guiding how to identify and handle these scenarios.

**When is the customer affected by missing comments problem?  
  
**Some comments are missing from the activity stream, even though they exist in the `sys_audit` and `sys_journal_field` tables.

### Facts

Before **Washington Patch 6**, all the updates were mostly loaded from the sys\_audit table itself and sys\_journal\_field table was only to load comments that are made during the creation of the parent records, but that lead to some missing entries because there can be some scripts that restricts the auditing of the records by setting the workflow to false, and the corresponding work notes added in such cases will not be recorded in the sys\_audit table, but they will only come under sys\_journal\_field table. So it became essential to refer to sys\_journal\_field as well so that none of the updates are missed.  
  
Now with such a change, the history set loader flow was modified and for journal fields, the system started fetching data from both sources i.e. sys\_audit and sys\_journal\_field tables and compared them. If the entries differed, both were added to the "sys\_history\_line" table. However, discrepancies in journal field records between "sys\_audit" and "sys\_journal\_field" led to duplication of comments. Thats how duplicate comments started appearing after WP6.

### Release

**[PRB1767585](https://support.servicenow.com/nav_to.do?uri=problem.do?sys_id=cfa14d399316ce18666cb66d6cba1066) (Washington Patch 6, Xanadu)**  
  
It was with release of PRB1767585, when the "HistorySetLoader" flow was updated to address concerns about the duplication of work notes. As part of this change, the property "glide.history\_set.pull\_journal\_entries\_from\_journal\_table" was introduced.

1\. History Sets are formed by pulling data from the "sys\_audit", "sys\_journal\_field" and "sys\_email" tables:

- "sys\_audit": Stores historical data for all record fields.
- "sys\_journal\_field": Contains user-added comments and work notes.
- "sys\_email": Contains emails triggered by the record.

2\. Pre-PRB1767585 Behavior:

Before PRB1767585, the system populated the "sys\_history\_set" and "sys\_history\_line" tables by fetching data from both the "sys\_audit" and "sys\_journal\_field" tables. For journal fields, the system fetched data from both sources and compared them. If the entries differed, both were added to the "sys\_history\_line" table. However, discrepancies in journal field records between "sys\_audit" and "sys\_journal\_field" led to duplication.

3\. Introduction of the Property:

To mitigate duplication, the "glide.history\_set.pull\_journal\_entries\_from\_journal\_table" property was introduced. When enabled, journal field data is sourced exclusively from the "sys\_journal\_field" table, eliminating the comparison with "sys\_audit".

4\. Post-PRB1767585 Observations:

Despite the property addressing many duplication issues, some edge cases were discovered that still led to duplicate comments.

PRB1806563

  
**[PRB1806563](https://support.servicenow.com/nav_to.do?uri=problem.do?sys_id=2240afb947305654adc09959126d4364) (Washington Patch 9, Xanadu Patch 4, Yokohama)  
  
**In this PRB, when the property `glide.history_set.pull_journal_entries_from_journal_table` is enabled, certain conditions were observed that could lead to duplicate comments appearing in the activity stream. One such scenario is described below:  
  
1\. A user adds a comment to an incident. This results in the creation of related records:

`sys_updated_on` of the incident: `2025-01-01 00:00:00`

`sys_created_on` of the sys\_audit record: `2025-01-01 00:00:00`

`sys_created_on` of the sys\_journal\_field record: `2025-01-01 00:00:01`

  
2\. Pre-PRB1806563:

The system determined the last recorded timestamp using the `sys_audit` table.

If no suitable entry was found in `sys_audit`, it defaulted to using the incident’s `sys_updated_on` timestamp (`2025-01-01 00:00:00`).

  
3\. When the history set is updated after first comment, it pulls the journal entry from the `sys_journal_field` table. However, the system sets the last recorded timestamp as `2025-01-01 00:00:00` (based on `sys_audit` or `sys_updated_on`).  
4\. When the user posts another comment: Because the last recorded time is still `2025-01-01 00:00:00`, the system mistakenly includes the previous comment again. This results in a duplicate entry in the `sys_history_set` (via `sys_history_line`), and the same comment appears twice in the activity stream.  
  
5\. Post-PRB1806563:  
  
The system now uses the `sys_created_on` timestamp of the `sys_journal_field` record as the last recorded time.  
In this case, it would correctly set the last recorded timestamp to `2025-01-01 00:00:01`, preventing the previous comment from being reloaded.  
This effectively avoids duplication in the activity stream.  
  
**[PRB1826101](https://support.servicenow.com/problem.do?sys_id=f6ea480b93b952140491b4886cba109b) (Washington Patch 10, Xanadu Patch 5, Yokohama)  
**  

While journal field data is stored in both the `sys_audit` and `sys_journal_field` tables, certain metadata—specifically the update count and internal checkpoint at which the comment was added—is available only in the `sys_audit` table.

When the property `glide.history_set.pull_journal_entries_from_journal_table` is enabled, the system generates `sys_history_line` records for journal fields exclusively from the `sys_journal_field` table. This causes the update count to default to 0 for all such records, since this data is not sourced from `sys_audit`.

This behaviour introduces several downstream problems:

1\. Calendar Behavior  
The calendar feature groups history entries into batches based on their update count. Since all journal entries now have an update count of 0, they get grouped into a single batch, anchored to the `sys_created_on` timestamp of the parent record.

2\. APIs in `HistoryWalker.java`  
The `HistoryWalker` component replays the history of a record using data from the `sys_history_line` table.  
These APIs rely on the update count to reconstruct changes accurately. With all journal fields defaulting to 0, replay logic is compromised.

3\. Missing Entries in the Activity Stream  
When the `glide.history.max_entries` property is:

- Greater than or equal to the total number of `sys_history_line` records: All entries are returned and ordered by update time—no issues observed.
- Less than the total number: Since all journal entries share an `internal_checkpoint` of 0, the system struggles to identify the latest records, leading to missing journal entries in the activity stream.
  
With PRB1826101, a new mechansim was introduced:

A HashMap is used to store update count and internal checkpoint values from the `sys_audit` table.

Keys are defined using a `JournalFieldKey` object, which combines:

- `fieldName`
- `newValue`
- `createdOn` (with a tolerance of ±2 seconds)

Using this matching logic, the system links each `sys_journal_field` entry to its corresponding `sys_audit` record, and successfully populates update count and internal checkpoint values into `sys_history_line`.

  
  
*From WP10, XP5, and Y versions onward, update count is always tracked—even when `glide.history_set.pull_journal_entries_from_journal_table` is enabled.*  
  

*Limitation of above change:* This matching logic breaks down when the journal and audit content diverge too far or sys\_audit and sys\_journal\_field tables show different behaviour, such as in script-based updates like:  
  

When scripts like the one below are fired:

```
var gr = new GlideRecord('incident');
if (gr.get('57af7aec73d423002728660c4cf6a71c')) {
gs.info("found incident");
gr.setDisplayValue('work_notes', 'Comment 1');
gr.setDisplayValue('work_notes', 'Comment 2');
gr.update();
}
```

In this scenario:

- Two journal records are created with values "Comment 1" and "Comment 2".
- One audit record is created with the concatenated value "Comment 2 Comment 1".

This discrepancy prevents correct tracking of the update count using JournalFieldKey. To ensure consistency between `sys_audit` and `sys_journal_field`, a new property was introduced `glide.split_journal_audit_records`:

By enabling the property 'glide.split\_journal\_audit\_records', the system ensures that sys\_audit and sys\_journal\_field maintain the same number of records in above cases, allowinf to track update count irresepective of anything.

- Two sys\_journal\_field records are created with values "Comment 1" and "Comment 2."
- Two sys\_audit records are created with values "Comment 1" and "Comment 2."

However even after making such changes, we have discovered some new use cases that still causes with the history sets causing either duplicate comments issue or missing comments issue, and following PRBs are defined to capture such use cases.  
  
Emerging issues with history sets causing either duplicate comments issue or missing comments **(can be observed even on WP10, XP5 and Y versions)**  
  
**[PRB1869081](https://support.servicenow.com/nav_to.do?uri=problem.do?sys_id=e307c344932062d4d6d8fdb86cba10d8) (XP9, YP5, Zurich)  
  
**

'snc\_read\_only' user role causes duplicates comments/work notes in the activity stream.

Steps to reproduce the issue:  

1) Execute the following script and do not open the record:

`var myGr = new GlideRecord('incident');`  
`myGr.get('57af7aec73d423002728660c4cf6a71c');`  
`myGr.comments="TEST COMMENT";`  
`myGr.update();`  

2) Impersonate 'David.Miller' (only has the 'snc\_read\_only' role)

3) Navigate to the record as David Miller

4) Now refresh and note how the entry is duplicated. This happens with every refresh.

5) Un-impersonate and navigate to \[sys\_audit\], no extra entries created. Same for \[sys\_journal\_field\]. The duplicates only exist on \[sys\_history\_line\].  

Root cause:

The issue occurs because the user David.Miller lacks write access to the sys\_history\_set table. As a result, the system is unable to record that the updates have been loaded into the corresponding sys\_history\_set record.  

Following logs are observed in such cases:

```
2025-03-17 05:02:58 (953) Default-thread-5 0CDC381E2B50EA50EE42FDA6CE91BF1A txid=0f2709522bd0 ReadOnlyRoleAccessHandler DEBUG: Security restricted: access for table: sys_history_set, user: David.Miller,
operation: write -- from class: ReadOnlyRoleAccessHandler
```

**[PRB1837173](https://support.servicenow.com/nav_to.do?uri=problem.do?sys_id=8e8159d993621ed4080af35d6cba108b) (XP9, YP5, Zurich)  
  
**When multiple users are simultaneously working on the same incident form and making updates around the same time, the Activity Stream—specifically the history set—may advance prematurely after one user's update is loaded. As a result, subsequent updates from other users may be unintentionally skipped. This occurs because the system assumes that all updates up to the latest recorded timestamp have already been captured, potentially causing some comments to appear missing in the activity stream.

### Use Case:

1. Two users open the same incident record in different sessions.
2. Both users add different comments almost simultaneously, e.g., at `2025-01-01 00:00:00`. The exact timestamps may differ slightly at the millisecond level.
3. When the first comment is loaded, the system sets the last recorded timestamp as `2025-01-01 00:00:00`.
4. When the second comment is added and the history set loader executes again, it uses the previously recorded timestamp (`2025-01-01 00:00:00`) as a cutoff and only fetches records with a newer timestamp.
5. Since the second comment shares the same timestamp down to the second (but not necessarily the millisecond), it gets skipped, and doesn't appear in the activity stream.

**[PRB1860893](https://support.servicenow.com/problem.do?sys_id=2539d60693482e10d6d8fdb86cba109b) (XP9, YP5, Zurich)  
  
**Comments not visible in Activity Stream due due to time difference in audit and journal records.  

In certain scenarios, comments may not appear in the Activity Stream due to a timestamp mismatch between records in the `sys_audit` and `sys_journal_field` tables.

### Background

In the `HistorySetLoader` class, the system first queries the `sys_audit` table and iterates over the results to populate entries in the `sys_history_line` table.  
When the property `glide.history_set.pull_journal_entries_from_journal_table` is enabled:

The system skips audit records related to journal fields. Instead, it sources data for those fields directly from the `sys_journal_field` table.

To retain critical metadata such as update count and internal checkpoint, a HashMap is used during this process:

- Key: A `JournalFieldKey` object (composed of `fieldName`, `newValue`, and `createdOn`).
- Value: An object containing the update count and internal checkpoint from the corresponding `sys_audit` record.
- Two `JournalFieldKey` objects are considered equal if: their `fieldName` and `newValue` match, and the `createdOn` timestamps are within 2 seconds of each other.

### Root Cause

In some cases, journal entries still show an update count of `0`, which prevents them from being correctly processed or displayed in the Activity Stream.

This happens when the `createdOn` timestamps of the `sys_audit` and `sys_journal_field` records differ by more than 2 seconds, breaking the matching logic used by the HashMap.  
  
**[PRB1844946](https://support.servicenow.com/problem.do?sys_id=32dcdab6c3071a90757171dc7a01313c) (XP9, YP5, Zurich)  
  
**

This duplication occurs under specific conditions:

1. When a comment is added, the sys\_updated\_on timestamp of the incident becomes one second earlier than the corresponding sys\_created\_on timestamp of sys\_journal\_field record.  
	2\. If emails are triggered by the incident update, the loading of sys\_email records within the related sys\_history\_set interferes with the last\_update\_recorded field in sys\_history\_set.  
	3\. This interference ultimately causes duplication of the comment when the incident is updated again.

### Resolution

### Unified Root Cause Behind Multiple PRBs Related to Activity Stream Issues

All PRBs discovered after WP10, XP5, and Y releases report different symptoms but stem from the same core component — the `HistorySetLoader` flow. These are not independent bugs but various manifestations of the same underlying issue.

The fix introduced under `PRB1844946` comprehensively addresses the following related PRBs, which is why they have been marked as duplicates:

PRB1869081 – `'snc_read_only' causes duplicate comments/work notes in the activity stream`

PRB1860893 – `Comments not visible in Activity Stream due to time difference in audit and journal records (Extension to DEF0601311)`

PRB1837173 – `Additional comments or work notes not displaying for all users when posted from a script while property glide.history_set.pull_journal_entries_from_journal_table is true`

### Key Enhancements in the Fix (PRB1844946)

- New `journal_sysid` Column:  
	Added to the `sys_history_line` table to uniquely identify and track loaded `sys_journal_field` records, preventing duplication directly at the database level.
- Property `glide.split_journal_audit_records`:  
	Ensures one-to-one mapping between `sys_journal_field` and `sys_audit` records for accurate and consistent synchronization.
- Precise Timestamp Matching:  
	The system now includes a `startTimestamp` in queries to `sys_journal_field`, ensuring it doesn't skip entries created at the same second.
- Flexible Matching Logic via `glide.history_set.journal_audit_time_tolerance`:  
	A configurable property (default: 5000 ms / 5 seconds) allows the system to match journal and audit records even when minor timestamp differences exist.
- As we have added a new column to the sys\_history\_line table and we avoid altering of schema during the upgrades itself. Thus, whenever customer upgrades to the fixed version, they might need to go to Table Rotations -> sys\_history\_line and click on the related link: synchronise shards

### Note

The fix for PRB1844946 involves a schema update to the `sys_history_line` table, specifically the addition of a new column titled "Journal sysid".

Since `sys_history_line` is a rotated table, this column is not added immediately during the upgrade process. Instead, the system waits for all table rotations to complete — which, by default, can take up to 28 days, based on the configured rotation schedule.

To apply the schema change immediately, you can manually trigger it by clicking the “Synchronise Shard” action on the corresponding `sys_table_rotation` record for `sys_history_line`.

### Workaround for Fixing Duplicate Comments on a Specific Record

To resolve issues on a single record (e.g., an incident):

1. Create the property `glide.history_set.pull_journal_entries_from_journal_table` and set it to true.
2. Open the affected record (e.g., INCxyz).
3. Right-click the banner → History → List.
4. This opens the corresponding `sys_history_set` record.
5. Delete that history set record.
6. Reload the incident form — a new `sys_history_set` will be generated without duplicate comments.

### Bulk Cleanup for Multiple Records

If many records are impacted, use this script to delete their associated `sys_history_set` entries:

```
var gr = new GlideRecord('sys_history_set');
gr.addQuery('sys_id', 'IN', <list_of_sys_ids>);
gr.query();
gr.deleteMultiple();
```

Replace `<list_of_sys_ids>` with a comma-separated list of affected record IDs.

**Problematic Scripts**  
  
The property 'glide.history\_set.pull\_journal\_entries\_from\_journal\_table' was introduced to address issues caused by scripts like the one below (Using current.comments in BR is also similar case):  
  
`var gr = new GlideRecord('incident');`  
`if (gr.get('57af7aec73d423002728660c4cf6a71c')) {`  
`gs.info("found incident");`  
`gr.work_notes= 'Comment 1';`  
`gr.work_notes = 'Comment 2';`  
`gr.update();`  
  
When this property is disabled or absent, the system populates sys\_history\_set and sys\_history\_line by fetching data from both sys\_audit and sys\_journal\_field. Since the system compares entries from both sources, discrepancies lead to duplication.  
  
In this scenario:  
  
\- Two journal records are created with values "Comment 1" and "Comment 2".  
\- One audit record is created with the concatenated value "Comment 2 Comment 1".  
\- This results in three records appearing in the history set—two from journal records and one from the audit record.  
  
The recommended fix is to enable 'glide.history\_set.pull\_journal\_entries\_from\_journal\_table', as it was designed to prevent duplicate comments, as it will pull comments into history set only from sys\_journal\_field table.  
  
A new property was introduced in XP5, and Y versions onward called 'glide.split\_journal\_audit\_records':  
  
By enabling the property 'glide.split\_journal\_audit\_records', the system ensures that sys\_audit and sys\_journal\_field maintain the same number of records, resolving duplication:  
  
\- Two sys\_journal\_field records are created with values "Comment 1" and "Comment 2."  
\- Two sys\_audit records are created with values "Comment 1" and "Comment 2."  
  
Even if 'glide.history\_set.pull\_journal\_entries\_from\_journal\_table' remains disabled, enabling 'glide.split\_journal\_audit\_records' prevents creation of 3 records in such cases.  
  
\-----------------------------------  
Functional Change in XP9  
\-----------------------------------  
  
The behavior of the system property glide.split\_journal\_audit\_records has been modified as follows:  
  
1\. When glide.split\_journal\_audit\_records is set to true:  
  
Two sys\_journal\_field records are created, with values "Comment 1" and "Comment 2".  
Two sys\_audit records are created, also containing "Comment 1" and "Comment 2" respectively.  
  
2\. When glide.split\_journal\_audit\_records is set to false:  
  
A single sys\_journal\_field record is created with the concatenated value: "Comment 2 Comment 1".  
A single sys\_audit record is created with the same concatenated value: "Comment 2 Comment 1".  
  
Important Note:  
  
By default, the glide.split\_journal\_audit\_records property is set to false.  
  
As of the XP9 release, customers may observe a change in behavior. Previously, scripts like the one above would result in the creation of two separate sys\_journal\_field entries. Now, under the default setting, the script produces only one journal field entry with the concatenated comments.  
  
If customers wish to retain the original behavior i.e., the creation of separate journal field records—they can do so by setting the property glide.split\_journal\_audit\_records to true.  
  
\-----------------------------------  
From XP 10 onwards:  
\-----------------------------------  
  
1\. When glide.split\_journal\_audit\_records is set to true:  
  
Two sys\_journal\_field records are created, with values "Comment 1" and "Comment 2".  
Two sys\_audit records are created, also containing "Comment 1" and "Comment 2" respectively.  
  
2\. When glide.split\_journal\_audit\_records is set to false:  
  
Two sys\_journal\_field records are created, with values "Comment 1" and "Comment 2".  
A single sys\_audit record is created with the same concatenated value: "Comment 2 Comment 1".  
  
\----------------------------------------------------------------------  
Recommended Configuration:  
\----------------------------------------------------------------------  
Enable: glide.history\_set.pull\_journal\_entries\_from\_journal\_table  
Enable: glide.split\_journal\_audit\_records