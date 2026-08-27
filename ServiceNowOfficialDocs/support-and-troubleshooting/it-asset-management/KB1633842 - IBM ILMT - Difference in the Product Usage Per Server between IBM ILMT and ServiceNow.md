---
title: "IBM ILMT - Difference in the Product Usage Per Server between IBM ILMT and ServiceNow"
aliases:
  - KB1633842
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB1633842
kb_number: KB1633842
last_modified: 2024-02-23
---

## IBM ILMT - Difference in the Product Usage Per Server between IBM ILMT and ServiceNow

  

### Summary

# Integrating with the IBM License Metric Tool (ILMT) or BigFix Inventory using v2 APIs

### Instructions

Scheduled Job 'SAM - Import IBM Usage Data From ILMT V2':-

https://<instance-name>.service-now.com/sysauto\_script.do?sys\_id=3c705d53f40e2150f8775dfabc9adaba

  

Script Includes Involved:-

SamILMTV2ImportJob:-

https://<instance-name>.service-now.com/sys\_script\_include.do?sys\_id=ea3a00de44f26110f877ce8937c7c83c

SamILMTV2APIHandler:-

https://<instance-name>.service-now.com/sys\_script\_include.do?sys\_id=1faacc9e44f26110f877ce8937c7c8f5

\=========================================

  

Data Insertion Flow:-

First we will fetch the license\_usage for the supported metrics (PVU, RVU, VPC) for the last 90 days.

Then we will fetch the license\_usage\_per\_server for the above fetched metrics.

\=========================================

  

Filters Applied:-

  

Filter 1:- https://<instance-name>.service-now.com/sys\_alias.do?sys\_id=ce368f0f0b2003006586650d37673a55

By default, the results are returned for the computer group of the user whose token is used for authentication and cover the period for which data is aggregated in this group.

