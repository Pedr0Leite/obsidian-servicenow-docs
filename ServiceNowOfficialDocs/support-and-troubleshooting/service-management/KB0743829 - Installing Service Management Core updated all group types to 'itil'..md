---
title: "Installing Service Management Core updated all group types to 'itil'."
aliases:
  - KB0743829
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0743829
kb_number: KB0743829
last_modified: 2024-04-07
---

## Installing Service Management Core updated all group types to 'itil'.

  

### Issue

# Symptoms

Installing Service Management Core updated all group types to 'itil'.  All groups that did not have a group type assigned, were given the ITIL group. 

# Release

London Patch 4 Hot Fix 2

# Steps To Reproduce

1.  Before installing Plugin "Facilities Service Management" checked existing Group Types in "sys\_user\_group" Table. 
2.  Currently following are the number of group of different types available in OOB

Group name:   
ITIL - 2   
Catalog - 6   
Groups with blank Type -19   
Total: 27 

3\. Next: Install "Service Management Core" Plugin.

Result: After plugin installation completed, In sys\_user\_group Table found groups that did not have a group type assigned, were given the ITIL group type.   
Install Start time: 2019-03-07 07:24:16   
Install finished time: 2019-03-07 07:28:00   
  
sys\_user\_group Table:   
Group Name:   
ITIL - 21   
Catalog - 6

-   So Plugin installation updated groups with type 'itil' for Groups which has empty type. 
-   Checked sys\_upgrade\_history\_log list and found following triggered at same time when "Service Management Core" plugin installed. 

File name: fix\_itil\_group\_type\_for\_sm\_apps   
Plugin: com.snc.service\_management.core   
Created time: 2019-03-07 07:24:23   
Finished time: 2019-03-07 07:28:00 

# Cause

1.  The fix job queries for all groups that have an empty group type field, and adds the "itil" group type to them. 
2.  In your reproduction, before installing SM, you had 2 groups with the itil group type and 19 with no group type. After installing SM Core, you had 21 with the itil group type (in other words, the groups that had no group type were updated to have the itil group type). 
3.  Once a group type was assigned, the groups could not be used for ITSM tasks like incidents, problems, changes. 
4.  Unfortunately, there is no way to prevent the fix job from running. To reverse the affects on an already upgraded instance, I'd recommend going to the list of groups, and updating the filter to only show those that have a group type of itil only. Then looking at the update times of the groups, you may be able to determine which groups were modified during upgrade and reset the group type to be empty. 

# Resolution

1.  To handle the issue in future upgrades, the following can be done: 
2.  As an admin, before upgrading the instance, run the following in a background script

var gr = new GlideRecord('sys\_user\_group');   
gr.addQuery('type', 'ISEMPTY', '');   
gr.query();   
var emptyGroupTypeIds = \[\];   
while(gr.next())   
emptyGroupTypeIds.push(gr.sys\_id + '');   
  
gs.info('Copy these and save them somewhere: ');   
gs.info(emptyGroupTypeIds); 

3\. The above script will find all user groups where the type is empty and print out the sys ids of those groups. Copy the list of sys ids and save them somewhere. Then, upgrade the instance   
  
4\. After upgrading the instance, run the following in a background script (replacing "PASTE\_SYS\_IDS\_HERE" with the sys ids you copied and saved)   
  
var gr = new GlideRecord('sys\_user\_group');   
gr.addQuery('sys\_id', 'IN', 'PASTE\_SYS\_IDS\_HERE');   
gr.type = '';   
gr.updateMultiple();   
  
The above script will reset the type of the affected groups to empty, reversing what the fix job does.
