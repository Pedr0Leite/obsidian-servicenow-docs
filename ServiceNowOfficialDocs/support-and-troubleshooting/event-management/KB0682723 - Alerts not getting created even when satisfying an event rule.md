---
title: "Alerts not getting created even when satisfying an event rule"
aliases:
  - KB0682723
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0682723
kb_number: KB0682723
last_modified: 2025-01-03
---

## Alerts not getting created even when satisfying an event rule

  

### Issue

# Symptoms

* * *

Issue: Alerts not being created even when there is a valid event rule. It fails with following error in the Node logs.

Java.lang.IllegalArgumentException: No value for:   
at com.snc.sw.kb.ClassificationEnum.getValueFromNumericValue(ClassificationEnum.java:31)   
at com.glideapp.itom.snac.processor.EventTransformationHandler.process(EventTransformationHandler.java:56)   
at com.glideapp.itom.snac.processor.EvtMgmtEventProcessor.applyEventHandlers(EvtMgmtEventProcessor.java:589)   
at com.glideapp.itom.snac.processor.EvtMgmtEventProcessor.processEvent(EvtMgmtEventProcessor.java:564)   
at com.glideapp.itom.snac.processor.EvtMgmtEventProcessor.processEventsForShard(EvtMgmtEventProcessor.java:423)   
at com.glideapp.itom.snac.processor.EvtMgmtEventProcessor.processEvents(EvtMgmtEventProcessor.java:390)   
at com.glideapp.itom.snac.processor.EvtMgmtEventProcessor.processHelper(EvtMgmtEventProcessor.java:301)   
at com.glideapp.itom.snac.processor.EvtMgmtEventProcessor.processHandling(EvtMgmtEventProcessor.java:263)   
at com.glideapp.itom.snac.processor.EvtMgmtEventProcessor.process(EvtMgmtEventProcessor.java:218)   
at com.glideapp.itom.snac.processor.EvtMgmtEventProcessor.jsFunction\_process(EvtMgmtEventProcessor.java:203)   
at sun.reflect.GeneratedMethodAccessor389.invoke(Unknown Source)   
at sun.reflect.DelegatingMethodAccessorImpl.invoke(DelegatingMethodAccessorImpl.java:43) 

# Release

* * *

All Releases

# Cause

* * *

When events are processed, it also looks to map the classification of the event when creating an alert. It looks to classify an alert based on the value from the event. Example: IT, Security.

_Classification value_ is a mandatory field for the alert to be created. If you are mapping the Classification to a null value in the event transform rule, Alert creation will fail with the mentioned exception. 

# Resolution

* * *

Do not map classification to null in your event transform rule.
