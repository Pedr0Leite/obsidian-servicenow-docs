---
title: "SLA definition Custom time zone source not applied to Task SLAs"
aliases:
  - KB0784170
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0784170
kb_number: KB0784170
last_modified: 2024-04-08
---

## SLA definition Custom time zone source not applied to Task SLAs

  

### Issue

ISSUE:  
You are experiencing an incorrect SLA definition time zone showing on the Task SLA.

  
You created new Choice list in SLA definition form to add time zone by dotwalking ..............Incident's -> Business Service->location-> timezone (task.business\_service.location.time\_zone)  
but in the incident - > task SLA, it reflects default time zone (Asia/ Dubai) instead of Europe/ London timezone

### Cause

MOST PROBABLE CAUSE:

The new custom timezone source was not included in the 'SLATimezone' script include.

  
You have modified the choice list to add your custom choice.  
However modifying the choice list is not all you need to do to add a custom timezone for your SLAs.  
  
The values you see in the timezone\_source choice list (e.g., task.caller\_id.time\_zone, task.cmdb\_ci.location.time\_zone, etc.) are not dot walking access to the time zone fields, but they are identifiers defined in the script include SLATimezone.  
  
See the Script Include: SLATimezone  
/nav\_to.do?uri=sys\_script\_include.do?sys\_id=e35516289f3200008f88ed93ee4bcc66  
  
Description: Decode SLA timezone choice values (set via com.snc.sla.timezone.source property) into actual timezone values.  
Called by TaskSLA()

In this script include all the OOTB Timezone sources have been defined.

### Resolution

  
PROPOSED SOLUTION:

You need to add your new custom timezone source in the SLATimezone script include.

  
Basically, you will also need to include your custom identifier in there, for example, within the "switch(source)" block in this script, you can add the identifier you set in your choice element, and in there specify the dot walking to your time zone.  
  
Please note, it looks like the script include was designed to be modified because of the commented line:  
  
// (add your own ideas here)  
  
  
For example, try something like:  
  
  
case 'task.business\_service.location.time\_zone':  
  
return gr.task.business\_service.location.time\_zone;  
  
  
Above was verified to fix the issue for the Customer.

  
  

### Related Links

NOTE: When you customize any object, a record is created in Customer Updates 'sys\_update\_xml' table and the Replace on upgrade field is set to false.  
The system does this to prevent customizations from being overwritten by system upgrades, and so the upgrade process automatically skips changes to these objects.  
This leaves you with the option to revert if you wish in the upgraded instance.  
  
To prepare for future upgrade, prior to upgrade,  
  
1\. in your instance, you can delete the customer update record that got created in 'sys\_update\_xml' table when modifications were made.  
  
Deleting this record that was created would mean that the system will not see the file as having ever been customized and it would be upgraded during the next upgrade.  
  
2\. Please also review the documentation below also for an Alternative option,  
https://docs.servicenow.com/csh?topicname=t\_OverwriteCustomizsDuringUpgrades.html&version=latest  
Procedure  
  
Open the customized object (for example, the ArrayUtil script include).  
Right-click the header and select Show Latest Update.  
Configure the form to add the Replace on upgrade field, if necessary.  
Select the Replace on upgrade check box and click Update.  
The customized object will be replaced on the next upgrade.
