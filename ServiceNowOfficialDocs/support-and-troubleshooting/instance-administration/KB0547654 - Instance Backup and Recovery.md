---
title: "Instance Backup and Recovery"
aliases:
  - KB0547654
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0547654
kb_number: KB0547654
last_modified: 2026-06-30
---

## Issue

ServiceNow has created an automated workflow to support the instance restore process. Customers can request an instance restore via a Service Catalog Item to create a Change, which is completed using **end-to-end automation**.

Learn more about this Service Catalog and its benefits on [Now Community](https://community.servicenow.com/community?id=community_blog&sys_id=c0beb213dba24c94f7fca851ca961970).

You can request the **Instance Restore** on any sub-production instance by following the steps described in the following article: [KB0791676 - Restoring an instance with the Now Support Service Catalog](https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0791676 "Restoring an instance with the Now Support Service Catalog")

**NOTE:** This procedure is for all hosted instances and is not applicable for on-premise instances.

## Backup Policy

* * *

**ServiceNow does full backups weekly and differential backups daily.**

**Full backups have a retention period of 14 days** (_Default Full Backup Retention Period_) _"Policy went effective as of May 8th 2023"_ **and a rolling 6 days of differential backups** (the 7th day of the week is the full backup and does not have a differential backup).

For Regulated Market environments, all new customers will adhere to the Default full Backup Retention policy starting October 18, 2023. Existing Customers saw the policy go into effect on March 01, 2024, but they are able to maintain their existing retention period (28-days) for the duration of the subscription term they are on when the update takes effect on March 01, 2024.

All database servers are backed up independently: production (primary and standby) and non-production.

ServiceNow stores backups on standalone storage racks, ensuring that no single point of failure can impact both the hosted instance and its backups simultaneously.

Backups for a specific instance do not run on a set schedule and the time of the backup is not guaranteed. The system finds the best time for backups within a 24-hour period and customers and ServiceNow cannot modify that time. For security reasons, ServiceNow will not provide customers screenshots of internal instances where backups are hosted under any circumstances.

To check when backups are taken, customers can access the ["List of backups for the instance" Service Catalog Item](https://support.servicenow.com/now?id=ns_automation_store&catalog_sys_id=69dd020ddbaecc1058a161cc1396192b "https://support.servicenow.com/now?id=ns_automation_store&catalog_sys_id=69dd020ddbaecc1058a161cc1396192b") on the Now Support Portal, and select the instance and the current date. The list of the latest backups will be displayed along with the date and time when they were taken.

ServiceNow does not offer an option for on-demand backups of any instance. Please check this Knowledge Article for more information: [KB0992741- Ad-hoc backup requests](https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0992741)

## Available Backups

* * *

To check when backups are taken, customers can access the ["List of backups for the instance" Service Catalog Item](https://support.servicenow.com/now?id=ns_automation_store&catalog_sys_id=69dd020ddbaecc1058a161cc1396192b "https://support.servicenow.com/now?id=ns_automation_store&catalog_sys_id=69dd020ddbaecc1058a161cc1396192b") on the Now Support Portal, and select the instance and the current date. The list of the latest backups will be displayed along with the date and time when they were taken.

**IMPORTANT: Having a retention period of 14 days for full backups and** **a rolling 6 days of differential backups does NOT mean that you can restore an instance to any point in time of the past 14 days and it does NOT mean that you will have a backup available per day for the past 14 days.**

In some situations, a point-in-time restore can be considered which is a mechanism to bring back an instance to any point in time in the past 4 days max but the request must be made within 3 days. This is also usually reserved for production instances only. Please check this Knowledge Article for more information: [KB0965019 - Restoring a Production Instance from Backup](https://support.servicenow.com/kb_view.do?sysparm_article=KB0965019 "Restoring a Production Instance from Backup")

Past those 4 days, only available backups can be restored and nothing in between 2 backups. For example, if a non-audited data set got created and deleted between 2 consecutive backups, we will not have a way to recover it. This is because that data set will not be available anywhere, neither in the backup taken before the data set got created nor in the backup taken after the data set got deleted.

The following chart explains which backups are available over a period of a week:![Available Backups.png](sys_attachment.do?sys_id=b2df0792479866d0b7832920326d435d "Available Backups")

## Recovery Requests

* * *

If you feel you have lost data or have corrupted data on a **production instance**, please [submit a case](https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0547260 "submit a case") on the Now Support Portal as soon as possible. We have standard operating procedures to assist you in recovering the data based on individual cases. Please check this Knowledge Article for more information: [KB1262470 - How to recover deleted data from ServiceNow instance](https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB1262470)

If you feel you have lost data or have corrupted data on a **non-production / sub-production instance**, we have various Self Service driven options to help you recover the data and ServiceNow Technical Support has limited scope with this. Please check this Knowledge Article for more information: [KB0996695 - Dataloss on sub production or non production instances](https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0996695)  
  
Due to capacity management, ServiceNow does not typically provision temporary instances, unless there is clear business justification that one of the sub-production instances cannot be used. Please check this Knowledge Article for more information: [KB0830706 - Requesting a temporary instance](https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0830706)

## Restoring a Production Instance from Backup

* * *

For **production** instances, a restore from backup is a **last resort** because the impact of a restore from a backup could be more detrimental than the issue that prompted the action. In most cases, such a restore means data loss because the data created or updated since the backup was taken will not be available after the restore.  
  
In some situations, a point-in-time restore can be considered but the request must be made within 3 days max after the start of the event that caused the need for a production restore.

If you feel you have lost data or have corrupted data on a **production instance**, please [submit a case](https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0547260 "submit a case") on the Now Support Portal as soon as possible. We have standard operating procedures to assist you in recovering the data based on individual cases.

Detailed information, timeline, and FAQs about restoring a production instance from backup is available in the following article: [KB0965019 - Restoring a Production Instance from Backup](https://support.servicenow.com/kb_view.do?sysparm_article=KB0965019 "Restoring a Production Instance from Backup")

## Resolution

Added the following verbiage to address a concern from a customer who wasn't clear if an outage impacting the server could take out the backup as well. Here is the blurb that was added:  
"ServiceNow stores backups on standalone storage racks, ensuring that no single point of failure can impact both the hosted instance and its backups simultaneously. "
