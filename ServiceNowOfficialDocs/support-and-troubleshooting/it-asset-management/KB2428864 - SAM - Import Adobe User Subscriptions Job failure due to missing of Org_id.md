---
title: "SAM - Import Adobe User Subscriptions Job failure due to missing of Org_id"
aliases:
  - KB2428864
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB2428864
kb_number: KB2428864
last_modified: 2026-05-08
---

## SAM - Import Adobe User Subscriptions Job failure due to missing of Org\_id

  

### Issue

SAM - Import Adobe User Subscriptions Job will fail with the Error 404 if the Org\_Id is missing. 

### Symptoms

The "SAM - Import Adobe User Subscriptions" will fail with NO error in the samp\_job\_log.LIST table. 

But if we can observe the "sys\_outbound\_http\_log\_list" for the URL: usermanagement.adobe.io, we can observe the Error 404

### Release

ALL

### Cause

Missing Org\_Id in the Attributes section of HTTP(s) Connection Adobe Credentials for the below connection URL  
  
Connection URL: https://ims-na1.adobelogin.com

The fact that the Direct Integration profile has the Org\_Id will not satisfy the GET request URL construction, as it will be dependent on HTTP(s) Connection Adobe Credentials. 

### Resolution

In general, A 404 error is an HTTP status code that indicates the webpage a user is trying to access cannot be found on the server. It signals that the requested page either doesn't exist, has been moved, or has been deleted. 

If you observe the GET request constructs from the HTTP(s) connection, the Attributes Organisation ID. So, if it is missing, then the URL gets constructed like https://usermanagement.adobe.io/v2/usermanagement//products, which is incorrect and can cause a 404 ERROR.   
  
![](/sys_attachment.do?sys_id=a0ad6c2093b4c358f2167de86cba10a3)  
  
Need to fill the Org\_ID from the above page to get the GET request constructed like below: {The below URL is for TEST illustration}  
  
https://usermanagement.adobe.io/v2/usermanagement/1234567890abcdef12345678@AdobeOrg/products
