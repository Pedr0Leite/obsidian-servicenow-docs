---
title: "How to access CI Data in  SNMP classify/identify probe"
aliases:
  - KB0721214
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0721214
kb_number: KB0721214
last_modified: 2025-04-08
---

## Issue

There may a need to access ciData through SNMP Classify/Identity probe.

The SNMP - Classify probe uses the following as part of its parameters: 

<parameter name="cidata" value="<CIData><data><fld name="ip\_address">10.xxx.xxx.xx</fld><fld name="dns\_name">a-1234.pncint.net</fld><fld name="name">a-1234-w01a</fld><fld name="dns\_domain">pncint.net</fld></data></CIData>"/>

## Resolution

The parameter values can be fetched by using the function call: this.getParameter

this.getParameter('\[PARAMETER NAME\]')   
Ex. this.getParameter('port') 

  
For reference, this can be seen that it is called multiple times in the Sensor records like "SNMP - Classify".   
  
Now, for the ciData parameter, because this contains an array of data, there is a special snippet of code that can be used to reference those values in particular.   
Observe the below "SNMP - Classify probe":

\---------------------------------------------------------------------------------------   
this.ciData = new CIData();   
this.ciData.fromXML(this.getParameter('cidata'));   
this.ci\_data = this.ciData.getData();   
\--------------------------------------------------------------------------------------- 

From here, if there is need to access or even create new values in this "cidata" parameter, this can do so by referencing the more specific parameter name like below. 

this.ci\_data\['PARAMETER\_NAME\]')   
Ex. this.ci\_data\['dns\_name'\] 

Example:

To set the "fqdn" parameter in this ciData from the Classify Sensor (which will then get passed along and processed to the Identity probe/sensor), this can be done like below. 

this.ci\_data\['fqdn'\] = this.ci\_data\['dns\_name'\]; 

  
From here, "fqdn" can be used in the ciData parameter in the Identity ecc\_queue records and once this ciData gets processed by the Identity Sensor process, this will then update this value on the appropriate CI record.
