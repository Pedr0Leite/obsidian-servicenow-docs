---
title: "Outbound SOAP request times out at 175 seconds when going through a MID Server"
aliases:
  - KB0547347
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0547347
kb_number: KB0547347
last_modified: 2026-07-02
---

## Outbound SOAP request times out at 175 seconds when going through a MID Server

  

### Issue

Outbound SOAP requests routed through a MID Server time out at 175 seconds with a socket timeout error, even after applying all system properties from the [Long-Running SOAP Request Support](https://docs.servicenow.com/csh?topicname=LongRunningSOAPRequestProps.html&version=latest) documentation to the sys\_properties table.

The problem occurs when running a test on, for example, an outbound SOAP Action > MyOutBound >GetSomething. This SOAP message function uses the Mid Server to get the data. After 60 seconds it moves to the ECC queue (this is fine), but after 175 seconds it receives a socket timeout. The request is expected to run for approximately 30 minutes. No matter how high the property values are set using the product documentation, the socket timeout at 175 seconds persists.

### Symptoms

No matter how high the values were changed from the list (as given in the product documentation article, [Long-running SOAP Request Support](https://docs.servicenow.com/csh?topicname=LongRunningSOAPRequestProps.html&version=latest "Long-running SOAP Request Support")), the SOAP request always received a socket timeout at 175 seconds.

### Release

### Cause

The timeout occurs at the MID Server level. Because the SOAP request routes through the MID Server, its causing the request to time out at 175 seconds.

### Resolution

The `glide.http.timeout` parameter must be added directly to the config.xml file on the MID Server host. This is a protected setting that cannot be configured from the MID Server Properties module in ServiceNow — it requires direct file access on the MID Server host.

To resolve the timeout, follow these steps:

1.  Log in to the MID Server host.
2.  Navigate to the `/agent` directory within the MID Server installation directory and open the config.xml file.
3.  Locate the Less Common Optional Parameters section within the file.
4.  Add the `glide.http.timeout` parameter block to that section. Set the value in milliseconds — the following example sets the timeout to 1,800,000 milliseconds (30 minutes):

<!-- \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*
 LESS COMMON OPTIONAL Parameters
\* There are other parameters available for more specialized needs. These optional
\* parameters are documented in the ServiceNow product documentation at the URL below:
\*
\* [https://docs.servicenow.com/csh?topicname=c\_MIDServerConfiguration.html&version=latest](https://docs.servicenow.com/csh?topicname=c_MIDServerConfiguration.html&version=latest)
\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\* -->
<parameter name="glide.http.timeout" value="1800000" />

1.  5\. Save the config.xml file and restart the MID Server for the change to take effect.

### Related Links

Long-Running SOAP Request Support documentation: [https://docs.servicenow.com/csh?topicname=LongRunningSOAPRequestProps.html&version=latest](https://docs.servicenow.com/csh?topicname=LongRunningSOAPRequestProps.html&version=latest%29)  
MID Server configuration parameters reference: [https://docs.servicenow.com/csh?topicname=c\_MIDServerConfiguration.html&version=latest](https://docs.servicenow.com/csh?topicname=c_MIDServerConfiguration.html&version=latest%29)

How to configure default response timeout for outbound async REST and SOAP messages: [https://support.servicenow.com/kb?id=kb\_article\_view&sysparm\_article=KB1430129](https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB1430129)
