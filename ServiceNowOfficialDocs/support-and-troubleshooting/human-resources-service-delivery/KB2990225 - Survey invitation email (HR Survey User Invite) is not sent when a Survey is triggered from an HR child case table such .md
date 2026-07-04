---
title: "Survey invitation email (HR Survey User Invite) is not sent when a Survey is triggered from an HR child case table such as Total Rewards, Benefits, or Payroll"
aliases:
  - KB2990225
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB2990225
kb_number: KB2990225
last_modified: 2026-05-06
---

## Survey invitation email (HR Survey User Invite) is not sent when a Survey is triggered from an HR child case table such as Total Rewards, Benefits, or Payroll

  

### Issue

When an HR case — such as an HR Total Rewards Case, Benefits Case, or Payroll Case — is closed and triggers a Survey, the `asmt_assessment_instance` record is created successfully every time. However, the survey invitation email is not always sent to the assigned user.

Checking the `sys_email` table confirms that no email record is generated for the affected survey instances. The `record.send_survey` event and the `notification_engine.process` event are both present and processed, yet no email is produced.

The issue appears intermittent because surveys triggered by the base `sn_hr_core_case` table work correctly, while those triggered by child tables do not.

### Release

All release

### Cause

The OOTB notification "HR Survey User Invite" contains the following Advanced Condition:

`answer = current.trigger_table == 'sn_hr_core_case';`

This condition performs an exact string match against the `trigger_table` field on the `asmt_assessment_instance` record. The `trigger_table` field stores the name of the table whose record triggered the survey.

When an HR case from a child table (e.g., `sn_hr_core_case_total_rewards`) is closed and triggers the survey, the `trigger_table` value is set to the child table name — not `sn_hr_core_case`. Because the condition only matches the exact string `'sn_hr_core_case'`, the notification evaluation returns `false` and no email is generated.

| Survey Instance | trigger\_table value | Notification fires? |
| --- | --- | --- |
| Triggered by base HR Case | `sn_hr_core_case` | Yes |
| Triggered by HR Total Rewards Case | `sn_hr_core_case_total_rewards` | No |
| Triggered by HR Benefits Case | `sn_hr_core_case_benefits` | No |
| Triggered by HR Payroll Case | `sn_hr_core_case_payroll` | No |

Note — This is expected OOTB behaviorThe "HR Survey User Invite" notification is delivered by the Human Resources: Core(`sn_hr_core`) scoped application and is intentionally scoped to `sn_hr_core_case`. This is not a platform bug. Any change to this behavior requires customization.

### Resolution

Both options below involve customizing OOTB components. ServiceNow Support cannot guarantee the behavior of customized configurations. Customers who implement these changes take on upgrade risk and are responsible for tracking and reapplying customizations after upgrades.

**Option 1: Modify the Advanced Condition on "HR Survey User Invite**

Replace the exact string match with a hierarchy-aware check using `GlideDBObjectManager.isInstanceOf()`. This makes the notification fire for `sn_hr_core_case` and all of its child tables, without needing to enumerate each child table individually.

Navigate to: All > System Notification > Email > Notifications > search for HR Survey User Invite > open in Advanced view.

Replace the Advanced condition field with the following:

Before

```
answer = current.trigger_table == 'sn_hr_core_case';
```

After

```
var tableName = current.getValue('trigger_table');
var dbom = GlideDBObjectManager.get();
answer = (tableName == 'sn_hr_core_case' || dbom.isInstanceOf(tableName, 'sn_hr_core_case'));
```

How it works: `GlideDBObjectManager.isInstanceOf(childTable, parentTable)` returns `true` if `childTable` extends `parentTable` in the table hierarchy. This covers Total Rewards, Benefits, Payroll, and any other current or future child tables of `sn_hr_core_case`.

Upgrade risk:

"HR Survey User Invite" is an OOTB record in the `sn_hr_core` scope. Direct modifications may result of conflict if the recode has been changed in upgrade package.So, you need to track/review the record changing after every upgrade.

**Option 2: Create a new notification for each child table**

Clone the OOTB "HR Survey User Invite" notification and create a separate copy for each child table that needs to trigger survey emails. This avoids modifying the OOTB record.

Steps:

1.  Open HR Survey User Invite and use the Copy UI action to duplicate it.
2.  Rename the copy (e.g., _HR Survey User Invite — Total Rewards_).
3.  Set the Advanced Condition to match the specific child table:

`answer = current.trigger_table == 'sn_hr_core_case_total_rewards';`

Repeat for each additional child table as needed.

Lower upgrade risk:

Because the OOTB record is not modified, this option carries lower upgrade risk. However, it requires maintenance if new child tables are added in the future.
