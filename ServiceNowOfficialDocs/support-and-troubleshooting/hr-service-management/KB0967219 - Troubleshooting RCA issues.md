---
title: "Troubleshooting RCA issues"
aliases:
  - KB0967219
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0967219
kb_number: KB0967219
last_modified: 2024-10-09
---

## Troubleshooting RCA issues

  

Restricted caller access (RCA) defines cross-scope access to an application and application resource, to set whether other applications can access data in another application.

**Useful community posts:**

-   [https://community.servicenow.com/community?id=community\_blog&sys\_id=ce28d5b8db690c5c5129a851ca961999](https://community.servicenow.com/community?id=community_blog&sys_id=ce28d5b8db690c5c5129a851ca961999 "https://community.servicenow.com/community?id=community_blog&sys_id=ce28d5b8db690c5c5129a851ca961999")
-   [https://community.servicenow.com/community?id=community\_question&sys\_id=cbd8b9badbb9570058dcf4621f961982](https://community.servicenow.com/community?id=community_question&sys_id=cbd8b9badbb9570058dcf4621f961982 "https://community.servicenow.com/community?id=community_question&sys_id=cbd8b9badbb9570058dcf4621f961982")

**Product doc**: [https://docs.servicenow.com/bundle/quebec-application-development/page/build/applications/concept/restricted-caller-access-privilege.html](https://docs.servicenow.com/bundle/quebec-application-development/page/build/applications/concept/restricted-caller-access-privilege.html "https://docs.servicenow.com/bundle/quebec-application-development/page/build/applications/concept/restricted-caller-access-privilege.html")

**Examples of RCA errors:**

Read operation on table 'sn\_hr\_core\_profile' from scope 'Global' was denied because the source could not be found. Please contact the application admin.  
Read operation on table 'sn\_hr\_core\_profile' from scope 'Global' was denied. The application 'Global' must declare a cross scope access privilege. Please contact the application admin to update their access requests.

Source descriptor is empty while recording access for table sn\_hr\_core\_profile: no thrown error

**Some troubleshooting tips:**

1.  OOB the necessary allowed RCA records are included.
2.  RCA issues on customer side are usually due to custom code (e.g. Creating/cloning an OOB widget might create a new RCA record in requested state.  Updating a script include will automatically invalidates an existing allowed RCA records).  **Note**: Customer are advised to perform RCA testing for any custom/customized widget in UAT before going to PROD.
3.  If gliderecord.get(<some valid sys\_id>) returns false, it’s possible due to RCA issue (should be unrelated to ACL since glideRecordSecure is not used)
4.  It’s an obvious RCA issue if you see errors like “The application 'Human Resources: Service Portal' must declare a cross scope access privilege”. 
5.  Some other time, RCA issue might not be as obvious (doesn’t show the cross scope access privilege error on the page) until you debug further.  But in general if there’s any access issue, it’s a good practice to check the system log and check the list of RCA records to see if we need to allow any of the invalidated or requested ones.
6.  If the “Source” of the RCA is a customer-created record, it is the customer’s responsibility to update their RCAs (i.e. not a ServiceNow bug). If the “Source” of the RCA is an OOB, not-modified record, it **may** be a ServiceNow bug. Try to reproduce the issue on an OOB instance to see if the “Requested” RCA will be created.
