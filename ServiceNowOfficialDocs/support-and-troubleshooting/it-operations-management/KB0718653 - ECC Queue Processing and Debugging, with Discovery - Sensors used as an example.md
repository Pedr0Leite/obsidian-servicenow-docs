---
title: "ECC Queue Processing and Debugging, with \"Discovery - Sensors\" used as an example"
aliases:
  - KB0718653
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0718653
kb_number: KB0718653
last_modified: 2025-09-09
---

## ECC Queue Processing and Debugging, with "Discovery - Sensors" used as an example

  

### Issue

The External Communication Channel (ECC) Queue displays input and output messages from and to MID Servers. The ECC Queue is the normal connection point between an instance and other systems that integrate with it, most commonly a MID Server. Messages are classified as Input (from a MID Server to the instance) or Output (from the instance to a MID server).

### ECC Queue Processing

ecc\_queue input records are processed by business rules (BR). Note that not all business rules processing ecc\_queue inputs will set such inputs to processed. Therefore, it may be expected that some ecc\_queue inputs will remain in ready state.

As an example, the business rule for processing discovery inputs is “Discovery - Sensors”. This BR in specific will set the state to processed for discovery inputs.

Where the condition is determined by the AutomationEccSensorConditions script, which decides if this is a discovery payload and whether to process it via a sensor:

AutomationEccSensorConditions.discovery(current)

And the script for the business rule is: (the Paris release added the additional information to the Job names, to aid tracing problematic jobs back to the ECC Queue)

var script = "var job = new DiscoverySensorJob();\\njob.process();";  
  
var probe = current.name;  
var name = current.getValue('name');  
var source = current.getValue('source');  
var sys\_id = current.getValue('sys\_id');  
var jobName;  
if (gs.nil(probe) || probe.indexOf('MultiPage') == -1)  
 jobName = 'ASYNC: Discovery - Sensors ' + name + ' (' + source + ') ' + sys\_id;  
else  
 jobName = 'ASYNC: Discovery - MultiPage Sensors ' + name + ' (' + source + ') ' + sys\_id;  
  
var sched = new SchedulePriorityECCJob(jobName, current, script);  
sched.schedule();

The script above is calling SchedulePriorityECCJob to create a sys\_trigger job. The payload is actually processed via a scheduled job. Therefore, the payload is not processed in the same session as the user logged in, or the SOAP Semaphore thread used by the MID Server. Because the payload is processed via a scheduled job and the session is not the same as the user logged in, it would not normally be possible to debug a sensor via the script debugger by re-processing a payload.  However, the "Run again (debug)" related link" on the ECCQueue input record form, added in New York, does allow re-running the sensor in the user transaction, so session debug can be used.

The SchedulePriorityECCJob also determines the priority of the job. For reference, here is the code from SchedulePriorityECCJob, at the time of this writing:

gs.include("Schedule");  
var SchedulePriorityECCJob = Class.create();  
SchedulePriorityECCJob.prototype = Object.extendsObject(Schedule,{  
 initialize: function(label, document, script) {  
  Schedule.prototype.initialize.call(this);  
  this.time = new GlideDateTime();  
  this.setDocument(document);  
  this.trigger\_type = 0;  
  this.script = script;  
  this.label = label;  
  this.priority = document.priority;  
  this.runAsUser = GlideUser.getUserByID(document.sys\_created\_by).getID();  
 },  
  
 setTime: function(time) {  
  this.time = time;  
 },  
  
 schedule: function() {  
  var t = this.\_getTrigger();  
    
  if (!gs.nil(this.document))  
   t.document = this.document;  
    
  if (!gs.nil(this.script))  
   t.script = this.script;  
    
  if (!gs.nil(this.label))  
   t.label = this.label;  
    
  // get the priority from current  
  if (!gs.nil(this.priority)) {  
   if (this.priority == 0) //interactive  
    t.priority = gs.getProperty('glide.ecc.async.priority.interactive', 50);  
   if (this.priority == 1) //expedited  
    t.priority = gs.getProperty('glide.ecc.async.priority.expedited', 105);  
   if (this.priority == 2) //standard  
    t.priority = gs.getProperty('glide.ecc.async.priority.standard', 110);  
  }  
  
  t.job\_context = 'fcRunAs=' + this.runAsUser;  
  t.trigger\_type = this.trigger\_type;  
  t.next\_action = this.time;  
  gs.print("Scheduling: " + this.label + " for: " + t.next\_action.getDisplayValue());  
  return t.insert();  
 },  
  
 type: 'SchedulePriorityECCJob'  
});  
  
The trigger record will be queued and the payload will be processed once assigned to a worker. 

**Important Note**: An interactive priority ecc\_queue job will cause a very high priority sys\_trigger job, potentially blocking some important instance platform jobs using the default 100 priority from running, if there are lots of the jobs and they are quite long running.

The following image illustrates the order of events:

![](/sys_attachment.do?sys_id=d8dc6ceedb42b450e515c223059619df)

### Debug Processing of ECC Queue Records

To be able to use script debugger, we need to be able to process the payload on the same session as the debugger. We review the business rule which processes the ECC queue record of interest, and the actual code which processes the payload. As an example for discovery, we see that the business rule calls "SchedulePriorityECCJob" and passes "var job = new DiscoverySensorJob(); job.process();" as the script. Reviewing "DiscoverySensorJob.process()" we find that SncSensorProcessor.process() processes the payload.

**Note**: The following will work when debugging script includes called by sensors. Sensors do not trigger the debugger directly.

Therefore, after review of the business rules and script includes we determine we can process the payload as follows:

1.  Get the sys id of the ecc\_queue record
2.  Go to "System Definition > Scripts - Background"
3.  Run the following script, replace <ecc\_queue\_sys\_id> with the correct sys ID.

var eccRecord = new GlideRecord('ecc\_queue');
eccRecord.get(‘<ecc\_queue\_sys\_id>');
var sp = new SncSensorProcessor(eccRecord);
sp.process(); 

Update: Since the New York version, the Related link "Run Again (Debug)" on the ecc\_queue input form will avoid you needing to run this script. It does the same thing, but with one click.

### Related Links

Documentation links:

-   [MID Server ECC Queue](https://docs.servicenow.com/csh?topicname=ecc-queue-mid-server.html&version=latest)
-   [The ECC queue for Discovery](https://docs.servicenow.com/csh?topicname=r_DiscoveryStatusECCQueue.html&version=latest)
-   [Script Debugger and Session Log](https://docs.servicenow.com/csh?topicname=script-debugger.html&version=latest "Script Debugger and Session Log")  
    -   [Set or remove breakpoints](https://docs.servicenow.com/csh?topicname=set-remove-breakpoints.html&version=latest "Set or remove breakpoints")
