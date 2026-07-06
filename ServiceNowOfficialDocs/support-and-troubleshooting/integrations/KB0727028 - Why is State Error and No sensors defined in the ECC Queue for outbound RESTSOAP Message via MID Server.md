---
title: "Why is State \"Error\" and \"No sensors defined\" in the ECC Queue for outbound REST/SOAP Message via MID Server?"
aliases:
  - KB0727028
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0727028
kb_number: KB0727028
last_modified: 2025-08-19
---

## Why is State "Error" and "No sensors defined" in the ECC Queue for outbound REST/SOAP Message via MID Server?

  

### Issue

When running Outbound REST or SOAP Message integrations via a MID Server, the ECC Queue input may be set as:

-   State = Error
-   Error String = No sensors defined

This applies to the scripting API and also applies to the messages created by the 'Test' related link on REST or SOAP Message method definition forms.

Note: This also potentially applies to other integrations probes using the MID Server. If this error is seen from Discovery, then please refer to [KB0547844](https://support.servicenow.com/kb_view.do?sysparm_article=KB0547844 "KB0547844"), [KB0717362](https://support.servicenow.com/kb_view.do?sysparm_article=KB0717362 "KB0717362") and others.

### Cause

This error really means "No Discovery Sensor Defined". Discovery was why the MID Server was designed, and at that time the only sensor business rule was "Discovery - Sensors" and this error comes from that. All other MID Server probes for SystemCommand etc. had ECC Queue output payload parameter skip\_sensors=true used so that "Discovery - Sensors" was skipped.

All subsequent new applications and features that leverage Discovery's MID Server should be setting the ECC Parameter skip\_sensors=true as well, so that Discovery - Sensors doesn't attempt to process the result from the probe. Most do. Some don't.

### Resolution

When scripting SOAPMessageV2 or RESTMessageV2, you should always set the skip\_sensor=true parameter, even if you have created your own ecc\_queue business rule sensor for the message.

This is done with the setEccParamater() method of the APIs. See the docs:

-   [RESTMessageV2 - setEccParameter(String name, String value)](https://docs.servicenow.com/search?q=RESTMessageV2+setEccParameter "RESTMessageV2 - setEccParameter(String name, String value)")
-   [SOAPMessageV2 - setEccParameter(String name, String value)](https://docs.servicenow.com/search?q=SOAPMessageV2+setEccParameter "SOAPMessageV2 - setEccParameter(String name, String value)")

For example:

var sm = new sn\_ws.RESTMessageV2("Yahoo Finance", "get");
sm.setBasicAuth("admin","admin");
sm.setStringParameter("symbol", "NOW");
sm.setStringParameterNoEscape("xml\_data","<data>test</data>");
sm.setMIDServer('mid\_server\_name');
**sm.setEccParameter("skip\_sensor","true"); // prevent Discovery sensors running for the ECC input**
sm.setEccCorrelator("rest.yahoo"); // unique identifier for this message, used by the custom sensor business rule for matching the ecc\_queue input
sm.executeAsync(); // send the ECC queue output and end this script. The Sensor business rule will carry on once the response arrives back from the MID Server

Please note the **correct use of executeAsync**() when a MID Server is involved in that example. 

After 'solving' this by adding the skip\_sensor attribute, **you may now find all your input records are stuck in Ready state**. That's probably correct, if you don't have any kind of Sensor to set it as processed. 

For more on those 2 points, see:

-   [KB0694711 Outbound REST Web Services RESTMessageV2 and SOAPMessageV2 execute() vs executeAsync() Best Practices](https://support.servicenow.com/kb_view.do?sysparm_article=KB0694711 "KB0694711 Outbound REST Web Services RESTMessageV2 and SOAPMessageV2 execute() vs executeAsync() Best Practices")
-   [KB0716391 Best practices for RESTMessageV2 and SOAPMessageV2](https://support.servicenow.com/kb_view.do?sysparm_article=KB0716391 "KB0716391 Best practices for RESTMessageV2 and SOAPMessageV2")
-   [PRB1305586 RESTMessageV2/SOAPMessageV2 APIs allow running via MID Servers Synchronously, without a Sensor ECC business rule, causing blocked instance threads while sleeping, and Scheduler overload](https://support.servicenow.com/kb_view.do?sysparm_article=KB0714559 "PRB1305586 RESTMessageV2/SOAPMessageV2 APIs allow running via MID Servers Synchronously, without a Sensor ECC business rule, causing blocked instance threads while sleeping, and Scheduler overload")

### Related Links

This issue is related to the following confirmed problem ticket:  
[KB0727122 Discovery - Sensors business rule will run for non-Discovery ecc\_queue inputs](https://support.servicenow.com/kb_view.do?sysparm_article=KB0727122 "KB0727122 Discovery - Sensors business rule will run for non-Discovery ecc_queue inputs")
