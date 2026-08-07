---
title: "Resolving \"Exhausted Default Semaphores\" errors caused by Service Portal widgets having poorly defined record watcher (recordWatch) calls"
aliases:
  - KB0635134
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0635134
kb_number: KB0635134
last_modified: 2026-05-06
---

## Resolving "Exhausted Default Semaphores" errors caused by Service Portal widgets having poorly defined record watcher (recordWatch) calls

  

### Issue

Frequent semaphore exhaustion of the default semaphore pool for all application nodes in a ServiceNow instance. A recent deployment (or enhancement) of Service Portal widgets to use the record watcher functionality are a requirement for this article to be relevant.

In this scenario, when specific incident records are updated, a select group of users needs to be shown in real-time that this update occurred while viewing the incident widget.

 **Note:** This article discusses an example for incident records, but it could apply to any record watcher table and related widgets.

### Symptoms

#### Customer visible symptoms

-   HTTP/1.1 429 (Too Many Requests)
    
-   Long response times for page loading within ServicePortal and elsewhere within the platform
    
-   Pages "clocking" with a timer in banner
    
-   Thousands of transaction (viewable in "transactions (all users)") calls per hour to "/sp/rectangle/<some\_sys\_id.
    
    ![](sys_attachment.do?sys_id=d694be9b1b51891056b699b8bd4bcb01)
    
-   Congested semaphores as shown in /stats.do page.  The semaphore consumers of the default semaphore pool will be calls to /api/now/sp/rectangle/<some\_sys\_id>.  
      
      
    ![](sys_attachment.do?sys_id=1e94be9b1b51891056b699b8bd4bcb14)

## ServiceNow visible symptoms

-   Exhausted default semaphore constantly, as seen from BigData:  
      
    ![](sys_attachment.do?sys_id=9294be9b1b51891056b699b8bd4bcb2c)
-   F5 Logs viewed in Splunk will display thousands of calls per hour and hundreds of thousands of calls per day for each of the affected Service Portal widgets.  
      
    ![](sys_attachment.do?sys_id=1294be9b1b51891056b699b8bd4bcb35)

### Cause

Improperly configured record watcher queries within some (but not necessarily all) of the frequently called ServicePortal widgets.  Record watcher examples should show three parameters.  

The first parameter is the scope, the second parameter is the table (for example, incident) and the third parameter is query filter conditions.

Without the filter conditions being present, any update to any record in the table will force the calling widget to be reloaded. This happens for all ServicePortal users of the specific widget and results in the referenced "flood-like" symptom of semaphore exhaustion.

See the developer documentation topic [Record Watch](https://developer.servicenow.com/app.do#!/document/content/app_store_doc_sp_widgets_jakarta_c_RecordWatch?v=jakarta "developer documentation") for further details.

### Resolution

Make certain the "watched" records for a given widget are highly filtered and specific for the narrowest possible set of results.

ServiceNow support can help identify the widgets likely to be involved by using F5 load balancer logs in addition to other tools. In both the "client controller" and the "server script" widget definition, be sure to have query-limiting filter conditions, as shown in the following examples.

**Client Controller example**

function(spUtil, $scope, $timeout) {  
    /\* widget controller \*/  
    var c = this;  
    $scope.incidata = {};  
    $scope.incidata.changed = false;  
    spUtil.recordWatch($scope, "incident", "priority=1^state!=7", function(name, data)

 **Note:** The third parameter in the spUtil.recordWatch string above is critical in preventing Semaphore exhaustion.

**Server Script example**

(function() {  
    /\* populate the 'data' object \*/  
    /\* e.g., data.table = $sp.getValue('table'); \*/  
    data.incidentCount = '';  
    var gr = new GlideRecord('incident');  
    gr.addQuery('priority', 1);  
    gr.addQuery('state','!=', 7);  
    gr.query();  
    data.incidentCount = gr.getRowCount();  
})();

### Advanced Debugging and Resolution

 **Note:** Using Chrome Developer Tools, it is possible to set a breakpoint and step into watched record responses being pushed to the client and verify the returned data and filter conditions.

1.  From the Chrome Tools console, while viewing a widget that contains suspect record watcher code, "search all files", search for "record.updated," and select the object to bring up the debugger view.
    
    ![](/sys_attachment.do?sys_id=a694be9b1b51891056b699b8bd4bcb3b)
    
2.  Set a break point
    
    ![](/sys_attachment.do?sys_id=2e94be9b1b51891056b699b8bd4bcb49)
    
    For the table being "watched", locate a record that the widget user should be concerned. For example, an incident owned by another team (in this example). The record update will trigger a call to the client and in turn, will force a reload of the widget scope.
    
    The following debugger example shows the incident record update that triggers the widget reload. It is clearly not something the users would or should be seeing if the record watcher filter conditions were correct.
    
    ![](/sys_attachment.do?sys_id=5e94be9b1b51891056b699b8bd4bcb2d)
    
     **Note:** Do NOT try the next steps on a system with meaningful data, because scripted updates like the one in the example are not recommended.
    
3.  Further confirm the problem by using a mass update script (like the following example) to update all records in the watched table and then look at the network tab in Chrome Tools. This is also likely to trigger an exhausted semaphore condition but will confirm with certainty that the spUtil.recordWatch filter conditions are being ignored (or are missing).
    
    Run this script from a different browser (Firefox or Chrome in Incognito mode) via Scripts Background as admin.
    
    \~~~example script~~~  
    var gr = new GlideRecord('incident');gr.query();while(gr.next()){gr.work\_notes = '.';gr.setForceUpdate(true);gr.setWorkflow(false);gr.update();}  
    \~~~/example~~~ 
    
4.  In the user browser with the suspect widget, with Chrome Tools open, view the Network tab and then in another browser session, run the background scripts to do the mass update.
    
    ![](/sys_attachment.do?sys_id=da94be9b1b51891056b699b8bd4bcb39)
    
    If the filter conditions were being applied properly, only updates to those specific records that the user or group is concerned with would trigger a client side refresh for the widget. In this example, several thousand calls are overwhelming the systems, which leads to rapid semaphore exhaustion and severely impacts performance.
    
5.  Once proper filter conditions have been added, using the debugging steps again should show a dramatic reduction in calls for widget refreshes such that application node stability is not impacted and the system is no longer overwhelmed.
