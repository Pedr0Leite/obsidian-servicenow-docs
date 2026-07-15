---
aliases:
  - Catalog Item Prefill and Modal
  - sysparm_variable_values
  - spModal catalog item
area: query
tags: [query, service-catalog, service-portal, modal, prefill, variables, troubleshooting, iframe]
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

**Opening in a modal — attempt 1 (undocumented combination — synthesized, not vault-confirmed):**
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
- This is the shape that triggered the "You are either not authorized or record is not valid" error — root cause was passing `sysparm_id` directly into `widget-sc-cat-item-v2`'s `widgetInput` instead of going through the `widget-modal` wrapper (see attempt 2).

**Opening in a modal — attempt 2 (user-confirmed working pattern, embeds via `widget-modal` wrapper):**
```js
function($scope, spModal, spUtil) {
  var c = this;

  c.openCatalogItem = function(catItemSysId) {
    spModal.open({
      title: 'Request Catalog Item',
      size: 'lg', // 'sm', 'md', 'lg', or 'xl'
      widget: 'widget-modal',
      widgetInput: {
        embeddedWidgetId: 'widget-sc-cat-item-v2',
        embeddedWidgetOptions: {
          sys_id: catItemSysId,      // target sc_cat_item sys_id
          auto_redirect: 'false',
          display_cart_on_right: false,
          disableUIActions: false
        }
      }
    }).then(function() {
      console.log('Modal closed');
    });
  };
}
```
- Key difference: `widget: 'widget-modal'` is a base-system wrapper widget built for embedding another widget inside `spModal`. The target widget's id and its own input go under `embeddedWidgetId` / `embeddedWidgetOptions`, not directly as top-level `widget`/`widgetInput`.
- `widget-sc-cat-item-v2` receives its config via `embeddedWidgetOptions.sys_id` (not `sysparm_id`) — this is likely why attempt 1 failed: `widget-sc-cat-item-v2` mounted directly never got a valid record reference through the plain `widgetInput` path.
- Options seen: `sys_id` (item to load), `auto_redirect` (string `'false'`/`'true'`, skip cart auto-redirect), `display_cart_on_right` (bool), `disableUIActions` (bool).
- Not in this example: no `sysparm_variable_values` equivalent — this pattern opens the item but doesn't demonstrate prefill. If prefill-in-modal is still needed, test whether `embeddedWidgetOptions` also accepts a `sysparm_variable_values`-style key, or fall back to option 1/2 below.
- No vault doc confirms `widget-modal` or `embeddedWidgetOptions` (not present anywhere in `ServiceNowOfficialDocs/`) — this is field-tested by the user, not platform-documented. Treat option list as possibly incomplete.
- Two ways to de-risk prefill specifically:
  1. Skip the modal, navigate instead (`$location.url('/sp?id=sc_cat_item&sys_id=...&sysparm_variable_values={...}')`) — prefill guaranteed, no modal UX.
  2. Clone `widget-sc-cat-item-v2`, add client-script logic reading `c.data.widgetInput.sysparm_variable_values` (or the `embeddedWidgetOptions` equivalent) and applying it to `c.data.item.variables` on init — modal UX + guaranteed prefill, more work.

**Troubleshooting "You are either not authorized or record is not valid" in the modal:**
- Confirmed causes, per `ServiceNowOfficialDocs/platform-user-interface/service-portal/widget-troubleshooting-guide.md` and `.../navigate-by-portal-url.md`:
  1. Missing/wrong required param — `widgetInput.sysparm_id` must be the exact `sc_cat_item` sys_id.
  2. Catalog item hidden from Service Portal, or blocked by user criteria/ACL for the current user.
- Diagnose: open the item directly via portal URL first (`/sp?id=sc_cat_item&sys_id=<id>`). If that works but the modal doesn't, it's a param/key mismatch in the `spModal.open` call, not an ACL/visibility issue.

**Opening in an iframe (simplest variable-passing, no modal UX):**
```js
// In widget Client Controller — inject $sce
function($scope, $sce) {
  var c = this;
  c.catalogItemUrl = $sce.trustAsResourceUrl(
    '/sp?id=sc_cat_item&sys_id=' + c.data.catItemSysId +
    '&sysparm_variable_values=' + encodeURIComponent(JSON.stringify({
      case: c.data.caseSysId,
      short_description: c.data.caseShortDescription
    }))
  );
}
```
```html
<iframe ng-src="{{c.catalogItemUrl}}" style="width:100%; height:600px; border:none;"></iframe>
```
- `$sce.trustAsResourceUrl` is mandatory — Angular (Service Portal) blocks untrusted dynamic `src` bindings by default.
- All URL-prefill caveats still apply (supported variable types, `glide.sc.enable_url_prefill` must be on).
- Tradeoff: real page load (no SPA feel), height is manual. Benefit: no ACL surprises, prefill guaranteed via documented URL path.

**Opening the iframe on button click via Bootstrap modal:**
```js
// In Client Controller — inject $sce, $timeout
c.openIframeModal = function() {
  c.catalogItemUrl = $sce.trustAsResourceUrl(
    '/sp?id=sc_cat_item&sys_id=' + c.data.catItemSysId +
    '&sysparm_variable_values=' + encodeURIComponent(JSON.stringify({case: c.data.caseSysId}))
  );
  $timeout(function() {
    $('#catItemModal').modal('show');
  });
};
```
```html
<button ng-click="c.openIframeModal()">Open Catalog Item</button>
<div id="catItemModal" class="modal fade" tabindex="-1" role="dialog">
  <div class="modal-dialog modal-lg" role="document">
    <div class="modal-content">
      <div class="modal-header">
        <button type="button" class="close" data-dismiss="modal">&times;</button>
      </div>
      <div class="modal-body" style="padding:0">
        <iframe ng-src="{{c.catalogItemUrl}}" style="width:100%; height:600px; border:none;"></iframe>
      </div>
    </div>
  </div>
</div>
```
- Bootstrap 3 modals are not natively Angular-driven — must trigger with jQuery `.modal('show')`. Wrap in `$timeout` so Angular finishes its digest (sets `catalogItemUrl`) before the modal opens; otherwise `ng-src` may not be bound yet.
- Set `catalogItemUrl` on click (not on page init) so Angular doesn't load the iframe src before the user opens it.
- Use for one-offs. For a pattern already using `spModal`/`widget-modal`, see attempt 2 above instead.

Source: [[raw/sessions/2026-07-15#Session 14:21 — obsidian-servicenow-docs]]

## Related
- [[service-catalog]]
- [[service-portal]]
- [[wiki/index|Wiki Index]]
