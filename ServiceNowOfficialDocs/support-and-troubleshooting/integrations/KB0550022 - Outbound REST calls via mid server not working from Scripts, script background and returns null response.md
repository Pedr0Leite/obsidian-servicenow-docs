---
title: "Outbound REST calls via mid server not working from Scripts, script background and returns null response"
aliases:
  - KB0550022
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0550022
kb_number: KB0550022
last_modified: 2024-04-07
---

## Outbound REST calls via mid server not working from Scripts, script background and returns null response

  

### Issue

Outbound REST calls via mid server not working from scripts, script background and returns null response

Problem

* * *

Outbound REST calls through the Mid Server are not working from scripts, script background and returns null response.  

Symptoms

* * *

For example: Here is a REST call script with a GET function executed thought the MID Server:  
  
var r = new RESTMessage('XYZ Organization', 'get');  
r.setStringParameter('XYZ\_host', '123.123.123.123');  
r.setStringParameter('org\_id', '4');  
var response = r.execute();

These are the symptoms:  

-   The Test (Related Link) always works successfully.
-   The previewed script, pasted into a Background Script _never_ works – the response value is always null.
-   In addition, the previewed script pasted into a script include and used by a scheduled job _never_ works – the response value is always null.

Cause

* * *

When using the Mid Server, the script executed from background or business rule/script does not wait for an response, hence the response is null.

Resolution

* * *

The REST call has to be modified like below to wait and get the response when executed from scripts, background scripts, or business rules. 

  
var r = new RESTMessage('XYZ Organization', 'get');  
r.setStringParameter('XYZ\_host', '123.123.123.123');  
r.setStringParameter('org\_id', '4');  
var response = r.execute();  
var k = 1;   
while ( response == null ) {   
gs.print( "waiting ... " + k + " seconds" );   
response = r.getResponse( 1000 );   
k++;   
  
if ( k > 30 ) {   
gs.print( 'service time-out' );   
break; // service did not respond after 30 tries   
}   
}   
gs.print( "RESPONSE: " + response );   
if ( response != null ) {   
gs.print( 'body=' + response.getBody() );   
}
