---
title: "How to reference form variables in a HTTP POST message"
aliases:
  - KB0549832
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0549832
kb_number: KB0549832
last_modified: 2024-04-07
---

## Issue

How to reference form variables in a HTTP POST message 

  

Problem

* * *

The article addresses what function should be used to obtain values sent from a third-party integration that sends information through a HTTP POST request.  

  

  
Resolution

* * *

Within the ServiceNow UI page, use RP.getParameterValue('<post\_variable>').

  

For example, the UI page would contain:

<?xml version="1.0" encoding="utf-8" ?>

<j:jelly trim="false" xmlns:j="jelly:core" xmlns:g="glide" xmlns:j2="null" xmlns:g2="null">  
  
<g:evaluate>

var \_var1 = RP.getParameterValue("variable1"); //variable1 is one of the variables in the POST request to the instance

gs.log(\_var1);

</g:evaluate>

</j:jelly>
