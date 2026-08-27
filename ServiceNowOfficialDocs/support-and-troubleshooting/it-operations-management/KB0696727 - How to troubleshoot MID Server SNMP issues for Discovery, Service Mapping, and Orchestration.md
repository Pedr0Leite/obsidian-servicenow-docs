---
title: "How to troubleshoot MID Server SNMP issues for Discovery, Service Mapping, and Orchestration"
aliases:
  - KB0696727
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0696727
kb_number: KB0696727
last_modified: 2026-05-14
---

## How to troubleshoot MID Server SNMP issues for Discovery, Service Mapping, and Orchestration

  

### Issue

Troubleshoot MID Server SNMP issues that affect Discovery, Service Mapping, and Orchestration. This article covers tools and techniques for diagnosing problems with SNMP data collection from target CIs through the MID Server.

### Troubleshooting Tools

A common issue with applications that use SNMP (Discovery, Orchestration, Service Mapping) is that SNMP data is not returned completely or at all. If the data is returned, the investigation should focus on a different area of the application, such as a script include or business rule. A good starting point is to verify whether the data is collected successfully.

Two of the main reasons an SNMP query may not collect the desired data are:

-   Invalid SNMP credential
-   SNMP query timeout

The following tools can help confirm whether data is returned:

-   MID Server logs
-   SNMP walk tools
-   Wireshark

### Credential Test

To test an SNMP credential:

1.  Go to **Discovery** \> **Credentials**.
2.  Select the SNMP credential used for the SNMP discovery.
3.  Select the **Test Credential** link.
4.  Enter values for **Target** and **MID Server**.
5.  Select **OK**.

**Note**: The Shazzam probe and SNMP credential test query OID 1.3.6.1.2.1.1.1 (sysDescr). However, SNMP probes request OID 1.3.6.1.2.1.1.2 (sysObjectID) before running the actual SNMP request to determine if the credential is valid. A target device must respond to both 1.3.6.1.2.1.1.1 and 1.3.6.1.2.1.1.2 to be discovered successfully. When troubleshooting SNMP discovery issues, test both OIDs.

### **Review MID Server logs**

