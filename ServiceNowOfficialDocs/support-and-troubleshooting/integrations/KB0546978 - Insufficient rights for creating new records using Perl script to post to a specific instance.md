---
title: "\"Insufficient rights for creating new records\" using Perl script to post to a specific instance"
aliases:
  - KB0546978
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0546978
kb_number: KB0546978
last_modified: 2024-08-15
---

## "Insufficient rights for creating new records" using Perl script to post to a specific instance

  

### Issue

#### Insufficient rights for creating new records" using Perl script to post to a SOAP request to a specific instance

When posting a request using a Perl script, the client received the following error  
  
_Insufficient rights for creating new records: com.glide.processors.soap.SOAPProcessingException: Insufficient rights for creating new records:_  
  
This error occurred only in one environment where the same script worked on all other instances. 

#### Symptoms:

When posting a SOAP request using a Perl script, there was an error returned consistently stating that the UserID being used in the script had " Insufficient rights for creating new records." Therefore, a new Change Request record was not being created in the instance. This very same user when logging in to the instance is able to create the Change Request record, but not from the script. This same script works on other environments like QA, Dev, and Test but does not work on Prod.  
  
Error seen in the logs:

insufficient rights for creating new records: com.glide.processors.soap.SOAPProcessingException: Insufficient rights for creating new records: com.glide.processors.soap.command.Insert.process(Insert.java:42)   
com.glide.processors.soap.SOAPProcessorThread.doCommand(SOAPProcessorThread.java:288)   
com.glide.processors.soap.SOAPProcessorThread.doCommand(SOAPProcessorThread.java:277)   
com.glide.processors.soap.SOAPProcessorThread.processStandardWebService(SOAPProcessorThread.java:212)   
com.glide.processors.soap.SOAPProcessorThread.processBody(SOAPProcessorThread.java:192)   
com.glide.processors.soap.SOAPProcessorThread.processRequest(SOAPProcessorThread.java:159)   
com.glide.processors.soap.SOAPProcessorThread.run0(SOAPProcessorThread.java:123)   
com.glide.util.ParentedThread.run(ParentedThread.java:51)  
  

### Cause

The issue appeared to be caused by the UserID not having the right ACL (Access Control List) permissions to create a record using the Change Request table. The real cause, however, was that the Change Request page was set as a public page and was bypassing the ACL logic. 

### Resolution

When the issue was debugged, we discovered that the Change Request page was set as a public page. Checking System Definition > Public Pages in the system confirmed that the Change Request page was set as a public page. The page was bypassing the ACL logic and trying to insert the payload as a guest user, causing the error. After the page was set as non-public, it started to work as expected. 

1.  Navigate to **System Definition > Public Pages**.
2.  Search for the page for Change Request and remove it from the list to make it a non-public page.

This is how it was debugged. In looking at the Local Hosts logs the line showed

" 01/14/15 11:32:41 (333) SYSTEM Bypassing ACL checks for a public page: /change\_request.do " .

Hence it was bypassing the ACL logic and trying to insert the data as a 'guest' user.

Trace / Log section:

01/14/15 11:32:35 (473) 00D307263CA53100AE2FA56CEC8D4FC4 /xmlstats.do -- transaction time: 0:00:00.037, waited: 0:00:00.000, source: 127.0.0.1 

01/14/15 11:32:41 (327) SYSTEM Inactivity time changed from 1800 seconds to 28800 seconds  
01/14/15 11:32:41 (327) SYSTEM Session created: 2DD343663CA53100AE2FA56CEC8D4F16, timeout after 480 minutes of inactivity  
01/14/15 11:32:41 (333) SYSTEM HTTP authorization validated user 'guest'  
01/14/15 11:32:41 (333) SYSTEM Bypassing ACL checks for a public page: /change\_request.do  
01/14/15 11:32:41 (334) SYSTEM \*\*\* Start #529, path: /change\_request.do, user: guest  
01/14/15 11:32:41 (334) SYSTEM SOAPProcessor: initial session inactivity timeout is 60 seconds  
01/14/15 11:32:41 (334) SYSTEM SOAPProcessor: initial soap request timeout is 15 seconds  
01/14/15 11:32:41 (334) SYSTEM SOAPProcessor: session inactivity timeout changed to 60 seconds  
01/14/15 11:32:41 (337) SYSTEM SOAPProcessor: <?xml version="1.0" encoding="UTF-8"?><soap:Envelope xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/" xmlns:soapenc="http://schemas.xmlsoap.org/soap/encoding/" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" soap:encodingStyle="http://schemas.xmlsoap.org/soap/encoding/"><soap:Body><insert xmlns="http://www.service-now.com/"><short\_description xsi:type="xsd:string">Remove legacy nagios configuration</short\_description><category xsi:type="xsd:string">MONITORING</category></insert></soap:Body></soap:Envelope>  
01/14/15 11:32:41 (339) SYSTEM Created SOAPProcessorThreade1d343663ca53100ae2fa56cec8d4f17  
01/14/15 11:32:41 (363) SYSTEM Insufficient rights for creating new records: com.glide.processors.soap.SOAPProcessingException: Insufficient rights for creating new records: com.glide.processors.soap.command.Insert.process(Insert.java:42)
