---
title: "How to Configure the \"SCCM 2016 Computer Identity\" Transform Map to Coalesce on Serial Number Instead of sys_id?"
aliases:
  - KB0792390
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0792390
kb_number: KB0792390
last_modified: 2025-04-08
---

## Issue

How to Configure the "SCCM 2016 Computer Identity" Transform Map to Coalesce on Serial Number Instead of sys\_id?

This is applicable if your SCCM environment has unique serial numbers and you want to coalesce on serial number.

This involves data source "SCCM 2016 Computer Identity" and transform map "SCCM 2016 Computer Identity".

## Resolution

By default in the transform map "SCCM 2016 Computer Identity", coalesce is on "sys\_id" which is determined from a source script.  
  
In this scenario the SCCM serial number is unique which currently has this field mapping and by default it is not a coalesce value:  
  
u\_biosserialnumber --> serial\_number

What needs to be done:

(1) If you want to change the coalesce to serial number, please ensure that the target table doesn't have any duplicate serial number records.

(2) Change the field mapping in the "SCCM 2016 Computer Identity" field maps to make the u\_biosserialnumber --> serial\_number mapping coalesce = true.

(3) Remove the \[sys\_id\] field mapping to prevent the script from running during transforms as it can cause issues with finding matching records.  
  
Removing the sys\_id mapping will cut down the processing time. The sys\_id script also does other processing like checking Identification and Reconciliation Engine (IRE) rules for identification as you won't need it anymore since serial number is considered a unique identifier in this case. Also, test for any speed implications as you are changing the identification method just to make sure there are no impacts there.
