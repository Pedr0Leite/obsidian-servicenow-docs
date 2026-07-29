---
title: "Requesting an instance rename with Now Support Service Catalog"
aliases:
  - KB0550695
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0550695
kb_number: KB0550695
last_modified: 2026-05-30
---

## Requesting an instance rename with Now Support Service Catalog

  

### Issue

ServiceNow has created an automated workflow to support the instance rename process. Users with the **NS Admin role** can request an instance rename via a Service Catalog item to create a Change, which is completed using **end-to-end automation**.

**Note:** This procedure is only applicable to some hosted instances, including production and sub-production. Demonstration, Developer instances, Jumpstart instances, and Temp instances are **excluded from this rename automation** and **cannot be renamed**. Please review our [Instance Rename Policy](https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0550841) for more information. If you need to rename an on-premise instance in Now Support, please follow [KB0551693 - Manage On-Premise Instance - Now Support Service Catalog](https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0551693). 

Learn more about this Service Catalog and its benefits on **[Now Community](https://community.servicenow.com/community?id=community_blog&sys_id=044e2fdbdb2fc89423f4a345ca96193f "Now Community")**.

Before requesting an instance rename, check if you have the customer\_admin role.  
**Identify the Now Support Administrators on your Account.**

If you want to check whether you have the customer\_admin role or want to identify your NowSupport administrator after you have logged in to Now Support, by following the steps below:

1.  Navigate to [Now Support portal](https://support.servicenow.com/now "Now Support portal")
2.  Click on your user name in the upper right corner and click on My Profile.
3.  See who is listed in the ServiceNow admins table for account support.

**You can request Instance Rename by following these steps:**

1.  Navigate to **[Now Support](https://support.servicenow.com/now "Now Support")**
2.  Click on the **Automation Store**
3.  On the left side, click on **Service Catalog**, click on **Instance Management**
4.  Go to the second page and click on **Rename an Instance**  
      
    ![Navigate to Now Support, click Automation Store, Service Catalog, Instance Management, go to second page, click Rename an Instance](sys_attachment.do?sys_id=f9f7d1df931db6107c79b36d6cba10a6)  
      
    
5.  Select the instance to rename from the filtered reference field  
    **Note:**  
    -   If you are having trouble finding your instance, use "\*" for a "contains" query.
    -   For OEM instances, the rename request should be made by OEM vendors. If you are not an OEM vendor, an error message will be shown and you will not be able to submit the request.
    -   The OEM instance naming convention requires to have "**oem**" in the name to differentiate from the enterprise instance.
6.  Provide a new instance name (Please refer to **[Instance rename policy](https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0550841 "Instance rename policy")** before providing a new instance name)
7.  Select Maintenance Start time from available slots  
    **IMPORTANT:** Please plan the instance rename several days in advance if possible. Note that if there are other change requests already pending for that instance (in particular instance moves) it will not be possible to schedule an instance rename until after those other change requests have been completed
8.  Specify how long the old URL should be active after renaming.  
    **Note:** By default, ServiceNow retains the old URL for **2 business days**. You can request to retain the old URL for **up to 30 days**.
9.  Acknowledge disclaimers for **rename action** and ServiceNow **Instance Rename Policy  
    **
10.  Click on **Submit**  
     -   A new change request is created for the rename request, and the request is displayed automatically.
     -   As needed, add people to the **Watch list** as necessary.
11.  Click **Update**

###  Important notes

1.  After the completion of the instance rename process, you might receive an _"**Unknown host**"_ error message while submitting a clone request or a _"**Target instance already exists**"_ error message while trying to create a new clone target. This usually means that there are already existing clone target records created for the renamed instance from another source instance. Please review and follow [KB0715227](https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0715227 "KB0715227") and [KB0686736](https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0686736 "KB0686736") to update your clone target.
2.  As a Customer Administrator, you can not rename an instance of a child company. If you need to rename your child company instance, you will need to log into your child company account to initiate the instance rename process.
3.  As a Partner Administrator, you can not rename your customers' instances. You will have to ask the customer administrator of that company to submit an instance rename request.
4.  The change window for the instance rename will appear on the change ticket as the planned start and end time. 
5.  Beginning at the Planned Start Time the instance will not be available for up to 30 minutes.
6.  Do not run any clones to/from the instance once the rename has started.
7.  New instance and old instance URLs are simultaneously available for the time provided in the request.  
    -   During this time, the cloning functionality is not available.
8.  After the rename, the following settings may require updating:  
    -   Email settings are reset to the out-of-box values and updated to reflect the new instance name. This change is made after the new instance URL becomes available. Any inbound emails sent to the old instance email may be lost after this change has been made. Customers will likely need to update the email settings in their instance to reflect any previously implemented customization.
    -   If the customer is using Single Sign On through the Multi-Provider SSO plugin, they will need to check each of their Identity Provider records (Multi-Provider SSO > Identity Provider) and update any URLs in those settings which point to the old instance name.

### MID Server considerations

-   Each MID server will need to be updated individually to point to the new instance name:  
    1.  Go to the MID server installation path
    2.  Edit the .\\agent\\config.xml file using a text editor (such as WordPad), as follows:  
        1.  Locate the <parameter name="url" value="https://YOUR\_INSTANCE.service-now.com" /> element
        2.  Change the value to the URL of the NEW Instance
    3.  Also, if there are any changes to the certificates, install the new certificates by following the documentation below:  
        -   [Add SSL certificates for the MID Server](https://docs.servicenow.com/bundle/vancouver-servicenow-platform/page/product/mid-server/task/add-ssl-certificates.html "Add SSL certificates for the MID Server")

### URL Retention Period

-   IMPORTANT: URLs are are retained for 2-7 days by default. ServiceNow implements a URL redirection (accessing "<old\_instance\_name>.service-now.com" which will cause a HTTP Redirect (301) to "<new\_instance\_name>.service-now.com") during this period. We strongly encourage you to review any integrations you may have that cannot support 301 redirections ahead of the retention period. 

### Release

N/a

### Resolution

  N/a
