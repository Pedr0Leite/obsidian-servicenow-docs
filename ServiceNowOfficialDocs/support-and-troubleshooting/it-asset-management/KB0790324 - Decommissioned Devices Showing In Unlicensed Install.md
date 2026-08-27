---
title: "Decommissioned Devices Showing In Unlicensed Install"
aliases:
  - KB0790324
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0790324
kb_number: KB0790324
last_modified: 2024-04-08
---

## Decommissioned Devices Showing In Unlicensed Install

  

### Issue

1.  Some of the decommissioned devices are showing in unlicensed install.
2.  Ideally, it is expected behavior that the "Decommissioned Devices" should be removed from the "Software Installs".
3.  This URL gives the list of "Software Installs" which were present on "Decommissioned" devices. 

https://<Instance\_Name>.service-now.com/cmdb\_sam\_sw\_install\_list.do?sysparm\_query=installed\_on.install\_status%3D15%5Eproduct\_result.product%3D8f109c060b3022002d6c650d37673a1a 

![](sys_attachment.do?sys_id=4fced001db40b4d0471f9c41ba96195c)

### Release

All Versions.

### Cause

1.  There is Business rule Remove Installs For Retired/Stolen CI on Computer \[cmdb\_ci\_computer\] table.
2.  This removes the records from Software Installation \[cmdb\_sam\_sw\_install\] table based on the following conditions:

current.hardware\_status == 'retired' || current.hardware\_status == 'stolen' || current.install\_status == 7 || current.install\_status == 8

3\. Here is the URL for the Business Rule:  https://<Instance\_Name>.service-now.com/nav\_to.do?uri=sys\_script.do?sys\_id=6799623353530300b77dddeeff7b129f

4\. In one of the customer instance, there is Sys Choice 'Decommission' added to install\_status, which is a custom one. https://<Instance\_Name>.service-now.com/sys\_choice\_list.do?sysparm\_query=name%3Dcmdb\_ci%5EelementSTARTSWITHinstall\_status

5\. Because of this custom choice, the business rule did not trigger.

6\. So corresponding software installs are not deleted from Software Installation \[cmdb\_sam\_sw\_install\] and the decommissioned devices are showing In the "Unlicensed Install" table.

### Resolution

1.  Navigate to "System Choice" with the help of below link:

https://<Instance\_Name>.service-now.com/sys\_choice\_list.do?sysparm\_query=name%3Dcmdb\_ci%5EelementSTARTSWITHinstall\_status

2\. Check the value of the "Demomissioned" field.

![](sys_attachment.do?sys_id=0bced001db40b4d0471f9c41ba96195a)

3\. Change the business rule condition as below so that it will be triggered for "Decommissioned" devices:

current.hardware\_status == 'retired' || current.hardware\_status == 'stolen' || current.install\_status == 7 || current.install\_status == 8 || current.install\_status == 15

This is for the CIs whose status would change to "Decommission" the next time.  
For the existing CIs, you can use the script which is present in the business rule: Remove Installs For Retired/Stolen CI or contact [Technical Support](http://www.servicenow.com/support/contact-support.html "Technical Support") if you need assistance regarding this.
