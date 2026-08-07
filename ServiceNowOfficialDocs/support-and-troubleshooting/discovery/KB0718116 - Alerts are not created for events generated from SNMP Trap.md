---
title: "Alerts are not created for events generated from SNMP Trap"
aliases:
  - KB0718116
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0718116
kb_number: KB0718116
last_modified: 2024-04-07
---

## Alerts are not created for events generated from SNMP Trap

  

### Issue

Alerts are not created for events generated from SNMP Traps.

#   

### Cause

1.  In the logs, below exception is thrown.  
      
    No value for: <place\_holder>: java.lang.IllegalArgumentException: No value for: <place\_holder>: com.snc.sw.kb.ClassificationEnum.getValueFromNumericValue(ClassificationEnum.java:31)   
    com.glideapp.itom.snac.processor.EventTransformationHandler.process(EventTransformationHandler.java:57)   
    com.glideapp.itom.snac.processor.EvtMgmtEventProcessor.applyEventHandlers(EvtMgmtEventProcessor.java:589)   
    com.glideapp.itom.snac.processor.EvtMgmtEventProcessor.processEvent(EvtMgmtEventProcessor.java:564)   
    com.glideapp.itom.snac.processor.EvtMgmtEventProcessor.processEventsForShard(EvtMgmtEventProcessor.java:423)   
    com.glideapp.itom.snac.processor.EvtMgmtEventProcessor.processEvents(EvtMgmtEventProcessor.java:390)   
    com.glideapp.itom.snac.processor.EvtMgmtEventProcessor.processHelper(EvtMgmtEventProcessor.java:301)   
    com.glideapp.itom.snac.processor.EvtMgmtEventProcessor.processHandling(EvtMgmtEventProcessor.java:263)   
    com.glideapp.itom.snac.processor.EvtMgmtEventProcessor.process(EvtMgmtEventProcessor.java:218)   
    com.glideapp.itom.snac.processor.EvtMgmtEventProcessor.jsFunction\_processWithLimit(EvtMgmtEventProcessor.java:212)   
    sun.reflect.GeneratedMethodAccessor113.invoke(Unknown Source)   
    sun.reflect.DelegatingMethodAccessorImpl.invoke(DelegatingMethodAccessorImpl.java:43)   
    java.lang.reflect.Method.invoke(Method.java:498)   
    org.mozilla.javascript.MemberBox.invoke(MemberBox.java:138)   
    org.mozilla.javascript.FunctionObject.doInvoke(FunctionObject.java:670)   
    org.mozilla.javascript.FunctionObject.call(FunctionObject.java:614)   
    org.mozilla.javascript.ScriptRuntime.doCall(ScriptRuntime.java:2582)   
    org.mozilla.javascript.optimizer.OptRuntime.call2(OptRuntime.java:42)   
    .....  
    .....  
    .....

             2. The issue was with the 'Classification' value(static) defined in the event rule.   
             3. When the event was being processed, the system couldn't find the static value in choice list configured for 'Classification'.   
             4. The 'Classification' value should be an integer. The system will pick the mapping value from sys\_choice table.   
           

### Resolution

 Modified the event rule classification field value to ${classification}.  
 Eg: The raw value from the event is '0'
