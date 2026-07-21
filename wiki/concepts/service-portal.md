---
aliases: [Service Portal, Widgets]
area: concept
tags: [concept, service-portal, widgets]
---
Service Portal notes: Angular provider, widget codes, EVAM, portal methods/events, Link function, search sources.

## Sources
- `Notion/ServiceNow/Service Portal/`
- `Notion/ServiceNow/Integrations/Service Portal ....md`

## Angular gotcha: dynamic iframe src requires `$sce.trustAsResourceUrl`

Angular (Service Portal) blocks untrusted dynamic `src` bindings on `<iframe>` elements. Any dynamically-built URL must be wrapped:
```js
c.iframeUrl = $sce.trustAsResourceUrl(builtUrl);
```
Without this, the iframe renders blank or throws `[$sce:insecurl]`. Inject `$sce` into the Client Controller.

Also: Bootstrap 3 modals in Service Portal are not Angular-driven — trigger with jQuery `.modal('show')`, wrapped in `$timeout` so Angular's digest completes first.

Source: [[raw/sessions/2026-07-15#Session 14:21 — obsidian-servicenow-docs]]

## Gotcha: `widget-sc-cat-item-v2` submits via Angular `$location` — `onload` never refires

The catalog item widget navigates on submission using Angular's `$location` client-side routing, not a full page load. Consequences:
- `iframe.onload` never fires again after the user submits — you cannot use it to detect completion.
- Use `$interval` polling on `iframe.contentWindow.location.href` (~500ms) and detect when the URL no longer contains the catalog page id.
- Wrap `contentWindow.location` access in `try/catch` — it throws a `SecurityError` transiently at the navigation moment, even on same-origin frames.
- Cancel the interval on modal close (`hidden.bs.modal`) and on `$scope.$destroy` to prevent leaks.

Seen in: `obsidian-servicenow-docs`
Source: [[raw/sessions/2026-07-15#Session 22:25 — obsidian-servicenow-docs]]

See [[catalog-item-prefill-and-modal]] for the full `$interval` polling pattern.

## Related concepts
- [[frameworks-libraries]]
- [[service-catalog]]

## Related queries
- [[catalog-item-prefill-and-modal]]

## Related
- [[wiki/index|Wiki Index]]
