---
title: "Manage Lifecycle Event \"Activity Sets\" tab won't load"
aliases:
  - KB2817303
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB2817303
kb_number: KB2817303
last_modified: 2026-03-04
---

## Manage Lifecycle Event "Activity Sets" tab won't load

  

### Issue

When navigating to the Manage Lifecycle Events "Activity Sets" tab, it won't load, showing the following error:  
"There was an unexpected error, refresh the page"![](/sys_attachment.do?sys_id=4798fe2f971b36d085e13bbe2153afdd)

### Symptoms

`RhinoExceptions *** ERROR *** JavaScript evaluation error on:`  
`(function process(/*RESTAPIRequest*/ request, /*RESTAPIResponse*/ response) {`  
`var leBuilderUtils = new hr_BuilderUtils();`  
`var type_id = request.queryParams.type_id.toString();`  
  
`return leBuilderUtils.getHRServicesForType(type_id);`  
  
`})(request, response);`  
`Stack trace:`  
`at sys_script_include.3f37f54623b31300fb0c949e27bf65ca.script:18`  
`at sys_script_include.d22e7bdbc0a8016500a18e024bfc9aa3.script:11`  
`at sys_ws_operation.baf8ded65f2033001fb28fb3de73138b.operation_script:2 (process)`  
`at sys_ws_operation.baf8ded65f2033001fb28fb3de73138b.operation_script:7`  
`Root cause of JavaScriptException: java.lang.NullPointerException`  
  
`java.lang.NullPointerException      `Following stacktrace, you will see that it touches the GlideChoiceList API Class:`   var hrTaskTypeChoices = new GlideChoiceList.getChoiceList("sn_hr_core_task", "hr_task_type");`  
  

### Release

Any

### Cause

Caused by defect PRB1874183

### Resolution

  
Run the below script from background scripts to clear and rebuild the cache for those specific choice on the affected table:  
  
`gs.info("Cached value: " + GlideCacheManager.get('sys_choice_compiled','sn_hr_core_task.hr_task_type.null.en.1.true'));`  
`gs.info("START remove cached entry...");`  
`GlideCacheManager.remove('sys_choice_compiled','sn_hr_core_task.hr_task_type.null.en.1.true');`  
`gs.info("FINISHED remove cached entry.");`  
`gs.info("Cached value: " + GlideCacheManager.get('sys_choice_compiled','sn_hr_core_task.hr_task_type.null.en.1.true'));`  
`gs.info("Retrieving choice list (rebuilds if not in cache).")`  
`var choiceList = GlideChoiceList.getChoiceList('sn_hr_core_task', 'hr_task_type');`  
`gs.info("ChoiceList.toJSON(): " + choiceList.toJSON());`  
`gs.info("Cached value: " + GlideCacheManager.get('sys_choice_compiled','sn_hr_core_task.hr_task_type.null.en.1.true'));`  
`gs.info("Calling choiceList.removeNone()");`  
`choiceList.removeNone();`  
`gs.info("Object toJSON() AFTER: " + choiceList.toJSON());`  
`gs.info("Cached value: " + GlideCacheManager.get('sys_choice_compiled','sn_hr_core_task.hr_task_type.null.en.1.true'));`  
`gs.info("Removing cached entry so that it is rebuilt for the next user.");`  
`GlideCacheManager.remove('sys_choice_compiled','sn_hr_core_task.hr_task_type.null.en.1.true');`
