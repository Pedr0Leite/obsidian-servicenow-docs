---
title: "Persisting an HTTP session across all REST calls"
aliases:
  - KB0657578
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0657578
kb_number: KB0657578
last_modified: 2024-11-22
---

## Persisting an HTTP session across all REST calls

  

### Issue

When using the REST API RestMessage, executing multiple REST calls in a loop does not use the original session and creates several sessions that can in turn cause authentication errors.

-   \]When viewing stats.do, you may see a list of many sessions being created after running scripted REST API.
-   You receive 401 or 429  errors in subsequent REST calls when expecting to use the same session.

### Cause

Session Cookie not formatted properly.

### Resolution

Session RE-use is possible through the use of cookies.  Cookies are sent in the SET-COOKIE Header and can be retrieved by using the getCookies(); method. 

A cookie should be properly formatted in order to work. Example: 

**Example Real Cookie returned from response**:

\[JSESSIONID=BDE538E6F87C4FA2DFFA0DA9F6E4E14F;Secure; Path=/; HttpOnly, glide\_user="";Secure; Expires=Thu, 01-Jan-1970 00:00:10 GMT; Path=/; HttpOnly, glide\_user\_session="";Secure; Expires=Thu, 01-Jan-1970 00:00:10 GMT; Path=/; HttpOnly, glide\_user\_route=glide.9c5c58ba0c5169641af04031a4b26990;Secure; Expires=Wed, 02-Jan-2086 22:48:02 GMT; Path=/; HttpOnly, glide\_session\_store=41E2F0FDDBC38300E814FA56BF961953;Secure; Expires=Fri, 15-Dec-2017 20:03:55 GMT; Path=/; HttpOnly, BIGipServerpool\_myinstancename=427827210.48704.0000; path=/\]  
  
  
**Example of Cookie after formatted to send in subsequent calls:**  
  
JSESSIONID=BDE538E6F87C4FA2DFFA0DA9F6E4E14F;glide\_user\_route=glide.9c5c58ba0c5169641af04031a4b26990;glide\_session\_store=41E2F0FDDBC38300E814FA56BF961953;BIGipServerpool\_myinstancename=427827210.48704.0000

The following code was used to properly format and store a cookie string and send in subsequent REST calls following an intial request:

var getCallRequest= new sn\_ws.RESTMessageV2(); 

getCallRequest.setEndpoint('https://<instanceName>.service-now.com/api/now/table/incident/<int\_sys\_id>'); 

getCallRequest.setBasicAuth('username','password'); 

getCallRequest.setHttpMethod("get"); 

getCallRequest.setRequestHeader("Accept", "application/json"); 

//execute print response info: 

var getCallResponse = getCallRequest.execute(); 

gs.print("status code: " + getCallResponse.getStatusCode()); 

gs.print("body: " + getCallResponse.getBody()); 

//print cookie info 

var cookies = getCallResponse.getCookies(); 

gs.log("cookies>>>>" + cookies); 

//extract cookies from response 

var jsessionid = ""; 

var glide\_user\_route = ""; 

var glide\_session\_store = ""; 

var BIGipServerpool = ""; 

var cookiesArray = (''+cookies).split(';'); 

//iterate through all cookies, found interesing ones 

for ( var i = 0; i < cookiesArray.length; i++) { 

if( cookiesArray\[i\].indexOf("JSESSIONID") > -1) { 

jsessionid = cookiesArray\[i\].substring( 

cookiesArray\[i\].indexOf("JSESSIONID"),cookiesArray\[i\].length); 

} 

if( cookiesArray\[i\].indexOf("glide\_user\_route") > -1) { 

glide\_user\_route = cookiesArray\[i\].substring( 

cookiesArray\[i\].indexOf("glide\_user\_route"),cookiesArray\[i\].length); 

} 

if( cookiesArray\[i\].indexOf("glide\_session\_store") > -1) { 

glide\_session\_store = cookiesArray\[i\].substring( 

cookiesArray\[i\].indexOf("glide\_session\_store"), cookiesArray\[i\].length); 

} 

if( cookiesArray\[i\].indexOf("BIGipServerpool") > -1 ) { 

BIGipServerpool = cookiesArray\[i\].substring( 

cookiesArray\[i\].indexOf("BIGipServerpool"), cookiesArray\[i\].length); 

} 

} 

//use same cookies in the next 50 calls 

var cookieValueStr = jsessionid + ";" + glide\_user\_route + ";" + glide\_session\_store + ";" + BIGipServerpool; 

gs.log(">>>>> cookieValueStr="+cookieValueStr); 

for (i = 0; i < 50; i++) 

{ 

//getCallRequest.setCookie(cookies); //setCookie not documented 

getCallRequest.setRequestHeader("Cookie",cookieValueStr); 

var putCallResponse = getCallRequest.execute(); 

gs.log(putCallResponse.getBody()); 

}
