---
aliases: [Catalog Item Prefill and Modal, sysparm_variable_values, spModal catalog item]
area: query
tags: [query, service-catalog, service-portal, modal, prefill, variables]
---
Q: In Service Portal, how do you open a catalog item and autopopulate fields — via URL variables or something else? Follow-up: how do you open a catalog item in a modal from a button click, with fields autopopulated from the current record (e.g. a case)?

## Answer

**Prefill via URL (documented, reliable):**
```
/sp?id=sc_cat_item&sys_id=<item_sys_id>&sysparm_variable_values={"department":"Sales","business_justification":"employee onboarding"}
```
- Key = variable name, value = variable value. Reference variables need a sys_id, not a display value.
- Values apply as if user-entered — Catalog UI Policies and catalog client scripts still fire.
- Toggle: `glide.sc.enable_url_prefill` (instance-wide). Per-widget: "Disable URL prefill" instance option on the catalog item widget.
- Not supported: attachment, custom, custom w/ label, label, masked, UI page, multi-row variable set (MRVS).
- Next Experience UI uses a different mechanism: `variableValues` property on the catalog item macroponent in UI Builder, not a URL param.
- Source: `ServiceNowOfficialDocs/servicenow-platform/service-catalog/prefill-variable-values-catalog-item-form.md`

**Opening in a modal (undocumented combination — synthesized, not vault-confirmed):**
```js
spModal.open({
  title: 'New Request',
  widget: 'widget-sc-cat-item-v2',   // or a cloned catalog item widget
  widgetInput: {
    sysparm_id: '<catalog_item_sys_id>',
    sysparm_variable_values: {
      case: caseSysId,
      short_description: caseShortDescription
    }
  },
  size: 'lg'
});
```
- `spModal.open` itself is confirmed real (only vault example: `ServiceNowOfficialDocs/platform-user-interface/service-portal/enable-esignature-sp.md`, using `widget` + `widgetInput` + `size`).
- **Not confirmed:** whether `widget-sc-cat-item-v2` reads `sysparm_variable_values` from `widgetInput` the same way it reads it from the URL. The prefill doc only documents the URL path.
- Two ways to de-risk:
  1. Skip the modal, navigate instead (`$location.url('/sp?id=sc_cat_item&sys_id=...&sysparm_variable_values={...}')`) — prefill guaranteed, no modal UX.
  2. Clone `widget-sc-cat-item-v2`, add client-script logic reading `c.data.widgetInput.sysparm_variable_values` and applying it to `c.data.item.variables` on init — modal UX + guaranteed prefill, more work.
- No vault doc confirms which path the base widget actually supports — test option 1 before investing in option 2.

## Related
- [[service-catalog]]
- [[service-portal]]
- [[wiki/index|Wiki Index]]
