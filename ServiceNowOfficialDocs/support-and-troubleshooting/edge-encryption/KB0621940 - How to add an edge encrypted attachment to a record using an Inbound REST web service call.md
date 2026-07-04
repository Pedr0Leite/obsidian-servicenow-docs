---
title: "How to add an edge encrypted attachment to a record using an Inbound REST web service call"
aliases:
  - KB0621940
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0621940
kb_number: KB0621940
last_modified: 2024-04-07
---

## How to add an edge encrypted attachment to a record using an Inbound REST web service call

  

### Issue

Adding an edge encrypted attachment to a record using an inbound REST web service call

Overview

* * *

You can encrypt an attachment to a record using an Edge Encryption proxy using an inbound REST POST. By using the REST client Postman, a Chrome browser extension, you can post an attachment to the incident table. This may also be done using other REST clients.

Add an edge encrypted attachment using an inbound REST web service call

* * *

1.  Create an Edge Encryption attachment configuration for the table the REST call makes an attachment to. In the following example, it is the incident table:
    1.  Login to the instance using the Edge Proxy and elevate Roles to security\_admin.
    2.  Navigate to **Edge Encryption Configuration > Encryption Configurations > Create New**.
    3.  Create a new record as follows:
        -   Table=Incident \[incident\]
        -   Type=Attachment
        -   Encryption type = <as appropriate to your environment>
        -   Active = checked
        -   Save
            
2.  In order for the instance to accept the attachment you must set this system property to false in the sys\_properties table:
    
    Name = glide.security.use\_csrf\_token
    
    Type = true|false
    
    Value = false
    
    Otherwise you will see this in the node log when trying to post the attachment:
    
    2017-04-06 14:51:43 (684) Default-thread-48 2882029C4FC2B2002BEDA9D18110C762 WARNING \*\*\* WARNING \*\*\* Attachment request received without valid CSRF token
    
3.  The Postman App and Postman Interceptor Extension need to be added to the Chrome browser. These can be found and added from the Chrome Web Store:  
      
    ![](sys_attachment.do?sys_id=8d8a6c66db42b450e515c223059619df)  
      
    
