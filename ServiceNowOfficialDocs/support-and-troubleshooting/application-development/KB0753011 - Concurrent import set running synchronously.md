---
title: "Concurrent import set running synchronously"
aliases:
  - KB0753011
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0753011
kb_number: KB0753011
last_modified: 2026-01-16
---

## Issue

Users may complain that they have enabled a concurrent import set but that it is running under one Import Set or not at all. Please read this article for a wonderful description of concurrent import sets. 

[KB0720801](https://support.servicenow.com/kb_view.do?sysparm_article=KB0720801 "KB0720801")

## Resolution

**Troubleshooting**

This is not an exhaustive list and can (and should) be added to as more items are found. Some of these are just items to check, as we encounter issues, particular cases can be flushed out.

1.  1.  Firstly, we should check the configuration. Enabling a concurrent import set is as easy as checking the select box in the scheduled import job. ![](sys_attachment.do?sys_id=ffc9d1d093aafed0101833527cba10d5)
    2.  If the job should be running, check the **System Import Sets -> Progress** module. Do we see any job running? Even if the job is not running concurrently, there should be an import. It just may be running on a single import set. This may help us understand the issue. If nothing runs at all, then it is probably not a concurrent import issue but a platform issue as even if the concurrent imports are not running, they should start a normal synchronous import. Not always so continue reading.  
          
          
        
    3.  Check the **System Import Sets -> Concurrent Import Sets** module. If the concurrent import set was created, you will see the parent import set in here and that will contain the children import sets.   
          
        
    4.  If there is a concurrent import set in step 3. Check the **System Import Sets -> Concurrent Import Set Jobs** module. This will indicate both the parent concurrent import set and the progress on the children imports. Review to see what state they are in. You can then troubleshoot the children as they are just normal import sets.  
          
        
    5.  Check the job setup. Concurrent import sets are run and managed by several jobs. Navigate to the following URL in the customers instance. This is the **System Scheduler -> Scheduled Jobs** module.  
          
        https://<INSTANCENAME>.service-now.com/sys\_trigger\_list.do?sysparm\_query=nameSTARTSWITHImport%20Set%20Transformer  
          
        You should see 2 'Import Set Transformer' jobs that has a 'System ID' labeled \`ACTIVE NODES\` on an OOB instance. These are used as the main configuration templates that are used to start worker jobs. They are configurational and do not do work by themselves. These \`ACTIVE NODES\` are referred to as 'parent' jobs.  
          
        The 'Import Set Transformer' jobs that have their 'System ID' labeled with the instance node name, actually do the work and are referred to as 'child' jobs. They also display "Import Set Transformer" in the 'Parent' column to reference back to the parent job that created them.  
          
        Each instance node creates the same number of child jobs as there are main jobs. In the example below, the instance has two nodes, there are two parent jobs, and four child jobs. If you had four nodes, you would still have two parent jobs but eight child jobs as the parent jobs have a multiplicative effect based on the number of nodes available.  
          
        ![](sys_attachment.do?sys_id=77c9d1d093aafed0101833527cba10db)_Add the "System ID" and "Parent" column header to the list view to see the example table._  
          
          
        If you see that the Parent jobs "System ID" is not set to Active Nodes. It should be changed to "Active Nodes".  
          
        If you see Parent Jobs and no child jobs or missing child jobs, you should set the "Next Action" of the parent job on the nodes/node that is missing children to one minute in the future. It should run and create the children.  
          
        Note: Unless there is a specific business need, it is generally not recommended to add additional Parent job records.  
          
        If you are missing the jobs entirely Engage an SME.
