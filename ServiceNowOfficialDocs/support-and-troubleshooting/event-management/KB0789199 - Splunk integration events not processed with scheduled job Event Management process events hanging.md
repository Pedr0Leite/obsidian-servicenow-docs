---
title: "Splunk integration events not processed with scheduled job Event Management process events hanging"
aliases:
  - KB0789199
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0789199
kb_number: KB0789199
last_modified: 2024-04-07
---

## Splunk integration events not processed with scheduled job Event Management process events hanging

  

### Issue

On splunk events aren't processed. The processing script keeps crashing after a period of time. The events in em\_event table never move from ready state

### Release

After upgrade to New York release (was not seen in customer's London patch 10 instance)

### Cause

the worker threads show 

org.mariadb.jdbc.internal.io.input.StandardPacketInputStream.getPacketArray(StandardPacketInputStream.java:262)  
org.mariadb.jdbc.internal.com.read.resultset.SelectResultSet.readNextValue(SelectResultSet.java:431)  
org.mariadb.jdbc.internal.com.read.resultset.SelectResultSet.addStreamingValue(SelectResultSet.java:416)  
org.mariadb.jdbc.internal.com.read.resultset.SelectResultSet.nextStreamingValue(SelectResultSet.java:403)  
org.mariadb.jdbc.internal.com.read.resultset.SelectResultSet.next(SelectResultSet.java:647)  
com.glide.db.meta.RowFetcher.fetchRows(RowFetcher.java:195)  
com.glide.db.meta.RowFetcher.fetchFullRows(RowFetcher.java:124)  
com.glide.db.meta.RowFiller.fetchFullRows(RowFiller.java:90)  
com.glide.db.meta.RowFiller.fillRows(RowFiller.java:81)  
com.glide.db.meta.Table.getStorage(Table.java:745)  
com.glide.db.meta.TableIterator.getStorageForCurrent(TableIterator.java:122)  
com.glide.db.meta.TableIterator.next(TableIterator.java:55)  
com.glide.script.GlideRecordITable.next(GlideRecordITable.java:459)  
com.glide.script.GlideRecord.next(GlideRecord.java:6480)  
com.glide.script.HistoryWalker.applyHistoryBackwards(HistoryWalker.java:356)  
com.glide.script.HistoryWalker.jumpToPreviousStableUpdate(HistoryWalker.java:343)  
com.glide.script.HistoryWalker.walkForwards(HistoryWalker.java:210)  
com.glide.script.HistoryWalker.walkTo(HistoryWalker.java:113)  
com.glide.script.AbstractWalker.walkForward(AbstractWalker.java:242)  
com.glide.script.fencing.ScopedHistoryWalker.jsFunction\_walkForward(ScopedHistoryWalker.java:194)  
sun.reflect.GeneratedMethodAccessor2251.invoke(Unknown Source)  
sun.reflect.DelegatingMethodAccessorImpl.invoke(DelegatingMethodAccessorImpl.java:43)  
java.lang.reflect.Method.invoke(Method.java:498)  
org.mozilla.javascript.MemberBox.invoke(MemberBox.java:138)  
org.mozilla.javascript.FunctionObject.doInvoke(FunctionObject.java:670)  
org.mozilla.javascript.FunctionObject.call(FunctionObject.java:614)  
org.mozilla.javascript.ScriptRuntime.doCall(ScriptRuntime.java:2582)  
org.mozilla.javascript.optimizer.OptRuntime.callProp0(OptRuntime.java:85)  
org.mozilla.javascript.gen.sys\_script\_include\_24a759e30a0a2c3960e024ad3b60d9e8\_script\_22209.\_c\_anonymous\_32(sys\_script\_include.24a759e30a0a2c3960e024ad3b60d9e8.script:970)  
org.mozilla.javascript.gen.sys\_script\_include\_24a759e30a0a2c3960e024ad3b60d9e8\_script\_22209.call(sys\_script\_include.24a759e30a0a2c3960e024ad3b60d9e8.script)  
org.mozilla.javascript.ScriptRuntime.doCall2(ScriptRuntime.java:2651)  
org.mozilla.javascript.ScriptRuntime.doCall(ScriptRuntime.java:2590)  
org.mozilla.javascript.optimizer.OptRuntime.call1(OptRuntime.java:32)  
org.mozilla.javascript.gen.sys\_script\_include\_24a759e30a0a2c3960e024ad3b60d9e8\_script\_22209.\_c\_anonymous\_13(sys\_script\_include.24a759e30a0a2c3960e024ad3b60d9e8.script:311)  
org.mozilla.javascript.gen.sys\_script\_include\_24a759e30a0a2c3960e024ad3b60d9e8\_script\_22209.call(sys\_script\_include.24a759e30a0a2c3960e024ad3b60d9e8.script)

it seems to get stuck in a ServiceManagement script include called: TaskSLAController

the script include is performing a search on the instance in the following tables (and never seems to complete):

sys\_history\_line0002 (300K count) and more specifically sys\_audit (4 million record count) 

there was just under 2 million records in the sys\_audit table related to updates during this time for:

x\_splu2\_splunk\_ser\_url which is field in the incident table (which is audited by default because the incident table itself is audited) also we could see updates related to correlation\_id

### Resolution

'The audit table has many updates related to the incident table. Since this table is audited by default the recommendation from our performance team is to exclude the auditing on the following field specifically (which seems to have been created in the incident table by the splunk integration)  
  
field "x\_splu2\_splunk\_ser\_splunk\_url"  
  
https://kadasteront.service-now.com/sys\_dictionary.do?sys\_id=ac3468a4dbf37640097d76100f9619fd&sysparm\_view=&sysparm\_record\_target=sys\_dictionary&sysparm\_record\_row=1&sysparm\_record\_list=name%3Dincident%5EelementCONTAINSx\_splu2%5EORDERBYname&sysparm\_record\_rows=1  
  
In order to do this you will need to follow the documentation to: exclude a field from auditing  
  
https://docs.servicenow.com/csh?topicname=t\_ExcludeAFieldFromBeingAudited.html&version=latest  
  
Also there needs to be some work to clean up the sys\_history\_line0002 and sys\_audit tables related to fields:

x\_splu2\_splunk\_ser\_splunk\_url (this maybe different in other instances depending on the splunk integration configuration) and correlation\_id (should probably work with splunk support in this case)