To get more detailed information in the MID Server logs for SNMP queries, set the parameter mid.log.level to debug. For instructions, see [Add a MID Server parameter.](https://docs.servicenow.com/csh?topicname=mid-server-parameters.html&version=latest#ariaid-title2 "Add a MID Server parameter")

After enabling debug logging, reproduce the issue and review the MID Server log files. For instructions on collecting log files, see the following documentation:

-   [Monitor the MID Server](https://docs.servicenow.com/csh?topicname=r_ServiceNowPlatform.html&version=latest "Monitor the MID Server")
-   [Manage ECC Queue content for a MID Server](https://docs.servicenow.com/csh?topicname=ecc-queue-mid-server.html&version=latest "Manage ECC Queue content for a MID Server")

### Enable detailed SNMP logs

1.  Go to the agent\\conf folder on the MID Server.
2.  Open the wrapper-override file.
3.  Add the following line to the additional Java parameters:   
    wrapper.java.additional.201=-Dsnmp4j.LogFactory=com.service\_now.mid.extension.trap.Snmp4j2DiscoLogFactory
4.  Restart the MID Server.
5.  Reproduce the issue.

#### **Example: Successful SNMP query**

The following log shows a successful query where all OIDs for an SNMP - Classify probe were returned. The classify probe was run with the default timeout of 1500 ms.

08/29/18 11:32:52 (911) Worker-Interactive:SNMP Worker starting: SNMP source: 
08/29/18 11:32:52 (926) Worker-Interactive:SNMP DEBUG: Timeout: 1500, Retries: 2
08/29/18 11:32:53 (004) Worker-Interactive:SNMP DEBUG: Using GETBULK
08/29/18 11:32:53 (004) Worker-Interactive:SNMP DEBUG: First attempt of getTable on target: /161, OIDs: \[1.3.6.1.2.1.4.20.1.1, 1.3.6.1.2.1.4.20.1.2, 1.3.6.1.2.1.4.20.1.3\], max rows: 10
08/29/18 11:32:53 (051) Worker-Interactive:SNMP DEBUG: First attempt of getTable on target: /161, OIDs: \[1.3.6.1.4.1.9.9.46.1.3.1.1.3\], max rows: 10
08/29/18 11:32:53 (051) Worker-Interactive:SNMP DEBUG: First attempt of getTable on target: /161, OIDs: \[1.3.6.1.2.1.2.2.1.1, 1.3.6.1.2.1.2.2.1.2, 1.3.6.1.2.1.2.2.1.3, 1.3.6.1.2.1.2.2.1.6, 1.3.6.1.2.1.2.2.1.7, 1.3.6.1.2.1.2.2.1.8\], max rows: 10
08/29/18 11:32:53 (114) Worker-Interactive:SNMP DEBUG: First attempt of getTable on target: /161, OIDs: \[1.3.6.1.2.1.47.1.1.1.1.11, 1.3.6.1.2.1.47.1.1.1.1.13, 1.3.6.1.2.1.47.1.1.1.1.2, 1.3.6.1.2.1.47.1.1.1.1.12, 1.3.6.1.2.1.47.1.1.1.1.4\], max rows: 10
08/29/18 11:32:53 (161) Worker-Interactive:SNMP DEBUG: First attempt of getTable on target: /161, OIDs: \[1.3.6.1.2.1.4.22.1.1, 1.3.6.1.2.1.4.22.1.2, 1.3.6.1.2.1.4.22.1.3\], max rows: 10
08/29/18 11:32:53 (161) Worker-Interactive:SNMP DEBUG: First attempt of getTable on target: /161, OIDs: \[1.3.6.1.2.1.25.3.2.1.2, 1.3.6.1.2.1.25.3.2.1.3\], max rows: 10
08/29/18 11:32:53 (161) Worker-Interactive:SNMP DEBUG: First attempt of getTable on target: /161, OIDs: \[1.3.6.1.2.1.43.5.1.1.17\], max rows: 10
08/29/18 11:32:53 (176) Worker-Interactive:SNMP DEBUG: Event: GenericScalarMetricEvent
08/29/18 11:32:53 (176) Worker-Interactive:SNMP DEBUG: Event: CheckSessionCanceledEvent, correlator: , sysID: 405c1f5cdb54a7008597d8c75e961967, canceled: false
08/29/18 11:32:53 (176) Worker-Interactive:SNMP Enqueuing: C:\\ServiceNow\\emprcoeljak\\agent\\work\\monitors\\ECCSender\\output\_0\\ecc\_queue.405c1f5cdb54a7008597d8c75e961967.xml
08/29/18 11:32:53 (176) Worker-Interactive:SNMP DEBUG: Event: GenericCounterMetricEvent
08/29/18 11:32:53 (192) Worker-Interactive:SNMP DEBUG: \*\* enqueued C:\\ServiceNow\\emprcoeljak\\agent\\work\\monitors\\ECCSender\\output\_0\\ecc\_queue.405c1f5cdb54a7008597d8c75e961967.xml
08/29/18 11:32:53 (192) Worker-Interactive:SNMP DEBUG: Event: MessageProcessedEvent, sysID: 405c1f5cdb54a7008597d8c75e961967
08/29/18 11:32:53 (192) Worker-Interactive:SNMP DEBUG: Event: SendMessageEvent, message: SNMP SNMP - Classify: 61 OIDs 
08/29/18 11:32:53 (192) Worker-Interactive:SNMP Worker completed: SNMP source:  time: 0:00:00.250

#### **Example: Failed SNMP query (timeout)**

The following log shows a partially successful query where only a fraction of the OIDs were returned. The timeout was set to 10 ms to simulate a timeout condition.

08/30/18 07:29:03 (997) Worker-Interactive:SNMP DEBUG: Timeout: 10, Retries: 2
08/30/18 07:29:03 (997) Worker-Interactive:SNMP DEBUG: Snmp4jSessionFactory: connection created for key SnmpSessionPoolKey\[target: &port:161&fixed\_cred:&tag:\]
08/30/18 07:29:04 (075) Worker-Interactive:SNMP DEBUG: Using GETBULK
08/30/18 07:29:04 (075) Worker-Interactive:SNMP DEBUG: First attempt of getTable on target: /161, OIDs: \[1.3.6.1.2.1.4.22.1.1, 1.3.6.1.2.1.4.22.1.2, 1.3.6.1.2.1.4.22.1.3\], max rows: 10
08/30/18 07:29:04 (075) Worker-Interactive:SNMP DEBUG: First attempt of getTable on target: /161, OIDs: \[1.3.6.1.2.1.4.20.1.1, 1.3.6.1.2.1.4.20.1.2, 1.3.6.1.2.1.4.20.1.3\], max rows: 10
08/30/18 07:29:04 (122) Worker-Interactive:SNMP DEBUG: First attempt of getTable failed on target: /161, OIDs: \[1.3.6.1.2.1.4.20.1.1, 1.3.6.1.2.1.4.20.1.2, 1.3.6.1.2.1.4.20.1.3\], error: Request timed out.
08/30/18 07:29:04 (122) Worker-Interactive:SNMP DEBUG: Second attempt of getTable on target: /161, OIDs: \[1.3.6.1.2.1.4.20.1.1, 1.3.6.1.2.1.4.20.1.2, 1.3.6.1.2.1.4.20.1.3\], max rows: 5
08/30/18 07:29:04 (169) Worker-Interactive:SNMP DEBUG: Second attempt of getTable failed on target: /161, OIDs: \[1.3.6.1.2.1.4.20.1.1, 1.3.6.1.2.1.4.20.1.2, 1.3.6.1.2.1.4.20.1.3\], error: Request timed out.
08/30/18 07:29:04 (169) Worker-Interactive:SNMP DEBUG: Third attempt of getTable on target: /161, OIDs: \[1.3.6.1.2.1.4.20.1.1, 1.3.6.1.2.1.4.20.1.2, 1.3.6.1.2.1.4.20.1.3\], max rows: 5, forcing GETNEXT pdu type
08/30/18 07:29:04 (215) Worker-Interactive:SNMP DEBUG: Event: GenericScalarMetricEvent
08/30/18 07:29:04 (215) Worker-Interactive:SNMP DEBUG: Event: CheckSessionCanceledEvent, correlator: , sysID: 561ea3acdbdca7008597d8c75e96191a, canceled: false
08/30/18 07:29:04 (215) Worker-Interactive:SNMP Enqueuing: C:\\ServiceNow\\emprcoeljak\\agent\\work\\monitors\\ECCSender\\output\_0\\ecc\_queue.561ea3acdbdca7008597d8c75e96191a.xml
08/30/18 07:29:04 (215) Worker-Interactive:SNMP DEBUG: Event: GenericCounterMetricEvent
08/30/18 07:29:04 (231) Worker-Interactive:SNMP DEBUG: \*\* enqueued C:\\ServiceNow\\emprcoeljak\\agent\\work\\monitors\\ECCSender\\output\_0\\ecc\_queue.561ea3acdbdca7008597d8c75e96191a.xml
08/30/18 07:29:04 (231) Worker-Interactive:SNMP DEBUG: Event: MessageProcessedEvent, sysID: 561ea3acdbdca7008597d8c75e96191a
08/30/18 07:29:04 (231) Worker-Interactive:SNMP DEBUG: Event: SendMessageEvent, message: SNMP SNMP - Classify: 12 OIDs 
08/30/18 07:29:04 (231) Worker-Interactive:SNMP Worker completed: SNMP source:  time: 0:00:00.218

### **SNMP Walk tool**

An SNMP walk tool can confirm whether results are returned as expected. If the third-party tool fails or returns partial results, this confirms the issue is not specific to the MID Server SNMP implementation. If the third-party tool succeeds consistently, review the MID Server logs for potential issues.

The following example uses SnmpWalk.exe to run a query from the MID Server for OID 1.3.6.1.2.1.1.1 (sysDescr), which returns a description of the device. The commands may change depending on the SNMP tool used. In the first test, the credential was set to "publi," which is an incorrect community string for this device. The correct community string is "public."

 C:\\SNMPWalk>.\\SnmpWalk.exe -r:10.127.212.181 -c:"publi" -os:.1.3.6.1.2.1.1 -op:.1.3.6.1.2.1.1.1.0  
  
%Failed to get value of SNMP variable. Timedout.  
  
Or you can use `snmpget` to get the special node information, if you get the OID.  

```
snmpget -v [version ] -c [scope] [IP address] [OID]
```

No credential failure error is returned. Instead, the query times out.

In the following example, the community string was corrected to "public."

C:\\SNMPWalk>.\\SnmpWalk.exe -r:10.127.212.181 -c:"public" -os:.1.3.6.1.2.1.1 -op:.1.3.6.1.2.1.1.1.0  
  
OID=.1.3.6.1.2.1.1.1.0, Type=OctetString, Value=Linux Linux-Tomcat 3.10.0-327.el7.x86\_64 31 SMP Thu Nov 19 22:10:57 UTC 2015 x86\_64

After correcting the community string, the sysDescr value was returned instead of timing out.

**Note**: Run the SNMP walk test from the same host where the MID Server is installed, using the same credential configuration.

#### **Network traffic monitoring tool (Wireshark example)**

A network traffic monitoring tool can help determine where the issue occurs, for example, whether packets are sent and whether responses are returned.

**Setup**

1.  Download and install Wireshark from the [Wireshark download page](https://www.wireshark.org/download.html). 
2.  Open the Wireshark application.
3.  Select the interface to use for collecting traffic. In the following image, Ethernet is selected.

![Wireshark Network Analyzer user interface](https://support.servicenow.com/sys_attachment.do?sys_id=7dca66de4734075411eaf24c736d43e7)

**Example: Reviewing SNMP query traffic**

The following example reviews the traffic for an SNMP query of table mgmt.mib-2.printmib.prtMarkerColorant.prtMarkerColorantTable prtMarkerColorantValue.

The ecc\_queue record shows what was returned:

![ ecc\_queue record results](sys_attachment.do?sys_id=a9cae2de4734075411eaf24c736d4330)

Use the following display filter to show only SNMP traffic to the target device:

udp && ip.addr == <target\_ip>

In the screenshot, the target IP was replaced with a loopback IP after the packets were collected.

![](sys_attachment.do?sys_id=3dca66de4734075411eaf24c736d43ec)

The following screenshot shows data returned by the device in detail for one of the OIDs.

![Example of data returned by device for one of the OIDs](sys_attachment.do?sys_id=7dcae2de4734075411eaf24c736d4336) 

Note: Wireshark has both capture filters and display filters.

-   **Capture** filters (for example, tcp port 80) reduce the size of a raw packet capture and are set before starting a capture.
-   **Display** filters (for example, tcp.port == 80) hide specific packets from the packet list and can be changed during a capture.

For large packet captures, setting a capture filter before starting the capture can improve system performance. 

#### **Decrypt SNMPv3 traffic in Wireshark**

SNMPv3 traffic is encrypted and must be decrypted for review. The following steps decrypt the packets in memory only.

1.  Open the captured packets in Wireshark.
2.  Go to **Edit** > **Preferences** > **Protocols**.
3.  Select **SNMP** from the protocol list.
4.  In the **Users Table** row, select **Edit**.
5.  Select **Add** and enter the following details:
    -   **Engine ID** — Collect from the Wireshark encrypted captures. This value is not encrypted. Open the SNMP packet header and check for the Engine ID string.
    -   **Username** — Enter the SNMPv3 user name.
    -   **Authentication model** — Select the authentication model (MD5 or SHA1) and enter the password.
    -   **Privacy protocol** — Select the privacy protocol (DES, AES, AES192, or AES256) and enter the privacy password.
6.  Verify that the packet content is now decrypted.

### Release

All supported releases

### Resolution

#### **Confirm correct credentials**

Incorrect credentials are the most common root cause. SNMP v1 and v2 are simpler to configure because they use only the community string. For SNMP v3, verify that the following values match what is configured on the target device: user name, authentication protocol, authentication key, privacy protocol, and privacy key. A third-party SNMP walk tool can also be used to verify that the credential is correct.

#### **Increase SNMP timeout**

The device may not be able to reply within the configured timeout, or a network issue may cause delays. In most cases, increasing the timeout increases the chances of retrieving the OIDs. SNMP timeout can be configured per MID Server or directly on a probe.

For available parameters, see the following documentation:

-   [SNMP Probes](https://docs.servicenow.com/csh?topicname=c_SNMPProbe.html&version=latest "SNMP Probes")
-   [MID Server SNMP Configuration Parameters](https://docs.servicenow.com/csh?topicname=mid-server-parameters.html&version=latest#d870369e2754 "MID Server SNMP Configuration Parameters")

#### **Response out of range**

Some devices can be configured with a start OID. When a walk is performed against such a device, the start OID is returned. Because this OID is not within the requested range, the value is not used. No results are returned to the probe even when credentials are correct. This is expected behavior because probes request specific values to classify and update devices, and anything outside the requested range is disregarded.

The following log example appears on the MID Server when debug logging is enabled:

DefaultUDPTransportMapping\_0.0.0.0/0 DEBUG: Response out of range. Received: iso.org.dod.internet.private.enterprises.f5.bigipTrafficMgmt.bigipSystem.sysGlobals.sysGlobalAttrs.sysGlobalAttr.sysAttrArpMaxEntries.0 (1.3.6.1.4.1.3375.2.1.1.1.1.1.0); Range is: 1.3.6.1.2.1.1.2 - 1.3.6.1.2.1.1.3. Request ID: 1853998886

In this example, the request is for OIDs  1.3.6.1.2.1.1.2 - 1.3.6.1.2.1.1.3 but the device returned 1.3.6.1.4.1.3375.2.1.1.1.1.1.0.

**Note**: The OID in this example is illustrative. The actual value varies by device.

To resolve this issue, review the device configuration and adjust it so the device returns the requested OIDs. Specific instructions vary by device.

#### **Context** 

Some probes need to use context to collect information when discovering Cisco devices. For example, probes triggered by the SNMP - Switch probe need to pass context information to collect information for each VLAN. Without context, only the default VLAN information is returned.

For more information, see the following articles:

-   [SNMP - Switch probe authentication error and Layer 2 data not collected](https://support.servicenow.com/kb_view.do?sysparm_article=KB0754353 "SNMP - Switch probe authentication error and Layer 2 data not collected")
-   [SNMPv3 fails to gather information on layer 2 tables for the non-default Vlans (Cisco switches only)](https://support.servicenow.com/kb_view.do?sysparm_article=KB0786155 "SNMPv3 fails to gather information on layer 2 tables for the non-default Vlans (Cisco Switches Only)")

### Related Links

-   [Discovery: Deep Dive - SNMP classification capabilities and properties](https://support.servicenow.com/kb_view.do?sysparm_article=KB0598507 "Discovery: Deep Dive - SNMP classification capabilities and properties")
-   [Why Discovery may not return a serial number for an SNMP device](https://support.servicenow.com/kb_view.do?sysparm_article=KB0695986 "Why Discovery may not return a serial number for an SNMP device")
-   [SNMP Probes](https://docs.servicenow.com/csh?topicname=c_SNMPProbe.html&version=latest#r_SNMPProbeMIBModules "SNMP Probes")