4.  From Chrome, navigate to **Settings > Extensions > Postman**.
5.  Select **Details > Launch App**.
6.  Set the action to be a POST and set the URL to point to the Edge Encryption hostname, port, and sys\_attachment.do (for example, [https://localhost:8092/sys\_attachment.do)](https://localhost:8092/sys_attachment.do%29).  
    You do not need to set an authorization or any other settings.
7.  Select Body and Form-data, and create the following content:  
      
    
    <table class="internalTable" style="width: 1371px;" align=""><tbody><tr class="sphr"><td style="vertical-align: middle; text-align: left;"><strong>Name</strong></td><td style="vertical-align: middle; text-align: left;"><strong>Value</strong></td><td style="vertical-align: middle; text-align: left;"><strong>Type</strong></td></tr><tr class="sp"><td style="width: 35px; vertical-align: middle;">Content-Type:&nbsp;</td><td style="width: 40px; vertical-align: middle;">multipart/form-data; boundary=---------------------------12296202189918688451571609901</td><td style="width: 40px; vertical-align: middle;">Text</td></tr><tr class="sp"><td style="vertical-align: middle; text-align: left;">Content-Length</td><td style="vertical-align: middle; text-align: left;">23038</td><td style="vertical-align: middle; text-align: left;">Text</td></tr><tr class="sp"><td style="vertical-align: middle; text-align: left;">-----------------------------12296202189918688451571609901</td><td style="vertical-align: middle; text-align: left;">&nbsp;</td><td style="vertical-align: middle; text-align: left;">Text</td></tr><tr class="sp"><td style="vertical-align: middle; text-align: left;">sysparm_sys_id</td><td style="vertical-align: middle; text-align: left;">6ef8cd2fdbf4f200d5cff2131f961927</td><td style="vertical-align: middle; text-align: left;">Text</td></tr><tr class="sp"><td style="vertical-align: middle; text-align: left;">-----------------------------12296202189918688451571609901</td><td style="vertical-align: middle; text-align: left;">&nbsp;</td><td style="vertical-align: middle; text-align: left;">Text</td></tr><tr class="sp"><td style="vertical-align: middle; text-align: left;">sysparm_table</td><td style="vertical-align: middle; text-align: left;">incident</td><td style="vertical-align: middle; text-align: left;">Text</td></tr><tr class="sp"><td style="vertical-align: middle; text-align: left;">-----------------------------12296202189918688451571609901</td><td style="vertical-align: middle; text-align: left;">&nbsp;</td><td style="vertical-align: middle; text-align: left;">Text</td></tr><tr class="sp"><td style="vertical-align: middle; text-align: left;">attachFile</td><td style="vertical-align: middle; text-align: left;">&lt;choose the attachment file, e.g. a file named myFile.txt&gt;</td><td style="vertical-align: middle; text-align: left;">File</td></tr><tr class="sp"><td style="vertical-align: middle; text-align: left;">filename</td><td style="vertical-align: middle; text-align: left;">myFile.txt</td><td style="vertical-align: middle; text-align: left;">Text</td></tr><tr class="sp"><td style="vertical-align: middle; text-align: left;">-----------------------------12296202189918688451571609901--</td><td style="vertical-align: middle; text-align: left;">&nbsp;</td><td style="vertical-align: middle; text-align: left;">Text</td></tr></tbody></table>
    
      
    
    **Notes:**
    
    -   12296202189918688451571609901 is arbitrary and used as the separator of the multipart form data
    -   Maintain the same number of dashes (--------) as in the example for all lines
    -   The value of Content-Length is arbitrary
    -   sysparm\_sys\_id is the sys\_id of the record in the ServiceNow instance where the attachment is made, in this case a sys\_id of an incident record
    -   sysparm\_table is the name of the table that corresponds to the sysparm\_sys\_id, i.e. the table that gets the attachment, in this case the incident table will get the attachment for the incident sys\_id of 6ef8cd2fdbf4f200d5cff2131f961927
    -   attachFile is the actual file that you attach (which you will add to the REST request as loaded from a local file location)
    -   filename is the name of the attachment file stored on the instance
    
      
      
    
8.  From the upper right corner, select the Interceptor icon and set it to active.  
    Following is the complete setting for Postman:  
      
    ![](sys_attachment.do?sys_id=818aac66db42b450e515c22305961922)  
      
      
    
9.  To make the encrypted attachment, select **Send** from Postman.  
    If this is successful, you should see **200 OK** and the Response Body **Attachment processed**:  
      
    ![](sys_attachment.do?sys_id=598aac66db42b450e515c2230596196f)  
      
    
10.  To verify the attachment is not accessible when bypassing the Edge Encryption Proxy, log into the instance using the non-Edge Encryption proxy URL (for example, the normal https://<instance\_name>.service-now.com) and go to the record where the attachment was made (for example, to the sysparm\_table table and the sysparm\_sys\_id sys\_id).
11.  Select the attachment.  
     The following information is displayed:  
       
     ![](sys_attachment.do?sys_id=5d8aac66db42b450e515c22305961984)  
       
     This indicates that the attachment is not accessible because it is encrypted and you are not accessing the record using the Edge Encryption proxy.  
       
     
12.  To verify that the attachment is accessible using the Edge Encryption Proxy, log into the instance using the Edge Encryption proxy URL, and go to the record where the attachment was made (to the sysparm\_table table and the sysparm\_sys\_id sys\_id). When you select the attachment, you have the option to download:  
       
     ![](sys_attachment.do?sys_id=958aac66db42b450e515c2230596198c)  
       
     After downloading the file, ensure that the content is as expected and is not encrypted.