[https://www.ibm.com/docs/en/license-metric-tool?topic=v2-retrieval-license-metric-utilization#license\_usage](https://www.ibm.com/docs/en/license-metric-tool?topic=v2-retrieval-license-metric-utilization#license_usage)

  

Filter 2:- The script include 'SamILMTV2APIHandler' adds the below 'metric\_code\_name' to the URL to fetch only supported metrics.

const supportedMetricCodenames = \[

'PVU\_FULL\_CAP',

'PVU\_SUB\_CAP',

'RVU\_FULL\_CAP',

'RVU\_SUB\_CAP',

'VIRTUAL\_PROCESSOR\_CORE',

\];

[https://www.ibm.com/docs/en/license-metric-tool?topic=v2-metric-ids-code-names#reference\_vys\_ysj\_b1b](https://www.ibm.com/docs/en/license-metric-tool?topic=v2-metric-ids-code-names#reference_vys_ysj_b1b)

  

Filter 3:- The product\_id, metric\_id, and bundle\_id received from the license\_usage API call will be used to query for license\_usage\_per\_server records in SamILMTV2APIHandler script include.

[https://www.ibm.com/docs/en/license-metric-tool?topic=v2-retrieval-license-usage-information-per-server](https://www.ibm.com/docs/en/license-metric-tool?topic=v2-retrieval-license-usage-information-per-server)

\=========================================

  

Note:-

\*\*\*\*with the above filters applied, the data in ServiceNow should match closely with the data from IBM ILMT\*\*\*

  
  

Sample API and Response in your configuration:-

  

license\_usage API:-

  

https://<IP\_ADDRESS>:<PORT>/api/sam/v2/license\_usage?token=XXXXX&columns\[\]=product\_name...&criteria={"or":\[\["metric\_code\_name","=","PVU\_FULL\_CAP"\],\["metric\_code\_name","=","PVU\_SUB\_CAP"\],\["metric\_code\_name","=","RVU\_FULL\_CAP"\],\["metric\_code\_name","=","RVU\_SUB\_CAP"\],\["metric\_code\_name","=","VIRTUAL\_PROCESSOR\_CORE"\]\]}&startdate=2023-11-25&enddate=2024-02-23&limit=5000

\-----------------------------------------------------------

  

Response:-

  

{

"total": 20,

"rows": \[

{"product\_id": 2996,"product\_name": "IBM MQ Advanced Message Security","metric\_id": 3,"metric\_code\_name": "PVU\_FULL\_CAP",...},

{"product\_id": 4530,"product\_name": "IBM InfoSphere Change Data Capture","metric\_id": 3,"metric\_code\_name": "PVU\_FULL\_CAP",...},

{"product\_id": 7256,"product\_name": "IBM Control Center Monitor for Non-Prod Environment","metric\_id": 3,"metric\_code\_name": "PVU\_FULL\_CAP",...},

{"product\_id": 8451,"product\_name": "IBM Data Replication for Non-Production Environments","metric\_id": 3,"metric\_code\_name": "PVU\_FULL\_CAP",...},

{"product\_id": 9991,"product\_name": "IBM MQ","metric\_id": 3,"metric\_code\_name": "PVU\_FULL\_CAP",...},

{"product\_id": 10472,"product\_name": "IBM WebSphere Application Server - Express","metric\_id": 3,"metric\_code\_name": "PVU\_FULL\_CAP",...},

{"product\_id": 11511,"product\_name": "IBM MQ Advanced","metric\_id": 3,"metric\_code\_name": "PVU\_FULL\_CAP",...},

{"product\_id": 12399,"product\_name": "IBM Control Center Monitor","metric\_id": 3,"metric\_code\_name": "PVU\_FULL\_CAP",...},

{"product\_id": 13288,"product\_name": "IBM MQ Managed File Transfer Service","metric\_id": 3,"metric\_code\_name": "PVU\_FULL\_CAP",...},

{"product\_id": 2996,"product\_name": "IBM MQ Advanced Message Security","metric\_id": 4,"metric\_code\_name": "PVU\_SUB\_CAP",...},

{"product\_id": 4530,"product\_name": "IBM InfoSphere Change Data Capture","metric\_id": 4,"metric\_code\_name": "PVU\_SUB\_CAP",...},

{"product\_id": 7256,"product\_name": "IBM Control Center Monitor for Non-Prod Environment","metric\_id": 4,"metric\_code\_name": "PVU\_SUB\_CAP",...},

{"product\_id": 8451,"product\_name": "IBM Data Replication for Non-Production Environments","metric\_id": 4,"metric\_code\_name": "PVU\_SUB\_CAP",...},

{"product\_id": 9991,"product\_name": "IBM MQ","metric\_id": 4,"metric\_code\_name": "PVU\_SUB\_CAP",...},

{"product\_id": 10472,"product\_name": "IBM WebSphere Application Server - Express","metric\_id": 4,"metric\_code\_name": "PVU\_SUB\_CAP",...},

{"product\_id": 11511,"product\_name": "IBM MQ Advanced","metric\_id": 4,"metric\_code\_name": "PVU\_SUB\_CAP",...},

{"product\_id": 12399,"product\_name": "IBM Control Center Monitor","metric\_id": 4,"metric\_code\_name": "PVU\_SUB\_CAP",...},

{"product\_id": 13288,"product\_name": "IBM MQ Managed File Transfer Service","metric\_id": 4,"metric\_code\_name": "PVU\_SUB\_CAP",...},

{"product\_id": 13632,"product\_name": "IBM Tivoli Monitoring","metric\_id": 7,"metric\_code\_name": "RVU\_FULL\_CAP",...},

{"product\_id": 13632,"product\_name": "IBM Tivoli Monitoring","metric\_id": 8,"metric\_code\_name": "RVU\_SUB\_CAP",...}

\]

}

\-----------------------------------------------------------

  
  

license\_usage\_per\_server API:-

  

https://<IP\_ADDRESS>:<PORT>/api/sam/v2/license\_usage\_per\_server?token=XXXXX&date=2024-02-23&columns\[\]=server.active\_computers...&criteria={"and":\[\["product\_id","=","8451"\],\["metric\_id","=","3"\],\["bundle\_id","=","0"\]\]}&limit=5000

\-----------------------------------------------------------

  

Response:-

  

{

"total":1,

"rows":\[

{"product\_name":"IBM Data Replication for Non-Production Environments","product\_id":8451,"metric\_code\_name":"PVU\_FULL\_CAP","metric\_id":3,"hwm\_quantity":240,"bundle\_id":0,"server":{"id":493,"name":"TLM\_VM\_XXXX","type":1,"hardware\_vendor":"-","hardware\_model":"-","total\_processors":1,"hardware\_serial\_number":"TLM\_VM\_XXXX","cores":2,"pvu\_per\_core":120,"active\_computers":1}}

\]

}

\=========================================

  
  

Table Transform Maps:-

https://<instance-name>.service-now.com/sys\_transform\_map\_list.do?sysparm\_query=name%3DTransform%20ILMT%20Product%20Usage%5EORname%3DTransform%20ILMT%20Device%20Usage&sysparm\_view=

  

For Product Usages and Device Usages, we process multiple rows in the staging table into a single row in product usage table because full cap and sub cap values for a product is returned as separate rows by the ILMT API but SN stores the data in the same row as different columns.

  

ILMT Product Usages:-

https://<instance-name>.service-now.com/ilmt\_v2\_product\_usage\_list.do?sysparm\_query=&sysparm\_first\_row=1&sysparm\_view=

  

ILMT Product Usage Per Servers:-

https://<instance-name>.service-now.com/ilmt\_v2\_usage\_per\_server\_list.do?sysparm\_query=&sysparm\_first\_row=1&sysparm\_view=

  

ILMT Discovered Computers:-

https://<instance-name>.service-now.com/ilmt\_discovered\_computer\_list.do

  

We create a new computer record only if there exists no Computer with matching 'server\_hw\_serial\_number' fetched from the license\_usage\_per\_server API .

\=========================================

### Related Links

[https://docs.servicenow.com/csh?topicname=integrating-ilmt-bigfix-v2-apis.html&version=latest](https://docs.servicenow.com/csh?topicname=integrating-ilmt-bigfix-v2-apis.html&version=latest)
