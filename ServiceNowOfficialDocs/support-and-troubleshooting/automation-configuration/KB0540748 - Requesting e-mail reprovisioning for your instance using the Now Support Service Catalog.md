---
title: "Requesting e-mail reprovisioning for your instance using the Now Support Service Catalog"
aliases:
  - KB0540748
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0540748
kb_number: KB0540748
last_modified: 2026-03-10
---

## Requesting e-mail reprovisioning for your instance using the Now Support Service Catalog

  

### Issue

ServiceNow has created an automated workflow to support reprovisioning email for an instance. Customers request email reprovisioning via a Service Catalog item to create a Change, which is completed using **end-to-end automation**.

If email settings for an instance have been changed, users with the **customer\_admin** role can request that email be reprovisioned for the selected instance. The process may take approximately an hour (but will usually be completed in less than 10 minutes) and you will receive a confirmation email when the process is complete. ServiceNow disables email after the provisioning process to stop queued emails from being sent.

**Note:** Email reprovisioning _**should not be**_ requested for an instance that is not experiencing an email configuration outage.

**Note:** the above does not apply for customers who have requested custom DKIM records as per [KB1002273](https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB1002273) as reprovisioning email is required after setting up custom DKIM

**Note:** 

**It's Better to check , the  'ignore cache' set to "true" on the 'sys\_properties' record, because when during the  email reprovisioning is being performed , It will disable and enable the email sending and receiving properties, which might cause the instance being unavailable, it's recommended to perform this post working hours in prod.**

You can request the reprovisioning email service catalog by following below steps:

1.  Navigate to the [**Now Support**](https://support.servicenow.com/now "Now Support")
2.  Browse to the [**Automation Store**](/now?id=ns_automation_store "Automation Store")
3.  Under **Instance Management**, select **Reprovision Email  
    or  
    **You can also access this catalog via Now Support app (Download Now Support App for **[Android](https://play.google.com/store/apps/details?id=com.servicenow.support "Android")** | **[iOS](https://apps.apple.com/app/now-support/id1504338471 "iOS")**)
4.  Choose the **instance** for which you want to request email reprovisioning
5.  Click on **Submit** button**  
    ![Service Catalog item](/sys_attachment.do?sys_id=60f7b18b975f72900ed83bbe2153afae "Service Catalog item")  
    **
6.  A new change request is created for the email reprovisioning and the request is displayed automatically. As needed, add people to the **Watch list** and any **Additional comments** as necessary and click on **Save**.  
      
    ![Service details](/sys_attachment.do?sys_id=e4f7b18b975f72900ed83bbe2153aff1 "Service details")  
      
    
7.  After the provisioning process has completed, you will receive a confirmation email. ServiceNow temporarily disables email after the provisioning process to stop queued emails from being sent.  To re-enable email sending and receiving after email provisioning go to System Mailboxes -> Administration -> Email Properties and check the boxes for "Email sending enabled" and "Email receiving enabled" and Save.

### Facts

 If you [create a new system property](https://docs.servicenow.com/csh?topicname=t_AddAPropertyUsingSysPropsList.html&version=latest) (Glide Property) in your ServiceNow instance, you should almost always have 'ignore cache' set to "true" on the 'sys\_properties' record. If a property value is changed that has 'ignore cache' set to false, then it will trigger a whole Glide System cache flush, potentially resulting in system-wide performance degradation as the caches are rebuilt.

You should not change Glide Property values frequently. As a general rule of thumb, they should not be changed more than once a month if 'ignore cache' is set to "true". They should not be changed more than once an hour if 'ignore cache' is set to "false".

If 'ignore cache' is set to false, when you change a Glide Property, it will cause a system-wide cache flush. This usually leads to mild performance degradation for anywhere from 5 to 30 minutes. In some very rare cases, this may result in severe performance degradation with average transaction response times increasing twofold or even threefold. The degradation experienced is very similar to that of applying an Update Set. You should take the same level of caution when changing a Glide Property that has 'ignore cache' set to false as you do when applying an Update Set.

### Release

### Resolution

### Related Links

[https://support.servicenow.com/kb?id=kb\_article\_view&sysparm\_article=KB1000746](https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB1000746)
