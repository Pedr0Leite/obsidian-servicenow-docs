---
title: "Unable to view email content from Activity stream on HR Case record"
aliases:
  - KB0719155
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0719155
kb_number: KB0719155
last_modified: 2025-09-03
---

## Unable to view email content from Activity stream on HR Case record

  

### Issue

HR Case records have been configured to display emails in the Activity stream/log; however, clicking the link (show email details) displays the following errors:

UI errors:

**No such parent record**

List View errors on sys\_email table:

**"Read operation on table 'sn\_hr\_core\_case\_total\_rewards' from scope 'Global' was denied because the source could not be found. Please contact the application admin.  
  
Error Message Read operation on table 'sn\_hr\_core\_case\_total\_rewards' from scope 'Global' was denied. The application 'Global' must declare a cross scope access privilege. Please contact the application admin to update their access requests.  
  
Error Message Read operation on table 'sn\_hr\_core\_case\_total\_rewards' from scope 'Global' was denied because the source could not be found. Please contact the application admin.  
  
Error Message Read operation on table 'sn\_hr\_core\_case\_total\_rewards' from scope 'Global' was denied. The application 'Global' must declare a cross scope access privilege. Please contact the application admin to update their access requests."**

![](sys_attachment.do?sys_id=cabe5530db857410471f9c41ba9619bd)

  

Log errors:

**Source descriptor is empty while recording access for table sn\_hr\_core\_case\_total\_rewards: no thrown error** 

**![](sys_attachment.do?sys_id=17ba20e6db42b450e515c22305961920)**

### Release

All releases

### Cause

HR Case records have been configured to display emails in the activity stream, which is not configured as such in an out-of-box instance.

For information on how to enable emails to be displayed in the activity stream check [KB0719147 - How to configure and display 'Sent/Received Email' in the activity stream/log](https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0719147 "KB0719147 - How to configure and display 'Sent/Received Email' in the activity stream/log")  

The email content cannot be accessed from the Human Resources: Core scope, hence these errors.

### Resolution

Create a Restricted Caller Access Privilege record by:

1) Navigating to System Applications ==> Application Restricted Access Privilege.

2) Click the New button and then add the following information:

**Source Scope** = Global  
**Source Type** = Scope  
**Status** = Allowed  
**Target Scope** = Human Resources: Core  
**Target Type** = Scope.

When the record is created now clicking on the 'show email details' link from the activity stream actually shows the content of the email.

### Related Links

Roles can be configured for the Activity stream from the system property (glide.ui.activity.email\_roles).
