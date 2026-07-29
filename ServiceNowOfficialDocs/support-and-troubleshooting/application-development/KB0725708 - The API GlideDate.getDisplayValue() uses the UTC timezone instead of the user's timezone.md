---
title: "The API GlideDate.getDisplayValue() uses the UTC timezone instead of the user's timezone"
aliases:
  - KB0725708
tags:
  - servicenow
  - support-kb
  - glidedate
  - glidedatetime
  - timezone
  - scripting
  - server-side
area: application-development
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0725708
kb_number: KB0725708
last_modified: 2024-01-28
---

## Issue

# Symptoms

* * *

The API **GlideDate.getDisplayValue()** gets the date and time field values in only the UTC (or GMT) timezone.

**GlideDate.getDisplayValue()** is using the UTC timezone to format the response rather than the user's timezone, as is the convention for the xxxDisplayValue() family of methods in the GlideDate/DateTime/Time hierarchy of classes. 

# Cause

* * *

The convention established by GlideDateTime and its related classes is that the get/setDisplayValue methods use the user's timezone while the get/setValue methods use UTC. However, GlideDate does not follow this convention.

# Resolution

* * *

The API **GlideDate.getDisplayValueInternal()** does use the user's timezone. However, it also uses a predictable format. So using this method is a workaround to getting a date and time in the user's timezone.

If one observes that **GlideDate.getDisplayValueInternal()** returns a date that is a day before or after the expected day, that is a result of the difference in hours between UTC and the system or user's timezone.

**To illustrate**:

// Verify we are in the Pacific timezone with this example -  
  
 if (gs.getSysTimeZone() != "US/Pacific") {  
     gs.print("This example requires the system timezone to be US/Pacific");  
 } else {  
  
  
 // Create a GlideDateTime and set the time to 4pm PDT.  
  
 var gdt = new GlideDateTime();  
 gdt.setDisplayValue("2018-12-17 16:00:00:00");  
  
 gs.print( "GlideDateTime.getDisplayValue returns " + gdt.getDisplayValue() );  
   
  
 // The time 16:00:00 in PDT equals to 12 midnight of the following day in UTC.  
 // The GlideDateTime.getValue() method returns the UTC value, so this will print "2018-12-18 00:00:00".  
   
 gs.print( "GlideDateTime.getValue() returns " + gdt.getValue() );  
   
  
 // Now get a GlideDate from the GlideDateTime object. The GlideDateTime.getDate() method returns a GlideDate.  
  
 var gd = gdt.getDate();  
  
   
 // In UTC terms, the date is 12-18, and GlideDate.getValue() follows the convention of using UTC.  
 // So this returns "2018-12-18" which is the correct and expected behaviour.  
  
 gs.print("GlideDate.getValue() returns " + gd.getValue());  
   
   
 // But, getDisplayValue returns the same value as getValue(), rather than following the convention of getDisplayValue().  
 // This would be to return the date in our timezone.  
 // We would like this to return "2018-12-17", but it does not.  
  
 gs.print("GlideDate.getDisplayValue() returns " + gd.getDisplayValue());   
   
  
 // However, the method GlideDate.getDisplayValueInternal() DOES use the user's timezone, so it does return "2018-12-17"  
  
 gs.print("GlideDate.getDisplayValueInternal() returns " + gd.getDisplayValueInternal());  
 }  
  

# Additional Information

* * *

-   [GlideDate - Scoped](https://docs.servicenow.com/csh?topicname=c_GlideDateScopedAPI.html&version=latest "GlideDate - Scoped") \[Madrid\]
-   [GlideDateTime - Global](https://docs.servicenow.com/csh?topicname=c_GlideDateTimeAPI.html&version=latest#c_GlideDateTimeAPI "GlideDateTime - Global") \[Madrid\]
-   [GlideDateTime - Scoped](https://docs.servicenow.com/csh?topicname=c_GlideDateTimeScoped.html&version=latest#c_APIRef "GlideDateTime - Scoped") \[Madrid\]

## Related

- [[KB0594666 - Problems with using gs.nowDateTime() or GlideDateTime.getDisplayValue() in a GlideDateTime constructor]] - related GlideDateTime display-value pitfalls
- [[KB0594663 - gs.dateDiff() (Global GlideSystem) returns invalid results]] - related date/time API scripting issue
- [[KB0812370 - Understand GlideDateTime in flow action scripts and output variables]] - GlideDateTime usage in Flow Designer
- [[c_GlideDateScopedAPI]] - GlideDate scoped API reference
- [[c_GlideDateTimeAPI]] - GlideDateTime global API reference

## Related Notes

- [[ServiceNowOfficialDocs/support-and-troubleshooting/access-controls-authentication/KB0750886 - ACL script is failing at script include function call|ACL script is failing at script include function call]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Core ServiceNow APIs/GlideDate/Convert text date to GlideDate Format/README|Convert text date to GlideDate Format]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Core ServiceNow APIs/GlideDateTime/AddDays/README|AddDays]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Core ServiceNow APIs/GlideDateTime/Business time utilities (add, diff, next open, in schedule)/README|Business time utilities (add, diff, next open, in schedule)]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Core ServiceNow APIs/GlideDateTime/Calculate Due date using user defined schedules/README|Calculate Due date using user defined schedules]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Core ServiceNow APIs/GlideDateTime/Check if today is weekend/README|Check if today is weekend]]
