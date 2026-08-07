---
title: "Description field on the \"discovery_printer_supplies\" table has hex values instead of a string"
aliases:
  - KB0713205
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0713205
kb_number: KB0713205
last_modified: 2024-04-07
---

## Description field on the "discovery\_printer\_supplies" table has hex values instead of a string

  

### Issue

# Symptoms

* * *

When you run disocvery on printers, the description field on "discovery\_printer\_supplies" records have hex values instead of a string.

# Release

* * *

Applicable to all releases

# Cause

* * *

The printer supplies information is queried at the OID "1.3.6.1.2.1.43.11" from the SNMP - Printing probe. 

If we are getting back a hex value from this probe, we are directly parsing this value from the payload and updating the description field on discovery\_printer\_supplies records. So you might see hex values in place of a string.

# Resolution

* * *

Create an update/insert business rule on discovery\_printer\_supplies table. Make the business rule advanced and paste the following code:

\--------------------------------------------------------------------------------

(function executeRule(current, previous /\*null when async\*/) {   
  
var input = current.description   
var nospace = input.replace(/\\s/g, ''); //remove spaces from the hex value we have   
  
regexp = /^\[0-9a-fA-F\]+$/;   
var res = regexp.test(nospace); //validate if the value we have is hex   
  
if (res == true){ //convert to string only if the value we have is hex   
var string = '';   
for (var i = 0; i < nospace.length; i += 2) {   
string += String.fromCharCode(parseInt(nospace.substr(i, 2), 16));   
}   
current.description = string;   
}   
  
})(current, previous); 

\--------------------------------------------------------------------------------

* * *

Save the business rule and run discovery on the affected printers.
