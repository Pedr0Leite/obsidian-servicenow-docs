---
title: "Incident Management State Model"
aliases:
  - KB0564465
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0564465
kb_number: KB0564465
last_modified: 2023-10-24
---

## Incident Management State Model

  

### Issue

The **Incident Management - Core** plugin **com.snc.incident\_management** has introduced a new Incident state model starting with the Helsinki release. While this new state model is available by default for Helsinki, it is not available on upgrade. We recommend that upgrade instances not install this state model.  
  

<table class="noteTable" align="left"><tbody><tr><td style="text-align: center;"><img title="Warning" src="/Warning_25x.pngx" alt="" align="bottom" border="" hspace="" vspace=""></td><td style="text-align: left;"><strong>Warning</strong>:&nbsp;<span style="text-align: start;">If the new state model is installed on upgraded instances, then you must ensure that the old states are mapped to the new ones. This is especially important if you have made customizations, implemented workflows, added&nbsp;script includes, and added business rules</span>.</td></tr></tbody></table>

Ref. plugin activation notes:

[http://docs.servicenow.com/?context=request-inci-core&version=latest](http://docs.servicenow.com/?context=request-inci-core&version=latest)

**NOTE**: The recommendation is to not activate this plugin in upgraded instances, however, if the instance data is not used in production yet, an administrator can submit a plugin activation request in **Now Support (HI) > Service Catalog > Activate Plugin**, acknowledging the following:  
\- The plugin activation is done by SN 'maint' users through a Change Request  
\- The content of this KB article has been read and understood  
\- Provide a business case as to activate the plugin for test or initial setup on disposable data

Script includes for the State Model

* * *

The Incident module contains out-of-box the IncidentStateSNC (read-only) and IncidentState (editable) script includes.

An upgraded instance has a version that caters to the existing state model as well as the new states. This is to encourage the use of constants when writing business logic, which helps with the installation of the new state model through the Incident Management – Core plugin.

A zbooted instance has a version that fulfills the new state model as well as the old states. The constants for the old states refer to the values defined for the new state values. This is clarified in the table in the "Mapping from old state model to new state model" section below.

  
Mapping from old state model to new state model

* * *

The table below represents the mapping of incidents state from the old state model to the new state model.  
  

<table class="internalTable" align=""><tbody><tr class="sphr"><td style="text-align: left;"><strong>Old Incident State Model</strong></td><td style="text-align: left;"><strong>New Incident State Model</strong></td></tr><tr class="sp"><td style="text-align: left;"><span style="text-align: start;">New 1</span></td><td style="text-align: left;"><span style="text-align: start;">New 1</span>&nbsp;</td></tr><tr class="sp"><td style="text-align: left;"><span style="text-align: start;">Active 2</span>&nbsp;</td><td style="text-align: left;"><span style="text-align: start;">In Progress 2</span>&nbsp;</td></tr><tr class="sp"><td style="text-align: left;"><span style="text-align: start;">Awaiting Problem 3</span></td><td style="text-align: left;"><span style="text-align: start;">On Hold 3</span>&nbsp;</td></tr><tr class="sp"><td style="text-align: left;"><span style="text-align: start;">Awaiting User Info 4</span>&nbsp;</td><td style="text-align: left;"><span style="text-align: start;">On Hold 3</span>&nbsp;</td></tr><tr class="sp"><td style="text-align: left;"><span style="text-align: start;">Awaiting Evidence 5</span>&nbsp;</td><td style="text-align: left;"><span style="text-align: start;">On Hold 3</span>&nbsp;</td></tr><tr class="sp"><td style="text-align: left;"><span style="text-align: start;">Resolved 6</span></td><td style="text-align: left;"><span style="text-align: start;">Resolved 6</span>&nbsp;</td></tr><tr class="sp"><td style="text-align: left;"><span style="text-align: start;">Closed 7</span>&nbsp;</td><td style="text-align: left;"><span style="text-align: start;">Closed 7</span>&nbsp;</td></tr><tr class="sp"><td style="text-align: left;">&nbsp;</td><td style="text-align: left;"><span style="text-align: start;">Canceled 8</span>&nbsp;</td></tr></tbody></table>

The old state model does not have the On Hold state. However, the new state model has three old incident states that map to On Hold. When the user selects the **On Hold** state, a new field **On Hold Reason** appears.

The **On Hold Reason** field contains the following options:

-   Awaiting Caller (maps to the old incident state: Awaiting User Info)
-   Awaiting Evidence (maps to the old incident state: Awaiting Evidence)
-   Awaiting Problem Resolution (maps to the old incident state: Awaiting Problem)
-   Awaiting Vendor

For example, if you had a workflow that triggered on state 5, you must modify your workflow to trigger on state 3, reason 2.

Updated business rules

* * *

The following scripts have been updated in order to change the Incident management state model. State values have been changed from hard-coded values to references to the IncidentState script include.

Best Practice - Incident Resolution Workflow - com.snc.bestpractice.incident 

<table class="internalTable" align=""><tbody><tr class="sphr"><td style="text-align: left;"><strong>Name</strong></td><td style="text-align: left;"><strong>Type</strong></td><td style="text-align: left;"><strong>Table</strong></td><td style="text-align: left;"><strong>SYS ID</strong></td></tr><tr class="sp"><td style="text-align: left;"><span style="text-align: start;">SNC- ITIL - Close Related</span></td><td style="text-align: left;"><span style="text-align: start;">Business Rule</span>&nbsp;</td><td style="text-align: left;"><span style="text-align: start;">sys_script</span>&nbsp;</td><td style="text-align: left;"><span style="text-align: start;">1c263220c6112275006955271bf6ba4f</span>&nbsp;</td></tr><tr class="sp"><td style="text-align: left;"><span style="text-align: start;">SNC- ITIL - Resolve&nbsp;Related Incidents</span></td><td style="text-align: left;"><span style="text-align: start;">Business Rule</span>&nbsp;</td><td style="text-align: left;"><span style="text-align: start;">sys_script</span>&nbsp;</td><td style="text-align: left;"><span style="text-align: start;">7c4ee2d40a0a3c1e00d5d8aa424b616f</span>&nbsp;</td></tr><tr class="sp"><td style="text-align: left;"><span style="text-align: start;">Create Normal Change</span>&nbsp;</td><td style="text-align: left;"><span style="text-align: start;">UI Action</span>&nbsp;</td><td style="text-align: left;"><span style="text-align: start;">sys_ui_action</span></td><td style="text-align: left;"><span style="text-align: start;">30c9566dc61122740030e173564c1c74</span>&nbsp;</td></tr><tr class="sp"><td style="text-align: left;"><span style="text-align: start;">Create Request</span>&nbsp;</td><td style="text-align: left;"><span style="text-align: start;">UI Action</span>&nbsp;</td><td style="text-align: left;"><span style="text-align: start;">sys_ui_action</span>&nbsp;</td><td style="text-align: left;"><span style="text-align: start;">50317d860a0a0b4b00857807b0815bb2</span>&nbsp;</td></tr><tr class="sp"><td style="text-align: left;"><span style="text-align: start;">Close Incident</span></td><td style="text-align: left;"><span style="text-align: start;">UI Action</span>&nbsp;</td><td style="text-align: left;"><span style="text-align: start;">sys_ui_action</span>&nbsp;</td><td style="text-align: left;"><span style="text-align: start;">bbddb6bbc0a8016400c56236de22441a</span>&nbsp;</td></tr></tbody></table>

Incident Alert Management – com.snc.iam

<table class="internalTable" style="border: 1px solid #e0e0e0;" align=""><tbody><tr class="sphr"><td style="text-align: left;"><strong>Name</strong></td><td style="text-align: left;"><strong>Type</strong></td><td style="text-align: left;"><strong>Table</strong></td><td style="text-align: left;"><strong>SYS ID</strong></td></tr><tr class="sp"><td style="text-align: left;">Show Related Incident Alert</td><td style="text-align: left;"><span style="text-align: start;">UI Action</span></td><td style="text-align: left;">sys_ui_action&nbsp;</td><td style="text-align: left;"><span style="text-align: start;">0a576a57eb131100eac006a2f206fe5c</span></td></tr><tr class="sp"><td style="text-align: left;">Create Incident Alert&nbsp;</td><td style="text-align: left;">UI Action&nbsp;</td><td style="text-align: left;">sys_ui_action&nbsp;</td><td style="text-align: left;"><span style="text-align: start;">25436602eb333000a04d4910f206fea0</span></td></tr></tbody></table>

Change Request - com.snc.change\_request

<table class="internalTable" style="border: 1px solid #e0e0e0;" align=""><tbody><tr class="sphr"><td style="text-align: left;"><strong>Name</strong></td><td style="text-align: left;"><strong>Type</strong></td><td style="text-align: left;"><strong>Table</strong></td><td style="text-align: left;"><strong>SYS ID</strong></td></tr><tr class="sp"><td style="text-align: left;"><span style="text-align: start;">Create Normal Change</span></td><td style="text-align: left;"><span style="text-align: start;">UI Action</span></td><td style="text-align: left;">sys_ui_action&nbsp;</td><td style="text-align: left;"><span style="text-align: start;">30c9566dc61122740030e173564c1c74</span>&nbsp;</td></tr><tr class="sp"><td style="text-align: left;"><span style="text-align: start;">Create Emergency Change</span>&nbsp;</td><td style="text-align: left;">UI Action&nbsp;</td><td style="text-align: left;">sys_ui_action&nbsp;</td><td style="text-align: left;"><span style="text-align: start;">d5378d81c38202003d2ae219cdba8fc5&nbsp;</span>&nbsp;</td></tr></tbody></table>

Incident - com.snc.incident

<table class="internalTable" style="border: 1px solid #e0e0e0;" align=""><tbody><tr class="sphr"><td style="text-align: left;"><strong>Name</strong></td><td style="text-align: left;"><strong>Type</strong></td><td style="text-align: left;"><strong>Table</strong></td><td style="text-align: left;"><strong>SYS ID</strong></td></tr><tr class="sp"><td style="text-align: left;"><span style="text-align: start;">Open - in "New" state</span></td><td style="text-align: left;"><span style="text-align: start;">Module</span>&nbsp;</td><td style="text-align: left;"><span style="text-align: start;">sys_app_module</span>&nbsp;</td><td style="text-align: left;"><span style="text-align: start;">bf287131c0a8016400df7ea4cfeee9b2</span>&nbsp;</td></tr><tr class="sp"><td style="text-align: left;"><span style="text-align: start;">Caller Close</span>&nbsp;</td><td style="text-align: left;"><span style="text-align: start;">Business Rule</span>&nbsp;</td><td style="text-align: left;"><span style="text-align: start;">sys_script</span>&nbsp;</td><td style="text-align: left;"><span style="text-align: start;">28beab035f201000b12e3572f2b477ed</span>&nbsp;</td></tr><tr class="sp"><td style="text-align: left;"><span style="text-align: start;">incident reopen</span>&nbsp;</td><td style="text-align: left;"><span style="text-align: start;">Business Rule</span>&nbsp;</td><td style="text-align: left;"><span style="text-align: start;">sys_script</span>&nbsp;</td><td style="text-align: left;"><span style="text-align: start;">91930e46c611227500b53b322750526a</span>&nbsp;</td></tr><tr class="sp"><td style="text-align: left;"><span style="text-align: start;">mark_closed</span>&nbsp;</td><td style="text-align: left;"><span style="text-align: start;">Business Rule</span>&nbsp;</td><td style="text-align: left;"><span style="text-align: start;">sys_script</span>&nbsp;</td><td style="text-align: left;"><span style="text-align: start;">bf3f8917c0a8016400a867dc0794e8ad</span>&nbsp;</td></tr><tr class="sp"><td style="text-align: left;"><span style="text-align: start;">incident autoclose</span>&nbsp;</td><td style="text-align: left;"><span style="text-align: start;">Business Rule</span>&nbsp;</td><td style="text-align: left;"><span style="text-align: start;">sys_script</span>&nbsp;</td><td style="text-align: left;"><span style="text-align: start;">d67b8d9ec0a80118008cd8f0f7f92fae</span>&nbsp;</td></tr><tr class="sp"><td style="text-align: left;"><span style="text-align: start;">Create Problem</span>&nbsp;</td><td style="text-align: left;"><span style="text-align: start;">UI Action</span>&nbsp;</td><td style="text-align: left;"><span style="text-align: start;">sys_ui_action</span>&nbsp;</td><td style="text-align: left;"><span style="text-align: start;">2f43c471c0a8006400a07440e49924c2</span>&nbsp;</td></tr><tr class="sp"><td style="text-align: left;"><span style="text-align: start;">Create Normal Change</span>&nbsp;</td><td style="text-align: left;"><span style="text-align: start;">UI Action</span>&nbsp;</td><td style="text-align: left;"><span style="text-align: start;">sys_ui_action</span>&nbsp;</td><td style="text-align: left;"><span style="text-align: start;">30c9566dc61122740030e173564c1c74</span>&nbsp;</td></tr><tr class="sp"><td style="text-align: left;"><span style="text-align: start;">Close Incident</span>&nbsp;</td><td style="text-align: left;"><span style="text-align: start;">UI Action</span>&nbsp;</td><td style="text-align: left;"><span style="text-align: start;">sys_ui_action</span>&nbsp;</td><td style="text-align: left;"><span style="text-align: start;">bbddb6bbc0a8016400c56236de22441a</span>&nbsp;</td></tr></tbody></table>

Incident Resolution Fields - com.snc.incident\_resolution\_fields

<table class="internalTable" style="border: 1px solid #e0e0e0;" align=""><tbody><tr class="sphr"><td style="text-align: left;"><strong>Name</strong></td><td style="text-align: left;"><strong>Type</strong></td><td style="text-align: left;"><strong>Table</strong></td><td style="text-align: left;"><strong>SYS ID</strong></td></tr><tr class="sp"><td style="text-align: left;"><span style="text-align: start;">mark_resolved</span></td><td style="text-align: left;"><span style="text-align: start;">Business Rule</span>&nbsp;</td><td style="text-align: left;"><span style="text-align: start;">sys_script</span>&nbsp;</td><td style="text-align: left;"><span style="text-align: start;">d3b21f640a0a3c7400f6acab7de3f5f8</span>&nbsp;</td></tr></tbody></table>

Problem Management - com.snc.problem

<table class="internalTable" style="border: 1px solid #e0e0e0;" align=""><tbody><tr class="sphr"><td style="text-align: left;"><strong>Name</strong></td><td style="text-align: left;"><strong>Type</strong></td><td style="text-align: left;"><strong>Table</strong></td><td style="text-align: left;"><strong>SYS ID</strong></td></tr><tr class="sp"><td style="text-align: left;">Close Incidents</td><td style="text-align: left;"><span style="text-align: start;">UI Action</span></td><td style="text-align: left;">sys_ui_action&nbsp;</td><td style="text-align: left;"><span style="text-align: start;">fc8b2c66c0a8000900f7bf2dc94a690a</span></td></tr></tbody></table>

Create knowledge from problem – com.snc.problem\_kb

<table class="internalTable" style="border: 1px solid #e0e0e0;" align=""><tbody><tr class="sphr"><td style="text-align: left;"><strong>Name</strong></td><td style="text-align: left;"><strong>Type</strong></td><td style="text-align: left;"><strong>Table</strong></td><td style="text-align: left;"><strong>SYS ID</strong></td></tr><tr class="sp"><td style="text-align: left;"><span style="text-align: start;">Communicate Workaround&nbsp;</span></td><td style="text-align: left;">UI Action</td><td style="text-align: left;"><span style="text-align: start;">sys_ui_action</span>&nbsp;</td><td style="text-align: left;">88273bc40a0a0b4f00e94d5eabade988</td></tr></tbody></table>

Service Management Basics - com.snc.service

<table class="internalTable" style="border: 1px solid #e0e0e0;" align=""><tbody><tr class="sphr"><td style="text-align: left;"><strong>Name</strong></td><td style="text-align: left;"><strong>Type</strong></td><td style="text-align: left;"><strong>Table</strong></td><td style="text-align: left;"><strong>SYS ID</strong></td></tr><tr class="sp"><td style="text-align: left;">SNC - ITIL - Close Related</td><td style="text-align: left;"><span style="text-align: start;">Business Rule</span></td><td style="text-align: left;"><span style="text-align: start;">sys_script</span></td><td style="text-align: left;"><span style="text-align: start;">1ddd8e50c6112275015cb235aa3b803a</span></td></tr></tbody></table>

We also recommend that you do the following:

-   Evaluate each of the scripts above for any customization performed on your instance. If you intend to retain the customization, you must reset to default in order to accept the changes and then reapply your customization. This ensures that you are on the latest feature set.  
      
    
    <table class="noteTable" style="text-align: start; border: 1px solid #e0e0e0;" align="left"><tbody><tr><td style="width: 50; vertical-align: middle; text-align: center;"><img style="align: baseline;" title="Note" src="/Note_25x.pngx" alt="" align="bottom" border="" hspace="" vspace=""></td><td style="vertical-align: middle; text-align: left;"><strong>Note</strong>:&nbsp;<span style="text-align: left;">There may be other scripts in addition to the ones mentioned above that have been created on your specific instance</span>.</td></tr></tbody></table>
    

-   Evaluate all of the tables mentioned above for custom records. These custom records might need amendments if they are dealing with **State** or **Incident state** fields. For example, relying on changes to them for a client script or writing to a child record based on changes to state on an incident.

<table class="noteTable" align="left"><tbody><tr><td style="width: 50; vertical-align: middle; text-align: center;"><img style="align: baseline;" title="Note" src="/Note_25x.pngx" alt="" align="bottom" border="" hspace="" vspace=""></td><td style="vertical-align: middle; text-align: left;"><strong>Note</strong>:&nbsp;<span style="text-align: start;">The Incident state model is customizable for advanced users. The script include named IncidentState holds the base states that the code uses to make state based decisions</span>.</td></tr></tbody></table>

### Related Links

[Request Incident Management — Core](https://docs.servicenow.com/bundle/vancouver-it-service-management/page/product/incident-management/task/activate-incident-management-core-plugin.html "Request Incident Management — Core")
