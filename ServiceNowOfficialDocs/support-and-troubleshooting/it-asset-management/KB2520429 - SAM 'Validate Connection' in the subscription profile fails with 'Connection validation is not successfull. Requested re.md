---
title: "SAM : 'Validate Connection' in the subscription profile fails with 'Connection validation is not successfull. Requested resource does not exist."
aliases:
  - KB2520429
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB2520429
kb_number: KB2520429
last_modified: 2026-05-22
---

## SAM : 'Validate Connection' in the subscription profile fails with 'Connection validation is not successfull. Requested resource does not exist.'

  

### Issue

Unable to validate the connection between ServiceNow and Salesforce, resulting in the inability to publish the Integration profile.

The error message received is 'Connection validation is not successful. The requested resource does not exist.'

The example of salesforce is used here, but this issue could happen for any of the other integrations as well.

1.  Navigate to samp\_sw\_subscription\_profile table.
2.  Open a profile
3.  Click on the 'Validate Connection' UI button 

Notice the error message as in the screenshot. PFA:  
![Unsuccessful connection validation .png](sys_attachment.do?sys_id=6295888d470983987947e551336d43ca)

### Facts

### Release

Tested and validated in : Yokohama patch4,  
Salesforce Spoke : sn\_sforce\_v2\_spoke : v 2.3.2

### Cause

1\. Checking the sys\_outbound\_http\_log table at the time of the connection validations, we could see a couple of requests failed with 400 error which essentially means bad request.

The URL looked something like below :

https://{instancename}--sit.sandbox.my.salesforce.com/services/data//query/?q=Select+OrganizationType+from+Organization

This clearly indicates a missing parameter.

2\. 'Connection validation' UI button basically validates the http connection that the customer has created for the particular profile.

3\. Compare the http connection record to a working instance, and verify if the API version attribute is missing in the form field of the http connection record.

PFA: version\_missing

4\. Compare to OOTB for any missing parameters in the connection\_attributes table corresponding to the related application of the integration profile.

https://{instance\_name}.service-now.com/connection\_attributes\_list.do?sysparm\_query=sys\_scope.nameLIKEsalesforce&sysparm\_view=

### Resolution

1\. Repair the Salesforce Spokes(or related plugin) plugin to reload the deleted file.

2\. Check the installation logs to ensure the api\_version is added: https://{instance\_name}.service-now.com/now/app-manager/home/app/id/4429c1ee1bd99410c9527669cc4bcb0a/v/2.3.3/details

3\. Verify that the api\_version is added: https://{instance\_name}.service-now.com/connection\_attributes\_list.do?sysparm\_query=nameLIKE589aaf931b5d1810c9527669cc4bcb77&sysparm\_view= 

(this example is for salesforce)

Also, verify in the http\_connection. PFA: after\_repair

4\. Test the connection validation again to ensure it is successful.
