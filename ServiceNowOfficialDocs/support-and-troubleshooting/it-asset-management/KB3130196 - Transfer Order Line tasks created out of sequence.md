---
title: "Transfer Order Line tasks created out of sequence"
aliases:
  - KB3130196
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB3130196
kb_number: KB3130196
last_modified: 2026-06-30
---

## Issue

On the alm\_transfer\_order\_line\_task table, tasks are being created out of the OOTB sequential order during the lifecycle of a single Transfer Order Line. Specifically, the task with order = 400 (Receive) is being instantiated before the task with order = 300 (Ship), and is later auto-closed as "Closed Skipped" when the preceding stage advances, while the task with order = 300 is created in its place.  
We have identified Known Error KB1649174 as a likely match for the symptoms observed, and we have already executed all the steps described in that article without resolving the issue. This case is being opened to request further engineering investigation.  
Environment  
  
Example   
Transfer Order: TO0010002  
  
Transfer Order Line: TOL0010002 related to TO0010002  
  
  
Asset:  Test Asset  
  
Timeline of events  
  
2026-06-16 12:59:20 — TOLTASK0001031 was created automatically. Order = 100, Stage = Requested, Short description = "Ready for fulfillment".  
2026-06-19 06:33:05 — User moved TOLTASK0001031 to Work in Progress and then to Closed Complete. At this same timestamp, the system created two tasks simultaneously:  
  
TOLTASK0001042 — Order = 200, Stage = Shipment Preparation, Short description = "Prepare for shipment".  
TOLTASK0001043 — Order = 400, Stage = Received, Short description = "Receive".  
  
No task with Order = 300 (Stage = In Transit, "Ship") was created at this point.  
2026-06-19 06:33:41 — User moved TOLTASK0001042 to Work in Progress and then to Closed Complete. At this same timestamp:  
  
TOLTASK0001043 (Order = 400, "Receive") was automatically transitioned to state = Closed Skipped, without any manual action on user's part.  
TOLTASK0001044 — Order = 300, Stage = In Transit, Short description = "Ship" — was created in state = Open.  
  
Summary of the anomaly  
  
Closing TOLTASK Order 100 generated TOLTASK Order 200 and TOLTASK Order 400 in parallel, while TOLTASK Order 300 was not generated.  
Closing TOLTASK Order 200 caused TOLTASK Order 400 to be automatically closed as "Closed Skipped" and TOLTASK Order 300 to be created in its place.  
  
The "Receive" task (Order 400) is therefore being created prematurely and later discarded, while the "Ship" task (Order 300) is being deferred until after Order 200 is closed.

## Resolution

This is expected behavior.   
  
This happens as per the design when Service Management Core plugin is activated, as the transfer order can be directly received or it can be shipped. So, based on the action taken the rest of the sequence is followed.  
So, if the Prepare for shipment is performed (TOLTASK0001042) , then the receive task(TOLTASK0001043) is skipped and then it moves to the next stage of shipment post which the existing "Receive" task is reopened the asset to be received.  
  
Please refer to below docs for more information where we have documented this behavior  
[https://www.servicenow.com/docs/r/it-asset-management/asset-management/manage-transfer-orders.html](https://www.servicenow.com/docs/r/it-asset-management/asset-management/manage-transfer-orders.html)

  
"Important:  
In the Asset Management application, the Transfer Order Line workflow manages the processing of transfer order lines. If your ServiceNow instance has the following plugins activated, the transfer order lines are processed using a workflow, depending on the plugin installed.  
If the Service Management Core plugin is activated, the Transfer Order Line SM core workflow manages the processing of the transfer order lines.  
If the Field Service Management plugin (com.snc.work\_management) is activated, the Transfer Order Line SMCore workflow manages the processing of the transfer order lines.  
For more information, see Move an asset through the transfer process."  
  
Then please refer below docs for "Move an asset through the transfer proces" link , this explains out of box behavior  
https://www.servicenow.com/docs/r/field-service-management/work-order-management/create-transfer-order-line-task.html
