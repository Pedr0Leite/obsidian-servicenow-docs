---
title: "Catalog Item REST Failure on Order Now"
aliases:
  - KB0717979
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0717979
kb_number: KB0717979
last_modified: 2024-04-07
---

## Issue

Symptoms

* * *

When pressing 'Order Now' against a custom Catalog Item it was stuck as 'Submitting.....'

Inspection of the browser console highlighted '404 (Not Found)' and 'REST Failure' errors:

![](sys_attachment.do?sys_id=fc0dac22db82b450e515c223059619b9)

Analysis of the node log file highlighted the following error and callstack:

11/13/18 07:10:59 (193) 34D76AFCDB71AF00D2E712523996195D JavaScript evaluation error on:  
(function process(/\*RESTAPIRequest\*/ request, /\*RESTAPIResponse\*/ response) {  
var request\_body = request.body.nextEntry();  
var quantity = '' + request\_body.sysparm\_quantity;  
var noValidation = (request\_body.sysparm\_no\_validation == 'true');

if (!/^\\+?(\[0-9\]\*)$/.test(quantity))  
throw new sn\_ws\_err.BadRequestError("Invalid Quantity value");  
else  
request\_body.sysparm\_quantity = quantity;

var itemId = '' + request.pathParams.sys\_id;  
request\_body.sysparm\_id = itemId;  
var catItem = new sn\_sc.CatItem(itemId);  
if (!catItem.canView())  
throw new sn\_ws\_err.BadRequestError("Security constraints prevent ordering of Item");

if(!noValidation) {  
var catUtil = new RestCatalogUtil();  
if (!catUtil.checkMandatoryVariables(itemId, request\_body.variables))  
throw new sn\_ws\_err.BadRequestError('Mandatory Variables are required');  
}  
var cart = new sn\_sc.CartJS("cart\_" +itemId);  
request\_body.sysparm\_cart\_name = "cart\_" +itemId;  
try {  
return cart.orderNow(request\_body);  
}catch(e) {  
gs.debug(e);  
throw new sn\_ws\_err.NotFoundError("Invalid Request");  
}  
})(request, response);  
: org.mozilla.javascript.JavaScriptException: \[object NotFoundError\] (sys\_ws\_operation.4f9131449f901200d54dd4b4232e708d.operation\_script; line 28): org.mozilla.javascript.gen.sys\_ws\_operation\_4f9131449f901200d54dd4b4232e708d\_operation\_script\_2031.\_c\_process\_1(sys\_ws\_operation.4f9131449f901200d54dd4b4232e708d.operation\_script:28)  
org.mozilla.javascript.gen.sys\_ws\_operation\_4f9131449f901200d54dd4b4232e708d\_operation\_script\_2031.call(sys\_ws\_operation.4f9131449f901200d54dd4b4232e708d.operation\_script)  
org.mozilla.javascript.ScriptRuntime.doCall2(ScriptRuntime.java:2650)  
org.mozilla.javascript.ScriptRuntime.doCall(ScriptRuntime.java:2590)  
org.mozilla.javascript.optimizer.OptRuntime.call2(OptRuntime.java:42)  
org.mozilla.javascript.gen.sys\_ws\_operation\_4f9131449f901200d54dd4b4232e708d\_operation\_script\_2031.\_c\_script\_0(sys\_ws\_operation.4f9131449f901200d54dd4b4232e708d.operation\_script:1)  
org.mozilla.javascript.gen.sys\_ws\_operation\_4f9131449f901200d54dd4b4232e708d\_operation\_script\_2031.call(sys\_ws\_operation.4f9131449f901200d54dd4b4232e708d.operation\_script)  
org.mozilla.javascript.ContextFactory.doTopCall(ContextFactory.java:563)  
org.mozilla.javascript.ScriptRuntime.doTopCall(ScriptRuntime.java:3428)  
org.mozilla.javascript.gen.sys\_ws\_operation\_4f9131449f901200d54dd4b4232e708d\_operation\_script\_2031.call(sys\_ws\_operation.4f9131449f901200d54dd4b4232e708d.operation\_script)  
org.mozilla.javascript.gen.sys\_ws\_operation\_4f9131449f901200d54dd4b4232e708d\_operation\_script\_2031.exec(sys\_ws\_operation.4f9131449f901200d54dd4b4232e708d.operation\_script)  
com.glide.script.ScriptEvaluator.execute(ScriptEvaluator.java:279)  
com.glide.script.ScriptEvaluator.evaluateString(ScriptEvaluator.java:118)  
com.glide.script.ScriptEvaluator.evaluateString(ScriptEvaluator.java:82)  
com.glide.script.fencing.GlideScopedEvaluator.evaluateScript(GlideScopedEvaluator.java:309)  
com.glide.script.fencing.GlideScopedEvaluator.evaluateScript(GlideScopedEvaluator.java:214)  
com.glide.script.fencing.GlideScopedEvaluator.evaluateScript(GlideScopedEvaluator.java:201)  
com.glide.rest.service.custom.CustomService.runScript(CustomService.java:95)  
com.glide.rest.service.custom.CustomService.execute(CustomService.java:82)  
com.glide.rest.handler.impl.ServiceHandlerImpl.invokeService(ServiceHandlerImpl.java:36)  
com.glide.rest.processors.RESTAPIProcessor.process(RESTAPIProcessor.java:271)  
com.glide.processors.AProcessor.runProcessor(AProcessor.java:483)  
com.glide.processors.AProcessor.processTransaction(AProcessor.java:205)  
com.glide.processors.ProcessorRegistry.process0(ProcessorRegistry.java:178)  
com.glide.processors.ProcessorRegistry.process(ProcessorRegistry.java:167)  
com.glide.ui.GlideServletTransaction.process(GlideServletTransaction.java:31)  
com.glide.sys.Transaction.run(Transaction.java:2038)  
java.util.concurrent.ThreadPoolExecutor.runWorker(ThreadPoolExecutor.java:1149)  
java.util.concurrent.ThreadPoolExecutor$Worker.run(ThreadPoolExecutor.java:624)  
java.lang.Thread.run(Thread.java:748)

11/13/18 07:10:59 (195) 34D76AFCDB71AF00D2E712523996195D #508476 \[REST API\] RESTAPIProcessor : Invalid Request

This was coming from line 28 of the 'Buy Item' Scripted REST Resource record, in the 'sys\_ws\_operation' table.

Release

* * *

Kingston

Cause

* * *

It was found that there was a ‘ghost’ reference against the ‘Execution Plan’ Reference field of the Catalog Item in question.

This was identified by the fact that there was the preview icon next to the field, but that the field itself contained no value.

![](sys_attachment.do?sys_id=780dac22db82b450e515c223059619bf)

Resolution

* * *

Text was entered into the ‘Execution Plan’ field, and then focus was taken from it. This resulted in an ‘Invalid Reference’ field error message being displayed against the field.

The text was then removed and the Catalog Item record saved, to overwrite any corrupted association that had previously existed.

Having done this the error on pressing ‘Order Now’ no longer occurred, and the Catalog Item request would submit successfully.
