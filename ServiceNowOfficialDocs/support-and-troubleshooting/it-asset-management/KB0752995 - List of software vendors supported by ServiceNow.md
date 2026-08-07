---
title: "List of software vendors supported by ServiceNow"
aliases:
  - KB0752995
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0752995
kb_number: KB0752995
last_modified: 2024-04-07
---

## List of software vendors supported by ServiceNow

  

### Issue

# Overview

This article demonstrates How to list all the supported vendors in ServiceNow-Software Asset Management. 

# AssetUtils.getVendors

The logic of listing the vendors is determined in the following script includes:

-   Log into the instance
-   Navigate >>  System Definition >> Script Includes 
-   ProcSourceRequestManager.findVendors() -> ProcSourceRequestManager.\_getVendors() -> AssetUtils.getVendors() 

Script Include - ProcSourceRequestManager   
https://<instancename>.service-now.com/nav\_to.do?uri=sys\_script\_include.do?sys\_id=b520d0bcff0302003706ffffffffff5c 

  
Script Include - AssetUtils   
https://<instancename>.service-now.com/nav\_to.do?uri=sys\_script\_include.do?sys\_id=3596241c475520003ecf706eecde2726 

The method in the script include takes model\_id as the parameter. Gets the list of active pc\_vendor\_cat\_item and sc\_cat\_item for the given model where the vendor field is not empty and vendor attribute on the core company is true.

Vendor information is coming from **"pc\_vendor\_cat\_item"** table or **'sc\_cat\_item'** table. 

# Additional Information

The publisher packs contain the list of publishers and those are supported vendors, the publishers which are shipped as part of the Content are for which we have Content data like Products, Packages, Rules etc.

Now whether ServiceNow supports that publisher is a much broader term which needs clarity as to what "support" constitutes. 

The samp\_sw\_publisher.list it should display all publishers in the content. the samp\_sw\_publisher table contains all the relevant publishers.
