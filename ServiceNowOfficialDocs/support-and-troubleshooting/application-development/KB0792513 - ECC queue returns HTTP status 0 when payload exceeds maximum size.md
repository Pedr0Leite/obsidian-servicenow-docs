---
title: "ECC queue returns HTTP status 0 when payload exceeds maximum size"
aliases:
  - KB0792513
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0792513
kb_number: KB0792513
last_modified: 2026-06-09
---

## ECC queue returns HTTP status 0 when payload exceeds maximum size

  

### Issue

Customer has a query to pull data from 3rd party through REST (Mid Server involved).

Query  has to pull huge data (nearly 22000+ records) from their third party but couldn't fetch any records. The http status is returning as "0".

The same is working fine when tried from SoapUI/Postman.

In the Node logs below is the data that is seen related to the transaction :

worker.6 worker.6 txid=865c132\*\*\*\*\*\* OUTBOUND\_HTTP: protocol= response\_status=-1 response\_time=26520 request\_length=0 response\_length=0 app\_scope=global

### Release

NA

### Cause

\->Below Error is seen in ECC Queue :(Input)

ERROR:  
\----------  
  
<error>Payload size of 47603255 bytes exceeded maximum of 20000000 bytes.  
Contents of the original payload were moved to C:ServiceNowMsiDevMidagentworkmonitorsECCSenderoutput\_oversizeecc\_queue.d8661b37db06c010360bc082ba96190a.xml on the MID server.  
Maximum payload size can be set with mid config parameter: mid.eccq.max\_payload\_size</error>

### Resolution

\->mid.eccq.max\_payload\_size" property is added to the "Configuration Parameters" tab (not the "Properties" tab) and restarted MidServer. Then the error did not reappear after retesting.

\->Post fixing the issue with "mid.eccq.max\_payload\_size" property,  started seeing issue with "com.glide.attachment.max\_get\_size" property.  
  
"Payload attachment exceeds the limit of 5242880 bytes set by system property com.glide.attachment.max\_get\_size."  
  
In order to fix this error,  added another property "com.glide.attachment.max\_get\_size" and did set the value of it to a higher value.
