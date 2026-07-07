---
title: "SmartData"
aliases:
  - SmartData
tags:
  - servicenow-dev-program
  - code-snippet
  - smartdata
  - script-includes
---

What it is
A tiny, reusable utility that auto-selects GlideAggregate vs GlideRecord based on intent. Includes count, distinct, stats, one, list, describe, preview and a client-callable GlideAjax wrapper that escapes encoded queries using GlideStringUtil.escapeQueryTermSeparator.

Why it’s useful

Devs can call one API and let it pick the best engine.

Handy helpers: describe(table) for schema, preview(table, query) for quick peeks.

AJAX-ready for client scripts/UI actions.

Shows secure-by-default thinking reviewers love.

How to test quickly

Create both Script Includes as provided.

Testing

Or run in Background Scripts:
var sd = new SmartData(); gs.info('Count: ' + sd.count('incident', 'active=true')); gs.info(JSON.stringify(sd.stats('incident', {fn:'AVG', field:'time_worked'}, ['assignment_group'], 'active=true'))); gs.info(JSON.stringify(sd.one('incident', 'active=true', ['number','priority'], '-sys_created_on'))); gs.info(JSON.stringify(sd.describe('problem')));

Security note
SmartDataAjax sanitizes sysparm_query via GlideStringUtil.escapeQueryTermSeparator to protect against malformed/injected encoded queries.

## Related Notes

- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Client-Side Components/UI Actions/Open Record in Alternate Instance/Script Includes/README|Script Includes]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Client-Side Components/UI Actions/Open Record in Alternate Instance/Script Includes/sys_script_include_config|sys_script_include_config]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Script Includes/API Model Template for New Application/README|API Model Template for New Application]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Script Includes/Add Business Days/README|Add Business Days]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Script Includes/Add and Remove Group Member/README|Add and Remove Group Member]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Script Includes/Advanced REST API Integration with Retry Logic/README|Advanced REST API Integration with Retry Logic]]
