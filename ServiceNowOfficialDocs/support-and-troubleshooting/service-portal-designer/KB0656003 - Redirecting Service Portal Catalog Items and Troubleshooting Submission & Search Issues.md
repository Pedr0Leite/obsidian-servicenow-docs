---
title: "Redirecting Service Portal Catalog Items and Troubleshooting Submission & Search Issues"
aliases:
  - KB0656003
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0656003
kb_number: KB0656003
last_modified: 2026-04-10
---

## Redirecting Service Portal Catalog Items and Troubleshooting Submission & Search Issues

  

### Issue

## **Issue 1: Redirecting a Service Portal Catalog Item After Submission**

## Symptoms

## Administrators need to redirect users to a specific page after submitting a catalog item or record producer in the Service Portal.

## Resolution

### 1\. Redirect Using the SC Catalog Item Widget (Widget Instance Level)

To configure a redirect for all catalog item submissions:

-   Navigate to: `/sp?id=sc_cat_item`
-   Press Ctrl + Right‑Click and select Instance Options.
-   Configure the following fields:
    -   Successful Order Page – Select the page users should be redirected to after submission.
    -   Successful Order Table – Select the table used to generate the success message link.

(Optional) Enable Auto-Redirect on Successful Order to automatically redirect users without requiring them to click the success message link.

Once configured, the success message link and/or auto‑redirect will take users to the desired page or record.  
  

**2. Redirect Using Record Producer Script**

For script‑based redirection on a Record Producer, set the `portal_redirect` property:

producer.portal\_redirect = "?id=sc\_home";  
This redirects the user to the specified Service Portal page after the record producer is submitted.

# **Issue 2: Catalog Item Stuck at “Submitting…” With 400 (Bad Request)**

### Symptoms

 Catalog item submission hangs at “Submitting…”.

 Browser console shows:

-   `400 (Bad Request)`
-   `"Mandatory variables are not filled"`

System logs show `BadRequestError` from the Service Catalog REST API.

#### Errors in Browser Console:

<table style="border-collapse: collapse; width: 100%;" border="1"><colgroup><col style="width: 99.906%;"></colgroup><tbody><tr><td><pre>uri: "api/sn_sc/v1/servicecatalog/items/bcf9c7129525d6405fabdeba66ae2a4c/submit_producer 400 (Bad Request)&nbsp;<br><br>{error: {…}, status: "failure"}&nbsp;<br>error&nbsp;<br>:&nbsp;<br>detail&nbsp;<br>:&nbsp;<br>""&nbsp;<br>message&nbsp;<br>:&nbsp;<br>"Mandatory variables are not filled"&nbsp;<br>__proto__&nbsp;<br>:&nbsp;</pre></td></tr></tbody></table>

![](/sys_attachment.do?sys_id=ac38f4a747844b10b8a4aa25126d433d) 

Error in logs

