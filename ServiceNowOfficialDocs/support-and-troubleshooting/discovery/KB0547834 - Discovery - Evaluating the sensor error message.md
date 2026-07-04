---
title: "Discovery - Evaluating the sensor error message"
aliases:
  - KB0547834
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0547834
kb_number: KB0547834
last_modified: 2024-04-30
---

## Discovery - Evaluating the sensor error message

  

### Issue

Evaluating the sensor error message 

  
  

# Overview

* * *

The `Sensor error` message occurs when the sensor cannot process the data that is sent back by the probe. Different versions of the sensor error message indicate different processing errors.

# Types of sensor error messages

* * *

The type of sensor error message is related to one of the error constructors in JavaScript. The following error constructors may contribute to the sensor error message.

-   `Error`: The generic constructor that indicates the sensor can not process the data.
-   `EvalError`: Indicates that an error has occurred in the global `eval()` function.
-   `InternalError`: Indicates that an internal error in the Javascript engine has occurred, such as for too much recursion.
-   `RangeError`: Indicates that a numeric variable or parameter is outside of its valid range in the sensor.
-   `ReferenceError`: Indicates an error occurs when the sensor processing attempts to dereference a variable that has not been declared.
-   `SyntaxError`: Indicates a syntax error in the sensor.
-   `TypeError`: Indicates that an operand or argument that is passed to a sensor function is incompatible with the type expected by that operator or function.
-   `URIError`: Indicates that `encodeURI()` or `decodeURI()` are passed invalid parameters in the sensor.

  

# Finding the cause of the sensor error message

* * *

To find the cause of this error, you identify the following:

-   The error
-   The name of the sensor where the error occurred
-   The datestamp of the error
-   The associated stack trace of the error

To identify the error, the name of the sensor, and the datestamp of the error:

1.  Navigate to **Discovery > Discovery Log**
2.  To find the error, filter on the **Level name** of **Error**.
    
    You can also view the error and the datestamp in the Error Gauge on the Discovery dashboard.
    
3.  Note the **Created** field of the error record.
    
    This timestamp is used to find the proper stack trace.
    
4.  Note the **Short Message** field of the error record
    
    This field shows the name of the sensor where the error has occurred.
    

In the following example, a generic sensor error occurred at in the **SMI – Fiber Channel Switch** sensor at 4:03 on 10-24-2014. 

![](/ErrorMessageShortMessageField.pngx)

In the following example, a sensor TypeError occurred in the **Windows – Installed Software** sensor. 

![](/ErrorShortMessageField.pngx)

To find the stack trace:

1.  Navigate to **System Logs > Errors**.
2.  Search for the date and time that matches the value in the '_Created field_ of the error record in the discovery log.
3.  The **Message** field of that entry contains the full stack trace of the error.   
    
    The stack trace contains the error message, the sys\_id of the script, and the line number where the error occurred.
    

In the following example, the stack trace shows the following:

-   **Line 1 and 2:** There was a JavaScript evaluation error on **new DiscoverySmiFcSwitchSensor()**.
-   **Line 3:** The Ci.controller variable is undefined.
-   **Line 4:** This script\_includes line indicates the sysid _7780111 ... d768_ and the error occurred at approximately line **26** of the JavaScript file.

![](/DiscoverySensorStackTrace.pngx)  

 After you have determined these details, you can fix the JavaScript file.

# Fixing the sensor error message

* * *

To fix the **Sensor Error Message**, you must fix the JavaScript file that contains the code that generated the error. 

To fix the JavaScript file:

1.  Navigate to the module in Discovery that the error occurred.
    
    In the example, you navigate to **Discovery Definition > Script Includes**.
    
2.  Fix the error.
    
    In the example, you search for **DiscoverySmiFcSwitchSensor** in the **Name** field.
    

![](/DiscoverySensorStackTraceJavaScript.pngx)  
Click on the link to go to the details page for that **Script Include**.Modify the JavaScript script on that page to fix the error indicated.Click **Update**.
