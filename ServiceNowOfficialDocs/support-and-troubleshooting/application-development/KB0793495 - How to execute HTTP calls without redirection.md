---
title: "How to execute HTTP calls without redirection"
aliases:
  - KB0793495
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0793495
kb_number: KB0793495
last_modified: 2024-04-08
---

## Issue

For our integration purposes, we would need to turn off http redirection in ServiceNow instances.

Note: This is already possible for  other applications (for example by Postman).

## Resolution

If using [GlideHTTPRequest:setFollowRedirect(boolean)](https://docs.servicenow.com/csh?topicname=GlideHTTPRequestAPI.html&version=latest#GlideHTTPRequest-setFollowRedirect "GlideHTTPRequest:setFollowRedirect(boolean)")  does not meet your  business requirement, then you can create the following property 'glide.http.redirect\_with\_auth', (type true/false) and set it to true.  
  
In order to validate this we did test with [http://gmail.com](http://gmail.com) and the results are as follows:   
  
Here is the script used for testing:

var get = new sn\_ws.RESTMessageV2();  
get.setHttpMethod("get");  
get.setEndpoint("[http://gmail.com](http://gmail.com)");  
var res = get.execute();  
gs.print("status code: " + res.getStatusCode());  
gs.print("body: " + res.getBody());

  

When the property is set to false:

\*\*\* Script: status code: 200  
\*\*\* Script: body:  
<!DOCTYPE html>  
<html lang="en">  
<head>  
<meta charset="utf-8">

  
  
When the property is set to true:

\*\*\* Script: status code: 302  
\*\*\* Script: body: <HTML>  
<HEAD>  
<TITLE>Moved Temporarily</TITLE>  
</HEAD>  
<BODY BGCOLOR="#FFFFFF" TEXT="#000000">  
<H1>Moved Temporarily</H1>  
The document has moved <A HREF="[https://mail.google.com/mail/](https://mail.google.com/mail/)">here</A>.  
</BODY>  
</HTML>

  

  

## Additional Information

Please note that this property affects **ALL outbound requests.**   
We therefore advise that you **test this thoroughly** in your Sub-Production before you migrate to production
