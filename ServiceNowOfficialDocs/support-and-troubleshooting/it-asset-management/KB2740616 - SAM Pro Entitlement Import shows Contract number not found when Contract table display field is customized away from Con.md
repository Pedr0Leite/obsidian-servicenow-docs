---
title: "SAM Pro Entitlement Import shows \"Contract number not found\" when Contract table display field is customized away from Contract Number"
aliases:
  - KB2740616
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB2740616
kb_number: KB2740616
last_modified: 2026-01-27
---

## Issue

→ Entitlement Import fails with “Contract number not found” even though the contract exists

## Resolution

→ Review the Contract table dictionary and identify which field is set as Display  
→ Revert the Contract table display configuration to OOB behavior so Contract Number is the Display field  
→ Ensure the previously set custom display field is not marked as Display  
→ Save changes and re-run the Entitlement Import  
→ After restoring Contract Number as the display field, the import validation resolves contracts correctly by contract number
