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

## Related concepts
- [[frameworks-libraries]]
- [[service-catalog]]

## Related queries
- [[catalog-item-prefill-and-modal]]

## Related
- [[wiki/index|Wiki Index]]
