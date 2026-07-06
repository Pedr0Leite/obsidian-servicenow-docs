---
title: "Troubleshoot MID Server connectivity with the instance"
aliases:
  - KB0780900
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0780900
kb_number: KB0780900
last_modified: 2026-01-16
---

## Troubleshoot MID Server connectivity with the instance

  

### Summary

Troubleshoot a MID Server that shows as down when the following conditions are met:

-   MID Server service is up and running.
-   You can connect to the instance from the MID Server host using a browser.
-   You can ping the instance from the MID Server host.
-   No Windows firewall is configured.
-   A proxy may be configured on the MID Server.

### Release

All supported releases

### Instructions

### **Step 1. Check the MID Server agent log**

Check the MID Server agent log for the following errors:

10/01/19 09:07:23 (175) StartupSequencer WARNING \* WARNING org.apache.commons.httpclient.ConnectTimeoutException: The host did not accept the connection within timeout of 10000 ms when posting to [https://<instance>.service-now.com/InstanceInfo.do?SOAP](https://\<instance\>.service-now.com/InstanceInfo.do?SOAP)  
10/01/19 09:07:23 (175) StartupSequencer SEVERE ERROR SOAP Request: <SOAP-ENV:Envelope xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:SOAP-ENC="http://schemas.xmlsoap.org/soap/encoding/" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:tns="http://www.service-now.com/GetMIDInfo" xmlns:m="http://www.service-now.com" xmlns:SOAP-ENV="http://schemas.xmlsoap.org/soap/envelope/" SOAP-ENV:encodingStyle="http://schemas.xmlsoap.org/soap/encoding/"><SOAP-ENV:Body><m:execute></m:execute></SOAP-ENV:Body></SOAP-ENV:Envelope>  
10/01/19 09:07:23 (175) StartupSequencer SEVERE ERROR SOAP Response: Status code=0, Response body=null  
10/01/19 09:07:23 (175) StartupSequencer SEVERE ERROR Problem invoking InstanceInfo on [https://<instance>.service-now.com/:](https://\<instance\>.service-now.com/:) Please check that the InstanceInfo page exists in the sys\_public table and active="true".  
10/01/19 09:07:23 (175) StartupSequencer SEVERE ERROR org.apache.commons.httpclient.ConnectTimeoutException: The host did not accept the connection within timeout of 10000 ms when posting to [https://<instance>.service-now.com/InstanceInfo.do?SOAP](https://\<instance\>.service-now.com/InstanceInfo.do?SOAP)  
(Network Configuration issue) Please check that the MID server can ping the instance: [https://<instance>.service-now.com/](https://\<instance\>.service-now.com/)  
You may also need to configure the network that the MID server uses to allow traffic over TCP port 443.  
10/01/19 09:07:23 (175) StartupSequencer SEVERE ERROR \* test failure  
java.lang.IllegalStateException: Unable to connect to instance.  
at com.service\_now.mid.services.StartupSequencer.runTests(StartupSequencer.java:386)  
at com.service\_now.mid.services.StartupSequencer$Starter.run(StartupSequencer.java:349)

### Step 2. Check SOAP calls

During the startup sequence, the MID Server checks connectivity with the instance by invoking a SOAP call to the following URL (replace <instance> with your instance name):

https://<instance>.service-now.com/InstanceInfo.do?SOAP

When you go to this URL, you should receive the following response: 

<SOAP-ENV:Envelope xmlns:SOAP-ENV="http://schemas.xmlsoap.org/soap/envelope/"> <SOAP-ENV:Header/> <SOAP-ENV:Body> <SOAP-ENV:Fault> <faultcode>SOAP-ENV:Server</faultcode> <faultstring> Error completing SOAP request - Only HTTP POST supported </faultstring> <detail>Error completing SOAP request</detail> </SOAP-ENV:Fault> </SOAP-ENV:Body> </SOAP-ENV:Envelope> 

This is the expected response because InstanceInfo.do?SOAP does not accept GET requests. To view this message in the browser, turn off friendly message display.

This browser test is not comprehensive. Some firewalls or proxy servers allow traffic initiated from a browser but block other traffic by filtering the user-agent or other HTTP header fields. In this case, testing the URL in a browser works but the MID Server still cannot connect. To perform a more thorough test, use a SOAP client tool such as Postman to perform a SOAP POST call to the instance with the following information: 

HTTP URL:  https://<instance>.service-now.com/InstanceInfo.do?SOAP

HTTP Headers:

Content-Type: text/xml;charset=UTF-8

user-agent: internal\_soap\_client

SOAPAction: Get

HTTP Body:

<SOAP-ENV:Envelope xmlns:xsd="[http://www.w3.org/2001/XMLSchema](http://www.w3.org/2001/XMLSchema)" xmlns:SOAP-ENC="[http://schemas.xmlsoap.org/soap/encoding/](http://schemas.xmlsoap.org/soap/encoding/)" xmlns:xsi="[http://www.w3.org/2001/XMLSchema-instance](http://www.w3.org/2001/XMLSchema-instance)" xmlns:tns="[http://www.service-now.com/GetMIDInfo](http://www.service-now.com/GetMIDInfo)" xmlns:m="[http://www.service-now.com](http://www.service-now.com)" xmlns:SOAP-ENV="[http://schemas.xmlsoap.org/soap/envelope/](http://schemas.xmlsoap.org/soap/envelope/)" SOAP-ENV:encodingStyle="[http://schemas.xmlsoap.org/soap/encoding/](http://schemas.xmlsoap.org/soap/encoding/)"><SOAP-ENV:Body><m:execute><table xsi:type="xsd:string">ecc\_agent\_log</table></m:execute></SOAP-ENV:Body></SOAP-ENV:Envelope>

![Example of HTTP headers](/sys_attachment.do?sys_id=9a4c3c2c93aef214c2513f986cba10b2)

![Example of HTTP body](/sys_attachment.do?sys_id=d24c3c2c93aef214c2513f986cba10ad)

You should receive a response with tags containing information from your instance:

<?xml version="1.0" encoding="UTF-8"?>
<SOAP-ENV:Envelope xmlns:SOAP-ENV="http://schemas.xmlsoap.org/soap/envelope/" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
  <SOAP-ENV:Body>
    <executeResponse xmlns="http://www.service-now.com">
      <result>
        <install\_name>XXXX</install\_name>
        <instance\_name>myinstance</instance\_name>
        <instance\_id>XXXX</instance\_id>
        <build\_date>XXXX</build\_date>
        <build\_tag>XXXX</build\_tag>
        <system\_id>XXXX</system\_id>
        <node\_id>XXXX</node\_id>
        <instance\_ip>XXXX</instance\_ip>
        <mid\_buildstamp>mXXXX</mid\_buildstamp>
        <mid\_version>XXXX</mid\_version>
      </result>
    </executeResponse>
  </SOAP-ENV:Body>
</SOAP-ENV:Envelope>

If your MID Server runs on Linux, you can use cURL instead: 

curl --header 'Content-Type: text/xml;charset=UTF-8' --header 'SOAPAction: Get' --header 'user-agent: internal\_soap\_client' --data '<SOAP-ENV:Envelope xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:SOAP-ENC="http://schemas.xmlsoap.org/soap/encoding/" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:tns="http://www.service-now.com/GetMIDInfo" xmlns:m="http://www.service-now.com" xmlns:SOAP-ENV="http://schemas.xmlsoap.org/soap/envelope/" SOAP-ENV:encodingStyle="http://schemas.xmlsoap.org/soap/encoding/"><SOAP-ENV:Body><m:execute><table xsi:type="xsd:string">ecc\_agent\_log</table></m:execute></SOAP-ENV:Body></SOAP-ENV:Envelope>' https://myinstance.service-now.com/InstanceInfo.do?SOAP | xmllint --format -

### **Step 3. Check MID Server proxy settings**

Check the MID Server proxy settings in the **/agent/config.xml** file:

<parameter name="mid.proxy.use\_proxy" value="true"/>  
<parameter name="mid.proxy.host" value="proxy.company.net"/>  
<parameter name="mid.proxy.port" value="803"/>

Configure your browser with the same proxy settings and test connectivity using the URL from Step 2:

https://<instance>.service-now.com/InstanceInfo.do?SOAP

**Step 4. Check the InstanceInfo Scripted Web Service** 

Check the **InstanceInfo** Scripted Web Service for any customizations:

https://<instance>.service-now.com/nav\_to.do?uri=sys\_web\_service.do?sys\_id=0cbfe98d83301000dada83ec37d929c8

### **Step 5. SSL troubleshooting**

To find the IP address of the instance, see [Finding the IP address information for your instance](https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0538621).

Alternatively, you can use the following commands:

ping instance\_name

dig +noall +answer instance\_name

If you suspect an SSL negotiation issue, enable SSL debugging:

1.  On the MID Server, open the **../agent/conf/wrapper-override.conf** file.
2.  Add the following line at the bottom of the file: wrapper.java.additional.3=-Djavax.net.debug=ssl
3.  Restart the MID Server service.
4.  Review the SSL debugging information in the wrapper.log file.

**Important**: Remove this line and restart the MID Server when you complete your investigation. 

Look for the following information in the log:

-   trustStore is: <Install>\\agent\\jre\\lib\\security\\cacerts
-   TLS protocol version (TLSv1.2)
-   Cipher Suites in ClientHello
-   Cipher Suites in ServerHello

If you run a Wireshark packet capture on the MID Server host, you can view the SSL session handshake. Filter by the IP address of the instance. The SSL handshake should follow this sequence:

<table style="width: 100%; border-collapse: collapse; border-spacing: 0px; border: 0px solid rgb(149, 165, 166);" border="1" width="420" cellspacing="0" cellpadding="0"><colgroup><col width="29"><col width="232"><col width="29"></colgroup><tbody><tr style="height: 13px;"><td style="width: 78.9205px; height: 215px; text-align: center; padding: 10px; border-color: rgb(149, 165, 166);" rowspan="11" height="233"><strong>MID Server&nbsp;</strong></td><td style="text-align: center; width: 255.284px; height: 13px; padding: 10px; border-color: rgb(149, 165, 166);">Client Hello →&nbsp;</td><td style="width: 78.0114px; height: 215px; text-align: center; padding: 10px; border-color: rgb(149, 165, 166);" rowspan="11"><strong>Instance</strong></td></tr><tr style="height: 20px;"><td style="text-align: center; width: 255.284px; height: 20px; padding: 10px; border-color: rgb(149, 165, 166);" height="21">← &nbsp;Server Hello</td></tr><tr style="height: 20px;"><td style="text-align: center; width: 255.284px; height: 20px; padding: 10px; border-color: rgb(149, 165, 166);" height="21">← &nbsp;Certificate</td></tr><tr style="height: 20px;"><td style="text-align: center; width: 255.284px; height: 20px; padding: 10px; border-color: rgb(149, 165, 166);" height="21">← &nbsp;Server Key Exchange</td></tr><tr style="height: 20px;"><td style="text-align: center; width: 255.284px; height: 20px; padding: 10px; border-color: rgb(149, 165, 166);" height="21">← &nbsp;Hello Done</td></tr><tr style="height: 20px;"><td style="text-align: center; width: 255.284px; height: 20px; padding: 10px; border-color: rgb(149, 165, 166);" height="21">Client Key Exchange →&nbsp;</td></tr><tr style="height: 20px;"><td style="text-align: center; width: 255.284px; height: 20px; padding: 10px; border-color: rgb(149, 165, 166);" height="21">Change Cypher Spec →&nbsp;</td></tr><tr style="height: 20px;"><td style="text-align: center; width: 255.284px; height: 20px; padding: 10px; border-color: rgb(149, 165, 166);" height="21">Encrypted Handshake Message →&nbsp;</td></tr><tr style="height: 20px;"><td style="text-align: center; width: 255.284px; height: 20px; padding: 10px; border-color: rgb(149, 165, 166);" height="21">← &nbsp;Change Cypher Spec</td></tr><tr style="height: 20px;"><td style="text-align: center; width: 255.284px; height: 20px; padding: 10px; border-color: rgb(149, 165, 166);" height="21">← &nbsp;Encrypted Handshake Message</td></tr><tr style="height: 22px;"><td style="text-align: center; width: 255.284px; height: 22px; padding: 10px; border-color: rgb(149, 165, 166);" height="23">← &nbsp;Application Data →&nbsp;</td></tr></tbody></table>
