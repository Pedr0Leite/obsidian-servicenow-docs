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

**Opening in a modal — attempt 3 (user-confirmed, stashes context in URL params instead of `widgetInput`):**
```js
function() {
    var url = new URL(window.location.href);
    url.searchParams.set('case_number', c.data.number);
    url.searchParams.set('case_sys_id', c.data.sys_id);
    url.searchParams.set('account_sys_id', c.data.account || '');
    url.searchParams.set('account_display', c.data.accountDisplay || '');
    url.searchParams.set('contact_sys_id', c.data.contact || '');
    url.searchParams.set('contact_display', c.data.contactDisplay || '');
    window.history.replaceState(null, '', url.toString());

    spModal.open({
        title: 'Escalate Case',
        size: 'lg',
        widget: 'widget-modal',
        widgetInput: {
            embeddedWidgetId: 'widget-sc-cat-item-v2',
            embeddedWidgetOptions: {
                sys_id: 'SYS_ID_OF_CATALOG_HERE',
                auto_redirect: 'false',
                display_cart_on_right: false,
                disableUIActions: false
            }
        }
    }).then(function() {
        var cleanUrl = new URL(window.location.href);
        ['case_number','case_sys_id','account_sys_id','account_display','contact_sys_id','contact_display'].forEach(function(p) {
            cleanUrl.searchParams.delete(p);
        });
        window.history.replaceState(null, '', cleanUrl.toString());
    });
};
```
- Same `widget-modal` wrapper as attempt 2, but sidesteps the "does `embeddedWidgetOptions` accept prefill data" open question entirely: instead of passing case/account/contact context through `widgetInput`, it writes those fields onto the page URL (`window.history.replaceState`) right before opening the modal.
- Lets the embedded catalog item widget's own client script (or any other widget on the page) read the context via `$location.search()` / raw `window.location`, without needing a prefill contract from `widget-sc-cat-item-v2` itself.
- Cleans up on close: `.then()` on `spModal.open` fires when the modal is dismissed (same close hook as attempt 2's `console.log('Modal closed')`), and strips the injected params back out so the URL doesn't retain stale case/account/contact state after the modal closes.
- `replaceState` (not `pushState`) is deliberate — avoids adding junk entries to browser history for a value that's only scaffolding for the modal's lifetime.
- Tradeoff vs. attempt 2: no `sysparm_variable_values` involved at all, so this is for passing *contextual reference data* (which case/account/contact triggered the escalation) rather than prefilling actual catalog variables — pair with option 1/2 under attempt 2, or the iframe pattern below, if the catalog item's own variables still need prefilling.
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

**Hiding the portal header inside the iframe (same-origin CSS injection):**
Same-origin iframes (both frames on the same SN instance domain) allow DOM access from the parent widget — cross-origin restrictions do not apply. On `iframe.onload`, inject a `<style>` tag to suppress the portal header:
```js
var iframe = document.querySelector('#catItemModal iframe');
iframe.onload = function() {
  try {
    var style = iframe.contentDocument.createElement('style');
    style.textContent = '.navpage-header, .portal-nav, .sp-header { display: none !important; }';
    iframe.contentDocument.head.appendChild(style);
  } catch(e) {}
};
```
- More fragile than building a dedicated headerless portal page, but avoids creating a second page.
- CSS selectors vary by theme — verify on the target instance.
- Wrap in `try/catch` as a precaution; `contentDocument` can be briefly inaccessible during load.

**Auto-closing the modal when the catalog item is submitted:**
`widget-sc-cat-item-v2` navigates after submission via Angular `$location` client-side routing — the iframe does **not** fire `onload` again. Poll `contentWindow.location.href` with `$interval` instead:
```js
// inject $interval, $sce, $timeout — cancel poll on modal close and $scope destroy
c.openIframeModal = function() {
  c.catalogItemUrl = $sce.trustAsResourceUrl(
    '/sp?id=sc_cat_item&sys_id=' + c.data.catItemSysId +
    '&sysparm_variable_values=' + encodeURIComponent(JSON.stringify({case: c.data.caseSysId}))
  );
  $timeout(function() { $('#catItemModal').modal('show'); });

  var poll = $interval(function() {
    try {
      var href = document.querySelector('#catItemModal iframe').contentWindow.location.href;
      if (href && href.indexOf('sc_cat_item') === -1) {
        $interval.cancel(poll);
        $('#catItemModal').modal('hide');
      }
    } catch(e) {} // contentWindow.location throws transiently during navigation
  }, 500);

  $('#catItemModal').on('hidden.bs.modal', function() { $interval.cancel(poll); });
  $scope.$on('$destroy', function() { $interval.cancel(poll); });
};
```
- Cancel the interval both on modal close (`hidden.bs.modal`) and `$scope.$destroy` to avoid leaks.
- The `try/catch` is required — `contentWindow.location` throws a `SecurityError` transiently at the moment of navigation even on same-origin frames.

Source: [[raw/sessions/2026-07-15#Session 22:25 — obsidian-servicenow-docs]]

## Related
- [[service-catalog]]
- [[service-portal]]
- [[wiki/index|Wiki Index]]
