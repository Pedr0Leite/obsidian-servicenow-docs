---
title: "How HR case priority is set"
aliases:
  - KB2923965
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB2923965
kb_number: KB2923965
last_modified: 2026-03-30
---

## How HR case priority is set

  

### Issue

 

 

How HR case priority is set

### Release

 

ALL

### Cause

 

Priority Override via Client Scripts

The priority of HR cases is controlled by specific HR Client Scripts rather than relying strictly on the standard `dl_u_priority` Data Lookup matrix. The two scripts responsible are:

-   Reset priority on subject person change
-   Reset priority on opened\_for change

These scripts fire when the `subject_person` or `opened_for` fields are populated or changed on an HR case form, bypassing the standard priority lookup evaluation.

Priority Evaluation Logic

Both client scripts invoke the `hr_CaseAjax` Script Include (`getPriority` function) to determine the final priority. The evaluation follows this sequence:

**Step 1 — VIP Check:** The script checks whether the `opened_for` or `subject_person` user has VIP status. If VIP is detected, the priority defined by the system property `sn_hr_core.hr_vip_default_priority` is applied.  
  
**Step 2 — Default Dictionary Value:** If no VIP status is detected, the script falls back to the **default dictionary value** for the Priority field on the HR Case table — not the Data Lookup matrix result.

### Resolution

 

1.  1
    
    **Understand the priority source.** HR case priority is determined by HR Client Scripts (**_Reset priority on subject person change_ / _Reset priority on opened\_for change_**), not the standard Priority Lookup Rules. This is expected platform behaviour.
    
2.  2
    
    **Verify field population.** Confirm whether the `opened_for` or `subject_person` fields are populated. Populating either field triggers the client scripts to evaluate VIP status and apply the appropriate default priority value.
    
3.  3
    
    **Check the VIP priority system property.** Navigate to **System Properties** and locate `sn_hr_core.hr_vip_default_priority`. Confirm the value is set correctly for VIP users — if the `opened_for` or `subject_person` user is flagged as VIP, this property value is applied directly.
    
4.  4
    
    **Review the default dictionary value for Priority.** If no VIP is detected, priority falls back to the default dictionary value for the **Priority** field on the HR Case table (`sn_hr_core_case`). Go to **System Definition › Dictionary**, filter by table `sn_hr_core_case` and field `priority`, and verify the default value matches your org's expectations.
