---
aliases:
  - "RunFlowsViaScript"
area: "Scripts"
source: custom
tags:
  - flow-designer
  - flow-api
  - sys-flow-context
  - flow-trigger-api
  - scripts
---

# RunFlowsViaScript

Three related Flow Designer scripting patterns in one file: (1) an IIFE calling `sn_fd.FlowAPI.executeFlow` with a `current`/`table_name` inputs object, showing the commented-out sync/timeout variant; (2) a Business Rule that first cancels any in-flight `sys_flow_context` for the current record (`sn_fd.FlowAPI.cancel`) before (3) firing the catalog item's configured flow via `sn_flow_trigger.FlowTriggerAPI.fireCatalogTrigger`. Useful when a data-driven flow needs to be restarted cleanly instead of stacking duplicate runs.

```javascript
(function() {
	try {
		var inputs = {};
		inputs['current'] = ''; // GlideRecord of table:  
		inputs['table_name'] = 'sc_req_item';

              // Execute Synchronously: Run in foreground.
              // var timeout = ; //timeout in ms
              //sn_fd.FlowAPI.executeFlow('global.test_flow', inputs, timeout)
              sn_fd.FlowAPI.executeFlow('global.NAME OF FLOW', inputs);
	} catch (ex) {
		var message = ex.getMessage();
		gs.print(message);
	}
})();

//----------------
(function executeRule(current, previous /*null when async*/ ) {

    var now_GR = new GlideRecord("sys_flow_context");
    now_GR.addQuery("name", '');// flow designer name
    now_GR.addQuery("source_record="+current.sys_id);
    now_GR.query();
    
    while (now_GR.next()) {
    sn_fd.FlowAPI.cancel(now_GR.getUniqueValue(), 'Canceling FJS - Data Driven Flow'); // flow designer name
    }
    
    startFlowDesignerFlow(current);
    
    function startFlowDesignerFlow(current) {
    var flow = current.cat_item.flow_designer_flow;
    var flowName = flow.sys_scope.scope + "." + flow.internal_name;
    
    sn_flow_trigger.FlowTriggerAPI.fireCatalogTrigger(flowName, current);
    }
    
    })(current, previous);
```

## Related

- [[Flow Designer]]
- [[How to nudge a flow]]
- [[sn_fd FlowAPI nudgeFlow does not work if completed]]
- [[What is “Presumed Interrupted” state]]
- [[re_run_flows]]
