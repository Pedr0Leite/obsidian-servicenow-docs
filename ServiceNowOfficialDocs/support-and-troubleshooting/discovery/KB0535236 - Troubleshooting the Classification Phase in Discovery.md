---
title: "Troubleshooting the Classification Phase in Discovery"
aliases:
  - KB0535236
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0535236
kb_number: KB0535236
last_modified: 2025-05-27
---

## Troubleshooting the Classification Phase in Discovery

  

### Release

All

### Resolution

The classification phase of Discovery begins right after the Shazzam port scanner probe and ends after processing those results, triggering the Identification phase in turn. Right after the Shazzam probe, look up the **Port Probe** table to determine what type of **Classify probe** needs to be launched.  
 

 ![Discovery Port Probes](/classification1.pngx "Discovery Port Probes")

After the information is returned from the Classify probe, Discovery undergoes the classification phase, which determines the device type for each probe protocol that is supported. This is the first time Discovery uses credentials to query a target. Discovery classifies computers based on Operating System (OS) and Network Devices based on their capabilities. Currently, we support the following protocols for classification: SSH, WMI, SNMP, and CIM.

![CI Classification](/clas2.pngx "CI Classification")

Under each protocol type, Discovery goes through the various classification types to determine what type the target device is. If a device matches the criteria for a given classifier, it is classified as such, and Identity probes specific to that device are then triggered.

For example, if the target can communicate through SSH, it could be a Linux, Mac, AIX, Solaris, etc. Each classification type then dictates the probes that Discovery runs for the Identification phase and Exploration phase.

If multiple ports are open to be classified, based on the _classification priority_, certain protocols are tried before others. 

![Discovery Port Probes Screen](/class3.pngx "Discovery Port Probes Screen")

In the base system, the classification priority is in this order: **WMI > SSH > SNMP > CIM**.

For example, if a device has both SNMP and SSH available for Discovery, the SSH classify probe is tried first. If it succeeds, then Discovery continues with SSH until the device is fully discovered. If it fails, then Discovery tries launching the SNMP classify probe to see if it is possible to explore with SNMP.

### Troubleshooting Classification

Errors and warnings found during classification are available in the Discovery log for each Discovery. These warnings are typical of probing in general. Make sure that the property glide.discovery.debug.classification is set to true.

If a classifier probe cannot connect to a device, the Discovery status lists it as **Active, couldn’t Classify**.

![Discovery Status List](/class4.pngx "Discovery Status List")

Common problems include:

-   Authentication: The proper probe credentials must be available on the instance. The credentials provided must have the right to perform the probes in question.

-   Connectivity: Socket timeouts and other forms of IO issues may be due to network configuration, congestion, or firewalls. Placing a MID in the same LAN as the target device may solve some of these issues.

-   Classifier: A custom classifier may need to be created for devices not supported in the base system. This is rare. For more information, see [Device Classifications](https://www.servicenow.com/docs/csh?topicname=create-discovery-ci-classification.html&version=latest "Device Classifications").

-   SNMP OIDs: If SNMP is being used, the device’s system OID may need to be added to the System OIDs table on the instance.  
      
    
-   WMI application: If the Windows application stops performing as expected when all else has been validated, restart the operating system to eliminate any residual potential issues (if possible).
-   Unix systems: When a UNIX Classify probe is having problems, the most likely cause is credentials. There are rare cases in which a UNIX system might have issues with local ACLs similar to Network devices or even logical firewalls, but this is not common. Use a third-party application such as puTTY, or your preferred SSH client from the MID Server host to confirm the credentials Discovery is attempting to use. You can also enable additional logging to assist with troubleshooting. 
-   Access control lists (ACLs): Routers, powering devices, switches, and even some printers can use Access Control lists that limit which IP addresses are allowed to make queries to the device. Ensure that your MID Server’s IP address is in that list. Since you cannot telnet to a UDP port, use a third-party query tool such as iReasoning from the MID Server host to validate the proper credentials and ACL access.
-   Logical firewall: In WMI communication, traffic only initiates on port 135. When two Windows operating systems communicate with WMI, they actually negotiate unused high ports to finish the conversation. This presents a problem for logical firewalls in Windows systems. Normally, firewalls allow port 135 to be seen as it is with the Discovery port scan probe but block the high ports that Discovery needs to communicate. To overcome this, use either of these options:  
    -   Configure firewalls to allow any port to use any protocol from the MID Server’s host, using the WMI script that is run locally.
    -   Lock down WMI to specific ports.

Any system configuration must be evaluated and determined safe by your local security policies and processes.
