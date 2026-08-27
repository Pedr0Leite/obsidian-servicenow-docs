---
title: "How SLAs Really Work"
aliases:
  - KB0529411
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0529411
kb_number: KB0529411
last_modified: 2026-06-03
---

## How SLAs Really Work

  

### Issue

There are many moving parts to the SLA engine and the engine itself has changed multiple times over the last several years. This article:

-   provides a brief explanation of the workings of the current SLA engine called the 2011 engine (com.snc.sla.engine.version)
-   gives steps for troubleshooting SLA issues

### How it works

From an event-driven perspective, the SLA process starts with a task table. Somebody or something does one of the following:

-   submits an incident
-   updates a problem
-   requests a service catalog item

When this happens, a business rule named **Run SLAs** kicks off. This business rule calls a script include named **TaskSLAController**. The TaskSLAController is the gateway to the SLA engine.

#### Transitions

As of the June 2011 re-write of the SLA engine, most of the real work for SLAs is handled by script includes. The code is written in a reusable and encapsulated way that allows extension and customization. It also makes for much more easily understood code and a grouping of tasks into logical parts. Probably the most creative and helpful example of this encapsulation is the code that handles the transitions between stages. The key component of this is a base class script include (SLAConditionBase) with methods that can easily be overwritten should you need custom functionality. (For more information, see [SLA condition rules](https://docs.servicenow.com/csh?topicname=c_SLAConditionRules.html&version=latest "SLA condition rules").) If you notice that your stages are mysteriously changing to **Complete** when you expect them to be **Achieved**, part of this mechanism may not be configured properly. If you notice systemic issues with calculations or SLA operation, one of the core script includes may have been customized and not updated during your last upgrade.

#### Workflow

Starting with the 2010 engine (introduced in one of the later Spring 2010 patches), SLA workflows have been used only for notification purposes. Before that time they were used to update fields and manage escalations. If you are not receiving the notifications you expect or are not receiving them at the correct times, workflow is the place to look for issues.

#### Breach timers

Breach timers are sys\_trigger records (in the **System Scheduler > Scheduled Jobs** module). This is a very central table that handles all items scheduled in the system. Every time that an SLA goes moves to **In Progress**, a breach timer is generated that expires at the time indicated in the **Planned End Time** field. When the breach timers expire, they call TaskSLA.breachTimerExpired(). There are not many issues with breach timers. If you did have an issue, then it might look like incidents that breach later than they should. Sys\_trigger records are not destroyed during a restart and there are no normal reasons for them to stop running unless something extreme such as an out-of-memory error occurs. If your sys\_trigger queue is backed up, all jobs in the queue stop running. Not only do SLAs stop breaching, but workflow notifications are not sent because workflow timers also run on sys\_trigger records. Everything that can be scheduled is scheduled in the sys\_trigger table.

#### Calculate on display

What updates SLAs? If you reported on SLAs and ran the same report twice, you would notice that the elapsed percentage fields on **In Progress** SLAs do not change. In some cases, customers call ServiceNow customer support and wonder why they can open an incident, then twenty seconds later look at the **Elapsed Percentage** field and it is still at zero. The problem is that the calculated fields on SLAs are not magically upgraded in real-time. Unless you turn on the glide.sla.calculate\_on\_display property, the calculations are not even upgraded when you look at the incident. The reason is that SLA calculations are only updated when an event occurs. By default this is when:

-   the conditions are met for the task\_sla to go through a transition
-   a breach timer expires
-   a calculation job runs (more information below)

Even if you turn on the glide.sla.calculate\_on\_display system property (sys\_property table), you will not receive the results you expect when looking at the task\_sla table directly or through the reporting engine. This is because the Calculate on Display business rule only runs when a user looks at a task record, not a task\_sla record. Consider this when planning and designing SLA reporting.

#### Calculation jobs

Calculation jobs are scheduled jobs (sys\_trigger table) that run at different intervals and update the calculated values of SLAs that will breach soon or have already breached. These calculation jobs help keep more reliable calculated values for SLAs that are near breach. For example, if you search in the scheduled jobs table for jobs that start with **SLA Update** you will find a number of jobs. One of the scheduled jobs runs every minute and updates all SLAs that will breach within 10 minutes.

### Troubleshooting

Most SLA issues take time and effort to solve. Sometimes the effort is in understanding how the SLA engine should be expected to operate (so kudos to you for reading this article). The time and effort are worthwhile because, for many companies, SLAs are the primary performance metric.

The best way to start out is to determine exactly what the expected behavior is. Consider the different areas mentioned above. What mechanism controls the behavior that you believe is acting unexpectedly? What version of the SLA engine are you running and are there any customizations?

#### Desk check

This background script grabs almost all of the pertinent details and outputs them in a timeline. The script is fairly simple on the display side, but it:

-   outputs all the configuration information for the schedule, workflow, and SLA definition
-   outputs a timeline of all the related activity, including the activities of the active workflow context, changes to task fields that affect the task SLA transitions, and the current values of the SLA calculations themselves

Note that the script does not force an update to the task SLA calculations, so it is only as accurate as the last calculation time. (This would be a nice feature to add in the future.)

```
/*
 * @Usage - Currently the following two examples are the way I
 * imagine this object being used. The first example will return a
 * report of a specified number of task_sla's. The second example
 * takes a sys_id of a task_sla record and returns a report about
 * that task_sla.
 */
var dCheck = newDCheck();
var filters = [{
    "field": "end_time",
    "operator": "!=",
    "value": ""
  },
  {
    "field": "sys_created_on",
    "operator": ">",
    "value": "2012-04-13 21:00:00"
  },
  {
    "field": "sys_created_on",
    "operator": "<",
    "value": "2012-04-13 23:00:00"
  }
];
gs.print(dCheck.getLatestByDefinition('name', 'ADSK - Incident- P3 Resolution(5 Days) ', 3, filters));
gs.print(dCheck.getSlaTimeline('5161366d0a0a0b3000d59bf577381424'));

/*
 * @Description - This script speeds up the information gathering process
 * about an existing task_sla. It outputs information about the
 * contract_sla (SLA Definition), task (Incident, Problem, etc.), task_sla
 * (running SLA), wf_context (Running Workflow) and wf_history (History
 * of the running Workflow). First it outputs information about the
 * definitions of the above items and then it compiles the history of
 * changes to each item and orders them by timestamp so that you can piece
 * together expected vs. actual behavior. See bottom of script for usage
 * information.
 */
function newDCheck() {
  return {

    //Specify sys_id of the SLA definition
    //@param fld {string} field of SLA Definition to query
    //@param value {string} value to match agains fld
    //@param filters {array} array of objects in format [{field:"",op:"",value:""},...]
    getLatestByDefinition: function(fld, value, test, filters) {
      if (typeof tests == "undefined")
        tests = 3; //number of sla's to test
      var out = ["NOTE: All times in GMT\n"];

      var sld = new GlideRecord("contract_sla");
      sld.addQuery(fld, value);
      sld.query();
      while (sld.next()) {
        //Print conditions from SLA definition
        out.push(this.printSlaDefinition(sld));

        //Pull out the field names
        var flds = this.getSlaConditions(sld);
        out.push("fields from conditions: " + flds.join());

        //Print information about the SLA schedule SKIPPED

        //Get group of task_sla records
        var slt = new GlideRecord("task_sla");
        slt.addQuery("sla", sld.sys_id + "");
        slt.addQuery("sys_created_on", "<", gs.daysAgoStart(1));
        if (filters)
          for (var iz = 0; iz < filters.length; iz++)
            slt.addQuery(filters[iz].field, filters[iz].operator, filters[iz].value);
        slt.orderByDesc("sys_created_on");
        slt.setLimit(tests);
        slt.query();
        //For each task_sla
        id = 0;
        while (slt.next()) {
          out.push("\n*******" + ++id + "*******");
          out.push(this.getSlaTimeline(slt, flds));
        }
      }
      return out.join("\n");
    },

    printSlaDefinition: function(contract) {
      var out = [];
      var sldFlds = ['name', 'workflow', 'collection', 'duration', 'duration_type', 'retroactive', 'set_start_to', 'schedule', 'timezone', 'type', 'start_condition', 'stop_condition', 'pause_condition', 'reset_condition'];
      for (var ia = 0; ia < sldFlds.length; ia++)
        out.push("contract_sla." + sldFlds[ia] + ": " + contract[sldFlds[ia]]);

      return out.join("\n");
    },

    getSlaConditions: function(contract) {
      var conds = ['start_condition', 'stop_condition', 'pause_condition', 'reset_condition'];
      var flds = [];
      for (var ib = 0; ib < conds.length; ib++) {
        var cond = contract[conds[ib]].split("^");
        for (var ic = 0; ic < cond.length; ic++) {
          var fld = cond[ic].split(/[^a-z_]/)[0];
          if (fld) flds.push(fld);
        }
      }
      return flds;
    },

    timeline: {
      _timeline: [],

      sort: function() {
        return this._timeline.sort();
      },

      push: function(value) {
        var i = this._timeline.length;
        while (i--)
          if (this._timeline[i] === value) return;
        this._timeline.push(value);
      },

      join: function(delim) {
        return this._timeline.join(delim);
      },

      reset: function() {
        this._timeline = new Array();
      }
    },

    getSlaTimeline: function(sla, condFlds) {
      //var timeline = [];
      var fields = [];

      if (typeof sla == "string") {
        var sltask = new GlideRecord("task_sla");
        sltask.get(sla);
        sla = sltask;
        fields.push(this.printSlaDefinition(sla.sla));
      } else if (!sla) return;
      if (!condFlds) condFlds = this.getSlaConditions(sla.sla);

      //Print task information (retroactive value, any field in conditions...)
      if (sla.task) {
        var taskRec = new GlideRecord("task");
        taskRec.addQuery("sys_id", sla.task + "");
        taskRec.query();
        if (taskRec.next()) {
          var tFlds = ['sys_id', 'number', sla.sla.set_start_to];
          for (var ih = 0; ih < tFlds.length; ih++)
            fields.push("task." + tFlds[ih] + ": " + sla.task[tFlds[ih]]);
          //Add task information to timeline (sys_created_on, sys_updated_on...)

          for (var ii = 0; ii < condFlds.length; ii++) {
            //Query audit tables for all field names from the conditions list ordered by Created On
            var aud = new GlideRecord("sys_audit");
            aud.addQuery("documentkey", sla.task.sys_id + "");
            aud.addQuery("fieldname", condFlds[ii]);
            aud.orderBy("sys_created_on");
            aud.query();
            if (aud.getRowCount() == 0) this.timeline.push(sla.task.sys_created_on + " Orig " + condFlds[ii] + ": " + sla.task[condFlds[ii]]);
            while (aud.next()) {
              this.timeline.push(aud.sys_created_on + " Task " + aud.fieldname + " old:" + aud.oldvalue + " new:" + aud.newvalue);
            }
            //Add audit information to timeline
          }
        } else { //bad reference
          fields.push("ERROR: task is a bad reference");
        }
      }

      //Print task_sla information
      var sFlds = ['sys_id', 'task', 'start_time', 'end_time', 'planned_end_time', 'duration', 'percentage', 'pause_time', 'pause_duration', 'stage', 'has_breached', 'sys_created_on', 'sys_updated_on'];
      for (var ie = 0; ie < sFlds.length; ie++)
        fields.push("task_sla." + sFlds[ie] + ": " + sla[sFlds[ie]]);

      //Add task_sla information to timeline (start_time, end_time, planned_end)
      var tlFlds = ['start_time', 'end_time', 'pause_time', 'planned_end_time', 'sys_created_on', 'sys_updated_on'];
      for (var ig = 0; ig < tlFlds.length; ig++)
        this.timeline.push(sla[tlFlds[ig]] + " SLA " + tlFlds[ig]);

      //Query wf_context for this task_sla
      var wf = new GlideRecord("wf_context");
      //Print wf_context info
      wf.addQuery("id", sla.sys_id + "");
      wf.query();
      //Query all Activities in the wf_context
      while (wf.next()) {
        fields.push("wf_context.name: " + wf.name);
        fields.push("wf_context.started: " + wf.started);
        fields.push("wf_context.ended: " + wf.ended);
        //Add Activity start/end to timeline
        var wfe = new GlideRecord("wf_history");
        wfe.addQuery("context", wf.sys_id + "");
        wfe.query();
        while (wfe.next()) {
          this.timeline.push(wfe.started + " WF " + wfe.activity.name + " (activity) began");
          this.timeline.push(wfe.ended + " WF " + wfe.activity.name + " (activity) ended");
        }
      }

      var slaTimeline = fields.join("\n") + "\n**Timeline (GMT)**\n" + this.timeline.sort().join("\n");
      this.timeline.reset();
      return slaTimeline;
    }
  }
}
```
