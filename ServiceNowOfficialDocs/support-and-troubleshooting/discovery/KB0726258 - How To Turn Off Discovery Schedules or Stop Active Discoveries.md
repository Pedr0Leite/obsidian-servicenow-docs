---
title: "How To Turn Off Discovery Schedules or Stop Active Discoveries"
aliases:
  - KB0726258
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0726258
kb_number: KB0726258
last_modified: 2024-01-23
---

## How To Turn Off Discovery Schedules or Stop Active Discoveries

  

### Issue

In some cases, it may be necessary to stop discovery from running. This KB outlines some common scenarios and steps to stop discovery.

**Note:** Any sample script in this KB is given only as a starting point. Sample scripts should be tested first in a non production instance and modified to meet each instance's requirements if necessary.

### Stop Active Discoveries

To stop active discoveries, you can use a list or a fix script. See below for steps to perform each method.

#### Using a list

1.  Navigate to **Discovery > Status** (discovery\_status).
2.  Search for statuses where "stateINStarting,Active" (Encoded query for state is one of Starting, Active).
3.  Select all records.
4.  Select **Cancel Discovery**.

#### Using a fix script

1.  Navigate to **System Definition > Fix Scripts**.
2.  Click **New**.
3.  Define the fix script.
4.  Click the **Run Fix Script** related link. The following could be used as a sample script:
    
    var dac = new SncDiscoveryCancel();  
    var status = new GlideRecord('discovery\_status');  
    status.addEncodedQuery('stateINStarting,Active');  
    status.query();  
    while(status.next()){  
        gs.log("Fix Script: Canceling discovery\_status " + status.sys\_id);  
        dac.cancelAll(status.sys\_id);  
    }
    

### Stop Discoveries For Specific CI Types/Classes

Discovery can be stopped for certain classes after a CI is classified via the Discovery Configuration Console.

To stop a discovery after a CI has been classified:

1.  Navigate to **Discovery Definition > Configuration Console**.
2.  Find the device class under "Devices" and set to **active = false**.
3.  In the following example image, we turn off "Network Printers" discovery.  
      
    ![In the Configuration Console, the Network Printers toggle is switched to inactive.](sys_attachment.do?sys_id=16cc842797fbb910d4743dae2153afbc "Configuration Console")

**Note**: Turning off all device types in the configuration console will not disable discovery. The Shazzam and Classification phases will still run. Discovery will stop once the devices are classified.

### Stop Discoveries From Running on Cloned Instances

As part of the cloning process, Post-clone cleanup scripts are run on the target instance. A Post-clone cleanup script can be used to keep discovery from running on a target instance.

To create a Post-clone cleanup script:

1.  Navigate to **System Clone > Clone Definition > Cleanup Scripts** and click **New**.
2.  Populate the "Name" and "Script" fields. The following could be used as a sample script:
    
    var schedules = new GlideRecord('discovery\_schedule')  
    schedules.addQuery('active', true);  
    schedules.query();  
    schedules.setValue('active', false);  
    schedules.updateMultiple(); 
    

Alternatively, use any of the previously mentioned methods to disable discovery once the cloning is complete.

### Additional Information

Other relevant KB and documents:

-   [Discovery Configuration Console](https://docs.servicenow.com/csh?topicname=c_DiscoveryConfigurationConsole.html&version=latest "Discovery Configuration Console")
-   [GlideRecord - Global](https://docs.servicenow.com/csh?topicname=c_GlideRecordAPI.html&version=latest "GlideRecord - Global")
-   [KB0680014: How to programatically stop Service Mapping discovery on a Business Service](https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0680014 "How to programatically stop Service Mapping discovery on a Business Service")
-   [Post-clone cleanup scripts](https://docs.servicenow.com/csh?topicname=post-clone-cleanup-scripts.html&version=latest "Post-clone cleanup scripts")
-   [System Clone](https://docs.servicenow.com/csh?topicname=c_SystemClone.html&version=latest "System Clone")
