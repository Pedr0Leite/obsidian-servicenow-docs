---
title: "Duplicate survey instances created need to be deleted"
aliases:
  - KB0960328
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0960328
kb_number: KB0960328
last_modified: 2026-05-21
---

## Issue

Duplicate survey instances created need to be deleted

How to delete instances

  
Quick way (not manually) to delete duplicate instances.  
  

## Resolution

With regards a quick way other than manual to delete survey instances, the other possible option would be to attempt to cancel the surveys.  
  
\--> a. OOB we provide a job as below  
Cancel Expired Assessments:  
By default, the system runs the script every 30 days to cancel expired assessment and survey instances that are in the Work in progress or Ready to take states.  
  
As a possibility, try and modify the OOB job script, add the relevant query to the script in the job; for the current instances, you want to be deleted then instead cancel them.  
The job can then be executed at your convenience using the 'execute now' ui action.

  
  
\--> b. You can also delete these survey instances using a script. Please note that assistance with custom scripting is outside the scope of service offered by our support team, but I can point you in the direction you need to do.  
If you need further assistance with scripting your desired functionality, I would suggest using our [developer community from](http://community.servicenow.com/ "developer community from") our Community forums as a resource.  
  
  

Please review these community links for your reference  
  
1\. Deletion of a certain cancelled survey

[Community link](https://community.servicenow.com/community?id=community_question&sys_id=bc3dc145db10e70854250b55ca9619a5&view_source=searchResult "Community link")  
This provides a script you can run in the background to delete the instance and instance questions  
  
2\. How to delete Cancelled Survey Instances?

[Delete Cancelled Survey Instances](https://community.servicenow.com/community?id=community_question&sys_id=c981df2ddbdcdbc01dcaf3231f961982&view_source=searchResult "delete Cancelled Survey Instances")  
  
This provides a custom scheduled job script that cancels surveys  
  
3\. I am trying to create a scheduled job that deletes "Ready to Take" surveys from the assessments table after 3 business days

[The scheduled job that deletes "Ready to Take" surveys](https://community.servicenow.com/community?id=community_question&sys_id=7cb303a5dbd8dbc01dcaf3231f961917&view_source=searchResult "scheduled job that deletes \"Ready to Take\" surveys")

  
NOTE: It is strongly recommend that for any approach you decide to take, please test and verify the outcome in a subprod instance before applying directly to prod.
