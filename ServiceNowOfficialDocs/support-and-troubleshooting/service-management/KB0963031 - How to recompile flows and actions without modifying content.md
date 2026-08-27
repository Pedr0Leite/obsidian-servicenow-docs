---
title: "How to recompile flows and actions without modifying content"
aliases:
  - KB0963031
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0963031
kb_number: KB0963031
last_modified: 2025-10-16
---

## How to recompile flows and actions without modifying content

  

**Before you begin**

Consult with ServiceNow before performing these steps. Recompiling can resolve some issues but may make it difficult to determine the root cause.

**Beginning with the San Diego release**

To recompile a flow, run this script:

var compiledSuccessfully = sn\_fd.FlowAPI.getRunner().flow('scope.my\_flow\_name').compile();

This is the same as:

var compiledSuccessfully = sn\_fd.FlowAPI.getRunner().flow('scope.my\_flow\_name').compile(false);

To force a recompile even if not needed, run this script: 

var compiledSuccessfully = sn\_fd.FlowAPI.getRunner().flow('scope.my\_flow\_name').compile(true);

To recompile a subflow, run this script:

var compiledSuccessfully = sn\_fd.FlowAPI.getRunner().subflow('scope.my\_subflow\_name').compile();

To recompile an action, run this script:

var compiledSuccessfully = sn\_fd.FlowAPI.getRunner().action('scope.my\_action\_name').compile();

**Prior to the San Diego release**

To recompile a flow or action without modifying content in releases prior to San Diego, run the following script. Use the sys\_hub\_flow table name for flows or sys\_hub\_action\_type\_definition table name for actions. The recompilation occurs the next time the flow runs. 

gr = new GlideRecord('<tablename>');  
// TODO add your query here  
gr.query();  
   while (gr.next()) {  
      // this won't impact Kingston action/flows which didn't have a master snapshot  
      if (JSUtil.nil(gr.getValue("master\_snapshot")))  
         continue;  
      gr.setValue("latest\_snapshot", gr.getValue("master\_snapshot"));  
      // setWorkflow(false) so this won't go in updateSets  
      gr.setWorkflow(false);  
      gr.update();  
}
