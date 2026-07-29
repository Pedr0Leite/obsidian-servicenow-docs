---
aliases:
  - "re_run_flows"
area: "Scripts"
source: custom
tags:
  - flow-designer
  - flow-api
  - scripting
  - scripts
---

# re_run_flows

Minimal template for re-triggering a Flow Designer flow against a specific record from a background script: build an `inputs` object with `current` (the GlideRecord) and `table_name`, then call `sn_fd.FlowAPI.executeFlow('scope.flow_name', inputs)` inside a try/catch. The bare-bones version of [[RunFlowsViaScript]].

```javascript
var tt = new GlideRecord('TABLE NAME');
tt.get('RECORD SYSID');


	try {
		var inputs = {};
		inputs['current'] = tt; // GlideRecord of table:  
		inputs['table_name'] = 'TABLE NAME';

        sn_fd.FlowAPI.executeFlow('SCOPE TECH NAME.FLOW NAME', inputs);
	} catch (ex) {
		var message = ex.getMessage();
		gs.error(message);
	}
```

## Related

- [[Flow Designer]]
- [[RunFlowsViaScript]]
