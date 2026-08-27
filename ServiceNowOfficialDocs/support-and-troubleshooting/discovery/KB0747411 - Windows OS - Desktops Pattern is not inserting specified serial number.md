---
title: "Windows OS - Desktops Pattern is not inserting specified serial number"
aliases:
  - KB0747411
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0747411
kb_number: KB0747411
last_modified: 2024-04-07
---

## Windows OS - Desktops Pattern is not inserting specified serial number

  

### Issue

When you customize the Pattern Windows OS - Desktops to choose a specific serial number to add to the cmdb for the CI in Discovery, it does not work. It always inserts the first serial number that is found. (This is Step 5 of the Pattern: Insert Serial Number to cmdb\_ci\_computer - the value field in this step specifies an array element number-$cmdb\_serial\_number\[1\].serial\_number. Changing it to element 2 does not work.) 

### Release

Kingston/London/Madrid

### Cause

The Pre/Post Processor Script for the Windows OS - Desktops Pattern contains a line of code that overrides the settings in the pattern and will always write element\[1\] of the array of serial numbers to the cmdb CI item that is discovered

### Resolution

1.  Navigate to the Pre/Post Processor Script for the Windows OS - Desktops Pattern: [https://<instance\_name>.service-now.com/nav\_to.do?uri=sa\_pattern\_prepost\_script.do?sys\_id=5c2729a40f2f920051a9fa6ce1050e55](https://\<instance_name\>.service-now.com/nav_to.do?uri=sa_pattern_prepost_script.do?sys_id=5c2729a40f2f920051a9fa6ce1050e55)
    1.  **Note** - In some newer versions, you will need to go to the pre script '**OSs - Pre Sensor**' instead
2.  Comment out Line 198 where it reads "handleWindowsHardwareInformation();"
    1.  The line number might be slightly different, depending on version and patch of the instance. 
    2.  It can also appear as **handleHardwareInformation(mainCis\[ciKey\].lookup)** in newer versions, in the '**OSs - Pre Sensor'** pre script.
3.  Modify the array element described in the "Symptoms" section of this article to match the serial number you desire to associate with the CI. \*You can always look in the payload of the Pattern to determine which array element your desired serial number is.
4.  Save and publish the pattern and do a cache.do to make sure the changes take effect.
5.  Run the Discovery
