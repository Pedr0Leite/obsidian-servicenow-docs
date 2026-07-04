---
title: "Discovery troubleshooting: Port Scan Natively Using Powershell"
aliases:
  - KB0549684
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0549684
kb_number: KB0549684
last_modified: 2026-05-19
---

## Discovery troubleshooting: Port Scan Natively Using Powershell

  

### Issue

When troubleshooting Discovery issues, it is often necessary to carry out a port scan of a device to see if the ports are open and responding. This is normally done from the MID server host server to the device that is not being discovered.

### Release

Any

### Resolution

There are applications such as nmap and zenmap that can be used to obtain this information, but it is also possible to do this from a very simple one-liner in Powershell and avoid installing 3rd party software.

Login to a MID server host and open a Powershell window. Then, use the following as a basis for your commands.

Replace "_**x.x.x.x**_" with the IP address of the device to port scan. 

**Example 1 - Single Port:**  
  
Here we are checking if port 135 is open. If the port is not open, you are returned to the command prompt.  
  
C:\\> **_135 | % {echo ((new-object Net.Sockets.TcpClient).Connect("x.x.x.x",$\_)) "$\_ is open"} 2> $null_**  
135 is open  
  
  
**Example 2 - Multiple Ports:**  
  
Here we are checking if ports 22,80,135, and 443 are open. In this example port 22 is not displayed as it is not open on the device.    
  
C:\\> **_(22,80,135,443) | % {echo ((new-object Net.Sockets.TcpClient).Connect("x.x.x.x",$\_)) "$\_ is open"} 2> $null_**  
80 is open  
135 is open  
443 is open

If you want to check all of the valid Discovery Ports (as defined in the product documentation article: [Discovery Ports and Protocols](https://docs.servicenow.com/csh?topicname=r_DiscoveryPortsAndProtocols.html&version=latest "Discovery Ports and Protocols")) then use the following command:

C:\\> **_(22,53,80,135,137,161,427,443,515,548,5060,5480,5989,9100) | % {echo ((new-object Net.Sockets.TcpClient).Connect("x.x.x.x",$\_)) "$\_ is open"} 2> $null_**

  
**Example 3 - Range of Ports:**  
  
Here we are checking if all ports between 1 and 1024 are open. If no ports in the range are open, you are returned to the command prompt.  
  
C:\\> **_1..1024 | % {echo ((new-object Net.Sockets.TcpClient).Connect("x.x.x.x",$\_)) "$\_ is open"} 2> $null_**  
80 is open  
135 is open
