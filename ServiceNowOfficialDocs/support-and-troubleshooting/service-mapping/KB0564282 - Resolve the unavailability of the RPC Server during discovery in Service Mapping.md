---
title: "Resolve the unavailability of the RPC Server during discovery in Service Mapping"
aliases:
  - KB0564282
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0564282
kb_number: KB0564282
last_modified: 2025-07-29
---

## Resolve the unavailability of the RPC Server during discovery in Service Mapping

  

### Issue

A warning icon on your business service map where a Windows Server should appear likely indicates an  RPC Server unavailable error. This issue prevents ServiceNow Service Mapping from properly discovering and monitoring your Windows Server.

This guide explains the two main causes of this error and provides step-by-step solutions to resolve them.

### Release

Any supported release

### Cause

The error occurs when Service Mapping cannot communicate with your Windows Server through Remote Procedure Call (RPC) connections. Two common scenarios trigger this problem:

1.  Wrong IP address configuration
2.  Firewall blocking the RPC communication

### Resolution

#### Solution 1: Fix an incorrect IP address configuration

**When this happens**

Your Windows Server has multiple IP addresses, but Service Mapping discovered only one. The system tries to connect using the wrong IP address and cannot access all required ports.

**How to fix it**

1.  Right-click the discovery error message on the service map.
2.  From the menu, select **Add Management IP** 
3.  Choose one of the correct IP addresses for your Windows Server.
4.  Wait for the discovery and mapping process to complete.
5.  Verify that no errors appear.

* * *

#### Solution 2: Configure firewall settings for RPC communication

**When this happens**

A firewall (Windows Firewall or external firewall) blocks RPC calls between the MID Server and Windows Server. RPC connections start on port 135 but can use any port from 1024 and higher once established.

**How to test and fix firewall issues**

**Step 1: Test if the firewall blocks RPC calls**

1.  On your MID Server, open the command prompt.
2.  Run the following command:
    
    wmic /NODE:target\_server\_ip\_address /user:domain\\user /password:xxxx cpu get
    
3.  Replace the placeholders:
    -   target\_server\_ip\_address with your Windows Server's IP
    -   domain\\user with valid credentials
    -   xxxx with the user's password

**Step 2: Check the results**

-   If you see "RPC Server unavailable": The firewall blocks the connection.
-   If the command succeeds: Continue to the next step.

**Step 3: Test Windows Firewall specifically**

1.  Temporarily disable Windows Firewall on the target server.
2.  Run the same wmic command from Step 1.
3.  Check the results:
    -   Success: Windows Firewall was blocking RPC calls.
    -   Still fails: An external firewall likely blocks the connection.

**Step 4: Configure firewall rules**

For Windows Firewall:

-   Create inbound rules to allow RPC traffic from your MID Server.
-   Allow port 135 and the dynamic RPC port range (1024-65535).

For external firewalls:

-   Work with your network team to allow RPC traffic between the MID Server and Windows Server.
-   Verify that both port 135 and the dynamic port range are accessible.
