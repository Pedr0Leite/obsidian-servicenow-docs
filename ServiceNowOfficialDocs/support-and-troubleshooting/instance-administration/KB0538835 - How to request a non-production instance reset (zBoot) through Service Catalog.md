---
title: "How to request a non-production instance reset (zBoot) through Service Catalog"
aliases:
  - KB0538835
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0538835
kb_number: KB0538835
last_modified: 2026-04-21
---

## How to request a non-production instance reset (zBoot) through Service Catalog

  

### Issue

You can request an automated reset (zBoot) of your **non-production** instance. A zBoot deletes all data on an instance and restores the instance to base system settings. This request is done through a Service Catalog item to create a Change (CHG), which is completed using end-to-end automation. If you have the customer\_admin or partner\_admin role, you can submit this request without contacting Technical Support. 

**Note:** After the zBoot completes, you must reinstall all plugins that are not part of the base system installation. You can install some plugins yourself. Other plugins require individual requests through the Service Catalog. For instructions, see [Plugin Activation Overview](https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0695388). 

This procedure applies only to non-production instances. To request a zBoot of a production instance, submit a case with [Technical Support](https://support.servicenow.com/kb_view.do?sysparm_article=KB0547203 "Technical Support"). 

**Important:** Only request a zBoot when you are ready for the process to begin at the designated start time. The zBoot resets the instance to the base system settings and removes all current customizations and data. 

### Release

All supported releases

### Resolution

To request a zBoot for a non-production instance

1.  Go to [Now Support](https://support.servicenow.com/now "Now Support")
2.  Go to the [Automation Store](/now?id=ns_automation_store "Automation Store")
3.  Under **Instance Management**, select **zBoot an Instance (Non-Prod)**. You can also access this catalog using the Now Support app (Download Now Support App for [Android](https://play.google.com/store/apps/details?id=com.servicenow.support "Android") | [iOS](https://apps.apple.com/app/now-support/id1504338471 "iOS")).
4.  Select the instance you want to reset.
5.  Select the maintenance start time when the instance can be reset.
6.  For the **Reinstall Demo Data after zBoot** option, make your permanent selection. You cannot modify this option after submission.   
      
    If you do not want demo data on your zBooted instance, wait for the instance to be successfully reset and then request for the demo data to be removed manually. You do this using the **Remove Demo Data** Service Catalog item.   
      
    ![Requesting to zBoot an instance](/sys_attachment.do?sys_id=72f9ab389779b2d8f03d739c1253afdd)  
      
    
7.  Select **Submit**. 
8.  Review the confirmation message.   
    ![Confirmation warning message](sys_attachment.do?sys_id=8ff9eb389779b2d8f03d739c1253af24)  
      
    
9.  Review the change request created for your zBoot. The planned end date is automatically calculated based on the planned start date plus five hours, which is approximately how long the zBoot process takes.  
      
    Add people to the Watch list and any additional comments as necessary, and then select **Save**.  
      
    ![Form to fill out, adding start/end date, people, etc.](/sys_attachment.do?sys_id=c7f9ab389779b2d8f03d739c1253afe2)  
      
    
10.  The zBoot operation starts at the specified date and time in the change request.
11.  Track the progress of the zBoot operation through the change request.
12.  To reschedule or cancel the zBoot, select the respective button in the change request.

### Request a zBoot for a Technology Partner Program developer Instance

1.  You can use the same service catalog item for developer instances within the Technology Partner Program. These instances use the naming convention:   
    
    SNC Instance - venXXXXXXXXXXX
    
2.  When you select a developer instance, the automated zBoot begins and the change request is assigned to the Technology Partner Program group.
3.  If the change fails, the change category is adjusted and the assignment group remains the Technology Partner Program group for investigation.