<table style="border-collapse: collapse; width: 100%;" border="1"><colgroup><col style="width: 99.906%;"></colgroup><tbody><tr><td><pre>2018-04-18 09:21:06 (638) API_INT-thread-1 A32A62A50F691300B04F419CE1050EFC txid=61ebae2d0f2d SEVERE *** ERROR *** Root cause of JavaScriptException: com.glide.rest.service.custom.errors.ScriptableBadRequestError&nbsp;<br>JavaScript evaluation error on:&nbsp;<br>(function process(/*RESTAPIRequest*/ request, /*RESTAPIResponse*/ response) {&nbsp;<br>var request_body = request.body.nextEntry();&nbsp;<br>var quantity = '' + request_body.sysparm_quantity;&nbsp;<br><br>if (!/^\+?([0-9]*)$/.test(quantity))&nbsp;<br>throw new sn_ws_err.BadRequestError("Invalid Quantity value");&nbsp;<br>else&nbsp;<br>request_body.sysparm_quantity = quantity;&nbsp;<br><br>var itemId = '' + request.pathParams.sys_id;&nbsp;<br>request_body.sysparm_id = itemId;&nbsp;<br>var catItem = new sn_sc.CatItem(itemId);&nbsp;<br>if (!catItem.canView())&nbsp;<br>throw new sn_ws_err.BadRequestError("Security constraints prevent ordering of Item");&nbsp;<br><br>var catUtil = new RestCatalogUtil();&nbsp;<br>if (!catUtil.checkMandatoryVariables(itemId, request_body.variables))&nbsp;<br>throw new sn_ws_err.BadRequestError('Mandatory Variables are required');&nbsp;<br><br>var cart = new sn_sc.CartJS("cart_" +itemId);&nbsp;<br>request_body.sysparm_cart_name = "cart_" +itemId;&nbsp;<br>try {&nbsp;<br>return cart.orderNow(request_body);&nbsp;<br>}catch(e) {&nbsp;<br>gs.debug(e);&nbsp;<br>throw new sn_ws_err.NotFoundError("Invalid Request");&nbsp;<br>}&nbsp;<br>})(request, response);&nbsp;<br><br>2018-04-18 09:21:06 (639) API_INT-thread-1 A32A62A50F691300B04F419CE1050EFC txid=61ebae2d0f2d SEVERE *** ERROR *** JavaScript evaluation error on:&nbsp;<br>(function process(/*RESTAPIRequest*/ request, /*RESTAPIResponse*/ response) {&nbsp;<br>var request_body = request.body.nextEntry();&nbsp;<br>var quantity = '' + request_body.sysparm_quantity;&nbsp;<br><br>if (!/^\+?([0-9]*)$/.test(quantity))&nbsp;<br>throw new sn_ws_err.BadRequestError("Invalid Quantity value");&nbsp;<br>else&nbsp;<br>request_body.sysparm_quantity = quantity;&nbsp;<br><br>var itemId = '' + request.pathParams.sys_id;&nbsp;<br>request_body.sysparm_id = itemId;&nbsp;<br>var catItem = new sn_sc.CatItem(itemId);&nbsp;<br>if (!catItem.canView())&nbsp;<br>throw new sn_ws_err.BadRequestError("Security constraints prevent ordering of Item");&nbsp;<br><br>var catUtil = new RestCatalogUtil();&nbsp;<br>if (!catUtil.checkMandatoryVariables(itemId, request_body.variables))&nbsp;<br>throw new sn_ws_err.BadRequestError('Mandatory Variables are required');&nbsp;<br><br>var cart = new sn_sc.CartJS("cart_" +itemId);&nbsp;<br>request_body.sysparm_cart_name = "cart_" +itemId;&nbsp;<br>try {&nbsp;<br>return cart.orderNow(request_body);&nbsp;<br>}catch(e) {&nbsp;<br>gs.debug(e);&nbsp;<br>throw new sn_ws_err.NotFoundError("Invalid Request");&nbsp;<br>}&nbsp;<br>})(request, response);&nbsp;<br><br>org.mozilla.javascript.JavaScriptException: [object BadRequestError] (sys_ws_operation.4f9131449f901200d54dd4b4232e708d.operation_script; line 18)&nbsp;<br>at org.mozilla.javascript.gen.sys_ws_operation_4f9131449f901200d54dd4b4232e708d_operation_script_4345._c_process_1(sys_ws_operation.4f9131449f901200d54dd4b4232e708d.operation_script:18)&nbsp;<br>at org.mozilla.javascript.gen.sys_ws_operation_4f9131449f901200d54dd4b4232e708d_operation_script_4345.call(sys_ws_operation.4f9131449f901200d54dd4b4232e708d.operation_script)&nbsp;<br>at org.mozilla.javascript.ScriptRuntime.doCall2(ScriptRuntime.java:2650)&nbsp;<br>at org.mozilla.javascript.ScriptRuntime.doCall(ScriptRuntime.java:2590)&nbsp;<br>at org.mozilla.javascript.optimizer.OptRuntime.call2(OptRuntime.java:42)&nbsp;<br>at org.mozilla.javascript.gen.sys_ws_operation_4f9131449f901200d54dd4b4232e708d_operation_script_4345._c_script_0(sys_ws_operation.4f9131449f901200d54dd4b4232e708d.operation_script:1)&nbsp;<br>at org.mozilla.javascript.gen.sys_ws_operation_4f9131449f901200d54dd4b4232e708d_operation_script_4345.call(sys_ws_operation.4f9131449f901200d54dd4b4232e708d.operation_script)&nbsp;<br>at org.mozilla.javascript.ContextFactory.doTopCall(ContextFactory.java:563)&nbsp;<br>at org.mozilla.javascript.ScriptRuntime.doTopCall(ScriptRuntime.java:3428)&nbsp;<br>at org.mozilla.javascript.gen.sys_ws_operation_4f9131449f901200d54dd4b4232e708d_operation_script_4345.call(sys_ws_operation.4f9131449f901200d54dd4b4232e708d.operation_script)&nbsp;<br>at org.mozilla.javascript.gen.sys_ws_operation_4f9131449f901200d54dd4b4232e708d_operation_script_4345.exec(sys_ws_operation.4f9131449f901200d54dd4b4232e708d.operation_script)&nbsp;<br>at com.glide.script.ScriptEvaluator.execute(ScriptEvaluator.java:263)&nbsp;<br>at com.glide.script.ScriptEvaluator.evaluateString(ScriptEvaluator.java:110)&nbsp;<br>at com.glide.script.ScriptEvaluator.evaluateString(ScriptEvaluator.java:76)&nbsp;<br>at com.glide.script.fencing.GlideScopedEvaluator.evaluateScript(GlideScopedEvaluator.java:309)&nbsp;<br>at com.glide.script.fencing.GlideScopedEvaluator.evaluateScript(GlideScopedEvaluator.java:214)&nbsp;<br>at com.glide.script.fencing.GlideScopedEvaluator.evaluateScript(GlideScopedEvaluator.java:201)&nbsp;<br>at com.glide.rest.service.custom.CustomService.runScript(CustomService.java:95)&nbsp;<br>at com.glide.rest.service.custom.CustomService.execute(CustomService.java:82)&nbsp;<br>at com.glide.rest.handler.impl.ServiceHandlerImpl.invokeService(ServiceHandlerImpl.java:36)&nbsp;<br>at com.glide.rest.processors.RESTAPIProcessor.process(RESTAPIProcessor.java:271)&nbsp;<br>at com.glide.processors.AProcessor.runProcessor(AProcessor.java:483)&nbsp;<br>at com.glide.processors.AProcessor.processTransaction(AProcessor.java:205)&nbsp;<br>at com.glide.processors.ProcessorRegistry.process0(ProcessorRegistry.java:178)&nbsp;<br>at com.glide.processors.ProcessorRegistry.process(ProcessorRegistry.java:167)&nbsp;<br>at com.glide.ui.GlideServletTransaction.process(GlideServletTransaction.java:31)&nbsp;<br>at com.glide.sys.Transaction.run(Transaction.java:2038)&nbsp;<br>at java.util.concurrent.ThreadPoolExecutor.runWorker(ThreadPoolExecutor.java:1149)&nbsp;<br>at java.util.concurrent.ThreadPoolExecutor$Worker.run(ThreadPoolExecutor.java:624)&nbsp;<br>at java.lang.Thread.run(Thread.java:748)&nbsp;<br><br>2018-04-18 09:21:06 (642) API_INT-thread-1 A32A62A50F691300B04F419CE1050EFC txid=61ebae2d0f2d #5706 [REST API] RESTAPIProcessor : Mandatory Variables are required</pre></td></tr></tbody></table>

**Cause**

The catalog item contains mandatory variables that are hidden by:

-   Catalog UI Policies
-   Catalog Client Scripts
-   If a mandatory variable is hidden at runtime, the Service Portal REST API rejects the submission.

## Resolution

1.  Review all variables on the catalog item (including variable sets).
2.  Identify variables where Mandatory is checked.
3.  Check for UI Policies or Client Scripts that hide these variables.
4.  If a mandatory variable is hidden, uncheck the Mandatory flag at the variable level.
5.  If no scripts hide mandatory variables but the issue persists:
6.  Ensure the portal page uses the out-of-the-box “SC Catalog Item” widget.

**Issue 3: Service Portal Catalog Item Search Returns No Results**

### Symptoms

Typeahead search in the Service Portal does not return the expected catalog items.

## Cause

The catalog item is not included in the catalog referenced by the sp\_portal record used by the current portal.

## Resolution

1.  Open the sp\_portal record for the portal where the search is performed.
2.  Check the Catalog field.
3.  Ensure the catalog item is included in the catalog associated with that portal.

### Release

All versions included

### Resolution

Each issue has a separate resolution in its own column. Kindly refer under resolution heading. 

### Related Links
