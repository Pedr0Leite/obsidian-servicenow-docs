---
title: "Troubleshooting Shazzam Phase"
aliases:
  - KB0535234
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0535234
kb_number: KB0535234
last_modified: 2025-05-27
---

## Troubleshooting Shazzam Phase

  

### Issue

This knowledge article covers how to Troubleshoot the Shazzam phase in Discovery and the solution to issues seen in the Shazzam phase.

Discovery reacts to the Shazzam port scan as follows:

-   If Discovery finds an IP address with a state of OPEN for any port communicating over WMI, SSH, or SNMP, Discovery lists the IP address in the Shazzam returns (result="open").
-   If Discovery does not receive a response from a port, it does not list the IP address in the returns from Shazzam.
-   If Discovery receives a response from the scan that refuses the connection, Discovery lists the IP address and the result (result="refused") in the Shazzam returns.

### Symptoms

-   [Cannot discover some devices](#r1 "Cannot discover some devices")
-   [Cannot discover any particular type of devices (SNMP/SSH/WMI)](#r2 "Cannot discover any particular type of devices (SNMP/SSH/WMI)")
-   [Cannot discover some SNMP devices](#r3 "Cannot discover some SNMP devices")
-   [Cannot discover some LPS devices](#r4 "Cannot discover some LPS devices")
-   [Is not turning information for a certain network segment, or for the entire network](#r5 "Is not turning information for a certain network segment, or for the entire network")
-   [Error TCP\_CONNECTION\_FAILURE java.net.SocketException: No buffer space available](#r6 "Error TCP_CONNECTION_FAILURE java.net.SocketException: No buffer space available")
-   [Does not discovers the same number of devices consistently](#r7 "Does not discovers the same number of devices consistently")
-   [Shazzam takes a long time to complete](#r8 "Shazzam takes a long time to complete")

### Release

All

### Resolution

#### Shazzam cannot discover some devices

It could be a network connectivity issue. Please check that the ports used by discovery as listed on [Shazzam probe, port probes, and protocols](https://docs.servicenow.com/search?q=Shazzam+probe%2C+port+probes%2C+and+protocols&facetreset=yes "Shazzam probe, port probes, and protocols") documentation for the device type are not blocked.

#### Shazzam cannot discover any particular type of devices (SNMP/SSH/WMI)

If it is not a network issue, first check the port\_probe\_spec Shazzam output payload and make sure your port is being scanned. If it is not scanned, then check the behavior of the schedule. For more information, see the documentation on [Discovery Behaviors](https://docs.servicenow.com/search?q=Discovery+behaviors&facetreset=yes "Discovery Behaviors").

Also, it is possible that the port probes are not prioritized property. For more information, see the documentation pages on [Selective Port Probe Scanning](https://docs.servicenow.com/search?q=Selective+port+probe+scanning&facetreset=yes "Selective Port Probe Scanning") and [Port Probes](https://docs.servicenow.com/search?q=Port+probes&facetreset=yes "Port Probes").

#### Shazzam cannot discover some SNMP devices

If the solutions above do not work, credentials for SNMP devices are needed for detecting SNMP are alive. Add the necessary SNMP credentials for the device.

If the credentials for the SNMP device are already added and the device is still not discovered, check what snmp version the discovery schedule is set to discover via field "Use SNMP Version" (The default is v1/v2). Set "Use SNMP Version" to "All" in order to attempt snmp v1, v2, and v3.

**Note:** Out of box Shazzam will attempt community string "public". This can be the default for some SNMP devices and thus such devices may be discovered successfully even when there are no SNMP credentials under discovery\_credentials. However, for most SNMP devices, snmp credentials need to be added to discovery\_credentials in order to discover them successfully.

#### Shazzam is not discovering some LPS devices

Make sure the device type port is open and the service is up and running on that device (for example, WMI service, SSH server). 

Shazzam has probe parameters that may need to be fine tuned. For example, if Shazzam is not finding SSH devices, the GenericTCP\_waitForConnectMS and BannerTCP\_waitForConnectMS wait time may need to be extended. For more information, see the [Configure Shazzam probe parameters and payload size](https://docs.servicenow.com/search?q=Configure+Shazzam+probe+parameters+and+payload+size&facetreset=yes "Configure Shazzam probe parameters and payload size") documentation page. 

Reducing the shazzam\_chunk\_size from 100 to a lower number may also help.

#### The MID Server is not turning information for a certain network segment, or for the entire network

Check network connectivity using PING, TRACEROUTE, TELNET, and SNMP scanning tools.

Make sure the MID Servers that Discovery is using can reach the desired segments of the network. See the page: [Configure an IP address range for the MID Server](https://docs.servicenow.com/csh?topicname=t_ConfigureMIDIPRange.html&version=latest "Configure an IP address range for the MID Server").

#### Error TCP\_CONNECTION\_FAILURE java.net.SocketException: No buffer space available (maximum connections reached?)

Possibly due to Multi-thread Shaazam. See section "Single Thread vs Multi-thread Shazzam".

#### Does not discovers the same number of devices consistently

With multi-thread Shazzam there will be an increase in the number of port scans at a specific time. Some network security devices and appliances may find this malicious and block/throttle port scan. This may lead to less IPs detected. See section "Single Thread vs Multi-thread Shazzam".

#### Shazzam takes a long time to complete on some MID servers

This can happen if the mid server keystore is no longer valid. If the keystore is no longer valid the MID server will not be able to collect the credentials from the instance. This causes the SNMP scanner in Shazzam to attempt a new credential load for each ip discovered, which is an expensive operation. This also locks the other scanner threads and causes Shazzam to take a lot longer. The following can be seen in the agent logs when this happens:

ConcurrentPortScannerEngine-3:<ecc\_queue\_sysId> SEVERE \*\*\* ERROR \*\*\* MID Server encryption keys do not match and are no longer valid. To restore proper functionality, invalidate and re-validate the MID Server.  
ConcurrentPortScannerEngine-3:<ecc\_queue\_sysId> SEVERE \*\*\* ERROR \*\*\* An error occurred while decrypting credentials from instance  
com.snc.automation\_common.integration.exceptions.AutomationIOException: No key pair found for DefaultSecurityKeyPairHandle  
at com.service\_now.mid.keypairs.provider.standard.StandardKeyPairsProvider.decrypt(StandardKeyPairsProvider.java:182)  
at com.glide.util.MIDServerInfoPayloadDecrypter.decryptPayload(MIDServerInfoPayloadDecrypter.java:30)  
at com.service\_now.mid.creds.provider.standard.StandardCredentialsProvider.loadCredentials(StandardCredentialsProvider.java:317)  
at com.service\_now.mid.creds.provider.standard.StandardCredentialsProvider.load(StandardCredentialsProvider.java:287)  
at com.service\_now.mid.creds.provider.standard.StandardCredentialsProvider.loadIfNecessary(StandardCredentialsProvider.java:299)  
at com.service\_now.mid.creds.provider.standard.StandardCredentialsProvider.iterator(StandardCredentialsProvider.java:171)  
at com.service\_now.mid.probe.shazzam.scanners.SNMP.getCredsIterator(SNMP.java:383)  
at com.service\_now.mid.probe.shazzam.scanners.SNMP.sendSpamTaps(SNMP.java:283)  
at com.service\_now.mid.probe.shazzam.scanners.SNMP.sendFirstTap(SNMP.java:252)  
at com.service\_now.mid.probe.shazzam.scanners.SNMP.nextPhase(SNMP.java:199)  
at com.service\_now.mid.probe.shazzam.PortScannerEngine.run(PortScannerEngine.java:70)  
at com.service\_now.mid.probe.shazzam.ConcurrentPortScannerEngine.run(ConcurrentPortScannerEngine.java:35)  
at java.base/java.lang.Thread.run(Thread.java:834)

The solution is to:

-   [Rekey the MID Server](https://www.servicenow.com/docs/csh?topicname=t_RekeyAMIDServer.html&version=latest "Rekey a MID Server")

### Single Thread vs Multi-thread Shazzam

Parameters mid.shazzam.threads and mid.shazzam.max\_scanners\_per\_thread were added in Orlando. Parameter mid.shazzam.threads specifies the number of concurrent threads that Shazzam uses, while mid.shazzam.max\_scanners\_per\_thread specifies the number of concurrent scanners processed by each Shazzam thread. Setting either of the parameter to 0 disables Shazzam multi-thread optimization. If any issues are found with the port scanning phase of discovery after upgrading from a pre Orlando release to Orlando+, try reverting to single threaded Shazzam.

### Related Links

-   [Discovery Phase Shazzam](https://hi.service-now.com/kb_view.do?sysparm_article=KB0535234 "Discovery Phase Shazzam")
-   [Shazzam probe causing node to run out of memory due to payload size](https://support.servicenow.com/kb_view.do?sysparm_article=KB0746251 "Shazzam probe causing node to run out of memory due to payload size")
-   [Shazzam probes can be stuck in the ECC Queue output behind probes from later phases of discovery, due to running at the same Standard priority](https://support.servicenow.com/kb_view.do?sysparm_article=KB0827897 "Shazzam probes can be stuck in the ECC Queue output behind probes from later phases of discovery, due to running at the same Standard priority")
