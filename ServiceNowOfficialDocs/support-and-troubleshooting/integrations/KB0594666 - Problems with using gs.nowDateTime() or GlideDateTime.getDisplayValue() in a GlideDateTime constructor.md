---
title: "Problems with using gs.nowDateTime() or GlideDateTime.getDisplayValue() in a GlideDateTime constructor"
aliases:
  - KB0594666
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0594666
kb_number: KB0594666
last_modified: 2025-10-08
---

## Problems with using gs.nowDateTime() or GlideDateTime.getDisplayValue() in a GlideDateTime constructor

  

### Issue

To avoid date and time issues in your applications, avoid using gs.nowDateTime() or GlideDateTime.getDisplayValue() in a GlideDateTime constructor.

The GlideDateTime constructor has a several options:

-   No-argument: Initializes to the current date/time
-   GlideDateTime object: Initializes to the same date/time as the argument
-   String: In the format YYYY-MM-DD HH:MI:SS and is treated as UTC date and time

Passing a non-UTC string value leads to time shifts and unexpected behavior in your applications.

### Release

Any supported release

### Cause

To create a GlideDateTime object with the current date and time, you should not provide a parameter. Call the constructor of the GlideDateTime class without arguments to initialize the value to the current date and time.

// Do this  
var dgt = new GlideDateTime();

//Not this  
var gdt = new GlideDateTime(gs.nowDateTime());

If you use the gs.nowDateTime() method to set a GlideDateTime object, the method returns the date time in local format and the local time zone. The GlideDateTime object uses the date time in the internal format and UTC time zone.

The code is uses the display date and time value where it should be UTC instead:

var gdt = new GlideDateTime();  
var gdt2 = new GlideDateTime(gdt.getDisplayValue());

This results in the second GlideDateTime object internal value shifting by an amount equivalent to the time zone offset between the session time zone and UTC.

For example:

var gdt = new GlideDateTime();  
gs.info('1. UTC: ' + gdt.getValue());  
gs.info('2. Local/Dispay: ' + gdt.getDisplayValue()); // Local TZ for this example is America/Los\_Angeles  
gs.info(' ');  
gs.info('3. nowDateTime: ' + gs.nowDateTime());  
gs.info(' ');  
var gdt2 = new GlideDateTime(gs.nowDateTime()); // BAD!  
gs.info('4. UTC: ' + gdt2);  
gs.info('5. Local/Display: ' + gdt2.getDisplayValue());

which outputs as:

\*\*\* Script: 1. UTC: 2022-01-18 16:48:13  
\*\*\* Script: 2. Local/Display: 2022-01-18 08:48:13  
\*\*\* Script:    
\*\*\* Script: 3. nowDateTime: 2022-01-18 08:48:13  
\*\*\* Script:    
\*\*\* Script: 4. UTC: 2022-01-18 08:48:13  
\*\*\* Script: 5. Local/Display: 2022-01-18 00:48:13

In this output, the first GlideDateTime object is initialized to the current date and time since no value was passed to its constructor. Output 2 and 3 display the local date and time formatted according to the glide.sys.date\_format and glide.sys.time\_format. Output 1 shows the GlideDateTime internal UTC value. 

The second GlideDateTime object received the local date and time value, which is already offset by UTC -8 because the instance is using America/Los Angeles as its default time zone during the session where the script is run.  The GlideDateTime(string) constructor expects a date and time value in UTC, so the American/Los\_Angeles date/time value is shifted by -8 hours for both the internal value (4) and display value (5).

Using a nonstandard data and time format can lead to more problems. If the GlideDateTime(string) constructor is unable to convert the string to a valid date and time using the yyyy-MM-dd HH:mm:ss format, it tries a number of other "emergency" formats. If the string argument can parse successfully with one of those formats, it may not be what is expected. 

Enabling Debug Date/Time shows if this is occurring. Common problems can occur when an instance is configured to use a date format like dd/MM/yyyy but is given a date in the format MM/dd/yyyy.  For example the 3rd January 2021 as 03/12/2021 using dd/MM/yyyy would match MM/dd/yyyy first and the date would be 12th March 2021.

With Debug Date/Time enabled, passing a junk string to GlideDateTime reports all the emergency formats tried in the debug output.  As of the Xanadu release, that list, in order, is:

yyyy-MM-dd HH:mm:ss  
yyyy-MM-dd'T'HH:mm:ss.SSSZ  
MM/dd/yyyy HH:mm:ss  
MM-dd-yyyy HH:mm:ss  
MM-dd-yyyy HH:mm  
MM-dd-yyyy  
MM/dd/yy HH:mm:ss  
MM/dd/yyyy  
dd-MM-yyyy HH:mm:ss  
dd-MM-yyyy HH.mm.ss  
dd-MM-yyyy HH.mm  
dd-MM-yy HH:mm:ss  
dd-MM-yy HH.mm.ss  
dd/MM/yyyy  
dd-MM-yyyy  
yyyy-MM-dd HH:mm  
yyyy-MM-dd

**Note**: The gs.nowDateTime() method is not available in scoped applications.

### Resolution

Ensure that display date and time values are not used in a context where UTC is expected.  You can make this clearer in code by using the getValue()/setValue() and getDisplayValue()/setDisplayValue() methods consistently throughout the code.

### Related Links

[GlideDateTime constructor](https://developer.servicenow.com/dev.do#!/reference/api/quebec/server/no-namespace/c_APIRef#r_ScopedGlideDateTimeGlideDateTime?navFilter=GlideDateTime "GlideDateTime constructor")
